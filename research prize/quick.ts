import { rename } from "node:fs/promises"
const root = "/Users/dtaxk/Desktop/research prize/state"
const lock = `${root}/quick.pid`
const path = `${root}/quick.txt`
const found = `${root}/quick_found.txt`
const old = Number((await Bun.file(lock).exists()) ? (await Bun.file(lock).text()).trim() : 0)
if (old > 1 && old !== process.pid) {
  const chk = Bun.spawnSync(["kill", "-0", String(old)])
  if (chk.exitCode === 0) {
    console.log(`busy ${old}`)
    process.exit(0)
  }
}
await Bun.write(Bun.file(lock), `${process.pid}\n`)
const prime = (n: number): boolean => {
  if (n < 2) return false
  if (n % 2 === 0) return n === 2
  if (n % 3 === 0) return n === 3
  const r = Math.sqrt(n)
  for (let i = 5; i <= r; i += 6) {
    if (n % i === 0 || n % (i + 2) === 0) return false
  }
  return true
}
const gold = (n: number): boolean => {
  for (let p = 3; p <= n / 2; p += 2) {
    if (!prime(p)) continue
    if (prime(n - p)) return true
  }
  return n === 4
}
const collatz = (n: bigint): string => {
  let v = n
  let steps = 0
  while (v !== 1n) {
    v = v % 2n === 0n ? v / 2n : 3n * v + 1n
    steps++
    if (steps > 200000) return "suspect-long"
    if (v > (1n << 72n) * 1000n) return "suspect-blowup"
  }
  return "ok"
}
const load = async (fallback: number): Promise<number> => {
  if (!(await Bun.file(path).exists())) return fallback
  const n = Number((await Bun.file(path).text()).trim())
  if (!Number.isFinite(n)) return fallback
  return n > fallback ? n : fallback
}
const save = async (g: number) => {
  await Bun.write(Bun.file(`${path}.tmp`), String(g))
  await rename(`${path}.tmp`, path)
}
const hunt = async (start: number) => {
  let g = await load(start % 2 === 0 ? start : start + 1)
  if (g % 2 === 1) g++
  let c = BigInt(g + 1)
  for (;;) {
    if (!gold(g)) {
      console.log(`GOLD-FOUND ${g}`)
      await Bun.write(Bun.file(found), `gold ${g}\n`)
      await save(g)
      process.exit(0)
    }
    const s = collatz(c)
    if (s !== "ok") {
      console.log(`COLLATZ-FOUND ${c} ${s}`)
      await Bun.write(Bun.file(found), `collatz ${c} ${s}\n`)
      await save(g)
      process.exit(0)
    }
    if (g % 20000 === 0) {
      console.log(`scan g=${g} c=${c}`)
      await save(g)
    }
    g += 2
    c += 2n
  }
}
const args = Bun.argv.slice(2).map(Number)
await hunt(args[0] || 1000000)
