# Literature — Darmon–Granville + Fermat-Catalan frame (R009 background)

- TITLE: On the equations z^m=F(x,y) and Ax^p+By^q=Cz^r (Darmon–Granville) + Fermat-Catalan conjecture (survey context)
- AUTHORS: Henri Darmon, Andrew Granville (1994 paper); conjecture context via Mauldin Notices AMS 1997, Bennett–Mihăilescu–Siksek survey, arXiv 2412.11933 survey, Warwick abc-talk slides
- YEAR: 1994 (paper); surveys 2016–2025
- SOURCE: https://math.mcgill.ca/darmon/pub/Articles/Research/12.Granville/paper.pdf + https://www.ams.org/notices/199711/beal.pdf + https://personal.math.ubc.ca/~bennett/BeMuSi-Springer-2016.pdf (excerpts retrieved 2026-09-18; full PDFs not line-read — relevance statements below rest only on retrieved passages)
- PROBLEM: generalized Fermat Ax^p+By^q=Cz^r, primitive (coprime) solutions.
- RESULT: Darmon–Granville: for FIXED signature with 1/p+1/q+1/r<1, finitely many primitive solutions (Faltings reduction). Fermat-Catalan conjecture: finitely many coprime power-sum solutions with 1/p+1/q+1/r<1 across ALL signatures; TEN solutions known (all involve an exponent 2; none with all exponents ≥3 — consistent with Beal holding where computed).
- METHOD: arithmetic geometry (Faltings, Chevalley–Weil, modular coverings); modern front: modular method/Frey varieties + elimination (Magma packages, e.g. Azon 2025) per signature.
- RELEVANCE: the deep theory our elementary pruners do not touch; defines what "stronger methods" means.
- KNOWN BOUND: finiteness theorems (non-effective in general); 10 known Fermat-Catalan solutions; signature-by-signature resolutions (survey tables).
- RELATION TO C20: survey formalizes "local obstructions" (all solutions mod s^m share s ⟹ no primitive solutions) — the grown-up version of residue reasoning, applied per-equation via deep machinery, not as a generic search sieve. Our C20 is the elementary shadow of this idea.
- RELATION TO C21: prime-exponent reduction is standard practice in this literature (modular method needs prime exponents); our gcd>2 skip is the trivial brute-force analogue.
- RELATION TO OUR IMPLEMENTATION: no overlap in capability; literature owns all deep results.
- NOVELTY IMPLICATION: any claim that C20/C21 open new theoretical ground is foreclosed by this literature.
- NOTES: excerpt-level sourcing; no theorem text invented beyond retrieved passages.
