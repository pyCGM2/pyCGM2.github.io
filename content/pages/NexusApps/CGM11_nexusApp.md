Title: CGM 1.1 - Nexus App Details
Slug: CGM11_NexusAppDetails


---

Return to all [available Nexus apps](/pages/nexusApps.html#list-of-available-applications)

---

This CGM version is a [*Vicon PiG as it should (have) work(ed) today*](/pages/CGM11.html)


## References

> Leboeuf, F., Baker, R., Barré, A., Reay, J., Jones, R., Sangeux, M., 2019. The conventional gait model , an open-source implementation that reproduces the past but prepares for the future. Gait Posture 69, 126–129. https://doi.org/10.1016/j.gaitpost.2019.01.034


## Settings

The CGM1.1 settings are located at *C:/programData/pyCGM2*


<div class="alert alert-dismissible alert-warning">
<p>By default, settings:</p>
<ul>
<li>enable the flat foot option</li>
<li>project joint moment in the Joint Coordinate System (JCS)</li>
</ul>
</div>


Check out [the documentation API](/documentation//html//settings.html#cgm-1-1-settings) for a complete description of the settings


## Nexus Pipelines

Located in *C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines*, you can import ready-to-use pipelines into Nexus :

  *  pyCGM2-CGM1_1-Calibration.Pipeline
  *  pyCGM2-CGM1_1-Fitting.Pipeline


| Calibration | Fitting |
|:------------|:--------|
|![cgm11calib](/images/nexusApps/CGM11calibration.png){ width=75% } | ![cgm11fitting](/images/nexusApps/CGM1fitting.png){ width=75% } |


<div class="alert alert-dismissible alert-info">
<p> All script arguments are detailed in the  <a href="/documentation//html//nexusOperations.html#cgm-1-1-the-vicon-plugin-gait-as-it-should-have-work-ed">documentation API</a> </p>
</div>
