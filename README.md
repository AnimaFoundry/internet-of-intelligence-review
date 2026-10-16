# Low-Power Sensing for an Internet of Intelligence

**Materials, Distributed Architectures, and World-Model Learning**  
AnimaFoundry | Review preprint v1.0.0 | 16 October 2026

Read the [paper (PDF)](paper.pdf) or [web-readable version](paper.md).

This English critical integrative review connects small sensing materials and energy budgets, implemented IoT and chip architectures, world-model learning, and the return of validated capabilities to heterogeneous endpoints. It cites 49 selected works and includes five comparison tables, an original schematic, explicit hypothetical calculations, and a falsifiable research agenda. Section 10 presents AnimaFoundry's motivating research vision.

**Status:** not peer reviewed. This is a selective literature synthesis, not a systematic review, a new-material invention, or an experimentally validated platform. Reported experiments belong to their cited authors. The accompanying calculations reproduce assumptions and arithmetic; they do not reproduce hardware or model performance.

## Evidence and source files

- [manuscript.md](manuscript.md): editable source with stable reference identifiers.
- [references.json](references.json): bibliographic records, source links, evidence types, and actual reading scope.
- [METHODS.md](METHODS.md): selection method, representative searches, exclusions, and limitations.
- [budget_example.json](budget_example.json): hypothetical traffic, throughput, and update-energy calculations.
- [SOURCE_AND_RIGHTS.md](SOURCE_AND_RIGHTS.md): authorship, attribution, rights, and dependency boundaries.
- [RELEASE_MANIFEST.json](RELEASE_MANIFEST.json): explicit published-file inventory and SHA-256 checksums.

## Rebuild and check

Use Python 3.12 in a fresh virtual environment. From the repository root:

```sh
python -m pip install -r requirements.txt
python scripts/verify_paper.py
python scripts/budget_example.py
python scripts/build_paper.py --destination build/reproduced
python scripts/verify_paper.py --rebuild build/reproduced
```

The checks cover reference resolution, declared numerical examples, the release file manifest, PDF text completeness, and reproduction of the PDF, readable manuscript, and original schematic. They do not validate the scientific truth of cited results. Rendering inspection is a separate editorial check. The PDF uses standard PDF fonts and a fixed build timestamp for reproducibility.

For visual inspection with Poppler:

```sh
pdftoppm -png -scale-to 1200 paper.pdf build/page
```

The build performs no network access. Dependency installation requires the package index. No source papers, model weights, or operational datasets are redistributed.

## Citation and corrections

See [CITATION.cff](CITATION.cff). Cite the version or commit used. Please report a specific passage and supporting primary source when proposing a correction. Changes to substantive claims require a new manuscript version; a GitHub release is not journal acceptance or external peer review.

## License

Original text and schematic: **CC BY 4.0**, with full terms in [LICENSE-TEXT](LICENSE-TEXT). Original scripts: **MIT**, in [LICENSE-CODE](LICENSE-CODE). The [license notice](LICENSE) identifies the scope. Referenced works retain their own rights; neither this review nor these licenses provides patent freedom to operate.
