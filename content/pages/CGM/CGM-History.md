Title: History and Nomenclature
Slug: CGM-History

A family of extremely similar biomechanical models designed to be used in clinical gait analysis were developed in the 1980s. The two main groups, based at Newington Children’s Hospital, Connecticut, and the Helen Hayes Hospital in New York, communicated when developing their models (but there are now different memories about the extent of that collaboration).

## Antecedents

The origins of the model can be traced back to the work of John Hagy and David Sutherland ([1972](http://jbjs.org/content/54/4/787)) working at the Shriner’s Hospital in San Francisco. They digitised the position of joints as estimated from biplanar cine recordings and used a three dimensional analysis to compute a range of angles that they considered clinically important. The approach was developed by a master's student Patrick Shoemaker ([1978](C:\Users\hls302\Dropbox\Active files\GitHub\pyCGM2io\content\reference files\Shoemaker 1978 MSc.pdf)) to incoporate Euler angles to represent true three dimensional joint orientation proposed by Ed Chao ([1980](http://dx.doi.org/10.1016/0021-9290(80%2990044-5)).

<figure align="middle">
 <img src="../images/CGM1/Sutherland femoral rotation.png" alt="Image of Sutherland and Hagy's derivation of femoral rotation" width="400">
 <figcaption align="middle">Image of Sutherland and Hagy's <a href="http://jbjs.org/content/54/4/787">(1972)</a> derivation of femoral rotation.</figcaption>
</figure>

## Newington Children's Hospital
Jim Gage, an orthopaedic surgeon, visited Sutherland (who had moved to San Diego by this time), prior to establishing a new gait analysis service at the Newington Children's Hospital (now superseded by the [Connecticut Children's Medical Centre](https://en.wikipedia.org/wiki/Connecticut_Children's_Medical_Center)). He worked with a number of engineers including Scott Tashman, Dennis Tyburski and Roy Davis who further developed the model. The most important development was to base the angle calculation on estimations of the joint centre locations (rather than directly from the positon of markers). An early version of this model was ready for the first patient seen by the service in July 1981.
Inverse dynamics were also implemented following the approach of David Winter ([1978](http://dx.doi.org/10.1007/BF00337349)) and had been incororated by 1985. The work is reported in two papers ([Davis et al., 1991](http://dx.doi.org/10.1016/0167-9457(91%2990046-Z), [Ounpuu et al. 1991](http://dx.doi.org/10.1097/01241398-199105000-00012)).

<figure align="middle">
 <img src="../images/CGM1/Opening of Newington lab.jpg" alt="First child in the Newington Lab, July 1981" width="250px">
 <figcaption align="middle">First child in the Newington Lab, July 1981</figcaption>
</figure>


## Helen Hayes Hospital
Developments at Helen Hayes occurred through the mid 1980s led by Murali Kadaba building on developments from Newington. The model was shared with 6 other users of the first generation of Vicon measurement systems. Three papers from Helen Hayes were the first to describe the model in the academic literature (Kadaba et al. [1989](http://dx.doi.org/10.1002/jor.1100070611), [1990](http://dx.doi.org/10.1002/jor.1100080310); [Ramikrishnan et al., 1991](http://dx.doi.org/10.1016/0021-9290(91%2990175-M))

## Vicon
In the late 1980s Oxford Metrics (manufacturers of the [Vicon](https://www.vicon.com/) systems) realised that they needed software to make their products clinically useful and in 1991 released their _Clinical Manger_ software. This incorporated a version of the CGM which was written in consultation with staff at both Newington and Helen Hayes. Over the years the code has proved particularly robust which is probably a product of the development of the new model with exhaustive cross-checking against the two independent implementations of essentially the same model. This became known as the _Vicon Clinical Manager_ (VCM))model. In 1998 Vicon introduced their Workstation software and cloned the VCM model as [_Plugin Gait_ (_PiG_)](https://www.vicon.com/downloads/documentation/vicon-documentation/plug-in-gait-model-details).

<figure align="middle">
  <iframe width="400" height="300"  src="https://www.youtube.com/embed/vyz1cFKAcgg" frameborder="0" allowfullscreen alt="Vicon Clinical Manager graphical user interface">
  </iframe>
  <figcaption>Vicon Clinical Manager graphical user interface</figcaption>  
</figure>

When developing PiG Vicon added an upper body model. This has never been published (other than in proprietary literature) or validated and will not be considered as part of the CGM.

## Subsequent use
Many of the early and influential clinical gait analysis facilities used Vicon systems and thus the conventional gait model. Five earlier papers documented its use and properties providing validation for academic work. Jim Gage became a strong international advocate for clinical gait analysis and started running educational courses with Roy Davis and Sylvia Ounpuu from 1991 onwards which were based around the model.

<figure align="middle">
 <img src="https://www.gillettechildrens.org/cache/Gait_Course10_(2%29_400_206_c1.jpg" width="400" alt="Jim Gage (4th from left) and faculty of gait course in 2015">
 <figcaption>
 <a href="https://www.gillettechildrens.org/blog/gillette-hosts-global-experts-in-gait-and-motion-analysis/">Jim Gage (4th from left) and faculty of gait course in 2015</a>
 </figcaption>  
</figure>

A series of three textbooks consolidated the content. By the early 2000s the CGM had thus become the most widely used and understood biomechanical model for clinical gait analysis and was also used widely for non clinical use.

<figure align="middle">
<a href="https://www.amazon.co.uk/Analysis-Cerebral-Clinics-Developmental-Medicine/dp/0521412773"><img src="..\images\CGM1\Gage I.png" alt="Gage's first book" width="150"></a>
<a href="http://admin.cambridge.org/academic/subjects/medicine/pediatrics-and-child-health/treatment-gait-problems-cerebral-palsy?format=WW"><img src="..\images\CGM1\Gage II.png" alt="Gage's second book" width="147"></a>
<a href="http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1898683654.html"><img src="http://media.wiley.com/product_data/coverImage300/54/18986836/1898683654.jpg" alt="Gage's third book" width="148"></a>
</figure>

## Nomencalture
As a result of the history outlined above the model has been referred to as the _Newington_, _Davis_, _Gage_, _Helen Hayes_, _Kadaba_, _VCM_ and _PiG_ model. This has led to considerable confusion with a misconception that there were significant differences between the models. Although there are small differences the models are essentially similar. To emphasize this Richard Baker introduce the name Conventional Gait Model when delivering a tutorial session, [_All you ever wanted to know about the Conventional Gait Model but were afraid to ask_ for the _Gait and Clinical Movement Analysis Society_](https://wwrichard.net/ayewtkatcgmbwata/) in 2003. He reinforced this terminology in his book, [_Measuring Walking: a Handbook of Clinical Gait Analysis_ (2013)](http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1908316667.html).

<figure align="middle">
<a href="https://wwrichard.net/ayewtkatcgmbwata/"><img src="..\images\CGM1\CDCover.png" alt="Conventional Gait Model CD" width="250" ></a>
<figcaption>Click on image to access</figcaption>
</figure>

## Competitors
Vicon's main competitor in North America was the [_Motion Analysis Corporation_](http://www.motionanalysis.com/). Its software implemented a different model based on the Cleveland Clinic Markerset. This has never been fully described in the academic literature and remained, essentially, a proprietary model. In Europe a group led by Aurelio Cappozzo ([1995](http://dx.doi.org/10.1016/0268-0033(95%2991394-T)) proposed the _Calibration of Anatomical System Technique_ (_CAST_) which was widely replicated in academic studies (and implemented by Italian manufacturer [_BTS_](http://www.btsbioengineering.com/)) but was not adopted much for clinical purposes outside Italy. More recently there has been a resurgence of interest in this technique which is the basis of [_Visual3d_](http://www2.c-motion.com/products/visual3d) modelling software from [_C-Motion_](http://www2.c-motion.com/). The _IOS_ mdoel from Bologna is a development of the CAST system and is probably the most validated gait model other than the CGM ([Leardini et al. 2007](http://dx.doi.org/10.1016/j.gaitpost.2006.12.018), [Manca et al. 2010](http://dx.doi.org/10.1016/j.gaitpost.2010.05.011).

## Current status
Despite several acknowledged weaknesses there has been little real development of the CGM model since the mid 1980s. With a greater diversity or suppliers of gait analysis hardware and software a greater variety of biomechanical models is now available and many new centres are choosing alternatives to the CGM. The current status is that the CGM is still probably the most widely used model for clinical gait analysis and is still the preferred model for most of the more established clinical services but does not have the same predominance as it used to.
