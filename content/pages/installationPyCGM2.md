Title: PyCGM2 Installation
Slug: pyCGM2Installation


<div class="alert alert-dismissible alert-danger">
    <b> Vicon Nexus 2.9 now embeds pyCGM2(version 3.2.9) and all its dependancies. You don t need any installation.</b>
    <br>
    In case, you want to work with <b>your own python environment</b> and use the <b>latest version</b> of pyCGM2, you can follow the steps of the next section
</div>


<div class="alert alert-dismissible alert-warning">
  <p class="mb-0">In case you face with any issues during installation, we invite you to post details of your issues into the <a href="https://github.com/pyCGM2/pyCGM2/issues" class="alert-link">Github issue page</a>.</p>
</div>

<p class="text-danger">Reminder, pyCGM2 is
<ul>
 <li class="text-danger">compatible with python2.7 only</li>
 <li class="text-danger">compatible with Vicon Nexus 2.7 and later </li>
 <li class="text-danger"> tested with Qualisys qtm 2019.3 </li>
</ul>
</p>

## Installation

 * Download the last release of pyCGM2
   <p><a class="btn btn-primary btn-lg" href="https://github.com/pyCGM2/pyCGM2/releases/tag/version(3.2.15)">pyCGM2-version 3.2.15</a></p>

 * With the Window file explorer, go to your downloaded file and unzip it
 * Double click on **installer.bat** :

Eventually, the pyCGM2 package will be placed into the dedicated folder of any python libraries (i.e *YOUR_PYTHON_CORE_PATH\Lib\site-packages*).
The installer will create a new pyCGM2 folder in **c:/programData** gathering all settings.   


## Notes

* **For Vicon user only,** the installer will copy convenient nexus files (i.e. vst or pipelines) into the folder **C:/Users/Public/Documents/Vicon/Nexus2.x**

* **For Qualisys user only,** an optimal use of pyCGM2 qtm workflow requires installation of extra dependancies (see [here](./qtmInstallAddon.html) )  
