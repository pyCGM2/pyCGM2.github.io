Title: Anatomical Segment Definitions
Slug: CGM-Segments

In biomechanical modelling each segment is defined by an orthogonal (right angle) coordinate system. Whilst the three axes are equivalent mathematically the model is best understood if each segment is considered to have a primary axis (running between the two joints at which it is attached to the neighbouring segments in the kinematic chain) and a secondary axis orthogonal to this and defined by a specific anatomical landmark that serves as a reference point for defining rotations about the principal axis.

Each segment is thus defined conceptually by defining its primary axis and secondary reference point. Of course a line and a segment define a triangle so each segment can be visualised by a triangle.

<table>
  <tr><td width="260">
  <figure align="middle">
    <img src="..\images\CGM1\PelvisSegment.png" alt="Anatomical defintion of pelvic segment" width="250">
  </td><td>
    <h2> Pelvis</h2>
    <p> The <em>primary axis</em> is the mediolateral axis running from one hip joint centre to the other. In most clinical applications it is assumed that the pelvis is symmetrical and that this axis is thus parallel to the line running from one anterior superior iliac spine (ASIS) to the other. </p>
    <p> The <em>reference point</em> for rotation about this axis is the mid-point of the posterior superior iliac spines (PSIS).</p>
    <p>The segment triangles is thus that formed by
      <ul>
        <li>the line running form one ASIS to the other and</li>
        <li>the mid-point of the PSISs</li>
      </ul>
    </p>
  </td></tr>
  <tr><td width="260">
  <figure align="middle">
    <img src="..\images\CGM1\FemurSegment.png" alt="Anatomical defintion of femur segment" width="100">
  </td><td valign="top">
    <h2> Femur</h2>
    <p> The <em>primary axis</em> is that running from the hip joint centre to the knee joint centre. </p>
    <p> The <em>reference point</em> is the lateral epicondyle.</p>
    <p>For validation purposes:
      <ul>
        <li>the hip joint centre will be taken as the geometrical centre of a sphere fitted to the articular surface of the femoral head. </li>
        <li>the knee joint centre will be taken as the mid-point of the medial and lateral epicondyles.  These are often difficult to palpate, however, and for some purposes the line between these landmarks will be assumed to be parallel to that linking the most posterior aspects of the femoral condyles.</li>
      </ul>
    </p>
  </td></tr>
  <tr><td width="260">
  <figure align="middle">
    <img src="..\images\CGM1\TibiaSegment.png" alt="Anatomical defintion of tibial segment" width="100">
  </td><td valign="top">
    <h2> Tibia</h2>
    <p> The <em>primary axis</em> is that running from the knee joint centre to the ankle joint centre. </p>
    <p> The <em>reference point</em> is the laterla malleolus.</p>
    <p>For validation purposes:
      <ul>
        <li>the ankle joint centre will be assumed to be the mid-point of the medial and lateral epicondyles.</li>
      </ul>
    </p>
  </td></tr>
  <tr><td width="260">
  <figure align="middle">
    <img src="..\images\CGM1\FootSegment.png" alt="Anatomical defintion of foot segment" width="250">
  </td><td valign="top">
    <h2> Foot</h2>
    <p> The <em>primary axis</em> is that running from the most posterior axis of the calcaneus along the second ray and parallel to the plantar surface of the foot. </p>
    <p> Rotation about this axis is not defined.</p>
  </td></tr>
</table>

<p></p>
Proceed to [marker placement theory](/pages/CGM-Markers).
