Title: Best practice
Slug: bestPractice



<div class="alert alert-dismissible alert-danger">
  <p class="mb-0">
  The code fails if :
  <ul>
  <li>the progression axis is Z</li>
  <li>one marker is missing. So check out the markerset of each CGM2.i. This specification
  also means your can put marker on a single limb only</li>
  </ul>
</div>


As far as it goes, we recommand this pratice for performing any pyCGM2 applicatons :

 * work with **gap-free trial**. Zero-values might corrupt the Inverse kinematics processing especially
 * **crop your trial** to a zone of interest.  .
 * if you manually edit gait events, **start with a Foot strike**
 * Convenient gait plot panels are displayed if you have previously detected both **foot strike** and **foot off**
