Title: CGM 2.3 - Nexus App Details
Slug: CGM23_NexusAppDetails

---

Return to all [available Nexus apps](/pages/nexusApps.html#list-of-available-applications)

---


This [CGM2 version](/pages/CGM23-Overview.html)  remove wand-mouted marker for skin cluster

## Reference



## Settings

The CGM2.3 settings are located at *C:/programData/pyCGM2*


<div class="alert alert-dismissible alert-warning">
<p>By default, settings:</p>
<ul>
<li>enable the flat foot option</li>
<li>project joint moment in the Joint Coordinate System (JCS)</li>
<li>set a uniform marker weight set</li>
</ul>
</div>


Check out [the documentation API](/documentation//html//settings.html#cgm-2-3-settings) for a complete description of the settings


## Nexus Pipelines

Located in *C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines*, you can import ready-to-use pipelines into Nexus :

  *  pyCGM2-CGM2_3-Calibration.Pipeline
  *  pyCGM2-CGM2_3-Fitting.Pipeline


| Calibration | Fitting |
|:------------|:--------|
|![cgm23calib](/images/nexusApps/CGM23calibration.png){ width=75% } | ![cgm23fitting](/images/nexusApps/CGM23fitting.png){ width=75% } |


Check out [the documentation API](/documentation//html//nexusOperations.html) for the description of all operations


### script argument examples

<div class="alert alert-dismissible alert-info">
<p> All script arguments are detailed in the  <a href="/documentation//html//nexusOperations.html#cgm-2-3">documentation API</a> </p>
</div>


**Calibration**

> -l=0 -r=0 -ps=py

Disable *the flat foot option* on both feet and add the suffix *py* to all model outputs


**Fitting**

>  -ps=py --proj=Global

Add the suffix *py* to all model outputs and project joint moment in the *Global* coordinate system
