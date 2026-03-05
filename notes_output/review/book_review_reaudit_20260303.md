# Re-audit vs book_review.docx (2026-03-03)

This report re-reads `notes_output/book_review.docx` and compares it against the current repository state (TeX sources only for automated checks).

## Extraction Completeness
- DOCX tables: 7
- Extracted JSON rows: 90
- Coverage check: 90/90 items matched to DOCX table rows (heuristic prefix match)

## Automated Status Summary (heuristic)
- CLOSED (auto-verified): 15
- OPEN (auto-detected): 0
- MANUAL (needs human/semantic verification): 75

## OPEN items (auto-detected)
- (none detected by TeX-only checks)

## CLOSED items (auto-verified)
- T1.R3 `lecture_1_intro.tex`: HIGH - 'YOLOv8' named without citation. Version numbers evolve rapidly; current readers may find the reference dated.
- T1.R5 `lecture_3_part_ii.tex (MLP Ch.6) vs lecture_4_part_i.tex (Backprop Ch.7)`: CRITICAL - Pre-activation is called p in Ch.6 (MLP) but z in Ch.7 (Backprop). Activation is y in Ch.6 but a in Ch.7. This is the single largest notation inconsistency in the book.
- T4.R1 `fl-intro.tex`: CRITICAL - This is a Beamer presentation file containing: instructor email (hamar@uwaterloo.ca), TA names and personal emails, office-hour logistics, specific grading percentages (40% assignments, 60% exam), and course admin directives. Uses \frame, \frametitle, \part commands incompatible with the book's article class. This file should NOT be in the book source directory.
- T4.R3 `ece657_notes.tex`: MEDIUM - The \sectionmark override sets headers to section NUMBER only. Reading 'Chapter 11' in the header is less useful than seeing the chapter title.
- T4.R4 `lecture_3_part_i.tex (Ch.5)`: CRITICAL - Production artifacts: % QC-BEGIN: perceptron_or_trace and % QC-END: perceptron_or_trace are embedded quality-control workflow markers. These must not appear in publication-ready source.
- T4.R7 `lecture_10_part_ii.tex (Ch.18, Fuzzy Inf.)`: MEDIUM - \markboth{Fuzzy inference}{} manually overrides the running header for this chapter, bypassing the fancyhdr setup. No other chapter does this. Likely a legacy artifact from standalone compilation.
- T4.R9 `Multiple chapters`: HIGH - Labels such as eq:auto:lecture_1_intro:1, eq:auto_cnn_ed5e022844, eq:auto_hopfield_591d3daa63 appear throughout. These are clearly machine-generated. Labels on never-referenced illustrative arithmetic create clutter.
- T5.R1 `lecture_1_intro.tex`: CRITICAL - The roadmap figure (fig:roadmap) shows the book's dependency graph but the Transformers chapter (Ch.14) is entirely absent. This is the most prominent modern chapter and its absence will confuse students.
- T5.R7 `Book-wide`: HIGH - No term/subject index is present. For a graduate reference text of 19 chapters, this is a significant usability gap.
- T5.R10 `lecture_8_part_i.tex (Ch.12, RNN)`: HIGH - Key Takeaways mentions 'gating strategies' in the RNN chapter. LSTM and GRU are pivotal architectures whose full gating equations (input, forget, output gates) must be present, not merely mentioned.
- T6.R1 `fl-intro.tex`: CRITICAL
- T6.R6 `ece657_notes.tex`: MEDIUM
- T6.R7 `lecture_10_part_ii.tex`: MEDIUM
- T6.R9 `appendix_logistics.tex`: MEDIUM
- T7.R1 `fl-intro.tex`: CRITICAL

## MANUAL items (not safely auto-checkable)
These are predominantly style/structure/pedagogy items or citation-placement preferences that require reading the surrounding text to confirm intent was met.
- T1.R1 `lecture_1_intro.tex`: MEDIUM - Equation environment used for a natural-language transitivity rule (If A=B and B=C, then A=C). This is an inference rule pattern, not an algebraic equation. The auto-generated label clutters cross-referencing.
- T1.R2 `lecture_1_intro.tex`: HIGH - '$<200$\, ms' uses raw math mode for a physical quantity with units. The siunitx package is imported but not used here.
- T1.R4 `lecture_3_part_i.tex (Ch. 5) + lecture_3_part_ii.tex (Ch. 6)`: HIGH - The book declares row-major convention. The feedforward formula (line 112) correctly uses row-major: z = aW + b. But the perceptron formula (lines 324-325) uses column-major notation: y = sign(w^T x + b). Visually inconsistent with the stated book-wide convention.
- T1.R6 `lecture_3_part_i.tex (Ch.5)`: MEDIUM - The proof assumes initialization w(0) = 0 implicitly (for the T*gamma lower bound) but does not state this explicitly in the proof setup.
- T1.R7 `lecture_3_part_i.tex (Ch.5)`: MEDIUM - The update condition is stated as y(w^T x + b) <= 0 (updates on exact boundary ties), whereas the convergence theorem proof implicitly uses strict < 0. This is a valid variant but may confuse students comparing results.
- T1.R8 `lecture_4_part_i.tex (Ch.7)`: LOW - Using MSE loss with one-hot targets for classification is presented as the default but can produce outputs outside [0,1] without a constraining output activation. Cross-entropy is mentioned later but the caveat is not flagged early enough.
- T1.R9 `lecture_8_part_i.tex (Ch.12, RNN)`: MEDIUM - Citations {Elman1990, Bengio1994} are used as canonical RNN references but are not visible in the reviewed refs.bib excerpt. Needs verification.
- T1.R10 `lecture_transformers.tex (Ch.14)`: MEDIUM - Citation {Bahdanau2015} is used for the attention mechanism. Needs full bibliography verification.
- T1.R11 `lecture_transformers.tex (Ch.14)`: HIGH - Key Takeaways mentions RoPE, ALiBi, FlashAttention, and PEFT techniques. Each of these needs a specific citation when introduced.
- T1.R12 `appendix_linear_systems.tex`: MEDIUM - nocite{Kailath1980, Chen1999LinearSystemTheoryDesign, Ogata2010} requires verification in refs.bib.
- T1.R13 `lecture_1_intro.tex`: LOW - 'James Slagle developed an early influential AI program' asserted without a citation.
- T2.R1 `notation.tex`: MEDIUM - The descriptive text ('This section collects book-wide notation...') appears AFTER the symbol table. Readers encounter the table without context.
- T2.R2 `notation.tex`: MEDIUM - The symbol n appears in the notation table as 'sequence length (tokens)' but is also used throughout supervised learning chapters for feature/input dimension. This is a collision not listed in Appendix D.
- T2.R3 `appendix_notation_collisions.tex`: HIGH - The index covers only 6 symbols. Missing: n (feature dim vs sequence length), d (data dimension vs embedding dimension -- noted in Ch.13), phi vs varphi (used for different feature maps), W (weight matrix vs embedding lookup).
- T2.R4 `lecture_3_part_i.tex (Ch.5)`: LOW - The text uses both 'sign(0)' and 'sgn(0)' for the same function. Notation note box uses 'sgn'; running text uses 'sign'.
- T2.R5 `lecture_4_part_ii.tex (Ch.8, RBF)`: MEDIUM - The RBF chapter uses varphi_i(x) for basis functions, while the global notation section reserves phi(.) for kernel feature maps. This is a documented collision but needs verification that varphi is used consistently throughout Chapter 8.
- T2.R6 `lecture_supervised.tex (Ch.3)`: MEDIUM - Verify that the loss function in Chapter 3 consistently uses calligraphic L (\mathcal{L}), not plain L, which the collision index reserves for number of layers or sequence length.
- T2.R7 `lecture_8_part_i.tex (Ch.11, CNN)`: LOW - Simple calculations like '65,536 x 100 = 6,553,600' are wrapped in numbered equation environments with auto-generated labels. These are illustrative, not results to cross-reference.
- T3.R1 `preface.tex`: HIGH - Prof. Karray is named in the Preface as having built ECE 657 and enabled course reshaping, but is absent from the Acknowledgments. This is an omission of a significant professional debt.
- T3.R2 `preface.tex`: LOW - 'courses that engage artificial intelligence' is non-idiomatic English.
- T3.R3 `preface.tex`: MEDIUM - 'That framework, though not originally mine' -- the framework is never identified or attributed. This is incomplete scholarly attribution.
- T3.R4 `lecture_1_intro.tex`: MEDIUM - 'Garbage in, garbage out' principle attributed loosely to the Babbage era. GIGO is typically attributed to early computing practice (1950s-60s), not the 19th century.
- T3.R5 `lecture_3_part_i.tex (Ch.5)`: LOW - 'introduced by Rosenblatt in 1958' -- the citation appears only in \nocite{Rosenblatt1958} at line 549, not inline at the point of introduction.
- T3.R6 `lecture_supervised.tex (Ch.3)`: HIGH - Chapter 3 covers ERM/MLE/MAP but foundational references may be missing: Vapnik (1998) for statistical learning theory; Fisher (1922) or Lehmann and Casella for MLE; MacKay (1992) or Tikhonov (1963) for MAP/regularization.
- T3.R7 `lecture_supervised.tex (Ch.3)`: MEDIUM - Key Takeaways mentions 'proper scoring rules.' The standard references are Brier (1950) for the Brier score and Gneiting and Raftery (2007) for the general theory.
- T3.R8 `lecture_3_part_ii.tex (Ch.6)`: MEDIUM - The backpropagation history is implied but Rumelhart, Hinton, and Williams (1986) -- the seminal paper -- should be explicitly cited where backpropagation is introduced.
- T3.R9 `lecture_8_part_ii.tex (Ch.11, CNN)`: MEDIUM - CNNs are introduced historically without citing LeCun et al. (1989, 1998) for LeNet, the architecture that established the modern CNN paradigm. AlexNet (Krizhevsky 2012) is in the bibliography but the earlier work is missing.
- T3.R10 `lecture_8_part_i.tex (Ch.9, SOM)`: LOW - 'introduced by Teuvo Kohonen' appears without a direct citation.
- T3.R11 `lecture_10_part_i.tex (Ch.10)`: LOW - Verify the Hopfield1982 ref.bib entry is complete: journal = PNAS, volume = 79, number = 8, pages = 2554-2558.
- T3.R12 `lecture_10_part_ii.tex (Ch.15, Softcomp)`: LOW - Citation {Zadeh1994} for soft computing. Canonical source: Zadeh (1994) Fuzzy logic, neural networks, and soft computing, CACM 37(3), 77-84.
- ... (45 more)
