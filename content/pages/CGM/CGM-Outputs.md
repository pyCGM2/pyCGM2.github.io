Title: Outputs
Slug: CGM-Outputs

## Kinematic outputs
The primary kinematic outputs are the three dimensional joint angles representing the orientation of the distal segment with respect to the proximal segment. The CGM also outputs the three dimensional segment angles (in relation to the global axis system) for the pelvis and the transverse plane component for the foot (foot progression). All three dimensional angles are represented using Cardan angles which can generally be more easily visualised as globographic angles (Baker,[2011](http://dx.doi.org/10.1016/j.jbiomech.2011.04.031)).

As originally described the pelvic segment angles were described using the same Cardan sequence as the joint angles. Baker ([2001](http://dx.doi.org/10.1016/S0966-6362(00%2900083-7)), however,  has pointed out that this results pelvic angles that differ from the conventional clinical understanding of the angles and that reversing the Cardan sequence would rectify this (confirmed by [Foti et al., 2001](C:\Users\hls302\Dropbox\Active files\GitHub\pyCGM2io\content\reference files\Foti 2001 G&P (Pelvic angles%29.pdf)). This is the approach described in the sequence below but it should be noted that most implementations of the CGM still adopt the original approach.

<table>
  <tr><td width="260">
  <figure align="middle">
    <img src="..\images\CGM1\PelvisJoint.png" alt="Definition of pelvic angles" width="250">
  </td><td>
    <h2> Pelvis</h2>
    (with respect to global coordinate system represented by in the figure by the horizontal disk centred on the mid-point of the hip joints).
    <p></p>
    <ul>
      <li> Internal/external rotation is the angle by which the mediolateral axis of the pelvis is rotated within the horizontal plane (<font color="red">red angle</font>) </li>
      <li> Obliquity is the angle by which the mediolateral axis of the pelvis is raised out of the horizontal plane (<font color="green">green angle</font>)</li>
      <li> Anterior/posterior pelvic tilt is the rotation about the mediolateral axis of the pelvis (<font color="blue">blue angle</font>). </li>    
    </ul>
  <tr><td width="260">
  <figure align="middle">
    <img src="..\images\CGM1\HipJoint.png" alt="Definition of hip joint angles" width="250">
  </td><td>
    <h2> Hip</h2>
    (with respect to pelvis coordinate system as represented in the figure by the disk in the sagittal plane of the pelvis and centred on the hip joint centre)
    <p></p>
    <ul>
      <li> Flexion/extension is the angle by which the long axis of the femur is rotated within the sagittal plane (<font color="red">red angle</font>) </li>
      <li> Ab/adduction is the angle by which the long axis of the femur is rotated out of the sagittal plane (<font color="green">green angle</font>)</li>
      <li> Internal/external rotation is that about the long axis of the femur (<font color="blue">blue angle</font>). </li>    
    </ul>
  </td></tr>
  <tr><td width="260">
  <figure align="middle">
    <img src="..\images\CGM1\KneeJoint.png" alt="Defintion of knee joint angles" width="250">
  </td><td>
    <h2> Knee</h2>
    (with respect to femur coordinate system as represented in the figure by the disk in the sagittal plane of the femur and centred on the knee joint centre)
    <p></p>
    <ul>
      <li> Flexion/extension is the angle by which the long axis of the Tibia is rotated within the sagittal plane (<font color="red">red angle</font>) </li>
      <li> Ab/adduction is the angle by which the long axis of the tibia is rotated out of the sagittal plane (<font color="green">green angle</font>)</li>
      <li> Internal/external rotation is that about the long axis of the tibia (<font color="blue">blue angle</font>). </li>    
    </ul>
    Valgus and external rotation have been greatly exaggerated to clarify the figure.
  </td></tr>
  <tr><td width="260">
  <figure align="middle">
    <img src="..\images\CGM1\AnkleJoint.png" alt="Definition of ankle joint angles" width="250">
  </td><td>
    <h2> Ankle</h2>
    (with respect to tibia coordinate system as represented in the figure by the disk in the sagittal plane of the tibia and centred on the ankle joint centre)
    <p></p>
    <ul>
      <li> Flexion/extension is the angle by which the long axis of the foot is rotated within the sagittal plane (<font color="red">red angle</font>) </li>
      <li> Internal/external rotation is the angle by which the long axis of the foot is rotated out of the sagittal plane (<font color="green">green angle</font>)</li>
      <li> Rotation about the long axis of the foot was not defined in the original CGM </li>    
    </ul>
    Foot progression is defined similarly to ankle rotation except that the angle is calculated relative to the global coordinate system rather than the tibia.
  </td></tr>
</table>
## Kinetic outputs
If force plate data is avaiable then inverse dynamics can be used to calculate the moments at each joint (the net joint forces can also be calcualated but have not clear clinical interpretation).

One of the differences between the Newington and Helen Hayes variants was that Newington took body segment inertial parameters from the work of Dempster et al (1955, [full report](http://www.dtic.mil/dtic/tr/fulltext/u2/087892.pdf)), whereas Helen Hayes used data from Hinrichs et al. ([1985](http://dx.doi.org/10.1016/0021-9290(85&2990016-8)) which was based on the measurments of Clauser et al. (11969, [full report](http://www.dtic.mil/dtic/tr/fulltext/u2/710622.pdf)). Joint moments are generally insnesitive to the choice of such parameters ([Rao et al. 2006](http://dx.doi.org/10.1016/j.jbiomech.2005.04.014), [Pearsall et al. 1999](http://dx.doi.org/10.1016/S0966-6362(99%2900011-9) and only minor diferences would thus be anticipated in the outputs. VCM use data from Dempster et al.

Joint moments are presented as the compononents along orthogonal coordiante systems. Precisely which coordiante system was not specified in the original papers but the VCM defaulted to that of the distal segment (whilst giving the user an option to specifiy the proximal segment or the global coordiante system as alternatives).

Joint power is also calculated as the  dot product of the joint moment and joint angular velocity vectors (not that this is the true angular velocity vector and not the time derivative of the Cardan angles). Power is a scalar quantity and there is thus not biomechanical justification for presenting "components" of power.

<p></p>
Proceed to  [description of variants](/pages/CGM-Variants.html).
