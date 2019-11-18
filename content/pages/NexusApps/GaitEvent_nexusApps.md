Title: Kinematic-based algorithms
Slug: KinematicBasedAlgorithms



A **kinematic-based algorithm**, detecting Gait events regardless of Force plate measurement

## Zeni's methods

### Reference

> Zeni, J.A., Richards, J.G., Higginson, J.S., 2008.
Two simple methods for determining gait events during treadmill
and overground walking using kinematic data 27, 710–714.
https://doi.org/10.1016/j.gaitpost.2007.07.007

## Nexus pipeline

<div class="alert alert-dismissible alert-warning">
<p class="mb-0"> In the current version, the pyCGM2 function requires standard CGM markers :
LPSI, RPSI, LHEE, LTOE, RHEE, RTOE
</div>


Located in C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines, you can import ready-to-use pipeline into Nexus :

  *  pyCGM2-Event-Detection.Pipeline

![zeni](/images/nexusApps/zeni.png){ width=75% }


<div class="alert alert-dismissible alert-info">
<p> All script arguments are detailed in the  <a href="/documentation//html//nexusOperations.html#event-detector">documentation API</a> </p>
</div>
