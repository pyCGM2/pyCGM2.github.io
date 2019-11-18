Title: CGM 2.7 Pelvis location in larger people
Slug: CGM27-Overview

Determing exactly where the pelvis is, and hence the hip joint centres are, within the abdomen is challenging for the CGM (as it is for any biomechanical model). In their original paper Davis et al. ([1991](http://dx.doi.org/10.1016/0167-9457%2891%2990046-Z)) allowed a measurement of the distance between the ASIS marker and the ASIS landmark in the horizontal direction to be used to help determine the position of the hip joint centre. Although this allows a mechanism for addressing this issue few analysts have confidence in its use.

Recent data suggesting that pelvic dimensions scale linearly with leg length ([Hara et al .2016](http://dx.doi.org/10.1038/srep37707)) has the potential to give good estimates of the size of the pelvis.

Akthough poorly documented in the formal literature several groups have previously experimented with methods for palpating the ASIS landmarks in relation to the ASIS and PSIS markers in a static calibration trial to estimate the pelvic position.

## Proposal
The equations of Hara et al. ([2016](http://dx.doi.org/10.1038/srep37707)) will be used to model the pelvic landmarks for kinematic fitting. Assuming equal weigthing this will genearlly result in the pelvis being located mid-way between the ASIS and PSIS markers.

A modification to this will be to use a pointer to indicate the position of first one ASIS landmark and then the other while the other ASIS and both PSIS markers remain in position. This will allow for a calibration of the ASIS landmarks within the pelvis which coupled with the estimate of pelvis size (based on leg length) will allow a calibration of modelled pelvic marker positions to fit the pelvis during dynamic trials.
