# Diagram code

These scripts regenerate the presentation diagrams with **Python + matplotlib**.

## Files

- `generate_capability_graph.py`
- `generate_architecture_graph.py`
- `generate_company_blueprint.py`
- `generate_all_diagrams.py`
- `diagram_utils.py`

## Usage

```bash
python generate_all_diagrams.py --outdir ../assets
```

or run any single script directly, for example:

```bash
python generate_architecture_graph.py --outdir ../assets
```

## Note

The packaged `assets/` folder contains the diagram PNGs that were used in the deck.  
The scripts are intended to regenerate **equivalent editable diagrams**, not bit-exact copies of the original PNG exports.
