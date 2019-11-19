Title: CGM 2.1 - Nexus App Details
Slug: CGM21_NexusAppDetails


---

Return to all [available Nexus apps](/pages/nexusApps.html#list-of-available-applications)

---

<div class="alert alert-dismissible alert-warning">
  <h4 class="alert-heading">Warning</h4>
  <p class="mb-0">All Nexus Apps decribed in this website is related to <b>the use of pyCGM2 as external libraries of Vicon Nexus</b>.
  <br>
  If you want to use the Nexus-embedded pyCGM2 code, please refer to your Vicon Nexus documentation </p>
</div>

This [CGM2 version](/pages/CGM21-Overview.html) altered the Hip Joint centre in accordiance with **Hara's regressions**


## References

> Leboeuf, F., Reay, J., Jones, R., Sangeux, M., 2019. The effect on conventional gait model kinematics and kinetics of hip joint centre equations in adult healthy gait. J. Biomech. https://doi.org/10.1016/j.jbiomech.2019.02.010

> R. Hara, J. McGinley, C. Briggs, R. Baker, and M. Sangeux, “Predicting the location of the hip joint centres, impact of age group and sex,” Sci. Rep., vol. 6, p. 37707, 2016.

> Leboeuf, F., Sangeux, M., Baker, R., 2017. The choice of hip regression equations has small effect on kinematic and kinetic outputs of the conventional gait model. Gait Posture 57, 161. https://doi.org/10.1016/j.gaitpost.2017.06.345


## Settings

The CGM2.1 settings are located at *C:/programData/pyCGM2*


<div class="alert alert-dismissible alert-primary">
<p>By default, settings:</p>
<ul>
<li>enable the flat foot option</li>
<li>project joint moment in the Joint Coordinate System (JCS)</li>
</ul>
</div>


Check out [the documentation API](/documentation//html//settings.html#cgm-2-1-settings) for a complete description of the settings


## Nexus Pipelines

Located in *C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines*, you can import ready-to-use pipelines into Nexus :

  *  pyCGM2-CGM2_1-Calibration.Pipeline
  *  pyCGM2-CGM2_1-Fitting.Pipeline


| Calibration | Fitting |
|:------------|:--------|
|![cgm21calib](/images/nexusApps/CGM21calibration.png){ width=75% } | ![cgm21fitting](/images/nexusApps/CGM21fitting.png){ width=75% } |


<div class="alert alert-dismissible alert-info">
<p> All script arguments are detailed in the  <a href="/documentation//html//nexusOperations.html#cgm-2-1">documentation API</a> </p>
</div>
