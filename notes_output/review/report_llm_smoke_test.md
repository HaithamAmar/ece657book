# Scientific QA Report

- Source PDF: `notes_output/ece657_notes.pdf`
- Total chunks: 1

## Chunk 1/126
- Character range: 0–7025

```text
Modern Intelligent Systems: A Graduate Companion
  Neural Networks, Fuzzy Logic, and Evolutionary Optimization

                        Haitham Amar

                      First edition, 2026
Modern Intelligent Systems: A Graduate Companion
Neural Networks, Fuzzy Logic, and Evolutionary Optimization

Copyright (c) 2026 Haitham Amar
All rights reserved.

No part of this book may be reproduced or transmitted in any form or by any means,
electronic or mechanical, including photocopying, recording, or any information storage
and retrieval system, without prior written permission of the copyright holder, except
where permitted by law.

This book is provided for educational purposes. The author makes no warranties of any
kind and assumes no responsibility for errors or omissions or for damages resulting from
the use of the information contained herein.

First edition, 2026
Published by Haitham Amar
Typeset in LaTeX.
Modern Intelligent Systems



Preface
Over time, through teaching courses that engage artificial intelligence both
directly—through machine learning and neural networks—and indirectly, at the
level of data collection and system design, a recurring gap became apparent.
While the literature offers many excellent treatments of individual techniques,
it rarely provides a coherent path that guides students from the foundational
notions of intelligence to the most advanced models used today. What is often
missing is a unified narrative that connects intuition, mathematical formulation,
and practical deployment across the diverse tools that constitute intelligent sys-
tems.
    Courses in machine learning tend to emphasize neural networks and deep
learning; others focus on optimization and operations research, from classical
search strategies to genetic algorithms. Each approach is valuable, yet time
constraints and disciplinary boundaries often force a narrowing of scope, sacri-
ficing breadth for depth or vice versa. In one course in particular, a broader
framework emerged—one that treated these methods not as isolated topics, but
as complementary responses to recurring modeling challenges. That framework,
though not originally mine, proved invaluable: it allowed students to situate
linear regression, neural networks, transformers, fuzzy inference systems, and
evolutionary algorithms within a single, coherent perspective on intelligent sys-
tem design. This book is an attempt to make that perspective explicit and
durable.
    This book has evolved into a concise graduate companion that blends the
original chapter voice of ECE 657 with laboratory-style checklists and reflective
prompts. The chapters move from supervised learning foundations to fuzzy
logic and evolutionary computing, mirroring the trajectory of the original course
material while adding connective tissue so that a reader can revisit the material
years later without hunting for missing context.

Origins in ECE 657
In 2019, I was asked to teach ECE 657 at the University of Waterloo. At the time,
the course leaned heavily toward soft computing, and fuzzy inference systems
had constituted a large portion of the material in earlier offerings. Prof. Karray,
who built the course, felt it was time to broaden its scope beyond that single


                                        3
Modern Intelligent Systems


paradigm, and he was generous enough to let me reshape the arc of the course.
    Over the following years, I came to view fuzzy inference systems as one im-
portant piece in a larger mosaic rather than the organizing principle. I iterated
on the syllabus—moving topics, adding and removing chapters, and tightening
mathematical through-lines—toward a narrative that is coherent, broad in cov-
erage, and implementable by an engineer.
    In the first edition (2026), the field is in the era of large language models,
and this book covers them (see Chapters 13 and 14). But it also emphasizes
other ideas and toolkits that may underwrite future breakthroughs in intelligent
systems: careful probabilistic thinking and diagnostics, principled optimization,
sequence modeling beyond any single architecture, and hybrid reasoning ap-
proaches that have repeatedly re-emerged in new forms.
    The material has since been rewritten to stand alone as a book. Any offering-
specific details (schedules, grading, local policies) now live in Appendix C (espe-
cially Using this book in ECE 657 ); readers outside that course can ignore the
appendix entirely.
 Perspective
 This book prioritizes ideas that survived multiple paradigm shifts. It
 emphasizes principles that remain useful even as architectures and tooling
 change.

    For a practical reader’s guide—roadmap, prerequisites, and suggested read-
ing paths—see the final sections of Chapter 1. Notation and reading conventions
are collected up front in Notation and Conventions.
    The result is a self-contained reference for researchers and engineers who want
a rigorous but narrative-friendly treatment of neural networks, soft computing,
and hybrid reasoning systems.




                                        4
Modern Intelligent Systems



Acknowledgments
This book grew out of teaching and revising the ECE 657 material over multiple
offerings. I am grateful to the students whose questions and feedback repeatedly
exposed where explanations were brittle and where the narrative needed better
bridges between intuition, math, and practice.
I also thank colleagues who shared perspectives on how these topics fit together
as an engineering discipline rather than as isolated techniques. Any remaining
errors and omissions are my responsibility.




                                       5
Modern Intelligent Systems                                                 Contents



Contents

Preface                                                                          3

Acknowledgments                                                                  5

Notation and Conventions                                                        30


Part I: Foundations and the ERM toolbox                                         33

1 About This Book                                                               33
  1.1  Historical Foundations of Intelligent Systems . . . . . . . .            33
  1.2  Defining Artificial Intelligence and Intelligent Systems . . .           36
  1.3  Intelligent Systems . . . . . . . . . . . . . . . . . . . . . . .        37
  1.4  Case Study: AI-Enabled Camera as an Intelligent System .                 39
  1.5  Levels and Architectures of Intelligent Systems . . . . . . .            41
  1.6  Intelligent Systems and Intelligent Machines . . . . . . . . .           44
  1.7  Levels, Meta-cognition, and Safety . . . . . . . . . . . . . .           46
  1.8  Audience, Prerequisites, and Scope . . . . . . . . . . . . . .           47
  1.9  Roadmap and Reading Paths . . . . . . . . . . . . . . . . .              48
  1.10 Using and Navigating This Book . . . . . . . . . . . . . . .             49
```

### Findings
- No scientific or mathematical content is presented in this chunk; it consists primarily of front matter, preface, acknowledgments, and table of contents.
- The preface and introductory remarks are clear, logically structured, and free of ambiguous claims or inconsistent notation.
- The scope and motivation for the book are well explained, with no logical gaps or unsupported statements.
- The mention of chapters and topics aligns with a coherent narrative for a graduate-level text.
- No definitions or technical terms are introduced here that require verification or clarification.
- The copyright and publication information are standard and appropriate.

**Conclusion:** No issues spotted.
