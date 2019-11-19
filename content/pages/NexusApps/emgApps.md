Title:EMG - Nexus Apps
Slug: emgApps


---

Return to all [available Nexus apps](/pages/nexusApps.html#list-of-available-applications)

---


<div class="alert alert-dismissible alert-warning">
  <h4 class="alert-heading">Warning</h4>
  <p class="mb-0">All Nexus Apps decribed in this website is related to <b>the use of pyCGM2 as external libraries of Vicon Nexus</b>.
  <br>
  If you want to use the Nexus-embedded pyCGM2 code, please refer to your Vicon Nexus documentation </p>
</div>

pyCGM2 proposes convenient operations for processing and then plotting EMG.

You can display :

 *  temporal EMG

![tempEmg](/images/emg/temporalEMG.png){ width=75% }

 *  gait normalized envelop

![envEmg](/images/emg/emgEnvelop.png){ width=25% }


<div class="alert alert-dismissible alert-primary">
First, set your own settings or adapt your emg acquisition software to our settings
</div>

## Settings

The emg settings are located at *C:/programData/pyCGM2*

Check out [the documentation API](/documentation//html//settings.html#emg-settings) for a complete description of the settings

The pre-defined emg configuration in pyCGM2 is the following:

<div class="alert alert-dismissible alert-warning">
Your EMG signal must be named : EMG1 , EMG2, EMG3,... EMG16 within the c3d file
</div>

 * EMG1: left rectus femoris
 * EMG2: right rectus femoris
 * EMG3: left vastus lateralis
 * EMG4: right vastus lateralis
 * EMG5: left semitendinosus
 * EMG6: right semitendinosus
 * EMG7: left tibialis anterior
 * EMG8: right tibialis anterior
 * EMG9: left soleus
 * EMG10: right soleus
 * EMG11 to 16: None


## Nexus Pipeline


Located in C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines, you can import ready-to-use pipeline into Nexus :

  *  pyCGM2-EMG.Pipeline

![emg](/images/nexusApps/emgPipeline.png){ width=75% }


<div class="alert alert-dismissible alert-info">
<p> All script arguments are detailed in the  <a href="/documentation//html//nexusOperations.html#plotting">documentation API</a> </p>
</div>
