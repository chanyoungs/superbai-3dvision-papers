# Slide text dump

This file is a literal text extraction from `vision_foundation_models_review.pptx`.

It preserves the slide wording as closely as possible. Time-sensitive notes from the deck are left untouched here, even if they are omitted from the cleaned report.

## Slide 1

```text
What DA3, MoGe-2, and VGGT mean
for our next vision model
```
- Compact review of architectures, benchmarks, and build implications for a strong 3D-aware vision foundation model.
- DA3  ·  any-view geometry
- MoGe-2  ·  metric monocular detail
- VGGT  ·  unified 3D backbone
- Architecture  •  Benchmarks  •  Company blueprint  •  Citation snapshot
- Key idea
- These papers converge on simple ViT-style backbones, but differ in representation choice, data curation, and what they optimize at inference time.
- 1

## Slide 2

- One-slide comparison
- Scope, geometry target, data recipe, and where each paper is strongest.
- Paper
- Input
- Representation
- Data
- Best at
- Caution
- MoGe-2
- 1 image
```text
Point map +
separate scale
```
```text
Synthetic +
refined real
```
```text
Metric mono
+ detail
```
```text
No multi-view
or tracks
```
- VGGT
```text
1 to 100+
images
```
```text
Cameras + depth
+ points + tracks
```
```text
Large mixed
3D-annotated sets
```
```text
Shared 3D
backbone
```
```text
Point head weaker
than depth+cam
```
- DA3
```text
1 to N, posed
or unposed
```
```text
Depth + ray
(+ optional cam)
```
```text
Public data +
teacher labels
```
```text
Any-view pose
+ recon
```
```text
Training cost;
dynamics later
```
- Capability snapshot
- Capability
- M2
- V
- D
- Metric mono
- H
- M
- M
- Any-view pose
- L
- H
- H
- Track transfer
- L
- H
- M
- 3DGS / NVS
- L
- H
- H
- Inference simplicity
- H
- M
- H
- Bottom line
- MoGe-2 is the cleanest answer for single-image metric geometry. DA3 is the current best any-view reconstruction bet. VGGT remains the most attractive general 3D backbone when we care about shared features and tracking.
- 2

## Slide 3

- How the three papers connect
- All three push toward scalable 3D geometry backbones, but they make different bets on representation and supervision.
- Convergence
```text
• Large DINO / ViT backbones plus dense prediction heads are now the default recipe.
• All three papers show that geometry quality scales with better data, not only fancier 3D modules.
```
- Divergence
```text
• DA3 argues for a minimal depth-ray target.
• MoGe-2 explicitly decouples metric scale from relative geometry.
• VGGT leans into many auxiliary outputs to regularize a shared backbone.
```
- Synthesis
```text
• Train with redundancy only when it improves representation learning.
• At deployment, prefer simpler, derived outputs that are easier to calibrate and trust.
```
- 3

## Slide 4

- Architectures at a glance
- Our diagrams compress each model to the part that matters most for system design.
- MoGe-2
- Decouple global scale from relative geometry.
- VGGT
- One backbone, many 3D outputs.
- DA3
- Minimal depth + ray target for any-view fusion.
- 4

## Slide 5

- Any-view geometry: DA3 moves the frontier
- Pose, feed-forward novel view synthesis, and scalability all improve over the earlier VGGT generation.
- Why this matters: DA3 is not just a better benchmark number; its smaller variants also scale to more views and higher throughput, making it the strongest current candidate for an any-view production backbone.
- 5

## Slide 6

- MoGe-2 closes the monocular accuracy–detail gap
- The paper’s core contribution is not only a stronger head, but a stronger data-cleaning story.
- Why it works
```text
1) Representation. Predict affine-invariant geometry, then recover metric scale with a separate CLS-token MLP head.
2) Data. 
Use synthetic predictions to filter noisy real depth locally and fill holes with edge-preserving completion.
3) Outcome. 
You retain strong geometry while getting much closer to Depth Pro’s sharpness.
```
- Ablation cues from the paper
- Finding
- Before
- After
- Metric depth rank
```text
3.83
(Depth Pro)
```
```text
1.95
(MoGe-2)
```
- Sharpness rank
```text
1.50
(Depth Pro)
```
```text
1.75
(MoGe-2)
```
- Refined real data F1
```text
10.3
(raw real)
```
```text
12.5
(refined)
```
- Interpretation: use MoGe-2-style scale decoupling and real-data refinement even if the final company model is multi-view.
- 6

## Slide 7

- Recommended blueprint for our company model
- Combine the strongest ideas instead of copying any one paper wholesale.
- Recommended synthesis = MoGe-2 metric head + DA3 depth-ray geometry + VGGT multi-output reuse
- Backbone
```text
• One shared ViT / DINO encoder with adaptive 1→N view attention.
• Train at multiple resolutions so monocular and multi-view modes share tokens.
```
- Heads
```text
• Default inference path: monocular metric head for 1 view, depth+ray + camera head for multi-view.
• Keep a track head and NVS head as reusable downstream adapters, not the core product output.
```
- Data + eval
```text
• Invest in a data engine: synthetic detail, refined real metric data, public multi-view 3D sets, and later in-domain capture.
• Benchmark pose, reconstruction, sharpness, tracking, NVS, and latency together.
```
- 7

## Slide 8

- Decision matrix and launch checklist
- Use the papers as complementary building blocks, then prove the stack with a broader eval harness than any single paper uses.
- Use case
- Default recipe
- Why
- Single-image metric perception
- MoGe-2-style metric head on shared backbone
- Best metric/detail trade-off in the review.
- Sparse unposed multi-view recon
- DA3 depth + ray (+ optional camera head)
- Strongest pose-free geometry and better view scalability.
- Track-heavy world model / video understanding
- VGGT-style shared track and camera head
- Best transfer story for shared 3D features.
- Edge or real-time deployment
- Distilled small/base variants
- Both DA3 and MoGe-2 show strong scaling benefits at smaller sizes.
- Launch checklist
```text
• Pose AUC, reconstruction F1/CD, and boundary sharpness all on the same held-out scenes.
• Latency + memory measured at 1 / 4 / 12 / 32 views, not just a single benchmark setting.
• Downstream checks: 3DGS / NVS, tracking, and any in-product perception tasks.
• OOD stress tests: thin structures, non-rigid scenes, fisheye/panoramas, and large scale ambiguity.
```
- Known paper-side failure modes
```text
• Dynamic / non-rigid motion is still a weak spot for DA3 and VGGT.
• Very fine wires, hair, and extreme foreground/background scale gaps remain hard for MoGe-2.
• Fisheye / panoramic imagery is explicitly called out as a limitation for VGGT.
```
- 8

## Slide 9

- Citations and reference snapshot
- The bibliographic references below are the versions used for this review; citation counts are only rough adoption signals and will move quickly.
- VGGT
- Wang, J., Chen, M., Karaev, N., Vedaldi, A., Rupprecht, C., & Novotny, D. (2025). VGGT: Visual Geometry Grounded Transformer. CVPR 2025.
- MoGe-2
- Wang, R., Xu, S., Dong, Y., Deng, Y., Xiang, J., Lv, Z., Sun, G., Tong, X., & Yang, J. (2025). MoGe-2: Accurate Monocular Geometry with Metric Scale and Sharp Details. arXiv:2507.02546.
- DA3
- Lin, H., Chen, S., Liew, J. H., Chen, D. Y., Li, Z., Shi, G., Feng, J., & Kang, B. (2025). Depth Anything 3: Recovering the Visual Space from Any Views. arXiv:2511.10647.
- Status / project snapshot
- Paper
- Status
- Availability
- VGGT
```text
CVPR 2025
Best Paper
```
- Project page + GitHub
- MoGe-2
```text
arXiv
Jul 2025
```
- Project page + code
- DA3
```text
arXiv 2025
ICLR 2026 Oral
```
- Project page + GitHub
- Citation snapshot (web, Mar 2026)
- Paper
- Approx.
- Source
- VGGT
- 792
- arXiv snippet
- MoGe-2
- 70
- arXiv snippet
- DA3
- 45
- OpenReview snippet
- Use counts only as weak adoption signals; the numbers move quickly and should not drive the model decision by themselves.
- 9
