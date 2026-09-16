import { rename } from "node:fs/promises"
const root = "/Users/dtaxk/Desktop/research prize/state"
const path = `${root}/riemann.txt`
const lock = `${root}/riemann.pid`
const old = Number((await Bun.file(lock).exists()) ? (await Bun.file(lock).text()).trim() : 0)
if (old > 1 && old !== process.pid) {
  const chk = Bun.spawnSync(["kill", "-0", String(old)])
  if (chk.exitCode === 0) {
    console.log(`busy ${old}`)
    process.exit(0)
  }
}
await Bun.write(Bun.file(lock), `${process.pid}\n`)
const load = async (fallback: number): Promise<number> => {
  if (!(await Bun.file(path).exists())) return fallback
  const n = Number((await Bun.file(path).text()).trim())
  if (!Number.isFinite(n)) return fallback
  return n > fallback ? n : fallback
}
const save = async (t: number) => {
  await Bun.write(Bun.file(`${path}.tmp`), String(t))
  await rename(`${path}.tmp`, path)
}
const raw = Bun.argv.slice(2).map(Number).filter((n) => Number.isFinite(n))
let cur = await load(raw[0] || 200)
for (;;) {
  const next = cur + 200
  console.log(`chunk ${cur}-${next}`)
  const proc = Bun.spawnSync(["bun", "/Users/dtaxk/Desktop/research prize/riemann.ts", String(cur), String(next), "1200"])
  const out = proc.stdout.toString()
  console.log(out.slice(-500))
  if (out.includes("SUSPECT")) break
  cur = next
  await save(cur)
}
