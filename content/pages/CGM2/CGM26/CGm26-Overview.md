Title: CGM 2.6 Knee calibration
Slug: CGM26-Overview

## Overview
The difficulty in defining the coronal plane of the thigh was first discussed by Ramakrishnan et al. in [1991](http://dx.doi.org/0021-9290%2891%2990175-M) and has been a challenge for clinical gait analysts ever since. ALthough there is less evidence to support the claim, models based upon the CAST technique ([Cappozzo et al. 1995]( http://dx.doi.org/10.1016/0268-0033%2895%2991394-T))  are generally assumed to be more robust to this error than the CGM. Allowing a calibration marker on the medial epicondyle has thus been introduced in CGM1.1 and is expected to bring the CGM into line with the other models. Given the importance of hip rotation in many clinical analyses however this is unlikley to be sufficient.

Although the coronal plane of the femur within the CGM is defined as that containing the medial and lateral epicondyles it is generally well established that the transepicondylar axis is aligned with the functional axis for knee flexion to within the accuracy attainable using marker based gait analysis and thus functional calibration appears to offer a solution. A variety of approaches have been proposed ([Baker et al. 1999](http://dx.doi.org/10.1016/S0167-9457%2899%2900027-5); [Schwartz & Rozumalski, 2005]( http://dx.doi.org/10.1016/j.jbiomech.2004.03.009); [Ehrig et al, 2007](http://dx.doi.org/S0021-9290%2806%2900415-5)). Until recently these had been validated by a number of essentially technical measures without reference to any gold standard.

<figure align="middle" >
  <img src="..\images\CGM2\CGM26Knees.png" alt="Analysis of different methods of functional knee claibration" width="400">
  <figcaption>Analysis of different methods of knee calibration <a href="http://dx.doi.org/10.1016/j.gaitpost.2016.09.008">Sauret et al. 2016</a>.</figcaption>
</figure>
<p></p>

Three very recent studies however ([Passmore & Sangeux, 2016](http://dx.doi.org/10.1016/j.gaitpost.2016.02.006); [Sangeux et al. 2016](http://dx.doi.org/10.1016/j.jbiomech.2016.10.049) and [Suaret et al. 2016](http://dx.doi.org/10.1016/j.gaitpost.2016.09.008)) have compared techniques with anatomical reference data. All confirmed that the functional calibration was effective and that the simplest method (minimising the standard deviation of the coronal plane cross-talk, [Baker et al. 1999](http://dx.doi.org/10.1016/S0167-9457%2899%2900027-5)) was at least as effective as later methods).

## Proposal
CGM 2.6 will incorporate functional calibration of the knee joint based upon a dynamic functional calibration test conducted after static calibration but before fitting the model to walking trials. The software will run on any .c3d trial that includes a sufficient range of knee movement to allow calibration but clinical recommendations will focus on non-weightbearing knee flexion coducted with or without the assistance of a gait analyst.

The approach will be validated using existing datasets including those with gold standard anatomical references.
