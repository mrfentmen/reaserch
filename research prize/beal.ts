import { rename, appendFile } from "node:fs/promises"
const root = "/Users/dtaxk/Desktop/research prize/state"
const gcd = (a: number, b: number): number => {
  let x = a
  let y = b
  while (y !== 0) {
    const t = x % y
    x = y
    y = t
  }
  return x
}
const floorRoot = (v: bigint, e: number): bigint => {
  let lo = 1n
  let hi = 1n << BigInt(Math.ceil(Number(v.toString(2).length) / e) + 1)
  if (hi > v) hi = v
  let best = 1n
  while (lo <= hi) {
    const mid = (lo + hi) >> 1n
    const p = mid ** BigInt(e)
    if (p === v) return mid
    if (p < v) {
      best = mid
      lo = mid + 1n
    } else hi = mid - 1n
  }
  return best
}
const args = Bun.argv.slice(2).map(Number)
const max = args[0] || 200
const emax = args[1] || 5
const shard = args[2] || 0
const shards = args[3] || 1
const bmin = args[4] || 2
const tag = `${max}_${emax}_${shard}_${shards}_${bmin}`
const path = `${root}/beal_${tag}.txt`
const lock = `${root}/beal_${tag}.pid`
const found = `${root}/beal_found.txt`
const nearpath = `${root}/beal_near.txt`
const old = Number((await Bun.file(lock).exists()) ? (await Bun.file(lock).text()).trim() : 0)
if (old > 1 && old !== process.pid) {
  const chk = Bun.spawnSync(["kill", "-0", String(old)])
  if (chk.exitCode === 0) {
    console.log(`busy ${old}`)
    process.exit(0)
  }
}
await Bun.write(Bun.file(lock), `${process.pid}\n`)
const load = async (): Promise<number> => {
  if (!(await Bun.file(path).exists())) return 0
  const parts = (await Bun.file(path).text()).trim().split(" ")
  if (parts[0] !== tag) return 0
  const n = Number(parts[1])
  return Number.isFinite(n) && n >= 0 ? n : 0
}
const save = async (done: number) => {
  await Bun.write(Bun.file(`${path}.tmp`), `${tag} ${done}`)
  await rename(`${path}.tmp`, path)
}
const hunt = async () => {
  const powers: { v: bigint; base: number; exp: number }[] = []
  for (let base = bmin; base <= max; base++) {
    if (base % shards !== shard) continue
    for (let exp = 3; exp <= emax; exp++) {
      powers.push({ v: BigInt(base) ** BigInt(exp), base, exp })
    }
  }
  powers.sort((a, b) => (a.v < b.v ? -1 : 1))
  const start = await load()
  let done = 0
  let near = 0
  for (let i = 0; i < powers.length; i++) {
    const first = powers[i]
    if (!first) continue
    for (let j = i; j < powers.length; j++) {
      const second = powers[j]
      if (!second) continue
      if (gcd(first.base, second.base) !== 1) continue
      if (done < start) {
        done++
        continue
      }
      const sum = first.v + second.v
      for (let e = 3; e <= emax; e++) {
        const f = floorRoot(sum, e)
        if (f ** BigInt(e) === sum) {
          const c = Number(f)
          if (gcd(first.base, c) !== 1 || gcd(second.base, c) !== 1) continue
          console.log(`FOUND ${first.base}^${first.exp} + ${second.base}^${second.exp} = ${c}^${e}`)
          await Bun.write(Bun.file(found), `${first.base}^${first.exp} + ${second.base}^${second.exp} = ${c}^${e}\n`)
          await save(done)
          process.exit(0)
        }
        const low = sum - f ** BigInt(e)
        const high = (f + 1n) ** BigInt(e) - sum
        const d = low < high ? low : -high
        const ad = d < 0n ? -d : d
        if (ad <= 1000n && ad > 0n && sum > 1000000n && first.v * 1000n > sum) {
          near++
          await appendFile(nearpath, `${first.base}^${first.exp} + ${second.base}^${second.exp} = ${sum} near ${d < 0n ? f + 1n : f}^${e} off by ${d}\n`)
        }
      }
      done++
      if (done % 50000 === 0) {
        console.log(`scan ${done} shard=${shard} base=${first.base} near=${near}`)
        await save(done)
      }
    }
  }
  await save(done)
  console.log(`done shard=${shard} pairs=${done}`)
}
await hunt()
