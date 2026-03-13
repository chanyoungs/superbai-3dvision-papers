const pptxgen = require('pptxgenjs');
const {
  imageSizingContain,
  warnIfSlideHasOverlaps,
  warnIfSlideElementsOutOfBounds,
  calcTextBox,
} = require('/home/oai/skills/slides/pptxgenjs_helpers');
const path = require('path');

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'OpenAI';
pptx.company = 'OpenAI';
pptx.subject = 'Latest MTMC models and recommendations';
pptx.title = 'Latest MTMC models and papers';
pptx.lang = 'en-US';
pptx.theme = {
  headFontFace: 'Aptos Display',
  bodyFontFace: 'Aptos',
  lang: 'en-US'
};
pptx.defineLayout({ name:'CUSTOM', width:13.333, height:7.5 });
pptx.layout = 'CUSTOM';
pptx.background = { color: 'F7F8FA' };
pptx.theme = {
  headFontFace: 'Aptos Display',
  bodyFontFace: 'Aptos',
  lang: 'en-US'
};

const C = {
  navy: '18323F',
  blue: '2A5B76',
  teal: '2A9D8F',
  muted: '5B6770',
  light: 'EEF3F6',
  sand: 'F4EFE6',
  purple: 'EDE8F6',
  gray: 'D8DEE3',
  black: '1E2226',
  white: 'FFFFFF'
};

const img = (name) => path.join('/mnt/data/mtmc_pkg/images', name);

function addHeader(slide, title, subtitle='') {
  slide.addText(title, { x:0.55, y:0.28, w:8.6, h:0.45, fontFace:'Aptos Display', fontSize:26, bold:true, color:C.navy, margin:0 });
  if (subtitle) slide.addText(subtitle, { x:0.58, y:0.78, w:8.8, h:0.28, fontSize:10.5, color:C.muted, margin:0 });
  slide.addShape(pptx.ShapeType.line, { x:0.55, y:1.08, w:12.1, h:0, line:{ color:'D4DCE2', pt:1.1 } });
}

function addFooter(slide, txt='MTMC survey · Mar 2026') {
  slide.addText(txt, { x:0.55, y:7.08, w:4.0, h:0.18, fontSize:8.5, color:'748089', margin:0 });
}

function bulletLines(items, fontSize=18, color=C.black) {
  const runs = [];
  items.forEach((t, i) => {
    runs.push({ text: '• ' + t + (i < items.length-1 ? '\n' : ''), options: { bullet: { indent: 14 }, breakLine:false } });
  });
  return { text: runs, options: { fontSize, color, breakLine:false } };
}

function addBullets(slide, items, box, fontSize=18) {
  const text = items.map(t => ({ text: t, options: { bullet: { indent: 14 }, breakLine: true } }));
  slide.addText(text, { ...box, fontSize, color:C.black, paraSpaceAfterPt:10, breakLine:true, margin:2 });
}

function addNotes(slide, lines) {
  slide.addNotes(lines.join('\n'));
}

// Slide 1
{
  const s = pptx.addSlide();
  s.background = { color:'F7F8FA' };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:13.333, h:7.5, fill:{ color:'F7F8FA' }, line:{ color:'F7F8FA', transparency:100 } });
  s.addText('Latest MTMC models\nand how to build the next one', {
    x:0.65, y:0.85, w:5.2, h:1.8, fontFace:'Aptos Display', fontSize:28, bold:true, color:C.navy,
    margin:0
  });
  s.addText('Survey review through 12 Mar 2026', { x:0.68, y:2.85, w:3.8, h:0.28, fontSize:12.5, color:C.muted, margin:0 });
  s.addText('Report + recommendations for a production-focused MTMC team', { x:0.68, y:3.18, w:4.7, h:0.35, fontSize:14, color:C.black, margin:0 });
  s.addImage({ path: img('taxonomy.png'), ...imageSizingContain(img('taxonomy.png'), 5.95, 0.68, 6.8, 5.75) });
  s.addShape(pptx.ShapeType.roundRect, { x:0.66, y:4.05, w:3.9, h:1.2, rectRadius:0.08, fill:{ color:'EDF3F7' }, line:{ color:'D4DCE2', pt:1 } });
  s.addText('Focus of this deck\n• model families\n• latest benchmark context\n• recommended hybrid stack', { x:0.9, y:4.28, w:3.35, h:0.8, fontSize:15, color:C.black, margin:0, breakLine:true });
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- Generated figure: images/taxonomy.png from src/build_assets.py',
    '- MCTR https://arxiv.org/abs/2408.13243',
    '- GMT https://arxiv.org/abs/2407.01007',
    '- ADA-Track https://openaccess.thecvf.com/content/CVPR2024/html/Ding_ADA-Track_End-to-End_Multi-Camera_3D_Multi-Object_Tracking_with_Alternating_Detection_and_CVPR_2024_paper.html',
    '- ADA-Track++ https://arxiv.org/abs/2405.08909',
    '- MCBLT https://arxiv.org/abs/2412.00692',
    '- ADMCMT https://openaccess.thecvf.com/content/CVPR2025/html/Fan_All-Day_Multi-Camera_Multi-Target_Tracking_CVPR_2025_paper.html',
    '[/Sources]'
  ]);
}

// Slide 2
{
  const s = pptx.addSlide();
  addHeader(s, 'Executive summary', 'What changed in MTMC research over the last two years');
  addBullets(s, [
    'Cross-camera identity is moving from heuristic post-processing to learned global association (MCTR, GMT).',
    'A shared 3D / world state is increasingly the strongest way to stabilize handoff across views (ADA-Track++, MCBLT, Sparse4D-OI).',
    'Deployment constraints now matter explicitly: online mode, camera-only inference, low-light, low-FPS, and calibration-light setups.'
  ], { x:0.7, y:1.45, w:5.35, h:2.45 }, 18);
  s.addShape(pptx.ShapeType.roundRect, { x:0.72, y:4.24, w:5.2, h:1.35, rectRadius:0.05, fill:{ color:'EAF4F1' }, line:{ color:'C9DDD9', pt:1 } });
  s.addText('Bottom line:\nUse a world-coordinate query memory, learn association inside the perception loop, and keep a slower global cleanup path.', { x:0.95, y:4.5, w:4.75, h:0.82, fontSize:17, color:C.black, bold:false, margin:0 });
  s.addImage({ path: img('timeline.png'), ...imageSizingContain(img('timeline.png'), 6.15, 1.35, 6.6, 4.95) });
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- Generated figure: images/timeline.png from src/build_assets.py',
    '- MCTR https://arxiv.org/abs/2408.13243',
    '- GMT https://arxiv.org/abs/2407.01007',
    '- ADA-Track https://openaccess.thecvf.com/content/CVPR2024/html/Ding_ADA-Track_End-to-End_Multi-Camera_3D_Multi-Object_Tracking_with_Alternating_Detection_and_CVPR_2024_paper.html',
    '- AI City 2025 overview https://arxiv.org/html/2508.13564v1',
    '- Sparse4D outside-in https://arxiv.org/abs/2601.10819',
    '[/Sources]'
  ]);
}

// Slide 3
{
  const s = pptx.addSlide();
  addHeader(s, 'Taxonomy of the current MTMC landscape');
  s.addImage({ path: img('taxonomy.png'), ...imageSizingContain(img('taxonomy.png'), 0.6, 1.35, 8.3, 5.7) });
  s.addShape(pptx.ShapeType.roundRect, { x:9.15, y:1.55, w:3.55, h:4.95, rectRadius:0.05, fill:{ color:'F4F7FA' }, line:{ color:'D7E0E6', pt:1 } });
  s.addText('How to read the field', { x:9.45, y:1.83, w:2.7, h:0.3, fontSize:18, bold:true, color:C.navy, margin:0 });
  addBullets(s, [
    '2D global association: simpler stack, strongest when cameras overlap a lot.',
    '3D query-based: most elegant joint perception + association story.',
    'Geometry-first / BEV: often strongest in structured challenge settings.',
    'Multimodal: important only when lighting is a real failure mode.',
    'Calibration-light / deployment: crucial for operational reality.'
  ], { x:9.32, y:2.2, w:3.1, h:3.8 }, 15.5);
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- Generated figure: images/taxonomy.png from src/build_assets.py',
    '- MCBLT https://arxiv.org/abs/2412.00692',
    '- ADMCMT https://openaccess.thecvf.com/content/CVPR2025/html/Fan_All-Day_Multi-Camera_Multi-Target_Tracking_CVPR_2025_paper.html',
    '- CALIBFREE https://openreview.net/forum?id=4kb6vectZ3',
    '- DGT https://www.nature.com/articles/s41598-026-35768-z',
    '[/Sources]'
  ]);
}

// Slide 4
{
  const s = pptx.addSlide();
  addHeader(s, 'Dataset and benchmark landscape');
  s.addImage({ path: img('dataset_landscape.png'), ...imageSizingContain(img('dataset_landscape.png'), 0.65, 1.35, 7.15, 5.55) });
  s.addShape(pptx.ShapeType.roundRect, { x:8.05, y:1.5, w:4.6, h:5.1, rectRadius:0.05, fill:{ color:'F4F7FA' }, line:{ color:'D7E0E6', pt:1 } });
  s.addText('Why the benchmarks matter', { x:8.35, y:1.8, w:3.6, h:0.3, fontSize:18, bold:true, color:C.navy, margin:0 });
  addBullets(s, [
    'WILDTRACK: calibrated overlapping pedestrians; still useful for geometry and transfer stress tests.',
    'MMPTrack: indoor people benchmark that exposes occlusion-heavy retail failure cases.',
    'M3Track: first strong all-day RGBT MCMT dataset.',
    'AI City 2025 Track 1: most important recent pressure test for large-scale 3D MTMC.'
  ], { x:8.22, y:2.15, w:4.1, h:3.65 }, 15.5);
  s.addText('Rule of thumb: pick your benchmark by deployment regime, not by convenience.', { x:8.35, y:5.95, w:3.7, h:0.42, fontSize:15.5, color:C.black, italic:true, margin:0 });
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- Generated figure: images/dataset_landscape.png from src/build_assets.py',
    '- CityFlow https://arxiv.org/abs/1903.09254',
    '- WILDTRACK https://www.epfl.ch/labs/cvlab/data/data-wildtrack/',
    '- M3Track / ADMCMT https://openaccess.thecvf.com/content/CVPR2025/html/Fan_All-Day_Multi-Camera_Multi-Target_Tracking_CVPR_2025_paper.html',
    '- AI City 2025 overview https://arxiv.org/html/2508.13564v1',
    '[/Sources]'
  ]);
}

// Slide 5
{
  const s = pptx.addSlide();
  addHeader(s, 'Family 1: 2D global association', 'The field is moving beyond “single-camera tracks first, cross-camera cleanup later”');
  s.addShape(pptx.ShapeType.roundRect, { x:0.72, y:1.55, w:6.75, h:0.42, rectRadius:0.03, fill:{ color:C.blue }, line:{ color:C.blue, pt:1 } });
  s.addText('Model', { x:0.9, y:1.67, w:0.9, h:0.16, fontSize:13.5, bold:true, color:C.white, margin:0 });
  s.addText('Key idea', { x:2.0, y:1.67, w:2.0, h:0.16, fontSize:13.5, bold:true, color:C.white, margin:0 });
  s.addText('Headline', { x:4.9, y:1.67, w:1.6, h:0.16, fontSize:13.5, bold:true, color:C.white, margin:0 });
  const rows5 = [
    { y:2.02, fill:'FFFFFF', model:'MCTR', idea:'End-to-end tracking + association modules on top of DETR-like detection', res:'71.81 HOTA / 80.21 IDF1 / 91.19 MOTA on MMPTrack industry; 9 FPS' },
    { y:2.82, fill:'F7FAFC', model:'GMT', idea:'Use global trajectories across views as the primary object', res:'Up to +21.3% CVMA / +17.2% CVIDF1 over prior two-stage methods' }
  ];
  rows5.forEach(r => {
    s.addShape(pptx.ShapeType.roundRect, { x:0.72, y:r.y, w:6.75, h:0.7, rectRadius:0.02, fill:{ color:r.fill }, line:{ color:'D6DEE4', pt:1 } });
    s.addText(r.model, { x:0.9, y:r.y+0.17, w:0.9, h:0.2, fontSize:13.5, color:C.black, margin:0 });
    s.addText(r.idea, { x:2.0, y:r.y+0.11, w:2.55, h:0.42, fontSize:12.7, color:C.black, margin:0 });
    s.addText(r.res, { x:4.9, y:r.y+0.11, w:2.25, h:0.42, fontSize:12.4, color:C.black, margin:0 });
  });
  addBullets(s, [
    'Best when cameras overlap substantially and you want a lighter stack than full 3D perception.',
    'The conceptual win: multi-camera cues help decide identity early, not only recover mistakes later.',
    'Limitation: world consistency is still weaker than in world-coordinate / 3D systems.'
  ], { x:0.75, y:4.25, w:6.6, h:2.1 }, 16.5);
  s.addImage({ path: img('comparison_matrix.png'), ...imageSizingContain(img('comparison_matrix.png'), 8.05, 1.48, 4.55, 4.95) });
  s.addText('MCTR and GMT are the clearest modern rejection of heuristic-heavy late MTMC.', { x:8.15, y:6.05, w:4.2, h:0.55, fontSize:15.5, color:C.black, margin:0 });
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- MCTR https://arxiv.org/abs/2408.13243',
    '- GMT https://arxiv.org/abs/2407.01007',
    '- Generated figure: images/comparison_matrix.png from src/build_assets.py',
    '[/Sources]'
  ]);
}

// Slide 6
{
  const s = pptx.addSlide();
  addHeader(s, 'Family 2: query-based 3D systems', 'Shared object queries + temporal memory are becoming the cleanest MTMC abstraction');
  s.addShape(pptx.ShapeType.roundRect, { x:0.72, y:1.5, w:6.78, h:0.42, rectRadius:0.03, fill:{ color:C.teal }, line:{ color:C.teal, pt:1 } });
  s.addText('Model', { x:0.92, y:1.62, w:1.0, h:0.16, fontSize:13.2, bold:true, color:C.white, margin:0 });
  s.addText('What changed', { x:2.18, y:1.62, w:2.1, h:0.16, fontSize:13.2, bold:true, color:C.white, margin:0 });
  s.addText('Why it matters', { x:4.9, y:1.62, w:1.8, h:0.16, fontSize:13.2, bold:true, color:C.white, margin:0 });
  const rows6 = [
    { y:1.98, fill:'FFFFFF', model:'ADA-Track', change:'Alternating detection and association in the decoder', why:'Bridges tracking-by-attention and tracking-by-detection' },
    { y:2.72, fill:'F7FAFC', model:'ADA-Track++', change:'Edge-augmented association + auxiliary token', why:'Improves association stability and raises AMOTA' },
    { y:3.46, fill:'FFFFFF', model:'Sparse4D-OI', change:'Adapts sparse query memory to outside-in static camera networks', why:'Best online camera-only result among reported AI City 2025 systems' }
  ];
  rows6.forEach(r => {
    s.addShape(pptx.ShapeType.roundRect, { x:0.72, y:r.y, w:6.78, h:0.64, rectRadius:0.02, fill:{ color:r.fill }, line:{ color:'D6DEE4', pt:1 } });
    s.addText(r.model, { x:0.92, y:r.y+0.17, w:1.0, h:0.16, fontSize:13.0, color:C.black, margin:0 });
    s.addText(r.change, { x:2.18, y:r.y+0.11, w:2.3, h:0.34, fontSize:12.5, color:C.black, margin:0 });
    s.addText(r.why, { x:4.9, y:r.y+0.11, w:2.1, h:0.34, fontSize:12.5, color:C.black, margin:0 });
  });
  s.addShape(pptx.ShapeType.roundRect, { x:0.78, y:5.0, w:6.95, h:1.0, rectRadius:0.04, fill:{ color:'EAF4F1' }, line:{ color:'D0E4DF', pt:1 } });
  s.addText('Shared pattern: the model tracks persistent objects, not just boxes.', { x:1.0, y:5.35, w:6.3, h:0.28, fontSize:17, color:C.black, margin:0 });
  s.addImage({ path: img('recommended_stack.png'), ...imageSizingContain(img('recommended_stack.png'), 8.0, 1.42, 4.7, 5.6) });
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- ADA-Track https://openaccess.thecvf.com/content/CVPR2024/html/Ding_ADA-Track_End-to-End_Multi-Camera_3D_Multi-Object_Tracking_with_Alternating_Detection_and_CVPR_2024_paper.html',
    '- ADA-Track++ https://arxiv.org/abs/2405.08909',
    '- Sparse4D outside-in https://arxiv.org/abs/2601.10819',
    '- Generated figure: images/recommended_stack.png from src/build_assets.py',
    '[/Sources]'
  ]);
}

// Slide 7
{
  const s = pptx.addSlide();
  addHeader(s, 'Family 3: geometry-first / challenge systems', 'The strongest structured-environment results still lean heavily on geometry, BEV, depth, and long-horizon association');
  addBullets(s, [
    'MCBLT: BEV + hierarchical GNNs; strong evidence that world-state-first design helps long videos.',
    'DepthTrack: Tracklet-Cluster Mapping links BEV tracklets with 3D point clusters; 2nd place on AI City 2025 Track 1.',
    'TeamQDT: practical recipe that upgrades an existing 2D MTMC stack into 3D with late depth fusion.'
  ], { x:0.74, y:1.55, w:5.65, h:2.6 }, 17);
  s.addShape(pptx.ShapeType.roundRect, { x:0.78, y:4.35, w:5.55, h:1.42, rectRadius:0.05, fill:{ color:'F4EFE6' }, line:{ color:'E2D7C8', pt:1 } });
  s.addText('Takeaway: if your deployment resembles a warehouse or synthetic smart-space benchmark, geometry is still a huge advantage.', { x:1.0, y:4.74, w:5.1, h:0.62, fontSize:16.5, color:C.black, margin:0 });
  s.addImage({ path: img('ai_city_2025_context.png'), ...imageSizingContain(img('ai_city_2025_context.png'), 6.55, 1.45, 5.95, 5.45) });
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- MCBLT https://arxiv.org/abs/2412.00692',
    '- DepthTrack https://openaccess.thecvf.com/content/ICCV2025W/AICity/papers/Tran_DepthTrack_Cluster_Meets_BEV_for_Multi-Camera_Multi-Target_3D_Tracking_ICCVW_2025_paper.pdf',
    '- TeamQDT https://arxiv.org/html/2509.09946v1',
    '- AI City 2025 overview https://arxiv.org/html/2508.13564v1',
    '- Generated figure: images/ai_city_2025_context.png from src/build_assets.py',
    '[/Sources]'
  ]);
}

// Slide 8
{
  const s = pptx.addSlide();
  addHeader(s, 'Family 4: robustness and deployment', 'The latest papers are finally tackling the failure modes product teams actually care about');
  s.addShape(pptx.ShapeType.roundRect, { x:0.72, y:1.48, w:5.65, h:4.95, rectRadius:0.05, fill:{ color:'F4F7FA' }, line:{ color:'D7E0E6', pt:1 } });
  s.addText('Three important directions', { x:1.0, y:1.8, w:3.1, h:0.3, fontSize:18, bold:true, color:C.navy, margin:0 });
  addBullets(s, [
    'ADMCMT / M3Track: use thermal + lighting-guided fusion for all-day tracking.',
    'CALIBFREE: learn view-agnostic embeddings without precise calibration or labels (promising but still immature).',
    'DGT and optimization work: prioritize latency, online global tracking, low-FPS robustness, and camera scalability.'
  ], { x:0.98, y:2.18, w:5.0, h:3.2 }, 16.5);
  s.addText('Guiding principle: add complexity only when it removes a real failure mode.', { x:0.98, y:5.65, w:4.9, h:0.38, fontSize:15.2, italic:true, color:C.black, margin:0 });
  s.addImage({ path: img('dataset_landscape.png'), ...imageSizingContain(img('dataset_landscape.png'), 6.55, 1.45, 6.0, 5.45) });
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- ADMCMT / M3Track https://openaccess.thecvf.com/content/CVPR2025/html/Fan_All-Day_Multi-Camera_Multi-Target_Tracking_CVPR_2025_paper.html',
    '- CALIBFREE https://openreview.net/forum?id=4kb6vectZ3',
    '- DGT https://www.nature.com/articles/s41598-026-35768-z',
    '- Sparse4D optimization https://arxiv.org/abs/2602.00450',
    '- Generated figure: images/dataset_landscape.png from src/build_assets.py',
    '[/Sources]'
  ]);
}

// Slide 9
{
  const s = pptx.addSlide();
  addHeader(s, 'Compare and contrast: what each family buys you');
  s.addImage({ path: img('comparison_matrix.png'), ...imageSizingContain(img('comparison_matrix.png'), 0.7, 1.35, 7.3, 5.7) });
  s.addShape(pptx.ShapeType.roundRect, { x:8.2, y:1.55, w:4.2, h:5.0, rectRadius:0.05, fill:{ color:'F4F7FA' }, line:{ color:'D7E0E6', pt:1 } });
  s.addText('Decision rule', { x:8.48, y:1.85, w:2.0, h:0.25, fontSize:18, bold:true, color:C.navy, margin:0 });
  addBullets(s, [
    'If ops simplicity wins: start near MCTR / GMT.',
    'If long-horizon identity wins: move to world-state / 3D.',
    'If low light wins: add thermal, not just a better ReID head.',
    'If calibration is unstable: keep a calibration-light backup path.',
    'If latency wins: protect online mode and use offline refinement separately.'
  ], { x:8.35, y:2.2, w:3.7, h:3.8 }, 15.5);
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- Generated figure: images/comparison_matrix.png from src/build_assets.py',
    '- Review synthesis from cited papers in report.md',
    '[/Sources]'
  ]);
}

// Slide 10
{
  const s = pptx.addSlide();
  addHeader(s, 'Recommended hybrid stack for your MTMC team', 'Combine the best ideas instead of copying any single paper end to end');
  s.addImage({ path: img('recommended_stack.png'), ...imageSizingContain(img('recommended_stack.png'), 0.62, 1.35, 8.35, 5.75) });
  s.addShape(pptx.ShapeType.roundRect, { x:9.2, y:1.58, w:3.55, h:4.9, rectRadius:0.05, fill:{ color:'F4F7FA' }, line:{ color:'D7E0E6', pt:1 } });
  s.addText('What to borrow', { x:9.48, y:1.88, w:2.2, h:0.25, fontSize:18, bold:true, color:C.navy, margin:0 });
  addBullets(s, [
    'World-coordinate query memory from Sparse4D / MCBLT.',
    'In-loop association from ADA-Track++.',
    'Global trajectory memory from GMT.',
    'Occlusion-aware identity layer and optional graph smoother.',
    'Two runtime modes: online serving and offline reprocessing.'
  ], { x:9.34, y:2.25, w:3.05, h:3.6 }, 15.2);
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- Generated figure: images/recommended_stack.png from src/build_assets.py',
    '- Sparse4D outside-in https://arxiv.org/abs/2601.10819',
    '- ADA-Track++ https://arxiv.org/abs/2405.08909',
    '- GMT https://arxiv.org/abs/2407.01007',
    '- MCBLT https://arxiv.org/abs/2412.00692',
    '[/Sources]'
  ]);
}

// Slide 11
{
  const s = pptx.addSlide();
  addHeader(s, 'Execution roadmap and evaluation');
  s.addShape(pptx.ShapeType.roundRect, { x:0.72, y:1.52, w:5.9, h:5.1, rectRadius:0.05, fill:{ color:'FFFFFF' }, line:{ color:'D7E0E6', pt:1 } });
  s.addText('4-phase build plan', { x:1.0, y:1.84, w:2.2, h:0.25, fontSize:18, bold:true, color:C.navy, margin:0 });
  addBullets(s, [
    'Phase 1: strong online RGB baseline with world-state query memory.',
    'Phase 2: add learned in-loop association and test AssA / IDF1 lift.',
    'Phase 3: add long-horizon global cleanup or graph smoothing.',
    'Phase 4: add thermal, depth, or calibration-light modules only if production evidence justifies them.'
  ], { x:0.98, y:2.18, w:5.3, h:3.1 }, 16.2);
  s.addShape(pptx.ShapeType.roundRect, { x:6.95, y:1.52, w:5.65, h:5.1, rectRadius:0.05, fill:{ color:'FFFFFF' }, line:{ color:'D7E0E6', pt:1 } });
  s.addText('Metrics that matter', { x:7.25, y:1.84, w:2.2, h:0.25, fontSize:18, bold:true, color:C.navy, margin:0 });
  addBullets(s, [
    'HOTA, IDF1, AssA, MOTA: standard view of quality.',
    'AvgTrackDur (or equivalent): continuity of identity over time.',
    'Latency / FPS at target camera count, not only single-scene speed.',
    'Failure buckets: low light, occlusion, camera handoff, calibration drift.'
  ], { x:7.2, y:2.18, w:5.0, h:2.7 }, 16.2);
  s.addShape(pptx.ShapeType.roundRect, { x:7.22, y:5.25, w:4.9, h:0.85, rectRadius:0.04, fill:{ color:'EAF4F1' }, line:{ color:'D0E4DF', pt:1 } });
  s.addText('Target outcome: best online quality under realistic sensor assumptions.', { x:7.48, y:5.53, w:4.3, h:0.25, fontSize:15.5, color:C.black, margin:0 });
  addFooter(s);
  addNotes(s, [
    '[Sources]',
    '- Sparse4D optimization / AvgTrackDur https://arxiv.org/abs/2602.00450',
    '- Review synthesis from report.md and cited papers',
    '[/Sources]'
  ]);
}

for (const slide of pptx._slides) {
  warnIfSlideHasOverlaps(slide, pptx, { allowContainment: true });
  warnIfSlideElementsOutOfBounds(slide, pptx);
}

pptx.writeFile({ fileName: '/mnt/data/mtmc_pkg/presentation.pptx' });
