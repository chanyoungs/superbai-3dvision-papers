# same as before
import json, os, textwrap
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

BASE = Path('/mnt/data/mtmc_pkg')
IMG = BASE / 'images'
DATA = BASE / 'data'
IMG.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

papers = [
    {'id':'MCTR','year':2025,'title':'MCTR: Multi Camera Tracking Transformer','venue':'WACV 2025 Workshop / arXiv 2024','setting':'2D MTMC, overlapping cameras','domain':'people / indoor','inputs':'RGB','state':'2D + global track embeddings','fusion':'Early global tracking state (not full 3D)','association':'learned end-to-end tracking + association modules','online':'Yes','calibration':'No','multimodal':'No','low_light':'No','headline':'71.81 HOTA / 80.21 IDF1 / 91.19 MOTA on MMPTrack industry; 9 FPS','relation':'Turns DETR-style E2E MOT into multi-camera tracking; strong rebuttal to heuristic-heavy pipelines.','url':'https://arxiv.org/abs/2408.13243'},
    {'id':'GMT','year':2025,'title':'GMT: Effective Global Framework for Multi-Camera Multi-Target Tracking','venue':'arXiv v2 2025','setting':'2D MCMT, overlapping cameras','domain':'pedestrian','inputs':'RGB','state':'Global trajectories across views','fusion':'Global trajectory modeling','association':'CFCE + GTA transformer association','online':'Not emphasized','calibration':'Uses spatial cues','multimodal':'No','low_light':'No','headline':'Up to +21.3% CVMA / +17.2% CVIDF1 over prior two-stage frameworks','relation':'Pushes the field from per-view trajectories to cross-view global trajectory objects.','url':'https://arxiv.org/abs/2407.01007'},
    {'id':'ADA-Track','year':2024,'title':'ADA-Track','venue':'CVPR 2024','setting':'Multi-camera 3D MOT','domain':'autonomous driving / nuScenes','inputs':'RGB multi-view','state':'3D object queries','fusion':'Sparse query-based multi-view fusion','association':'Alternating detection and association','online':'Yes','calibration':'Yes','multimodal':'No','low_light':'No','headline':'0.456 AMOTA on nuScenes test; beats STAR-Track and PF-Track','relation':'Combines tracking-by-attention and tracking-by-detection; a pivotal query-based 3D tracker.','url':'https://openaccess.thecvf.com/content/CVPR2024/html/Ding_ADA-Track_End-to-End_Multi-Camera_3D_Multi-Object_Tracking_with_Alternating_Detection_and_CVPR_2024_paper.html'},
    {'id':'ADA-Track++','year':2025,'title':'ADA-Track++','venue':'arXiv 2024/2025','setting':'Multi-camera 3D MOT','domain':'autonomous driving / nuScenes','inputs':'RGB multi-view','state':'3D object queries','fusion':'Sparse query-based multi-view fusion','association':'Edge-augmented cross-attention + auxiliary token','online':'Yes','calibration':'Yes','multimodal':'No','low_light':'No','headline':'0.500 AMOTA on nuScenes test; +0.7 to +1.1 AMOTA over ADA-Track depending on detector','relation':'Refines ADA-Track by making association itself more stable and less confused.','url':'https://arxiv.org/abs/2405.08909'},
    {'id':'MCBLT','year':2025,'title':'MCBLT: Multi-Camera Multi-Object 3D Tracking in Long Videos','venue':'arXiv 2024 / revised 2025','setting':'Outside-in 3D MTMC','domain':'indoor infrastructure','inputs':'RGB + camera parameters','state':'3D BEV detections + graphs','fusion':'BEV + hierarchical GNN','association':'Graph-based long-term association','online':'Not main focus','calibration':'Yes','multimodal':'No','low_light':'No','headline':'81.22 HOTA on AI City 2024; 95.6 IDF1 on WILDTRACK','relation':'Strong geometry-first long-horizon design; influential bridge between BEV perception and MTMC association.','url':'https://arxiv.org/abs/2412.00692'},
    {'id':'ADMCMT','year':2025,'title':'All-Day Multi-Camera Multi-Target Tracking (ADMCMT + M3Track)','venue':'CVPR 2025','setting':'All-day MCMT','domain':'pedestrian / UAV / low light','inputs':'RGB + thermal','state':'2D tracking with multimodal fusion','fusion':'All-Day Mamba Fusion (ADMF)','association':'Transformer tracking + Nearby Target Collection','online':'Yes','calibration':'Overlap-based','multimodal':'Yes','low_light':'Yes','headline':'Introduces first RGBT MCMT dataset M3Track; strong generalization across lighting conditions','relation':'Adds the modality story the mostly-RGB literature lacked.','url':'https://openaccess.thecvf.com/content/CVPR2025/html/Fan_All-Day_Multi-Camera_Multi-Target_Tracking_CVPR_2025_paper.html'},
    {'id':'DepthTrack','year':2025,'title':'DepthTrack: Cluster Meets BEV for Multi-Camera Multi-Target 3D Tracking','venue':'ICCV 2025 Workshop / AI City 2025','setting':'3D MTMC challenge system','domain':'warehouse / indoor','inputs':'RGB + depth maps','state':'BEV tracklets + clustered point clouds','fusion':'Tracklet-Cluster Mapping (TCM)','association':'Modular association with ReID and geometry','online':'No','calibration':'Yes','multimodal':'Depth','low_light':'Partial (low-light enhancement)','headline':'2nd place AI City 2025 Track 1; 63.14 HOTA','relation':'Representative of high-performing geometry-first offline pipelines in synthetic/structured spaces.','url':'https://openaccess.thecvf.com/content/ICCV2025W/AICity/papers/Tran_DepthTrack_Cluster_Meets_BEV_for_Multi-Camera_Multi-Target_3D_Tracking_ICCVW_2025_paper.pdf'},
    {'id':'TeamQDT','year':2025,'title':'Online 3D Multi-Camera Perception through Robust 2D Tracking and Depth-based Late Aggregation','venue':'ICCV 2025 Workshop / AI City 2025','setting':'Online 3D MTMC challenge system','domain':'warehouse / indoor','inputs':'RGB + depth maps','state':'2D tracks upgraded to 3D boxes','fusion':'Late-stage depth fusion','association':'2D MOT + global ID consistency + clustering','online':'Yes','calibration':'Yes','multimodal':'Depth','low_light':'No','headline':'3rd place AI City 2025 Track 1; 28.75 HOTA official challenge score','relation':'A practical recipe for teams that already have strong 2D MTMC and want a 3D path without retraining everything.','url':'https://arxiv.org/html/2509.09946v1'},
    {'id':'Sparse4D-OI','year':2026,'title':'A Unified 3D Object Perception Framework for Real-Time Outside-In Multi-Camera Systems','venue':'arXiv 2026','setting':'Outside-in 3D MTMC','domain':'industrial infrastructure','inputs':'RGB only','state':'World-coordinate sparse 3D queries','fusion':'Early multi-view aggregation in shared world frame','association':'Temporal memory + occlusion-aware ReID','online':'Yes','calibration':'Yes','multimodal':'No','low_light':'No','headline':'45.22 HOTA on AI City 2025; best online camera-only result among reported systems','relation':'Adapts Sparse4D from autonomous driving to fixed-camera infrastructure and shows the promise of query-memory systems.','url':'https://arxiv.org/abs/2601.10819'},
    {'id':'CALIBFREE','year':2026,'title':'CALIBFREE','venue':'ICLR 2026 withdrawn submission','setting':'Calibration-free MCMT','domain':'surveillance','inputs':'RGB','state':'Learned view-agnostic/view-specific embeddings','fusion':'Self-supervised feature disentanglement','association':'Representation-learning first','online':'Potentially','calibration':'No','multimodal':'No','low_light':'No','headline':'Reported +3% overall accuracy and +7.5 F1 on MMP-MvMHAT','relation':'Promising direction for deployments where calibration is unavailable or drifts over time.','url':'https://openreview.net/forum?id=4kb6vectZ3'},
    {'id':'DGT','year':2026,'title':'Dynamic Global Tracking (DGT)','venue':'Scientific Reports 2026','setting':'Online MCMT','domain':'multi-camera vehicle tracking','inputs':'RGB','state':'Global trajectories during tracking','fusion':'Hybrid Fusion Module','association':'Integrates cross-camera association into tracking loop','online':'Yes','calibration':'Not required in core design','multimodal':'No','low_light':'No','headline':'IDF1 61.19 (speed) / 70.49 (performance) at 90 FPS on HST','relation':'Strong example of deployment-oriented online global association.','url':'https://www.nature.com/articles/s41598-026-35768-z'},
]

datasets = [
    {'dataset':'WILDTRACK','year':2018,'domain':'pedestrians / outdoor','cameras':7,'approx_frames_k':0.4,'modalities':'RGB','notes':'Highly calibrated, overlapping, 2 FPS, ~56K view boxes over 400 annotated frames','url':'https://www.epfl.ch/labs/cvlab/data/data-wildtrack/'},
    {'dataset':'CityFlow','year':2019,'domain':'vehicles / city-scale','cameras':40,'approx_frames_k':None,'modalities':'RGB','notes':'>3 hours, 40 cameras, 10 intersections, >200K boxes; geometry provided','url':'https://arxiv.org/abs/1903.09254'},
    {'dataset':'MMPTrack','year':2021,'domain':'people / indoor','cameras':None,'approx_frames_k':None,'modalities':'RGB(+RGBD labeling)','notes':'Five environments: industry, retail, cafe, lobby, office; dense labels','url':'https://arxiv.org/abs/2111.15157'},
    {'dataset':'M3Track','year':2025,'domain':'people / UAV / all-day','cameras':2,'approx_frames_k':236,'modalities':'RGB+Thermal','notes':'19 scenes, 118Kx2 frames, 1.188M boxes, low-light and moving cameras','url':'https://openaccess.thecvf.com/content/CVPR2025/html/Fan_All-Day_Multi-Camera_Multi-Target_Tracking_CVPR_2025_paper.html'},
    {'dataset':'VisionTrack','year':2025,'domain':'pedestrians','cameras':None,'approx_frames_k':None,'modalities':'RGB','notes':'Introduced with GMT; positioned as higher-diversity MCMT dataset','url':'https://arxiv.org/abs/2407.01007'},
    {'dataset':'AI City 2025 Track 1','year':2025,'domain':'people + robots / synthetic indoor 3D','cameras':504,'approx_frames_k':None,'modalities':'RGB + GT depth in challenge package','notes':'42 hours, 504 cameras, 19 indoor layouts, >360 object instances','url':'https://arxiv.org/html/2508.13564v1'}
]

paper_df = pd.DataFrame(papers)
dataset_df = pd.DataFrame(datasets)
paper_df.to_csv(DATA/'papers.csv', index=False)
paper_df.to_json(DATA/'papers.json', orient='records', indent=2)
dataset_df.to_csv(DATA/'datasets.csv', index=False)
dataset_df.to_json(DATA/'datasets.json', orient='records', indent=2)

plt.rcParams['figure.dpi'] = 180
plt.rcParams['font.size'] = 10
family_colors = {'2D global association':'#335C67','3D query-based':'#2A9D8F','BEV / geometry-first':'#577590','multimodal / robustness':'#BC6C25','deployment / calibration-free':'#8D5A97'}
paper_family = {'MCTR':'2D global association','GMT':'2D global association','ADA-Track':'3D query-based','ADA-Track++':'3D query-based','Sparse4D-OI':'3D query-based','MCBLT':'BEV / geometry-first','DepthTrack':'BEV / geometry-first','TeamQDT':'BEV / geometry-first','ADMCMT':'multimodal / robustness','CALIBFREE':'deployment / calibration-free','DGT':'deployment / calibration-free'}

fig, ax = plt.subplots(figsize=(13,4.6))
ax.set_xlim(2023.7, 2026.3); ax.set_ylim(-2.2, 2.2); ax.axhline(0, color='#444', lw=1.6); ax.set_yticks([]); ax.set_xticks([2024,2025,2026]); ax.set_title('MTMC research timeline (papers/models emphasized in this review)')
positions = {'MCTR':(-0.9), 'GMT':(0.9), 'ADA-Track':(-0.3), 'ADA-Track++':(0.5), 'MCBLT':(1.5), 'ADMCMT':(-1.4), 'DepthTrack':(1.1), 'TeamQDT':(-0.8), 'Sparse4D-OI':(0.7), 'CALIBFREE':(-1.5), 'DGT':(1.5)}
for p in papers:
    x = p['year'] + (0.08 if p['year']==2025 and p['id'] in ['DepthTrack','TeamQDT'] else 0)
    y = positions[p['id']]
    c = family_colors[paper_family[p['id']]]
    ax.scatter([x],[y], s=160, color=c, zorder=3)
    ax.plot([x,x],[0,y], color=c, lw=1.2, alpha=0.7)
    ax.text(x+0.03, y+(0.12 if y>=0 else -0.12), p['id'], fontsize=10, ha='left', va='center')
ax.text(2024.02,1.85,'Query-based 3D takes off\n(ADA-Track)', fontsize=10)
ax.text(2025.0,-1.95,'AI City 2025 creates a strong\n3D MTMC systems wave', fontsize=10)
ax.text(2026.03,1.85,'Deployment-focused work\n(latency, camera-only, calibration-light)', fontsize=10)
legend_handles = [plt.Line2D([0],[0], marker='o', color='w', markerfacecolor=v, markersize=9, label=k) for k,v in family_colors.items()]
ax.legend(handles=legend_handles, ncol=3, loc='lower center', bbox_to_anchor=(0.5,-0.35), frameon=False)
for spine in ax.spines.values(): spine.set_visible(False)
fig.tight_layout(); fig.savefig(IMG/'timeline.png', bbox_inches='tight'); plt.close(fig)

fig, ax = plt.subplots(figsize=(14,7)); ax.set_xlim(0, 100); ax.set_ylim(0,100); ax.axis('off'); ax.text(2,95,'Taxonomy of recent MTMC models', fontsize=18, weight='bold')
root = FancyBboxPatch((34,83), 32, 10, boxstyle='round,pad=0.02,rounding_size=1.5', fc='#1F3B4D', ec='none'); ax.add_patch(root); ax.text(50,88,'MTMC design space', color='white', ha='center', va='center', fontsize=16, weight='bold')
boxes = [(4,55,28,18,'2D global association\nMCTR, GMT\n\n+ No full 3D stack needed\n+ Strong overlap handling\n− weaker world consistency'),(36,55,28,18,'3D query-based E2E\nADA-Track, ADA-Track++, Sparse4D-OI\n\n+ unified perception + association\n+ strong occlusion recovery\n− calibration and training cost'),(68,55,28,18,'BEV / geometry-first\nMCBLT, DepthTrack, TeamQDT\n\n+ precise world state\n+ long-horizon association\n− depends on geometry/depth quality'),(20,24,28,18,'Multimodal robustness\nADMCMT / M3Track\n\n+ low-light resilience\n+ modality-guided fusion'),(52,24,28,18,'Calibration-light / deployment\nCALIBFREE, DGT, optimization work\n\n+ practical deployment\n+ simpler ops story')]
for x,y,w,h,label in boxes:
    patch = FancyBboxPatch((x,y), w, h, boxstyle='round,pad=0.02,rounding_size=1.2', fc='#EEF4F7', ec='#6388A1', lw=1.8); ax.add_patch(patch); ax.text(x+w/2, y+h/2, label, ha='center', va='center', fontsize=11)
for x,y,w,h,_ in boxes[:3]: ax.add_patch(FancyArrowPatch((50,83),(x+w/2,y+h), arrowstyle='-|>', mutation_scale=18, lw=1.4, color='#4A6677'))
for x,y,w,h,_ in boxes[3:]: ax.add_patch(FancyArrowPatch((50,55),(x+w/2,y+h), arrowstyle='-|>', mutation_scale=18, lw=1.4, color='#4A6677'))
ax.text(2,5,'Key axes used in this review: state space (2D vs world/3D), fusion stage, association learning, online/offline, and robustness strategy.', fontsize=11, color='#333')
fig.tight_layout(); fig.savefig(IMG/'taxonomy.png', bbox_inches='tight'); plt.close(fig)

features = ['World/3D state','End-to-end','Online-ready','Needs calibration','Depth/Thermal','Long-horizon memory','Explicit global trajectories']
feature_values = {'MCTR':[0,1,1,0,0,1,1],'GMT':[0,0,0,1,0,1,1],'ADA-Track':[1,1,1,1,0,1,0],'ADA-Track++':[1,1,1,1,0,1,0],'MCBLT':[1,0,0,1,0,1,0],'ADMCMT':[0,1,1,0,1,1,0],'DepthTrack':[1,0,0,1,1,1,0],'TeamQDT':[1,0,1,1,1,1,0],'Sparse4D-OI':[1,1,1,1,0,1,0],'CALIBFREE':[0,0,1,0,0,1,0],'DGT':[0,0,1,0,0,1,1]}
order = [p['id'] for p in papers]; mat = np.array([feature_values[o] for o in order])
fig, ax = plt.subplots(figsize=(14,6.7)); ax.imshow(mat, cmap='Blues', aspect='auto', vmin=0, vmax=1); ax.set_xticks(range(len(features))); ax.set_xticklabels(features, rotation=25, ha='right'); ax.set_yticks(range(len(order))); ax.set_yticklabels(order); ax.set_title('Model capability matrix (qualitative)')
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]): ax.text(j, i, '✓' if mat[i,j] else '–', ha='center', va='center', color=('white' if mat[i,j] else '#444'), fontsize=11, weight='bold')
for spine in ax.spines.values(): spine.set_visible(False)
fig.tight_layout(); fig.savefig(IMG/'comparison_matrix.png', bbox_inches='tight'); plt.close(fig)

fig, ax = plt.subplots(figsize=(11.5,6.2)); ax.set_title('Dataset / benchmark landscape used by recent MTMC work'); ax.set_xlabel('Number of cameras (approx.)'); ax.set_ylabel('Dataset recency')
for d in datasets:
    cams = d['cameras'] if d['cameras'] is not None else (5 if d['dataset']=='MMPTrack' else 8)
    y = d['year']; size = 800 if d['dataset']=='AI City 2025 Track 1' else (550 if d['dataset']=='M3Track' else 360); color = '#2A9D8F' if 'Thermal' in d['modalities'] else ('#577590' if 'depth' in d['notes'].lower() else '#335C67')
    ax.scatter(cams, y, s=size, alpha=0.75, color=color, edgecolors='white', linewidth=1.2); ax.text(cams+0.8, y+0.02, d['dataset'], fontsize=10, va='center')
ax.set_xlim(0, 540); ax.set_yticks([2018,2019,2021,2025]); ax.grid(alpha=0.25); ax.text(308,2025.2,'AI City 2025 dominates in camera count\nand 3D MTMC challenge pressure.', fontsize=10); ax.text(14,2025.05,'M3Track adds the missing\nall-day / thermal axis.', fontsize=10)
fig.tight_layout(); fig.savefig(IMG/'dataset_landscape.png', bbox_inches='tight'); plt.close(fig)

leaders = pd.DataFrame([('ZV',69.9118,'Offline'),('SKKU-AutoLab / DepthTrack',63.1396,'Offline'),('Sparse4D camera-only',45.22,'Online'),('TeamQDT',28.7515,'Online'),('UTE AI Lab / VGCRTrack',25.3983,'Online')], columns=['Method','HOTA','Mode']).sort_values('HOTA')
fig, ax = plt.subplots(figsize=(11.5,5.5)); colors = leaders['Mode'].map({'Offline':'#9AA4AE','Online':'#2A9D8F'}); ax.barh(leaders['Method'], leaders['HOTA'], color=colors)
for i,(h,m) in enumerate(zip(leaders['HOTA'], leaders['Mode'])): ax.text(h+1, i, f'{h:.2f}', va='center', fontsize=10)
ax.set_title('AI City 2025 Track 1 context: online vs offline systems'); ax.set_xlabel('HOTA'); ax.text(47, 3.9, 'Best online camera-only\nreported result', fontsize=10, color='#1E6F64'); ax.grid(axis='x', alpha=0.25)
fig.tight_layout(); fig.savefig(IMG/'ai_city_2025_context.png', bbox_inches='tight'); plt.close(fig)

fig, ax = plt.subplots(figsize=(14,7.5)); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off'); ax.text(2,95,'Recommended hybrid MTMC stack for a high-performing team', fontsize=18, weight='bold')
layers = [(4,72,92,12,'1. Per-camera perception: strong detector + lightweight single-camera track prior + quality flags', '#EDF3F7'),(4,55,92,12,'2. Shared world-coordinate query memory: sparse 3D/object queries in a common frame', '#E7F4F1'),(4,38,92,12,'3. Alternating detect-associate decoder: learned association inside the perception loop', '#EAF1F8'),(4,21,92,12,'4. Dual identity layer: occlusion-aware ReID + global trajectory memory + graph smoother', '#F7F0E8'),(4,4,92,12,'5. Runtime modes: online low-latency mode and offline global refinement mode', '#F2EDF7')]
for x,y,w,h,txt,fc in layers: ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=1.4',fc=fc,ec='#678',lw=1.5)); ax.text(x+2,y+h/2,txt,va='center',fontsize=12)
for y0,y1 in [(72,67),(55,50),(38,33),(21,16)]: ax.add_patch(FancyArrowPatch((50,y0),(50,y1),arrowstyle='-|>',mutation_scale=16,color='#47616F',lw=1.4))
notes = [(75,77,'MCTR / GMT\nuse cross-view info early'),(76,60,'Sparse4D / MCBLT\nworld-state first'),(74,43,'ADA-Track++\nlearn association in-decoder'),(72,26,'GMT + MCBLT + occlusion-aware ReID\nlong horizon identity stability'),(71,9,'DepthTrack / TeamQDT / DGT\ndeployment-friendly modes')]
for x,y,txt in notes: ax.text(x,y,txt,fontsize=10,ha='left',va='center',color='#264653')
ax.text(2,1.5,'Optional modality branch: add thermal only if low-light is a real failure mode; add depth only if the deployment can sustain it.', fontsize=10)
fig.tight_layout(); fig.savefig(IMG/'recommended_stack.png', bbox_inches='tight'); plt.close(fig)

compare_cols = ['id','year','venue','setting','inputs','state','fusion','association','online','calibration','headline']
compare_md = paper_df[compare_cols].rename(columns={'id':'Model','year':'Year','venue':'Venue/status','setting':'Setting','inputs':'Inputs','state':'State','fusion':'Fusion','association':'Association','online':'Online','calibration':'Calibration','headline':'Headline result'}).to_markdown(index=False)
dataset_md = dataset_df.rename(columns={'dataset':'Dataset','year':'Year','domain':'Domain','cameras':'Cameras','approx_frames_k':'Approx. frames (k)','modalities':'Modalities','notes':'Notes'})[['Dataset','Year','Domain','Cameras','Approx. frames (k)','Modalities','Notes']].to_markdown(index=False)
refs = [('Amosa et al., 2023 review', 'https://www.sciencedirect.com/science/article/pii/S0925231223006811'),('Sensors 2023 review for intelligent transportation', 'https://www.mdpi.com/1424-8220/23/7/3852'),('MCTR', 'https://arxiv.org/abs/2408.13243'),('GMT', 'https://arxiv.org/abs/2407.01007'),('ADA-Track', 'https://openaccess.thecvf.com/content/CVPR2024/html/Ding_ADA-Track_End-to-End_Multi-Camera_3D_Multi-Object_Tracking_with_Alternating_Detection_and_CVPR_2024_paper.html'),('ADA-Track++', 'https://arxiv.org/abs/2405.08909'),('MCBLT', 'https://arxiv.org/abs/2412.00692'),('ADMCMT / M3Track', 'https://openaccess.thecvf.com/content/CVPR2025/html/Fan_All-Day_Multi-Camera_Multi-Target_Tracking_CVPR_2025_paper.html'),('AI City 2025 challenge overview', 'https://arxiv.org/html/2508.13564v1'),('DepthTrack', 'https://openaccess.thecvf.com/content/ICCV2025W/AICity/papers/Tran_DepthTrack_Cluster_Meets_BEV_for_Multi-Camera_Multi-Target_3D_Tracking_ICCVW_2025_paper.pdf'),('TeamQDT late aggregation', 'https://arxiv.org/html/2509.09946v1'),('Outside-in Sparse4D adaptation', 'https://arxiv.org/abs/2601.10819'),('Sparse4D optimization / AvgTrackDur', 'https://arxiv.org/abs/2602.00450'),('CALIBFREE', 'https://openreview.net/forum?id=4kb6vectZ3'),('DGT', 'https://www.nature.com/articles/s41598-026-35768-z'),('CityFlow dataset', 'https://arxiv.org/abs/1903.09254'),('MMPTrack dataset', 'https://arxiv.org/abs/2111.15157'),('WILDTRACK dataset', 'https://www.epfl.ch/labs/cvlab/data/data-wildtrack/')]
ref_lines = '\n'.join([f'{i+1}. **{name}** — {url}' for i,(name,url) in enumerate(refs)])
report = f'''# Latest MTMC (Multi-object Tracking Multi-camera) models and papers

**Prepared:** 2026-03-12  
**Scope:** public papers, challenge reports, and notable preprints available up to 2026-03-12.  
**Important caveat:** scores across datasets are *not directly comparable*. The comparison below emphasizes model ideas, assumptions, and deployment trade-offs more than raw leaderboard values.

## Executive summary

The center of gravity in MTMC has shifted in three directions:

1. **From heuristic late association to learned global association.** MCTR and GMT explicitly model multi-camera identity reasoning rather than treating cross-camera matching as a small post-processing stage.
2. **From 2D track stitching to world-coordinate / 3D reasoning.** ADA-Track, ADA-Track++, MCBLT, DepthTrack, TeamQDT, and outside-in Sparse4D variants all show that a common 3D state reduces cross-view ambiguity.
3. **From benchmark-only accuracy to deployable systems.** 2025–2026 work increasingly studies online operation, camera-only inference, low FPS, low light, calibration-light setups, and latency/FPS constraints.

My bottom-line recommendation for an MTMC team is:

- **Use a world-coordinate query memory as the core representation.**
- **Learn association inside the perception loop** (ADA-Track++ style), not only after detection.
- **Keep a second, slower global trajectory memory/smoother** (GMT/MCBLT style) for long-horizon identity cleanup.
- **Add robustness modules only for real failure modes**: thermal for low light, depth for world grounding, calibration-free embedding learning when calibration is weak.

## 1) What changed recently

![MTMC timeline](images/timeline.png)

Recent MTMC work is no longer one monolithic pipeline. It is splitting into a few strong families:

![Taxonomy](images/taxonomy.png)

### My reading of the landscape

- **If cameras overlap strongly and you want a relatively simple stack**, MCTR/GMT-style global association is attractive.
- **If you need the best long-term cross-view consistency**, a shared 3D/world state is increasingly the dominant pattern.
- **If your deployment is indoor infrastructure (warehouse, retail, hospital)**, outside-in 3D perception is becoming the most relevant formulation.
- **If lighting is a major failure mode**, the all-day multimodal story in ADMCMT is more important than marginal benchmark gains on daylight-only datasets.
- **If ops complexity matters**, DGT / calibration-light work matters more than raw SOTA tables.

## 2) Dataset and benchmark landscape

![Dataset landscape](images/dataset_landscape.png)

{dataset_md}

### Practical interpretation

- **WILDTRACK** is still valuable for calibrated overlapping pedestrian scenes, but it is small and low-FPS.
- **CityFlow** remains important for non-overlapping vehicle MTMC and large camera networks.
- **MMPTrack** is a strong indoor people benchmark and helped expose occlusion-heavy retail failures.
- **M3Track** is the big new dataset contribution for all-day / low-light / RGBT MTMC.
- **AI City 2025 Track 1** is the most important recent forcing function for 3D MTMC in structured indoor spaces.

## 3) Paper-by-paper survey

### A. 2D global association family

#### MCTR (2025 workshop / 2024 arXiv)
**Core idea.** Turn DETR-style end-to-end MOT into multi-camera tracking by adding a learned tracking module and a learned association module.  
**Why it matters.** It is one of the clearest demonstrations that multi-camera tracking can be learned end-to-end instead of built from many hand-tuned stages.  
**Best use case.** Overlapping cameras, RGB only, team wants to avoid heavy calibration dependence.  
**Main limitation.** Still weaker on long-horizon identity consistency than heavily engineered offline systems.

#### GMT (2025 arXiv v2)
**Core idea.** Stop treating each camera’s trajectory as primary. Build **global trajectories** spanning multiple views, then associate new detections directly to those global trajectories.  
**Why it matters.** Conceptually, this is one of the cleanest upgrades over classic single-camera-then-cluster pipelines.  
**Best use case.** Overlapping cameras where explicit cross-view trajectory objects are natural.  
**Main limitation.** Less clearly packaged as a full deployment system than the 2025 challenge stacks.

### B. Query-based 3D end-to-end family

#### ADA-Track (CVPR 2024)
**Core idea.** Alternate detection and association in the decoder instead of forcing one shared query embedding to do everything at once.  
**Why it matters.** It bridges the gap between tracking-by-attention and tracking-by-detection.  
**Best use case.** Teams comfortable with DETR-style multi-view 3D detection and wanting a principled, learned association design.

#### ADA-Track++ (2025 preprint)
**Core idea.** Improve ADA-Track’s association with edge-augmented cross-attention and an auxiliary token that reduces confusing attention normalization effects.  
**Why it matters.** It strengthens the argument that **association should be a first-class learned module inside the decoder**.  
**Best use case.** The same settings as ADA-Track, but especially when association quality is the current bottleneck.

#### Outside-in Sparse4D adaptation (2026)
**Core idea.** Re-purpose Sparse4D-style query memory for fixed camera networks observing a shared space from the outside-in, with occlusion-aware ReID and Sim2Real augmentation.  
**Why it matters.** This is a strong sign that the object-query + temporal-memory paradigm transfers beyond autonomous driving.  
**Best use case.** Large indoor camera networks where camera-only inference matters.

### C. Geometry-first / BEV / challenge-system family

#### MCBLT (2025 revision)
**Core idea.** Aggregate multi-view images into BEV 3D detections, then do long-horizon MTMC with hierarchical GNNs in BEV.  
**Why it matters.** It is a particularly strong *world-state first* argument and a useful reference architecture for indoor infrastructure.

#### DepthTrack (2025)
**Core idea.** Use Tracklet-Cluster Mapping to connect BEV tracklets and 3D point clusters, avoiding a heavy explicit 3D detector training story.  
**Why it matters.** It is one of the strongest recent modular systems and shows how far geometry + depth + ReID can go.

#### TeamQDT late aggregation (2025)
**Core idea.** Keep the 2D MTMC core, then lift tracked targets into 3D using depth, clustering, and pose/footpoint cues.  
**Why it matters.** This is a very practical “don’t rebuild everything” path for existing MTMC teams.

### D. Robustness and deployment family

#### ADMCMT + M3Track (CVPR 2025)
**Core idea.** Add thermal input and a lighting-aware fusion module so MCMT still works at night / in low light.  
**Why it matters.** Most MTMC papers quietly assume good daytime RGB; this paper addresses a genuine production failure mode.

#### CALIBFREE (2026 withdrawn submission)
**Core idea.** Learn calibration-free multi-camera tracking features with self-supervised disentanglement of view-specific vs view-agnostic information.  
**Why it matters.** Not mature enough to bet the whole system on yet, but strategically important if your camera setup changes often or calibration is expensive.

#### DGT (2026)
**Core idea.** Integrate cross-camera association into the tracking loop for real-time MCMT, rather than extracting complete trajectories and clustering afterward.  
**Why it matters.** Good reminder that the deployment target can favor lower-latency global tracking over benchmark-optimized offline pipelines.

## 4) Compare and contrast

### Capability matrix

![Capability matrix](images/comparison_matrix.png)

### Compact comparison table

{compare_md}

## 5) How the models relate to each other

A useful mental model is:

- **Classic MTMC** = per-camera detection/MOT + ReID + cross-camera matching.
- **MCTR / GMT** = make cross-camera reasoning primary, not a cleanup step.
- **ADA-Track / ADA-Track++ / Sparse4D-OI** = represent objects as persistent queries in a shared multi-view state and learn association as part of perception.
- **MCBLT / DepthTrack** = build a stronger 3D / BEV state first, then associate in that state.
- **ADMCMT** = same MTMC logic, but with a modality branch to survive darkness.
- **CALIBFREE / DGT** = make the system easier to operate when calibration, latency, or compute are the first-order constraints.

In that sense, the field is converging toward a **hybrid**: a global world-state representation, a learned in-loop association module, and a deployment-aware outer shell.

## 6) Benchmark context that matters right now

![AI City 2025 context](images/ai_city_2025_context.png)

Interpretation:

- The best **offline** systems still have a large quality advantage in structured challenge settings.
- The most interesting **online** progress is now coming from query-memory models and strong modular depth-fusion systems.
- The most useful near-term production target is probably **“best online quality under realistic sensor assumptions”**, not absolute offline leaderboard rank.

## 7) Recommendations for your MTMC team

### Recommendation 1 — make 3D/world state the canonical identity space
Use image-plane detections as evidence, but let identities live in a shared world state whenever calibration is available. This directly attacks cross-view ambiguity, occlusion, and handoff problems. The strongest ideas here come from **MCBLT**, **DepthTrack**, and **Sparse4D-OI**.

### Recommendation 2 — learn association *inside* the perception model
Do not reserve association for a late Hungarian/ReID stage. The ADA-Track / ADA-Track++ lesson is that detection and association inform each other. The best next-generation MTMC model should have a decoder (or equivalent module) where **association is optimized jointly with detection/state refinement**.

### Recommendation 3 — keep a dual-timescale identity stack
Use:
- a **fast online association path** for frame-to-frame responsiveness; and
- a **slower global trajectory memory / graph smoother** for long-horizon cleanup.

That combines the strengths of **ADA-Track++ / Sparse4D** with **GMT / MCBLT**.

### Recommendation 4 — build occlusion-aware identity features, not only stronger detectors
The latest outside-in work suggests that **occlusion-aware ReID** and long-lived query memory are often more valuable than squeezing a few more AP points from the detector.

### Recommendation 5 — add modality branches only where justified
- Add **thermal** if night / low-light is a top failure mode (ADMCMT).
- Add **depth** if you can obtain it cheaply and it materially stabilizes world-state estimation (DepthTrack / TeamQDT / challenge-winning pipelines).
- Avoid carrying every sensor everywhere if the ops burden outweighs the gain.

### Recommendation 6 — train for deployment conditions, not only for benchmark conditions
The 2026 optimization work is important because it shows identity can collapse at low FPS even when detections still look acceptable. Evaluate the exact conditions you expect in production: FPS, compression, camera count, and low precision.

### Recommendation 7 — measure identity persistence explicitly
In addition to HOTA/IDF1/AssA, track something like **AvgTrackDur** (or your own equivalent) because it captures the user-visible continuity of identities better than a single summary number.

## 8) A concrete model blueprint I would build

![Recommended stack](images/recommended_stack.png)

### Proposed hybrid architecture

1. **Per-camera front-end**
   - strong detector
   - lightweight single-camera tracker prior
   - quality / occlusion / visibility flags
2. **Shared world-coordinate query bank**
   - sparse persistent object queries
   - camera-aware projection into each view
   - temporal memory through occlusion
3. **Alternating detect-associate decoder**
   - ADA-Track++ style learned association in-loop
4. **Global identity layer**
   - GMT-style global trajectories
   - MCBLT-style graph smoothing for long horizons
   - occlusion-aware ReID head
5. **Mode adapters**
   - online mode for serving
   - offline refinement mode for analytics / reprocessing
   - optional depth and thermal branches only when needed

## 9) Suggested roadmap for your team

### Phase 1 — strong online RGB baseline
Build a camera-only online system with a world-coordinate query memory and occlusion-aware ReID. This gives a practical baseline and reveals whether your bottleneck is detection, association, or calibration.

### Phase 2 — learned in-loop association
Add an ADA-Track++-style alternating association decoder. If that lifts AssA / IDF1 without destabilizing latency, make it the core.

### Phase 3 — long-horizon global cleanup
Add a GMT/MCBLT-inspired trajectory memory or graph smoother, either online with bounded memory or as an offline second pass.

### Phase 4 — robustness branches
Only now add:
- thermal branch for low-light sites,
- depth / geometric enrichment for particularly ambiguous spaces,
- calibration-light representation learning for unstable sites.

## 10) References / source links

{ref_lines}
'''
(BASE/'report.md').write_text(report, encoding='utf-8')
print('done')
