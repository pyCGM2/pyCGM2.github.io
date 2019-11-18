Title: CGM 2.8 Modified kinetic output
Slug: CGM28-Overview

## Overview
The CGM generates non-orthogonal joint angles but orthogonal moments. There is also ambiguity about whether these should be referred to the coordiante system of the proximal or distal segment at any particular joint. Schache and Baker ([2007]( http://dx.doi.org/S0966-6362%2806%2900161-5)) have suggested that it would be more sensible to output the components of moment about the same axes as joint rotations are calculated. This should result in more clinically meaningful moment data and also removes the ambiguity over coordinate systems.

<figure align="middle" >
  <img src="..\images\CGM2\CGM28KneeMoments.png" alt="Use of orthogonal and non-orthogonal coordinate systems for describing knee moments" width="400">
  <figcaption>Use of orthogonal and non-orthogonal coordinate systems for describing knee moments <a href="http://dx.doi.org/S0966-6362%2806%2900161-5">Schache and Baker 2007</a>.</figcaption>
</figure>
<p></p>

## Proposal
CGM 2.8 will use the proposal of Schache and Baker ([2007]( http://dx.doi.org/S0966-6362%2806%2900161-5)) to output joint moments. (It should be noted that  moments are calculated conventionally - it is only after this that the components about the non-orthogonal axes are computed for data output.)
