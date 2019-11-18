Title: Gap Filling
Slug: MoGapFill


Nexus proposes different gap filling methods. An approach published in Journal of Biomechanics, by Burke and Lasenby give accurate results.

The proposed method is based on **Low dimensional Kalman Filter**.


A concrete explanation of the algorithm can be found in this [post](articles/kalmanGapFilling.html)


## Reference

    > Burke, M., Lasenby, J., 2016.
    Estimating missing marker positions using low dimensional Kalman smoothing.
    J. Biomech. 49, 1854–1858.
    https://doi.org/10.1016/j.jbiomech.2016.04.016


## Nexus Pipelines

Located in C:/Users/Public/Documents/Vicon/Nexus2.x/Configurations/Pipelines, you can import ready-to-use pipeline into Nexus :

  *  pyCGM2-MoGapFill.Pipeline

  ![mogapfill](/images/nexusApps/kalmanMoGap.png){ width=75% }

  <div class="alert alert-dismissible alert-info">
  <p> No script arguments</a> </p>
  </div>
