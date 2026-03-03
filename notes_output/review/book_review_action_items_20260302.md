# Action Items From `notes_output/book_review.docx`
- Source review: `notes_output/book_review.docx` (Review Date: March 2026)
- Extracted items JSON: `notes_output/review/book_review_extracted_items_20260302.json` (90 rows)
- Notes: This list is a direct conversion of the review tables into executable tasks. It does *not* assume items are still open; treat each as “verify current state, then fix if needed.”

---

## P0 Queue

### Editorial / Writing / Voice
- [ ] **fl-intro.tex | ENTIRE FILE - Beamer slides | All lines**
  - Review severity: `CRITICAL`
  - Issue: This is a Beamer presentation file containing: instructor email (hamar@uwaterloo.ca), TA names and personal emails, office-hour logistics, specific grading percentages (40% assignments, 60% exam), and course admin directives. Uses \frame, \frametitle, \part commands incompatible with the book's article class. This file should NOT be in the book source directory.
  - Recommended change: Remove fl-intro.tex from book source directory immediately. Archive to a separate course-materials repository. Verify it is not included anywhere in book_chapters.tex or ece657_notes.tex.
- [ ] **lecture_3_part_i.tex (Ch.5) | QC markers left in source | Lines 360-371**
  - Review severity: `CRITICAL`
  - Issue: Production artifacts: % QC-BEGIN: perceptron_or_trace and % QC-END: perceptron_or_trace are embedded quality-control workflow markers. These must not appear in publication-ready source.
  - Recommended change: Remove all % QC-BEGIN and % QC-END blocks. Run: grep -rn 'QC-BEGIN\|QC-END' *.tex to find all occurrences across the manuscript.

### LaTeX / Production
- [ ] **fl-intro.tex | ENTIRE FILE | All**
  - Review severity: `CRITICAL`
  - Issue: Remove fl-intro.tex from book source directory. Archive to course materials repo. Contains personal contact info, grading details, and Beamer commands incompatible with the book class.
- [ ] **lecture_3_part_i.tex | QC comment markers | Lines 360-371**
  - Review severity: `CRITICAL`
  - Issue: Remove all % QC-BEGIN and % QC-END blocks. Run: grep -rn 'QC-BEGIN|QC-END' *.tex to audit all chapter files.

### Pedagogy / Structure
- [ ] **lecture_1_intro.tex | Roadmap missing Transformers | fig:roadmap, Lines 376-413**
  - Review severity: `CRITICAL`
  - Issue: The roadmap figure (fig:roadmap) shows the book's dependency graph but the Transformers chapter (Ch.14) is entirely absent. This is the most prominent modern chapter and its absence will confuse students.
  - Recommended change: Extend the TikZ roadmap to add a 'Transformers\n(Attention)' node to the right of RNN, with an arrow from RNN to Transformers. Consider also adding an NLP/Embeddings node between RNN and Transformers.

### Priority Action Summary
- [ ] **All .tex files | eq:auto equation labels | Various**
  - Review severity: `CRITICAL`
  - Issue: Audit all eq:auto labels; remove from unreferenced equations; replace referenced ones with descriptive names.
- [ ] **fl-intro.tex | Entire file | All**
  - Review severity: `CRITICAL`
  - Issue: Remove from source directory. Contains personal emails, TAs, grading. Archive to course-materials repo.
- [ ] **lecture_1_intro.tex (fig:roadmap) | Roadmap figure | Lines 376-413**
  - Review severity: `CRITICAL`
  - Issue: Add Transformers node to roadmap TikZ figure.
- [ ] **lecture_3_part_i.tex | QC markers | Lines 360-371**
  - Review severity: `CRITICAL`
  - Issue: Remove all % QC-BEGIN and % QC-END comment blocks. Audit all .tex files.
- [ ] **lecture_3_part_ii.tex + lecture_4_part_i.tex | Pre-activation naming (p vs z) | Lines 57-60 / 37-44**
  - Review severity: `CRITICAL`
  - Issue: Add notation note box at start of Ch.7: p in Ch.6 = z here; y in Ch.6 = a here.

### Scientific / Mathematical
- [ ] **lecture_3_part_ii.tex (MLP Ch.6) vs lecture_4_part_i.tex (Backprop Ch.7) | Pre-activation variable naming | Lines 57-60 (Ch.6); Lines 37-44 (Ch.7)**
  - Review severity: `CRITICAL`
  - Issue: Pre-activation is called p in Ch.6 (MLP) but z in Ch.7 (Backprop). Activation is y in Ch.6 but a in Ch.7. This is the single largest notation inconsistency in the book.
  - Recommended change: Add a Notation note box at the start of Ch.7 before line 37: 'This chapter uses z for pre-activation (called p in Chapter 6) and a for activation (called y in Chapter 6). The change aligns with Goodfellow et al. (2016) and is maintained from Chapter 7 onward.' Alternatively, unify to z/a throughout both chapters.

## P1 Queue

### Academic / Scholarly Rigor
- [ ] **lecture_supervised.tex (Ch.3) | ERM/MLE/MAP foundational citations | Full chapter**
  - Review severity: `HIGH`
  - Issue: Chapter 3 covers ERM/MLE/MAP but foundational references may be missing: Vapnik (1998) for statistical learning theory; Fisher (1922) or Lehmann and Casella for MLE; MacKay (1992) or Tikhonov (1963) for MAP/regularization.
  - Recommended change: Verify these standard citations appear when introducing each framework. Add if missing.
- [ ] **preface.tex | Prof. Karray attribution | Lines 10-12**
  - Review severity: `HIGH`
  - Issue: Prof. Karray is named in the Preface as having built ECE 657 and enabled course reshaping, but is absent from the Acknowledgments. This is an omission of a significant professional debt.
  - Recommended change: Add explicit credit in Acknowledgments: 'I am especially grateful to Prof. Fakhri Karray, who built ECE 657 and generously invited me to broaden its scope -- an act of intellectual generosity that made this book possible.'

### Editorial / Writing / Voice
- [ ] **Multiple chapters | Auto-generated equation labels | Various**
  - Review severity: `HIGH`
  - Issue: Labels such as eq:auto:lecture_1_intro:1, eq:auto_cnn_ed5e022844, eq:auto_hopfield_591d3daa63 appear throughout. These are clearly machine-generated. Labels on never-referenced illustrative arithmetic create clutter.
  - Recommended change: Run: grep -n 'eq:auto' *.tex to find all occurrences. Remove labels from equations that are never \ref or \eqref'd. Replace labels on referenced equations with descriptive names (e.g., eq:perceptron_or_update, eq:hopfield_energy).
- [ ] **acknowledgments.tex | Brevity of acknowledgments | Lines 1-17**
  - Review severity: `HIGH`
  - Issue: Acknowledgments are ~80 words. The preface names Prof. Karray specifically; the acknowledgments do not. Academic books routinely acknowledge institution, funding, named colleagues, and reviewers.
  - Recommended change: Expand to 200-300 words. Name Prof. Fakhri Karray, the ECE department at University of Waterloo, graduate students/TAs who contributed, and any reviewers or colleagues who gave feedback.

### LaTeX / Production
- [ ] **All .tex files | eq:auto equation labels | Various**
  - Review severity: `HIGH`
  - Issue: Audit all eq:auto labels. Remove from never-referenced equations. Replace on referenced ones with descriptive names. Run: grep -n 'eq:auto' *.tex | wc -l to count.

### Notation / Symbol Consistency
- [ ] **appendix_notation_collisions.tex | Missing symbols in collision index | Full appendix**
  - Review severity: `HIGH`
  - Issue: The index covers only 6 symbols. Missing: n (feature dim vs sequence length), d (data dimension vs embedding dimension -- noted in Ch.13), phi vs varphi (used for different feature maps), W (weight matrix vs embedding lookup).
  - Recommended change: Add rows for: n, d, phi vs varphi (phi reserved for kernel feature maps, varphi for RBF), and W (weight matrix vs embedding -- context clarifies).

### Pedagogy / Structure
- [ ] **All lecture files | Exercises not formal problem sets | Various**
  - Review severity: `HIGH`
  - Issue: Exercise boxes contain prompts labeled as 'ideas,' not structured problems. No numbered exercises, difficulty ratings, or deliverables. For a graduate companion used in courses, this is a significant pedagogical gap.
  - Recommended change: Upgrade to numbered exercises with clear deliverables. Add difficulty ratings (Basic / Intermediate / Advanced). Add Hint: or See also: pointers. Place in a dedicated Exercises section at chapter end rather than inside a tcolorbox.
- [ ] **Book-wide | No subject index | N/A**
  - Review severity: `HIGH`
  - Issue: No term/subject index is present. For a graduate reference text of 19 chapters, this is a significant usability gap.
  - Recommended change: Add \usepackage{makeidx} and \makeindex to preamble. Seed with priority terms: attention, backpropagation, Bayes classifier, bias-variance, calibration, CNN, cross-entropy, defuzzification, ERM, evolutionary algorithm, fuzzy set, gradient descent, Hopfield, kernel, LSTM, membership function, MLP, perceptron, RBF, regularization, RNN, SOM, softmax, t-norm, transformer, vanishing gradient.
- [ ] **lecture_8_part_i.tex (Ch.12, RNN) | LSTM/GRU gating equations | Full chapter**
  - Review severity: `HIGH`
  - Issue: Key Takeaways mentions 'gating strategies' in the RNN chapter. LSTM and GRU are pivotal architectures whose full gating equations (input, forget, output gates) must be present, not merely mentioned.
  - Recommended change: Verify LSTM (Hochreiter and Schmidhuber 1997) and GRU (Cho et al. 2014) each have a dedicated subsection with complete gating equations, input/forget/output gate formulations, and at least one worked numerical trace.

### Priority Action Summary
- [ ] **All lecture files | Exercises not formal problem sets | Various**
  - Review severity: `HIGH`
  - Issue: Upgrade to numbered exercises with deliverables and difficulty ratings.
- [ ] **Book-wide | Subject index absent | N/A**
  - Review severity: `HIGH`
  - Issue: Add makeidx package and populate with 50+ key terms.
- [ ] **acknowledgments.tex | Brevity | Lines 1-17**
  - Review severity: `HIGH`
  - Issue: Expand to 200-300 words. Name Prof. Karray, institution, students, TAs, reviewers.
- [ ] **lecture_1_intro.tex | YOLOv8 citation missing | Line 197**
  - Review severity: `HIGH`
  - Issue: Add Jocher et al. 2023 / Ultralytics YOLOv8 citation.
- [ ] **lecture_3_part_i.tex (Ch.5) | Row vs column notation conflict | Lines 110-117 vs 324-329**
  - Review severity: `HIGH`
  - Issue: Add parenthetical: w^T x is the scalar inner product, consistent with row convention.
- [ ] **lecture_8_part_i.tex (Ch.12) | LSTM/GRU equations completeness | Full chapter**
  - Review severity: `HIGH`
  - Issue: Verify complete gating equations for LSTM and GRU are present.

### Scientific / Mathematical
- [ ] **lecture_1_intro.tex | Camera case study | Line 195**
  - Review severity: `HIGH`
  - Issue: '$<200$\, ms' uses raw math mode for a physical quantity with units. The siunitx package is imported but not used here.
  - Recommended change: Replace with \qty{200}{\ms} or \SI{200}{\ms}. Audit all physical quantities throughout the manuscript for siunitx consistency.
- [ ] **lecture_1_intro.tex | Camera case study | Line 197**
  - Review severity: `HIGH`
  - Issue: 'YOLOv8' named without citation. Version numbers evolve rapidly; current readers may find the reference dated.
  - Recommended change: Add \citep for YOLOv8 (Jocher et al. 2023 / Ultralytics technical report) and a note that model versions change; readers should consult current documentation.
- [ ] **lecture_3_part_i.tex (Ch. 5) + lecture_3_part_ii.tex (Ch. 6) | Feedforward eqn vs Perceptron formula | Lines 110-117 (Ch.5) vs 324-329 (Ch.5)**
  - Review severity: `HIGH`
  - Issue: The book declares row-major convention. The feedforward formula (line 112) correctly uses row-major: z = aW + b. But the perceptron formula (lines 324-325) uses column-major notation: y = sign(w^T x + b). Visually inconsistent with the stated book-wide convention.
  - Recommended change: In the perceptron formula, add a note: 'w^T x is shorthand for the scalar inner product (row convention: xw), consistent with the book-wide row-major style.' Alternatively rewrite as y = sign(xw + b).
- [ ] **lecture_transformers.tex (Ch.14) | PEFT/RoPE/ALiBi/FlashAttention citations | Various**
  - Review severity: `HIGH`
  - Issue: Key Takeaways mentions RoPE, ALiBi, FlashAttention, and PEFT techniques. Each of these needs a specific citation when introduced.
  - Recommended change: Add: RoPE - Su et al. (2021); ALiBi - Press et al. (2022); FlashAttention - Dao et al. (2022); LoRA - Hu et al. (2022); prompt tuning - Lester et al. (2021).

## P2 Queue

### Academic / Scholarly Rigor
- [ ] **lecture_11.tex (Ch.19, Evo) | No mention of Bayesian optimization | ~Lines 27-30**
  - Review severity: `MEDIUM`
  - Issue: Genetic algorithms are introduced as the method for expensive black-box optimization without acknowledging Bayesian optimization (BO), which is often preferred when evaluations are few.
  - Recommended change: Add: 'When the evaluation budget is very small (tens to hundreds of trials), Bayesian optimization (see e.g. Frazier 2018) may outperform population-based search; GAs are preferred when populations are affordable and no surrogate model is readily available.'
- [ ] **lecture_11.tex (Ch.19, Evo) | Sims1994 citation context | Line 10**
  - Review severity: `MEDIUM`
  - Issue: \citealp{Sims1994} is cited for 'Karl Sims-style intuition.' Sims (1994) is a SIGGRAPH paper on evolved virtual creatures. Verify bibliography key is correct.
  - Recommended change: Verify: Sims, K. (1994). Evolving Virtual Creatures. SIGGRAPH, pp. 15-22.
- [ ] **lecture_1_intro.tex | GIGO attribution | Lines 48-49**
  - Review severity: `MEDIUM`
  - Issue: 'Garbage in, garbage out' principle attributed loosely to the Babbage era. GIGO is typically attributed to early computing practice (1950s-60s), not the 19th century.
  - Recommended change: Add a footnote: 'The phrase garbage in, garbage out is commonly attributed to computing practice of the 1950s-60s; its pedagogical relevance to data quality predates the phrase. Historical credit belongs to Babbage only informally.'
- [ ] **lecture_3_part_ii.tex (Ch.6) | Backpropagation foundational citation | Lines 349-353**
  - Review severity: `MEDIUM`
  - Issue: The backpropagation history is implied but Rumelhart, Hinton, and Williams (1986) -- the seminal paper -- should be explicitly cited where backpropagation is introduced.
  - Recommended change: Add \citep{Rumelhart1986} with a note: 'The efficient organization of these updates was formalized in Rumelhart et al. (1986), a foundational paper in this tradition.'
- [ ] **lecture_8_part_ii.tex (Ch.11, CNN) | LeCun citation for CNN origin | Lines 33-37**
  - Review severity: `MEDIUM`
  - Issue: CNNs are introduced historically without citing LeCun et al. (1989, 1998) for LeNet, the architecture that established the modern CNN paradigm. AlexNet (Krizhevsky 2012) is in the bibliography but the earlier work is missing.
  - Recommended change: Add \citep{LeCun1989, LeCun1998} when introducing CNNs historically.
- [ ] **lecture_supervised.tex (Ch.3) | Proper scoring rules citations | Full chapter**
  - Review severity: `MEDIUM`
  - Issue: Key Takeaways mentions 'proper scoring rules.' The standard references are Brier (1950) for the Brier score and Gneiting and Raftery (2007) for the general theory.
  - Recommended change: Verify \citep{Gneiting2007} appears when proper scoring rules are introduced in Chapter 3. Add if missing.
- [ ] **preface.tex | Unattributed framework | Line 5**
  - Review severity: `MEDIUM`
  - Issue: 'That framework, though not originally mine' -- the framework is never identified or attributed. This is incomplete scholarly attribution.
  - Recommended change: Either identify the framework explicitly with a citation, or rephrase to remove the attribution claim: 'the pedagogical arc that emerged over several offerings of ECE 657 proved invaluable.'

### Editorial / Writing / Voice
- [x] **ece657_notes.tex | Running headers show number only | Lines 62-65**
  - Review severity: `MEDIUM`
  - Issue: The \sectionmark override sets headers to section NUMBER only. Reading 'Chapter 11' in the header is less useful than seeing the chapter title.
  - Recommended change: Change \renewcommand{\sectionmark}[1]{\markboth{\thesection}{}} to \renewcommand{\sectionmark}[1]{\markboth{\thesection\ ---\ #1}{}} to show number and title. Use \truncate{} from the truncate package for long titles.
- [x] **lecture_10_part_ii.tex (Ch.18, Fuzzy Inf.) | Manual \markboth override | Line 3**
  - Review severity: `MEDIUM`
  - Issue: \markboth{Fuzzy inference}{} manually overrides the running header for this chapter, bypassing the fancyhdr setup. No other chapter does this. Likely a legacy artifact from standalone compilation.
  - Recommended change: Remove the \markboth{Fuzzy inference}{} command. The global \sectionmark handles this automatically.
- [ ] **lecture_1_intro.tex | SAE Levels comparison claim | Lines 217-219**
  - Review severity: `MEDIUM`
  - Issue: 'It is compatible with domain-specific taxonomies (e.g., SAE Levels 0-5 for automated driving)' -- this compatibility is asserted but not demonstrated. The SAE taxonomy is for driving automation, not general intelligent systems.
  - Recommended change: Either remove the SAE comparison or add a footnote showing the correspondence (e.g., SAE Level 0-1 ~ reactive/deliberative, Level 2-3 ~ adaptive, Level 4-5 ~ meta-cognitive with caveats).
- [ ] **lecture_transformers.tex (Ch.14) | Opinionated author note on LLMs | Lines 21-34**
  - Review severity: `MEDIUM`
  - Issue: The Perspective box states an opinion about language models not forming faithful world models. Scientifically defensible but presented without counterpoint.
  - Recommended change: Add: 'This view is widely held but debated; see [e.g., Bubeck et al. 2023 on GPT-4 capabilities, or Mitchell 2021 on AI reasoning] for alternative perspectives on what LLM competence implies.'

### LaTeX / Production
- [x] **Multiple chapters | graphicspath per chapter | Various**
  - Review severity: `MEDIUM`
  - Issue: Add global \graphicspath{{assets/}} in ece657_notes.tex as fallback. Document expected directory layout.
- [x] **appendix_logistics.tex | University-specific content in published book | Full appendix**
  - Review severity: `MEDIUM`
  - Issue: Add a prominent header box: FOR ECE 657 AT UNIVERSITY OF WATERLOO ONLY. Consider whether this appendix belongs in the published book at all, or is better distributed as a separate course handout.
- [x] **ece657_notes.tex | Running header (number only) | Lines 62-65**
  - Review severity: `MEDIUM`
  - Issue: Change \sectionmark to include chapter title: \markboth{\thesection --- #1}{}
- [x] **lecture_10_part_ii.tex | Manual \markboth override | Line 3**
  - Review severity: `MEDIUM`
  - Issue: Remove \markboth{Fuzzy inference}{} -- handled by global fancyhdr setup.

### Notation / Symbol Consistency
- [ ] **lecture_4_part_ii.tex (Ch.8, RBF) | phi vs varphi in RBF chapter | Lines 40-42**
  - Review severity: `MEDIUM`
  - Issue: The RBF chapter uses varphi_i(x) for basis functions, while the global notation section reserves phi(.) for kernel feature maps. This is a documented collision but needs verification that varphi is used consistently throughout Chapter 8.
  - Recommended change: Audit all of Chapter 8: confirm varphi (\varphi) is used for RBF basis functions everywhere, not phi (\phi), consistent with the Notation section convention.
- [ ] **lecture_supervised.tex (Ch.3) | Loss symbol: L vs script-L | Full chapter**
  - Review severity: `MEDIUM`
  - Issue: Verify that the loss function in Chapter 3 consistently uses calligraphic L (\mathcal{L}), not plain L, which the collision index reserves for number of layers or sequence length.
  - Recommended change: Run grep -n '\\mathcal{L}\|[^a-z]L[_^{]' lecture_supervised.tex to audit all loss symbol uses.
- [x] **notation.tex | Symbol table placement | Lines 6-51 vs 54-87**
  - Review severity: `MEDIUM`
  - Issue: The descriptive text ('This section collects book-wide notation...') appears AFTER the symbol table. Readers encounter the table without context.
  - Recommended change: Move introductory paragraph (lines 54-67) and the Conventions subsection header to BEFORE the table (before the \begingroup on line 6).
- [ ] **notation.tex | n: sequence length vs feature dimension collision | Lines 15-51**
  - Review severity: `MEDIUM`
  - Issue: The symbol n appears in the notation table as 'sequence length (tokens)' but is also used throughout supervised learning chapters for feature/input dimension. This is a collision not listed in Appendix D.
  - Recommended change: Add n to appendix_notation_collisions.tex: 'n: input feature dimension (supervised chapters); sequence length (NLP/Transformer chapters).'

### Pedagogy / Structure
- [ ] **All lecture files | Common pitfalls inconsistency | Various**
  - Review severity: `MEDIUM`
  - Issue: Common Pitfalls appears in some chapter summary boxes (Ch.1, 5, 6) but not others (Ch.8, 9, 10). This structural inconsistency is noticeable when reading sequentially.
  - Recommended change: Standardize every closing summary box to include: (a) Minimum viable mastery bullets, (b) Common pitfalls, and (c) Where we head next paragraph.
- [ ] **All lecture files | Learning Outcomes depth variance | Various**
  - Review severity: `MEDIUM`
  - Issue: Learning Outcomes boxes vary from 2 to 5 bullets. Some outcomes are orientation goals (navigate the book structure) rather than measurable learning objectives.
  - Recommended change: Standardize to 3-4 Bloom's taxonomy action-verb outcomes per chapter: define, derive, implement, compare, analyze, evaluate. Remove orientation/administrative outcomes.
- [ ] **Book-wide | Ethics coverage uneven | Ch.13 (NLP) only**
  - Review severity: `MEDIUM`
  - Issue: Bias/fairness considerations appear in Ch.13 (NLP) but are absent from CNN (Ch.11, facial recognition risks), Evolutionary Computing (Ch.19, objective gaming), and Fuzzy Systems (Ch.15-18, membership subjectivity in high-stakes decisions).
  - Recommended change: Add a short 'Ethical considerations' note (2-3 sentences) to at least Ch.11 (CNN), Ch.19 (Evo), and Ch.1 (intro). A dedicated ethics appendix would be the strongest solution.
- [ ] **Book-wide | Pseudocode absent | Various**
  - Review severity: `MEDIUM`
  - Issue: Several chapters reference 'pseudocode' in exercises but no formal algorithm pseudocode blocks exist. Graduate students need standard algorithmic notation.
  - Recommended change: Add \usepackage{algorithm, algpseudocode} to preamble. Add Algorithm environments for: Perceptron learning (Ch.5), Backpropagation (Ch.7), SOM training (Ch.9), Mamdani FIS inference (Ch.18), Canonical GA (Ch.19).
- [ ] **Book-wide | Reinforcement learning gap | Ch.5 mention only**
  - Review severity: `MEDIUM`
  - Issue: RL is mentioned briefly in Chapter 5 as a third learning paradigm but the book has no RL chapter. For an intelligent systems book this is a notable gap.
  - Recommended change: Add an RL overview section within Chapter 1 or 19, or an appendix, noting RL is outside the book scope and pointing to Sutton and Barto (2018) Reinforcement Learning: An Introduction as the standard reference.
- [ ] **lecture_1_intro.tex | Reading path references | Lines 415-420**
  - Review severity: `MEDIUM`
  - Issue: Three reading paths are defined. Verify the \Cref labels in each path resolve to correct chapter numbers, especially for the ML-focused path which should include Transformers.
  - Recommended change: Verify: ML path = Ch.3-4 -> Ch.5-7 -> Ch.8 -> Ch.11-13 -> Ch.14 (Transformers). Confirm all \Cref labels in reading paths resolve correctly.
- [ ] **lecture_3_part_i.tex (Ch.5) | Part II reference without Part definition | Line 67**
  - Review severity: `MEDIUM`
  - Issue: The heading 'Where this fits in Part II' appears in Chapter 5 but the book has no formal Part declarations in the main text (only Back matter uses \part*).
  - Recommended change: Either: (a) add formal \part declarations throughout the main document (Part I: Foundations, Part II: Neural Networks, Part III: Soft Computing), or (b) replace all 'Part II' references with 'the neural strand' or 'the neural chapters.'
- [ ] **lecture_8_part_i.tex (Ch.9, SOM) | U-matrix diagnostics | Line 78**
  - Review severity: `MEDIUM`
  - Issue: U-matrix and component planes are mentioned as diagnostics but if not formally defined with equations in the full chapter, students lack actionable tools.
  - Recommended change: Verify that the U-matrix (neighbor-distance heat map) is formally defined with equations and at least one worked example or figure in the complete chapter body.

### Priority Action Summary
- [ ] **appendix_notation_collisions.tex | Missing symbols | Full appendix**
  - Review severity: `MEDIUM`
  - Issue: Add n, d, phi vs varphi, W (weight vs embedding) to collision index.
- [ ] **book_appendices.tex | Appendix ordering | Full file**
  - Review severity: `MEDIUM`
  - Issue: Reorder: A=Notation Collisions, B=Reproducibility, C=Kernels, D=Linear Systems, E=Logistics.
- [ ] **ece657_notes.tex | Running headers show number only | Lines 62-65**
  - Review severity: `MEDIUM`
  - Issue: Add chapter title to running header via updated \sectionmark.
- [ ] **lecture_10_part_ii.tex | Manual \markboth override | Line 3**
  - Review severity: `MEDIUM`
  - Issue: Remove; handled by global fancyhdr.
- [ ] **notation.tex | Table before context text | Lines 6-51 vs 54-87**
  - Review severity: `MEDIUM`
  - Issue: Move introductory text to before the symbol table.
- [ ] **preface.tex | Prof. Karray attribution incomplete | Lines 10-12**
  - Review severity: `MEDIUM`
  - Issue: Acknowledge in both Preface and Acknowledgments.

### Scientific / Mathematical
- [ ] **appendix_linear_systems.tex | Bibliography entries for further reading | End of file**
  - Review severity: `MEDIUM`
  - Issue: nocite{Kailath1980, Chen1999LinearSystemTheoryDesign, Ogata2010} requires verification in refs.bib.
  - Recommended change: Verify: Kailath (1980) Linear Systems; Chen (1999) Linear System Theory and Design; Ogata (2010) Modern Control Engineering.
- [ ] **lecture_1_intro.tex | eq:auto:lecture_1_intro:1 | Lines 55-60**
  - Review severity: `MEDIUM`
  - Issue: Equation environment used for a natural-language transitivity rule (If A=B and B=C, then A=C). This is an inference rule pattern, not an algebraic equation. The auto-generated label clutters cross-referencing.
  - Recommended change: Remove the equation environment; render as a blockquote or inline text. If kept as display math, add a clarifying note that this illustrates an inference rule, not an algebraic identity.
- [ ] **lecture_3_part_i.tex (Ch.5) | Perceptron convergence theorem proof | Lines 393-430**
  - Review severity: `MEDIUM`
  - Issue: The proof assumes initialization w(0) = 0 implicitly (for the T*gamma lower bound) but does not state this explicitly in the proof setup.
  - Recommended change: Add after 'Assume there exists a unit vector w*': 'Initialize w(0) = 0. Then after T mistakes...' The proof is otherwise correct.
- [ ] **lecture_3_part_i.tex (Ch.5) | Update condition: <= 0 vs < 0 | Lines 353-355**
  - Review severity: `MEDIUM`
  - Issue: The update condition is stated as y(w^T x + b) <= 0 (updates on exact boundary ties), whereas the convergence theorem proof implicitly uses strict < 0. This is a valid variant but may confuse students comparing results.
  - Recommended change: Choose one convention. If <= 0 is kept (Rosenblatt original), add a footnote stating this. If < 0 is preferred, adjust the worked trace in lines 360-388 accordingly.
- [ ] **lecture_8_part_i.tex (Ch.12, RNN) | Foundational RNN citations | Line 65**
  - Review severity: `MEDIUM`
  - Issue: Citations {Elman1990, Bengio1994} are used as canonical RNN references but are not visible in the reviewed refs.bib excerpt. Needs verification.
  - Recommended change: Verify both exist in refs.bib: Elman (1990) Finding Structure in Time; Bengio et al. (1994) Learning Long-Term Dependencies with Gradient Descent is Difficult. Add entries if missing.
- [ ] **lecture_transformers.tex (Ch.14) | Bahdanau attention citation | Line 70**
  - Review severity: `MEDIUM`
  - Issue: Citation {Bahdanau2015} is used for the attention mechanism. Needs full bibliography verification.
  - Recommended change: Verify refs.bib entry: Bahdanau, Cho, Bengio (2015) Neural Machine Translation by Jointly Learning to Align and Translate, ICLR 2015.

## P3 Queue

### Academic / Scholarly Rigor
- [ ] **lecture_10_part_i.tex (Ch.10) | Hopfield1982 bibliography entry | Line 43**
  - Review severity: `LOW`
  - Issue: Verify the Hopfield1982 ref.bib entry is complete: journal = PNAS, volume = 79, number = 8, pages = 2554-2558.
  - Recommended change: Verify and complete the refs.bib entry.
- [ ] **lecture_10_part_ii.tex (Ch.15, Softcomp) | Zadeh1994 citation | Line 52**
  - Review severity: `LOW`
  - Issue: Citation {Zadeh1994} for soft computing. Canonical source: Zadeh (1994) Fuzzy logic, neural networks, and soft computing, CACM 37(3), 77-84.
  - Recommended change: Verify refs.bib entry matches this publication.
- [ ] **lecture_3_part_i.tex (Ch.5) | Rosenblatt inline citation | Line 323**
  - Review severity: `LOW`
  - Issue: 'introduced by Rosenblatt in 1958' -- the citation appears only in \nocite{Rosenblatt1958} at line 549, not inline at the point of introduction.
  - Recommended change: Add \citep{Rosenblatt1958} inline after 'introduced by Rosenblatt in 1958'.
- [ ] **lecture_8_part_i.tex (Ch.9, SOM) | Kohonen citation | Lines 24-26**
  - Review severity: `LOW`
  - Issue: 'introduced by Teuvo Kohonen' appears without a direct citation.
  - Recommended change: Add \citep{Kohonen1982} or \citep{Kohonen1990} after 'introduced by Teuvo Kohonen.'
- [ ] **preface.tex | Opening sentence phrasing | Line 3**
  - Review severity: `LOW`
  - Issue: 'courses that engage artificial intelligence' is non-idiomatic English.
  - Recommended change: Change to: 'courses that engage with artificial intelligence' or 'courses in artificial intelligence.'

### Editorial / Writing / Voice
- [ ] **Multiple chapters | citet vs citep usage | Various**
  - Review severity: `LOW`
  - Issue: Several citations use \citet (author-as-noun) in contexts where \citep (parenthetical) would be more appropriate, and vice versa.
  - Recommended change: Audit all \citet uses: \citet is correct only when the author is the grammatical subject of the sentence ('Russell and Norvig (2021) define...'). All other citations should use \citep.
- [ ] **Multiple chapters | e.g. parenthesization | Various**
  - Review severity: `LOW`
  - Issue: Some chapters use (e.g., ...) parenthetically; others use e.g., in running text without parentheses. Should be standardized.
  - Recommended change: Standard practice: always use parenthetical form (e.g., ...) in running text. Apply consistently across all chapters.
- [x] **ece657_notes.tex | \setcounter command syntax | Line 188**
  - Review severity: `LOW`
  - Issue: \setcounter{secnumdepth}3 is valid but unconventional (missing braces around the value).
  - Recommended change: Change to: \setcounter{secnumdepth}{3}
- [x] **ece657_notes.tex | captionsetup justification | Line 44**
  - Review severity: `LOW`
  - Issue: singlelinecheck=false forces all captions to be centered, including single-line captions. This can produce unusual layouts for very short captions.
  - Recommended change: Change global default to singlelinecheck=true. Apply centering selectively: \captionsetup[figure]{justification=centering, singlelinecheck=false}
- [ ] **lecture_11.tex (Ch.19, Evo) | Author's note on GA relevance | Lines 31-35**
  - Review severity: `LOW`
  - Issue: The note correctly defends GA relevance in 2026 but should briefly acknowledge competing approaches to avoid appearing one-sided.
  - Recommended change: Add a sentence acknowledging Bayesian optimization and model-based optimization as alternatives worth considering before choosing a GA approach.

### LaTeX / Production
- [x] **book_appendices.tex | Appendix ordering | Full file**
  - Review severity: `LOW`
  - Issue: Consider reordering: A = Notation Collisions (most consulted), B = Reproducibility Standards, C = Kernel Methods, D = Linear Systems Primer, E = Course Logistics (or remove from book).
- [x] **ece657_notes.tex | \setcounter{secnumdepth}3 | Line 188**
  - Review severity: `LOW`
  - Issue: Change to \setcounter{secnumdepth}{3} (add braces).
- [x] **ece657_notes.tex | captionsetup singlelinecheck | Line 44**
  - Review severity: `LOW`
  - Issue: Change global singlelinecheck to true; apply centering only to figure captions.

### Notation / Symbol Consistency
- [ ] **lecture_3_part_i.tex (Ch.5) | sign(0) vs sgn(0) inconsistency | Lines 160 vs 188-190**
  - Review severity: `LOW`
  - Issue: The text uses both 'sign(0)' and 'sgn(0)' for the same function. Notation note box uses 'sgn'; running text uses 'sign'.
  - Recommended change: Standardize to one spelling throughout Chapter 5: either always 'sgn' or always 'sign'. Update both lines 160 and the notation note box to match.
- [ ] **lecture_8_part_i.tex (Ch.11, CNN) | Illustrative arithmetic in equation environments | Lines 71-79**
  - Review severity: `LOW`
  - Issue: Simple calculations like '65,536 x 100 = 6,553,600' are wrapped in numbered equation environments with auto-generated labels. These are illustrative, not results to cross-reference.
  - Recommended change: Remove equation environments from illustrative arithmetic; use display math (\[...\]) without labels instead.

### Pedagogy / Structure
- [ ] **lecture_10_part_i.tex (Ch.10, Hopfield) | Missing Transformer connection | Lines 28-34**
  - Review severity: `LOW`
  - Issue: The energy-based memory framing anticipates modern Transformer attention but does not provide an explicit forward pointer.
  - Recommended change: Add: 'The modern Transformer attention mechanism (Chapter 14) can be interpreted as a continuous Hopfield network retrieval step (Ramsauer et al. 2021, Hopfield Networks is All You Need, ICLR); this connection is worth revisiting after Chapter 14.'

### Priority Action Summary
- [ ] **Multiple chapters | e.g. parenthesization | Various**
  - Review severity: `LOW`
  - Issue: Always use (e.g., ...) in running text.
- [x] **ece657_notes.tex | \setcounter{secnumdepth}3 | Line 188**
  - Review severity: `LOW`
  - Issue: Add braces: \setcounter{secnumdepth}{3}
- [ ] **lecture_3_part_i.tex | sign(0) vs sgn(0) | Lines 160 / 188-190**
  - Review severity: `LOW`
  - Issue: Standardize to one spelling throughout Ch.5.

### Scientific / Mathematical
- [ ] **lecture_1_intro.tex | Slagle citation | Line 68**
  - Review severity: `LOW`
  - Issue: 'James Slagle developed an early influential AI program' asserted without a citation.
  - Recommended change: Add: Slagle, J. R. (1963). A heuristic program that solves symbolic integration problems in freshman calculus. PhD thesis, MIT.
- [ ] **lecture_4_part_i.tex (Ch.7) | Loss + one-hot targets for classification | Lines 49-58**
  - Review severity: `LOW`
  - Issue: Using MSE loss with one-hot targets for classification is presented as the default but can produce outputs outside [0,1] without a constraining output activation. Cross-entropy is mentioned later but the caveat is not flagged early enough.
  - Recommended change: Add a Pitfall note: 'MSE with one-hot targets may produce out-of-range outputs for classification; cross-entropy with sigmoid/softmax output is preferred. See the cross-entropy derivation later in this chapter.'
