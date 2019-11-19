Title: Nexus Application Guidelines
Slug: nexusAppGuidelines


<div class="alert alert-dismissible alert-warning">
  <h4 class="alert-heading">Warning</h4>
  <p class="mb-0">All Nexus Apps decribed in this website is related to <b>the use of pyCGM2 as external libraries of Vicon Nexus</b>.
  <br>
  If you want to use the Nexus-embedded pyCGM2 code, please refer to your Vicon Nexus documentation </p>
</div>


## Functionality

pyCGM2 operations were designed on **the basis of the C3d format file**. Operations read the c3d and store data into it with the same nomenclature of the Vicon Pig ( ie LHipAngles, LFootProgressAngles...).

Model processing with pyCGM2 doesn't differ from the use of Vicon PiG in Nexus. The model need to be first calibrate though the pipeline:
**Calibration** (ie PiG Static) after static reconstruction. Then, kinematics and kinetics of motion trials are worked out through the pipeline: **fitting** (ie PiG Dynamic)


<div class="alert alert-dismissible alert-warning">
  <p class="mb-0">All nexus Apps developped with PyCGM2 come along with ready-to-use pipelines located in the
  folder (C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines).<br>
  You can conveniently imported them from Nexus </p>
</div>


Each pyCGM2 operations rely on pre-definied **settings** (located at c:/programData/pyCGM2).

<div class="alert alert-dismissible alert-warning">
<ul>
<li>&nbsp;If the content of the setting file does t match with your gait analysis routine ( for instance, you usually calibrate your Vicon PiG with the flat foot option disable, <strong>you can alter the setting file directly</strong> )</li>
<li>If you want to alter the behaviour of the setting file occasionaly, simply because your ongoing gait analysis does t match with settings, <strong>you need specifying it through script arguments&nbsp;</strong> &nbsp;</li>
</ul>
</div>


As example, this figure presents the *pyCGM2-CGM1 calibration* Nexus Pipeline.

![pipeline](/images/nexusApps/exampleScriptArg.png){ width=100%}

The blue highlihted-operation calibrates the CGM by calling the setting file: *CGM1.settings**"**.

The *CGM1.settings* file enables flat foot option by default and unfortunatly your patient cannot stand with his left foot flat on the floor.
As a consequence, you need to disable the left flat foot option through **the Script argument box**


<div class="alert alert-dismissible alert-info">
<p>Check out the <a href="/documentation//html//index.html">documentation API</a> for a comprehensive description of settings and vicon operations</p>
</div>
