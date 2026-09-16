const root = "/Users/dtaxk/Desktop/research prize/state"
const found = `${root}/riemann_found.txt`
type C = { re: number; im: number }
const add = (a: C, b: C): C => ({ re: a.re + b.re, im: a.im + b.im })
const div = (a: C, b: C): C => {
  const d = b.re * b.re + b.im * b.im
  return { re: (a.re * b.re + a.im * b.im) / d, im: (a.im * b.re - a.re * b.im) / d }
}
const mag = (a: C): number => Math.sqrt(a.re * a.re + a.im * a.im)
const npow = (n: number, re: number, im: number): C => {
  const ln = Math.log(n)
  const m = Math.exp(-re * ln)
  const ang = im * ln
  return { re: m * Math.cos(ang), im: m * -Math.sin(ang) }
}
const bern = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730]
const fact = [2, 24, 720, 40320, 3628800, 479001600]
const zetaEM = (re: number, im: number, n: number, p: number): { z: C; err: number } => {
  const s: C = { re, im }
  let acc: C = { re: 0, im: 0 }
  for (let k = 1; k < n; k++) acc = add(acc, npow(k, re, im))
  const nn = npow(n, re, im)
  acc = add(acc, { re: nn.re / 2, im: nn.im / 2 })
  acc = add(acc, div(npow(n, re - 1, im), { re: re - 1, im }))
  let rise: C = { re: s.re, im: s.im }
  let last = 0
  for (let k = 1; k <= p; k++) {
    if (k > 1) rise = { re: rise.re * (re + 2 * k - 3) - rise.im * im, im: rise.re * im + rise.im * (re + 2 * k - 3) }
    if (k > 1) rise = { re: rise.re * (re + 2 * k - 2) - rise.im * im, im: rise.re * im + rise.im * (re + 2 * k - 2) }
    const pw = npow(n, re + 2 * k - 1, im)
    const coeff = (bern[k - 1] as number) / (fact[k - 1] as number)
    const term: C = { re: (rise.re * pw.re - rise.im * pw.im) * coeff, im: (rise.re * pw.im + rise.im * pw.re) * coeff }
    last = mag(term)
    acc = add(acc, term)
  }
  return { z: acc, err: last * 5 }
}
const hunt = async (t0: number, t1: number) => {
  const res = [0.2, 0.3, 0.4, 0.6, 0.7, 0.8]
  for (let t = t0; t <= t1; t += 0.25) {
    const n = Math.min(5000, Math.max(2000, Math.ceil(t * 2)))
    for (const re of res) {
      const r = zetaEM(re, t, n, 5)
      const m = mag(r.z)
      if (m < 0.01 && r.err < 0.015) {
        const r2 = zetaEM(re, t, Math.min(8000, n + 2000), 6)
        const m2 = mag(r2.z)
        if (m2 < 0.01 && r2.err < 0.015) {
          console.log(`SUSPECT re=${re} t=${t} |z|=${m} v2=${m2} err=${r2.err}`)
          await Bun.write(Bun.file(found), `re=${re} t=${t} mag=${m} v2=${m2} err=${r2.err}\n`)
          return
        }
      }
    }
    if (Math.round(t * 4) % 40 === 0) console.log(`scan t=${t}`)
  }
  console.log(`done ${t0}-${t1}`)
}
const selftest = async () => {
  const a = zetaEM(0.5, 14.134725, 3000, 5)
  const b = zetaEM(0.6, 14.0, 3000, 5)
  const c = zetaEM(0.5, 21.02204, 3000, 5)
  console.log(`zero1 mag=${mag(a.z)} err=${a.err} want<0.05`)
  console.log(`offline mag=${mag(b.z)} err=${b.err} want>0.05`)
  console.log(`zero2 mag=${mag(c.z)} err=${c.err} want<0.05`)
  const ok = mag(a.z) < 0.05 && a.err < 0.015 && mag(b.z) > 0.05 && mag(c.z) < 0.05 && c.err < 0.015
  console.log(ok ? "TRUST-HIGH" : "TRUST-FAIL")
}
const args = Bun.argv.slice(2)
if (args[0] === "selftest") await selftest()
else {
  const nums = args.map(Number)
  await hunt(nums[0] || 10, nums[1] || 100)
}
