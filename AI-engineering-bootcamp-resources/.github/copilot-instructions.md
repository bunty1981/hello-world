# Copilot / AI Agent Instructions

This repository is a collection of Jupyter notebooks used for an educational course. These notes are concise, action-oriented guidelines for an AI coding assistant to be immediately productive here.

1. Repo big picture
- Purpose: a set of section folders (named `secXX-...`) containing three notebooks each: `*_Lectures.ipynb`, `*_Exercises.ipynb`, and `*_Solutions.ipynb`.
- Primary artifacts: Jupyter notebooks located under top-level folders like `sec12-53-python-variables/` and `sec18-iterations/`.

2. Important conventions to preserve
- Notebook metadata: Cells include a `metadata.id` and `metadata.language`. When programmatically editing notebooks, preserve `metadata.id` exactly and do not strip language metadata.
- Exercise pattern: Many code cells are intentionally blank (placeholders). Do not auto-fill exercises unless the user explicitly asks.
- Naming: Section directories follow `secNN-<slug>/` and notebook filenames include `Lectures`, `Exercises`, or `Solutions`.

3. Typical developer workflows (how to run/edit notebooks)
- Create an isolated Python environment and install Jupyter tools: ``python3 -m venv .venv``; ``source .venv/bin/activate``; ``pip install jupyter nbformat``.
- Run interactively: ``jupyter lab`` or ``jupyter notebook`` in the repo root.
- Execute a notebook headlessly (useful for CI or testing a change):
  ``jupyter nbconvert --to notebook --execute --inplace path/to/notebook.ipynb``
- Convert a notebook to a script for quick editing: ``jupyter nbconvert --to script path/to/notebook.ipynb``

4. Programmatic editing guidance (examples)
- Use the `nbformat` library to read/modify notebooks and always write back with the same cell `metadata.id` fields preserved. Minimal example:

```python
import nbformat
nb = nbformat.read('sec18-iterations/Sequences_Exercises.ipynb', as_version=4)
# modify nb.cells[n].source but keep nb.cells[n].metadata intact
nbformat.write(nb, 'sec18-iterations/Sequences_Exercises.ipynb')
```

5. Project-specific caveats and patterns
- Some exercise cells may contain accidental syntax issues or test artifacts. Example: `sec18-iterations/Sequences_Exercises.ipynb` contains a malformed line around a list operation (you may see stray quotes or unfinished prints). Validate code before executing notebooks automatically.
- Solutions notebooks often contain the canonical answers; prefer editing Exercises rather than Solutions unless instructed.

6. Integration and dependencies
- No top-level `requirements.txt` or explicit CI was found in the repository root. Assume minimal Python 3 environment is required. If you need to run notebooks, install `jupyter` and `nbformat`.

7. When to ask for human review
- Before populating multiple exercise cells, running the whole notebook, or changing cell metadata ids — request confirmation.
- If you find non-obvious changes across many notebooks, summarize proposed edits and get approval.

8. Useful file examples to reference
- Example exercise notebook: `sec18-iterations/Sequences_Exercises.ipynb`
- Directory pattern: `sec12-53-python-variables/`, `sec13-59-python-syntax-arithmetic-operators/`, etc.

If any of these points are unclear or you'd like the agent to follow stricter rules (for example: never modify Solutions notebooks), tell me which rule to prefer and I will update this file.
