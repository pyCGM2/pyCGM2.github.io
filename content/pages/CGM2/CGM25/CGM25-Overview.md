Title: CGM 2.5 Upper body model
Slug: CGM25-Overview

# Overview
Although many gait analysis services include some sort of analysis of upper body movement as part of their standard analysis there has been much less consistency in which model is used than for the lower limb. No upper body model for clinical gait analysis has been rigorously validated. Applying extra markers accurately to the trunk, head and arms can add extra time to an analysis and is often not justified by the clinical use that is made of the data.

<figure align="middle" >
  <img src="..\images\CGM2\CGM25Thorax.png" alt="CGM2 Thorax Model" width="400">
  <figcaption>Single segment thorax model for CGM2 </figcaption>
</figure>
<p></p>

As [Perry](https://books.google.co.uk/books?id=DICTQAAACAAJ&source=gbs_book_other_versions) noted the Head, Arms and Trunk (HAT) can be thought of as a <em>passenger segment</em> and understanding how this is carried by the les or <em>locomotor unit</em> is essential to understand the mechanics of gait. It is not all clear how much detail is required. Given that most of the mass of the upper body is within the trunk it can be assumed that an accurate understanding of this location is essential. The orientation of the head and arms is less important and a general overview of these may be all that is required.

Whilst the original paper of [Davis et al. 1991](http://dx.doi.org/10.1016/0167-9457%2891%2990046-Z) suggested placing markers laterally over the acromium processes, more recent papers ([e.g. Armand et al. 2014]( http://dx.doi.org/10.1016/j.gaitpost.2013.06.016)) suggest that marker placed directly on the mid-line of the trunk may give a better indication of how the trunk itself is moving. [Eames et al. 1999](http://dx.doi.org/10.1016/S0167-9457%2899%2900022-6) proposed a minimal markerset for head and arms and validated the calculation of full body centre of mass obtained against force plate data.

## Proposal
CGM 2.5 will use three markers proposed by Armand et al. [2014]( http://dx.doi.org/10.1016/j.gaitpost.2013.06.016) (Sternum, T2, T10) to track the thorax which will be linked to the pelvis by a ball joint at the lumbar sacral joint. Testing will be perfromed to quantify the effect this has on how the lower limbs and trunk are tracked.

The approach of Eames et al. [1999](http://dx.doi.org/10.1016/S0167-9457%2899%2900022-6) will be used to track the head and arms to give a broad impression of their orientation. Markers will be given a low weighting in the tracking cost function to ensure that tracking these segments has a minimal effect on the tracking of other more important segments.



## marker set

![cgm25ms](/images/CGM2/CGM25_markerset.png){ width=50% }

<div class="alert alert-dismissible alert-info">
<b>REMINDER</b>
<br>
<p> An <b> optional marker</b> is used for improving the tracking-labelling process. They do not take part in any biomechanical calculation </p>
<br>
There is <b> no equivalent marker of RBAK</b>  on the left side. This optional marker help the autolabelling at detecting the left from the right side.
</div>

Check out our [palpation guidelines](Palpation.html) for get assistance on marker placement

Calibrations with either native processing (ie the lateral marker defines the coronal plane ! ) or KAD can be also enable

## Anthropometric parameters

### Required

|Name | details |
|------|---------|
|Bodymass|Patient mass |
|Height| Patient height |
|Leg length|Full leg length, measured between the ASIS marker and the medial malleolus, via the knee joint.  Measure with patient standing, if possible. If the patient is standing in the crouch position, this measurement is NOT the shortest distance between the ASIS and medial malleoli, but rather the measure of the skeletal leg length.|
|Knee Width|The medio-lateral width of the knee across the line of the knee axis.. Measure with patient standing, if possible. |
|Ankle Width|The medio-lateral distance across the malleoli. Measure with patient standing, if possible. |
|Sole Thickness|The difference in the thickness of the sole at the toe and the heel. A positive
sole delta indicates that the patient’s heel is raised compared with the toe |
|Elbow Width|Width of elbow along flexion axis (roughly between the medial and lateral epicondyles of the humerus) |
|Wrist Width|Anterior/Posterior thickness of wrist at position where wrist marker bar is
attached. |
|Shoulder Offset|Vertical offset from the base of the acromion marker to shoulder joint
center |
|Hand Thickness|Anterior/Posterior thickness between the dorsum and palmar surfaces of the hand. |


### Optional

|Name | details |
|------|---------|
|Inter-ASIS distance| No Need if the HJC regressive equtions are not the native Davis equations  |
|ASIS-Trochanter Distance| No Need if the HJC regressive equtions are not the native Davis equations |
|Tibial Torsion| The angle between the knee flexion and the ankle dorsi-plantar axes. The ankle is usually externally rotated with respect to the knee flexion axis. **If you are using a KAD or Medial knee Marker**, and the medial malleoli markers are attached to the patient, the tibial torsion is  automatically calculated|
