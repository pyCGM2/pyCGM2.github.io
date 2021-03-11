Title: The CGM 2.i Project
Slug: mainPage
save_as: index.html



<div class="alert alert-dismissible alert-danger">
    <b> The pyCGM2 website moves to another platform.</b>
    <br>
    The NEW WEB SITE is located <a href="https://pycgm2.netlify.app"> https://pycgm2.netlify.app </a>    
</div>



<div class="alert alert-dismissible alert-primary">
<b>PLEASE CITE THIS PAPER</b><br>
<a href="https://doi.org/10.1016/j.gaitpost.2019.01.034"> Leboeuf, F., Baker, R., Barré, A., Reay, J., Jones, R., Sangeux, M., 2019. The conventional gait model , an open-source implementation that reproduces the past but prepares for the future. Gait Posture 69, 126–129.</a>
</div>


The Conventional Gait Model (CGM) is a widely used biomechanical model for clinical gait analysis.
It was first developed in the 1980s and although, it has many strengths, it has several well-known weaknesses.
This project will develop and validate a new version of the CGM which maintains those strengths but corrects the weaknesses.

The new model will be as compatible as possible with the old but cannot be identical.
It is therefore important that future users know exactly how the new version differs from the old.
This will be ensured by developing the model in a series of iterations each addressing a specific weakness and
each fully validated to understand the behaviour of the new model in comparison to the old one.

The new model need to be **as open and transparent as possible**.

All code will be developed in [python](https://www.python.org/) and made available through
the platform [GitHub](https://github.com/).


<!----
<div class="alert alert-dismissible alert-danger">
    The project is part-funded by  <a href="https://www.vicon.com/">Vicon</a>
    and we will focus first on implementations to support use of the new models
    with <B>Vicon's suite</B> of clinical gait analysis software.
    <br>
    <B>We are opened to developing similar relationships with other manufacturers<B>
</div>
---->

## What's on the website

The web-site contains a full description of each of the models and instructions to capture and process data.

There is also a growing repository of [c3d files](/pages/Open-access-Gait-Data.html) that can be used for reference purposes.


## How to start

<div class="alert alert-dismissible alert-danger">
    <b> Vicon Nexus 2.9 now embeds pyCGM2(version 3.2.9) and all its dependancies. You don t need any installation. Just run Vicon Nexus</b>
    <br>
    In case, you want to work with <b>your own python environment</b> and use the <b>latest version</b> of pyCGM2, you can follow the next steps
</div>


 1. [Set up your python environment](/pages/pythonInstallation)
 2. [Install the pyCGM2 package](/pages/pyCGM2Installation)
 3. Take time to read [best practice](pages/bestPractice.html)
 4. Try one of our pyCGM2 Applications


 <div class="alert alert-dismissible alert-warning">
   If you are a vicon user and don t want to use Nexus-embedded pyCGM2 code</h4>
   <p class="mb-0">Take also time to read <a href="pages/nexusAppGuidelines.html" class="alert-link">basic explanations </a>.to know <b>how the code works</b> and how you can <b>interact</b> with it</p>
 </div>





Take time to read basic explanations of how the code works and how you can interact with it

## Contribute

As an open-source package, pyCGM2 will also live from your [contributions](/pages/contribute.html).

if you want :

   -  Help with validation
   - Share data
   - Share code
   - Propose a case study

feel free to [contact](/pages/contactus.html) us
