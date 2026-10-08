# AMO practice-paper reviews

Reviews of the AMO Level 1 practice papers against the AMO Vertical Syllabus v5.9.

- `reviews/classN/README.md`: summary for each class. The `paperN.md` files have question-by-question notes.
- `reviews/syllabus_visual_rules.md`: number-line and colour checks (Visual Standards rules 9 and 12c).
- `fixes/classN/*.json`: the text fixes applied to each paper. `cover.json` is applied to every paper.
- `tools/apply_fixes.py`: makes the v3 DOCX from v2 (`python3 tools/apply_fixes.py SRC OUT CLASS fixes/classN`). PDFs are rebuilt with `soffice --headless --convert-to pdf`.
- `papers/classN_vX/`: the corrected DOCX and PDF files, with a zip of each class (Classes 1–2 v2→v3; Classes 3–4 v3→v4). PDFs need the LibreOffice Math module (`libreoffice-math`), otherwise the equations (fractions) disappear.
- `tools/blueprint_check.py`: checks the chapter counts, the Easy/Medium mix and the Section II pairs against the syllabus workbook.
