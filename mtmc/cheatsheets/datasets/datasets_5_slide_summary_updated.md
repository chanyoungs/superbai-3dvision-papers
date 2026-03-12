# Datasets - 5 Slide Summary (Updated with Thumbnails)

Scope: datasets used across CAMELTrack, MOTIP, ReST, MCBLT, and One Graph.

---

## Slide 1 - Why Dataset Choice Matters

These papers do not evaluate exactly the same tracking problem.

Representative benchmark families:
### DanceTrack
![DanceTrack](assets/thumbs/dancetrack.png)
- uniform appearance + diverse motion

### WildTrack
![WildTrack](assets/thumbs/wildtrack.png)
- 7 synchronized overlapping cameras

### AICity'24
![AICity'24](assets/thumbs/aicity24.png)
- synthetic indoor MTMC + 3D geometry

### SCOUT
![SCOUT](assets/thumbs/scout.png)
- scene-aware MTMC with structural occlusion

Main message:
- some datasets stress association under weak appearance
- some stress cross-view MTMC
- some reward explicit 3D / scene reasoning

## Slide 2 - Single-View MOT Datasets

### DanceTrack
![DanceTrack](assets/thumbs/dancetrack.png)
- uniform appearance + diverse motion
- Used by: CAMELTrack, MOTIP

### SportsMOT
![SportsMOT](assets/thumbs/sportsmot.png)
- sports players + camera motion
- Used by: CAMELTrack, MOTIP

### MOT17
![MOT17](assets/thumbs/mot17.png)
- classic pedestrian MOT benchmark
- Used by: CAMELTrack, One Graph

### MOT20
![MOT20](assets/thumbs/mot20.png)
- dense crowds + identity ambiguity
- Used by: One Graph

### BFT
![BFT](assets/thumbs/bft.png)
- bird flocks + highly dynamic motion
- Used by: MOTIP

### PoseTrack21
![PoseTrack21](assets/thumbs/posetrack21.png)
- pose-aware person tracking
- Used by: CAMELTrack

### BEE24
![BEE24](assets/thumbs/bee24.png)
- small objects + complex motion
- Used by: CAMELTrack

## Slide 3 - Classic Multi-Camera Benchmarks

### WildTrack
![WildTrack](assets/thumbs/wildtrack.png)
- 7 synchronized overlapping cameras
- Used by: ReST, MCBLT, One Graph

### CAMPUS
![CAMPUS](assets/thumbs/campus.png)
- classic small-scale MTMC scene
- Used by: ReST

### PETS-09
![PETS-09](assets/thumbs/pets09.png)
- legacy surveillance MTMC benchmark
- Used by: ReST

What they mainly test:
- cross-view identity association
- calibration-aware reasoning
- recovery after occlusion or temporary disappearance in one view

## Slide 4 - Large-Scale 3D / Scene-Aware Benchmarks

### AICity'24
![AICity'24](assets/thumbs/aicity24.png)
- synthetic indoor MTMC + 3D geometry
- Used by: MCBLT

### SCOUT
![SCOUT](assets/thumbs/scout.png)
- scene-aware MTMC with structural occlusion
- Used by: One Graph

These benchmarks reward explicit geometry, longer time horizons, and scene priors.

## Slide 5 - What Each Dataset Family Tells Us

### Association under weak appearance
![DanceTrack](assets/thumbs/dancetrack.png)
- DanceTrack, SportsMOT

### Cross-view MTMC
![WildTrack](assets/thumbs/wildtrack.png)
- WildTrack, CAMPUS, PETS-09

### Long-horizon 3D / scene-aware reasoning
![AICity'24](assets/thumbs/aicity24.png)
![SCOUT](assets/thumbs/scout.png)
- AICity'24, SCOUT

### Transfer beyond standard pedestrian street MOT
![BFT](assets/thumbs/bft.png)
![PoseTrack21](assets/thumbs/posetrack21.png)
![BEE24](assets/thumbs/bee24.png)
- BFT, PoseTrack21, BEE24

Main takeaway:
- dataset choice reveals whether a paper is mainly about better 2D matching, better cross-view reasoning, or better geometry-aware long-horizon tracking.