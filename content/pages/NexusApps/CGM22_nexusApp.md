Title: CGM 2.2 - Nexus App Details
Slug: CGM22_NexusAppDetails


---

Return to all [available Nexus apps](/pages/nexusApps.html#list-of-available-applications)

---


This [CGM2 version](/pages/CGM22-Overview.html) use **an inverse kinematic** processing as default segmental tracking method.


## References

> Leboeuf, F., Sangeux, M., Baker, R., 2017. Direct kinematics and kinematic fitting provide very similar outputs when using the conventional gait model. Gait Posture 57, 196. https://doi.org/10.1016/j.gaitpost.2017.06.364


## Settings

The CGM2.2 settings are located at *C:/programData/pyCGM2*


<div class="alert alert-dismissible alert-warning">
<p>By default, settings:</p>
<ul>
<li>enable the flat foot option</li>
<li>project joint moment in the Joint Coordinate System (JCS)</li>
<li>set a uniform marker weight set</li>
</ul>
</div>


Check out [the documentation API](/documentation//html//settings.html#cgm-2-2-settings) for a complete description of the settings


## Nexus Pipelines

Located in *C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines*, you can import ready-to-use pipelines into Nexus :

  *  pyCGM2-CGM2_2-Calibration.Pipeline
  *  pyCGM2-CGM2_2-Fitting.Pipeline


| Calibration | Fitting |
|:------------|:--------|
|![cgm22calib](/images/nexusApps/CGM22calibration.png){ width=75% } | ![cgm22fitting](/images/nexusApps/CGM22fitting.png){ width=75% } |


<div class="alert alert-dismissible alert-info">
<p> All script arguments are detailed in the  <a href="/documentation//html//nexusOperations.html#cgm-2-3">documentation API</a> </p>
</div>
