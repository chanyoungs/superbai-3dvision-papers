# Visuals manifest

This file explains what each regenerated visual represents and whether it is a direct chart/table reproduction or a synthesized explanatory figure.

| File | Type | Provenance | Notes |
|---|---|---|---|
| `diagrams/01_title_concept.png` | conceptual map | synthesized from all five papers | Bubble map used for deck framing only. |
| `diagrams/02_exec_synthesis_scatter.png` | qualitative scatter | synthesized from all five papers | Directional placement only; not a paper-reported metric plot. |
| `diagrams/03_comparison_table.png` | summary table | data-backed from paper-reported results | Combines key reported results and architectural descriptors. |
| `diagrams/04_wildtrack_bar.png` | bar chart | data-backed from ReST / MCBLT / UMPN | Uses reported WildTrack IDF1 and MOTA values. |
| `diagrams/05_taxonomy_arch.png` | architecture taxonomy | synthesized from method sections | Groups the papers into late-graph, early-BEV, and learned-association patterns. |
| `diagrams/06_rest_pipeline.png` | pipeline diagram | synthesized from ReST method section | Explains ReST’s spatial-first then temporal graph flow. |
| `diagrams/07_mcblt_pipeline.png` | pipeline diagram | synthesized from MCBLT method section | Shows early BEV fusion, 2D–3D association, and long-term memory block. |
| `diagrams/08_aicity_ablation.png` | line chart | data-backed from MCBLT Table 5 | Uses exact HOTA / AssA values from the uploaded PDF. |
| `diagrams/09_umpn_dynamic_graph.png` | graph diagram | synthesized from One Graph / UMPN method section | Highlights view, temporal, contextual, and optional camera edges. |
| `diagrams/10_scout_scene_priors.png` | grouped bar chart | data-backed from UMPN Table 4 | Uses exact SCOUT values with and without scene priors. |
| `diagrams/11_association_heads.png` | module diagram | synthesized from CAMELTrack and MOTIP method sections | Shows how their learned association ideas can be ported into MTMC. |
| `diagrams/12_company_blueprint.png` | recommended blueprint | synthesized from all five papers | Presentation recommendation, not a paper-native system. |

## Exact data-backed visuals

The following visuals use direct numeric values from the source papers:

- `03_comparison_table.png`
- `04_wildtrack_bar.png`
- `08_aicity_ablation.png`
- `10_scout_scene_priors.png`

## Synthesized explanatory visuals

The remaining figures are interpretive diagrams created for the presentation to make the methods comparable and to communicate a recommended company architecture.
