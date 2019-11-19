Title: CGM 2.4 - Nexus App Details
Slug: CGM24_NexusAppDetails


---

Return to all [available Nexus apps](/pages/nexusApps.html#list-of-available-applications)

---

<div class="alert alert-dismissible alert-warning">
  <h4 class="alert-heading">Warning</h4>
  <p class="mb-0">All Nexus Apps decribed in this website is related to <b>the use of pyCGM2 as external libraries of Vicon Nexus</b>.
  <br>
  If you want to use the Nexus-embedded pyCGM2 code, please refer to your Vicon Nexus documentation </p>
</div>

This [CGM2 version](/pages/CGM24-Overview.html)  introduce a two segment foot model.

## References

> Leboeuf, F., Sangeux, M., Reay, J., Greuel, H., Jones, R., Baker, R., 2018. P 120 - CGM2: Proposal of an evolved conventional gait model. Gait Posture 65, 436–437. https://doi.org/10.1016/j.gaitpost.2018.07.043


## Settings

The CGM2.4 settings are located at *C:/programData/pyCGM2*


<div class="alert alert-dismissible alert-primary">
<p>By default, settings:</p>
<ul>
<li>enable the flat foot option</li>
<li>project joint moment in the Joint Coordinate System (JCS)</li>
<li>set a uniform marker weight set</li>
</ul>
</div>


Check out [the documentation API](/documentation//html//settings.html#cgm-2-4-settings) for a complete description of the settings


## Nexus Pipelines

Located in *C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines*, you can import ready-to-use pipelines into Nexus :

  *  pyCGM2-CGM2_4-Calibration.Pipeline
  *  pyCGM2-CGM2_4-Fitting.Pipeline


| Calibration | Fitting |
|:------------|:--------|
|![cgm24calib](/images/nexusApps/CGM24calibration.png){ width=75% } | ![cgm24fitting](/images/nexusApps/CGM24fitting.png){ width=75% } |


<div class="alert alert-dismissible alert-info">
<p> All script arguments are detailed in the  <a href="/documentation//html//nexusOperations.html#cgm-2-4">documentation API</a> </p>
</div>
