Title: CGM 2.6 - Nexus App Details
Slug: CGM26_NexusAppDetails


---

Return to all [available Nexus apps](/pages/nexusApps.html#list-of-available-applications)

---

<div class="alert alert-dismissible alert-warning">
  <h4 class="alert-heading">Warning</h4>
  <p class="mb-0">All Nexus Apps decribed in this website is related to <b>the use of pyCGM2 as external libraries of Vicon Nexus</b>.
  <br>
  If you want to use the Nexus-embedded pyCGM2 code, please refer to your Vicon Nexus documentation </p>
</div>

This [CGM2 version](/pages/CGM26-Overview.html) refines the definition of the knee flexion axis through the implementation of functional knee calibration methods.

2 methods are proposed :

  - the [Calibration2Dof](/pages/kneeCalib2dof.html)
  - the [SARA method](/pages/kneeCalibSara.html)

## Theory

The **Calibration2Dof** (Sangeux et al., 2016) method, inherit from the DynaKAD method (Baker, 1999). The method models the knee as a 2 degrees of freedom joint.
It postulates that varus- valgus range of movement is not physiological and derives from cross-talk with flexion-extension.
On this basis, the Calibration2Dof method consists in rotatig the femur coordinate system along its longitudinal axis to minimise the standard deviation of the varus-valgus angles
during functional knee flexion movements .

The **SARA method** is part of the family of Axis Transformation Technique (ATT) (Ehrig et al., 2007).
This method use the femur and tibia coordinate systems and models the knee as a hinge.

## References

**Calibration 2DOF**
> Sangeux, M., Barré, A., Aminian, K., 2016. Evaluation of knee functional calibration with and without the effect of soft tissue artefact. J. Biomech. 0, 655–667. https://doi.org/10.1016/j.jbiomech.2016.10.049

> Baker, R., 1999. A new approach to determine the hip rotation from clinical gait analysis data 18, 655–667.


**SARA**

> Ehrig, R., Taylor, W.R., Duda, G., Heller, M., 2007. A survey of formal methods for determining functional joint axes. J. Biomech. 40, 2150–7. https://doi.org/10.1016/j.jbiomech.2006.10.026

> Sangeux, M., Barré, A., Aminian, K., 2016. Evaluation of knee functional calibration with and without the effect of soft tissue artefact. J. Biomech. 0, 655–667. https://doi.org/10.1016/j.jbiomech.2016.10.049



## functionality

  * collect knee active or passive flexion ( one acquisition for each knee)
  * fill gaps
  * crop your c3d to the area of interest (or select start and end frame from the argument script box)
  * run the python operation

<div class="alert alert-dismissible alert-info">
 The Calibration2Dof method does not alter the knee joint centre. <br>
 The knee flexion calibrated from condyle markers serves as initial guess of the optimisation process. Ensure you have a correct palpation of the condyle markers.
</div>

<div class="alert alert-dismissible alert-info">
The SARA method alters the knee joint centre and then recompute the femur coordinate system from the the knee joint centre, considering the optimal knee flexion axis
</div>



## Nexus Pipeline


Located in C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines, you can import ready-to-use pipelines into Nexus :

  *  pyCGM2-CGM2_6-knee2Dof.Pipeline
  *  pyCGM2-CGM2_6-kneeSARA.Pipeline


for both pipelines, only the main python operation is different


| Calibration2Dof | SARA |
|:--------------- |:-----|
|![2dof](/images/nexusApps/CGM26Calib2Dof.png){ width=75% } | ![sara](/images/nexusApps/CGM26CalibSara.png){ width=75% }|



<div class="alert alert-dismissible alert-info">
<p> All script arguments are detailed in the  <a href="/documentation//html//nexusOperations.html#knee-calibration">documentation API</a> </p>
</div>
