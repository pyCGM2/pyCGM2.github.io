Title: CGM 1.0 - Nexus App Details
Slug: CGM10_NexusAppDetails


---

Return to all [available Nexus apps](/pages/nexusApps.html#list-of-available-applications)

---

<div class="alert alert-dismissible alert-warning">
  <h4 class="alert-heading">Warning</h4>
  <p class="mb-0">All Nexus Apps decribed in this website is related to <b>the use of pyCGM2 as external libraries of Vicon Nexus</b>.
  <br>
  If you want to use the Nexus-embedded pyCGM2 code, please refer to your Vicon Nexus documentation </p>
</div>


This [CGM version](/pages/CGM10.html) is **a replication of the native Vicon Plugin gait**


## Settings

The CGM1 settings are located at *C:/programData/pyCGM2*


<div class="alert alert-dismissible alert-primary">
<p>By default, settings:</p>
<ul>
<li>enable the flat foot option</li>
<li>project joint moment in the distal segment</li>
</ul>
</div>


Check out [the documentation API](/documentation//html//settings.html#cgm-1-settings) for a complete description of the settings


## Nexus Pipelines

Located in *C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines*, you can import ready-to-use pipelines into Nexus :

  *  pyCGM2-CGM1-Calibration.Pipeline
  *  pyCGM2-CGM1-Fitting.Pipeline


| Calibration | Fitting |
|:------------|:--------|
![cgm1calib](/images/nexusApps/CGM1calibration.png){ width=75% } | ![cgm1fitting](/images/nexusApps/CGM1fitting.png){ width=75% }


<div class="alert alert-dismissible alert-info">
<p> All script arguments are detailed in the  <a href="/documentation//html//nexusOperations.html#cgm-1-the-vicon-plugin-gait-clone">documentation API</a> </p>
</div>
