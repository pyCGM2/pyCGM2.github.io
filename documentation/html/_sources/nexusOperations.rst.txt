========================================================
Nexus Operations
========================================================

Sections below present all available nexus python operations.

.. warning::
    Be aware, all arguments of the python scripts serve at altering the local settings.
    If you run one of these scripts, it will call its matching settings.




CGM 1 ( the Vicon plugin-gait Clone ).
========================================


Calibration
------------------

.. automodule:: CGM1_Calibration
    :members:

Fitting
------------------

.. automodule:: CGM1_Fitting
    :members:


CGM 1.1 ( the Vicon plugin-gait as it should (have) work(ed) ).
================================================================


Calibration
------------------

.. automodule:: CGM1_1_Calibration
    :members:

Fitting
------------------

.. automodule:: CGM1_1_Fitting
    :members:


CGM 2.1 (new Hip centre)
========================================


Calibration
------------------

.. automodule:: CGM2_1_Calibration
    :members:

Fitting
------------------

.. automodule:: CGM2_1_Fitting
    :members:



CGM 2.2 (Inverse Kinematics)
========================================


Calibration
------------------

.. automodule:: CGM2_2_Calibration
    :members:

Fitting
------------------

.. automodule:: CGM2_2_Fitting
    :members:


CGM 2.3 (skin markers)
========================================


Calibration
------------------

.. automodule:: CGM2_3_Calibration
    :members:

Fitting
------------------

.. automodule:: CGM2_3_Fitting
    :members:


CGM 2.4 (two segment foot)
========================================


Calibration
------------------

.. automodule:: CGM2_4_Calibration
    :members:

Fitting
------------------

.. automodule:: CGM2_4_Fitting
    :members:


CGM 2.5 (Upper limb)
========================================


Calibration
------------------

.. automodule:: CGM2_5_Calibration
    :members:

Fitting
------------------

.. automodule:: CGM2_5_Fitting
    :members:




CGM2.6 ( knee calibration)
========================================


Calibration2Dof method (dynakad-like)
----------------------------------------

Details about the Calibration2Dof method can be found in :

 *  `Baker et al (1999), Human Movement Science <http://dx.doi.org/10.1016/S0167-9457(99)00027-5>`_
 *  `Sangeux et al (2016), Journal of Biomechanics <https://doi.org/10.1016/j.jbiomech.2016.10.049>`_

.. automodule:: 2DofCalibration
    :members:


SARA method
-----------------------------

Details about the SARA method can be found in `Ehrig et al.(2007), Journal of Biomechanics <http://dx.doi.org/10.1016/j.jbiomech.2006.10.026>`_

.. danger:: the SARA method doesn t work for CGM version 1 to 2.2.


.. automodule:: SARA
    :members:


plotting
========================================

spatio-temporal parameters
-----------------------------

.. automodule:: plotSpatioTemporalParameters
    :members:


temporal Kinematics
---------------------

.. automodule:: plotTemporalKinematics
    :members:

temporal Kinetics
---------------------

.. automodule:: plotTemporalKinetics
    :members:


Gait-Normalized Kinematics
-----------------------------

.. automodule:: plotNormalizedKinematics
    :members:

Gait-Normalized Kinetics
-----------------------------

.. automodule:: plotNormalizedKinetics
    :members:

Movement Analysis Profile (MAP)
-------------------------------

.. automodule:: plotMAP
    :members:

Temporal EMG
-------------------------------

.. automodule:: plotTemporalEmg
    :members:


Gait-Normalized EMG
-----------------------------

.. automodule:: plotNormalizedEmg
    :members:



Event Detector
========================================


Zeni's method
----------------------------------------

Zeni's method is  kinematic based only.

Detail can be found in   `Zeni et al (2008), Gait and Posture <https://doi.org/10.1016/j.gaitpost.2007.07.007>`_

.. automodule:: zeniDetector
    :members:


External Contribution
========================================


Kalman Gap Filling
----------------------------------------
This contribution comes from Mickael Burke.

Details about the method can be found in `Burke and Lasenby. (2016), Journal of Biomechanics <https://doi.org/10.1016/j.jbiomech.2016.04.016>`_


.. automodule:: KalmanGapFilling
    :members:
