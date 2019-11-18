Title: CGM2 - QTM Installation add-on
Slug: qtmInstallAddon


## Installation add-on

For an optimal use of pyCGM2-qtm workflows,  install **Mokka** and the **Qualisys gait web report uploader** in addition to pyCGM2


**Mokka : MOtion Kinematics and Kinetics Analyser**

 * download [Mokka](https://biomechanical-toolkit.github.io/mokka/)
 * unzip the downloaded folder
 * add the folder to your [windows path variable](https://docs.alfresco.com/4.2/tasks/fot-addpath.html)



**Gait web report uploader**


 * download [paf-web-report-uploader](https://github.com/qualisys/paf-web-report-uploader)
 from the Qualisys github folder
 * open a window console
 * go to your local folder
 * type the command
 ```
 python setup.py install
 ```

 the package called **qtmWebGaitReport** will be added to you python libraries (i.e into the folder *YOUR_PYTHON_CORE_PATH\Lib\site-packages\qtmWebGaitReport-(version)-py2.7.egg*).

 the final steps consist in configuring your qualisys.com credentials to log in to Report Center (https://report.qualisys.com)

  * edit a file *config.json* in the folder *YOUR_PYTHON_CORE_PATH\Lib\site-packages\qtmWebGaitReport-(version-py2.7.egg)* with the following content

  ```
  {
    "baseUrl" : "https://report.qualisys.com",
    "clientId" : "YOUR ID",
    "token" : YOUR TOKEN"
  }
  ```
