Title: CGM 2.5 - Nexus App Details
Slug: CGM25_NexusAppDetails


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

## Reference



## Settings

The CGM2.5 settings are located at *C:/programData/pyCGM2*


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

  *  pyCGM2-CGM2_5-Calibration.Pipeline
  *  pyCGM2-CGM2_5-Fitting.Pipeline


| Calibration | Fitting |
|:------------- |:-------------|
|![cgm25calib](/images/nexusApps/CGM25calibration.png){ width=75% } | ![cgm25fitting](/images/nexusApps/CGM25fitting.png){ width=75% } |


<div class="alert alert-dismissible alert-info">
<p> All script arguments are detailed in the  <a href="/documentation//html//nexusOperations.html#cgm-2-5">documentation API</a> </p>
</div>
