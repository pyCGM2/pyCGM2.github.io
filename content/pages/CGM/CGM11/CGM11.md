Title: CGM 1.1
Slug: CGM11

## Overview
Whilst creating CGM 1.0 we identified four aspects of PiG that we felt could be addressed immediately. **CGM 1.1 is thus a version of the CGM in which there three issues have been addressed**.

<ol>
  <li> There is an inconsistency between the way that the foot rotation offset is applied during static calibration and then applied later when fitting to dynamic data which has been corrected. </li>
  <li> The correct Cardan sequence for pelvic angles has been applied.</li>
  <li> Under a specific combinations of conditions the  medial malleolar malleolar marker was not being used appropriately during static calibration and teh logic for when it is used has been corrected</li>
  <li>Given that using a medial malleolar marker (if placed) has been used routinely for static calibration of the tibia for over a decade it is not at all clear why a simialr option to use a medial epicondyle marker for calibration of the femur has not been introduced. This is now possible, if the medial epicondyle marker (LKNM, RKNM) is found then this will be used to define the coronal plane of the knee in the same way as the KAD is used if it is present.
</ol>
Other than this the model is an exact clone of the current version of PiG.

## Marker set

![cgm11ms](/images/CGM1/CGM11_markerset.png){ width=50% }

<div class="alert alert-dismissible alert-info">
<b>REMINDER</b>
<br>
<p> An <b> optional marker</b> is used for improving the tracking-labelling process. They do not take part in any biomechanical calculation </p>
<br>
There is <b> no equivalent marker of RBAK</b>  on the left side. This optional marker help the autolabelling at detecting the left from the right side.
</div>

Check out our [palpation guidelines](Palpation.html) for get assistance on marker placement

Calibrations with either native processing (ie the wand defines  the coronal plane) or KAD can be also enable

## Anthropometric parameters



### Required

|Name | details |
|------|---------|
|Bodymass|Patient mass |
|Height| Patient height |
|Leg length|Full leg length, measured between the ASIS marker and the medial malleolus, via the knee joint.  Measure with patient standing, if possible. If the patient is standing in the crouch position, this measurement is NOT the shortest distance between the ASIS and medial malleoli, but rather the measure of the skeletal leg length.|
|Knee Width|The medio-lateral width of the knee across the line of the knee axis.. Measure with patient standing, if possible. |
|Ankle Width|The medio-lateral distance across the malleoli. Measure with patient standing, if possible. |
|Sole Thickness|The difference in the thickness of the sole at the toe and the heel. A positive sole delta indicates that the patient’s heel is raised compared with the toe |
|Elbow Width|Width of elbow along flexion axis (roughly between the medial and lateral epicondyles of the humerus) |
|Wrist Width|Anterior/Posterior thickness of wrist at position where wrist marker bar is
attached. |
|Shoulder Offset|Vertical offset from the base of the acromion marker to shoulder joint
center |
|Hand Thickness|Anterior/Posterior thickness between the dorsum and palmar surfaces of the hand. |




### Optional

|Name | details |
|------|---------|
|Inter-ASIS distance| ASIS-ASIS distance is the distance between the left ASIS and right ASIS. This measurement is only needed when markers cannot be placed directly on the ASIS, for example, in obese patients |
|ASIS-Trochanter Distance| ASIS-greater trochanter distance is the vertical distance, in the sagittal plane, between the ASIS and greater trochanter when the patient is lying supine. Measure this distance with the femur rotated such that the greater trochanter is positioned as lateral as possible.|
|Tibial Torsion| The angle between the knee flexion and the ankle dorsi-plantar axes. The ankle is usually externally rotated with respect to the knee flexion axis. **If you are using a KAD or Medial knee Marker**, and the medial malleoli markers are attached to the patient, the tibial torsion is  automatically calculated|
