Title: Overview of issues to be addressed
Slug: CGM2-Issues

## Backard compatibility and future proofing
Although backwards compatibility is listed above as the eighth criteria, ensuring that the new CGM is accepted by existing users will be largely dependent on it appearing as a development of the previous model rather than the creation of a new one. On the other hand some differences will be required to exploit technological and clinical progress in the thirty years since the model was originally developed. Maintaining an appropriate balance between these two apparently opposing and contradictory requirements is a key component of this project. The sections below are intended to give an overview of how this, and other challenges will be addressed.

The primary case for this being a development of the CGM (rather than a development of a new model) will be that the anatomical definition of lower limb segment co-ordinate systems ([see current defintions](../pages/CGM-Definitions)) and the model degrees of freedom (three rotation per joint) will be preserved. A two segment foot will be introduced in such a way that the hind-foot is similar to the existing foot and a new forefoot segment will be introduced that is similar to that of the [Oxford Foot Model]( http://dx.doi.org/10.1016/S0021-9290%2801%2900101-4
).

Despite preserving the overall structure of the model some discrepancies with older versions will be inevitable because the new version will calibrate and track these segments better. One example is the incorporation of the Harrington equations [9] to determine the hip joint centres as published research clearly now indicates these are superior to the Davis model. In such cases there will be a rigorous analysis of how such developments affect results.

Another difference will arise as a result of improved understanding of soft tissue artefact (STA) since the original development of the CGM . We now understand that the conventional lateral knee marker is particularly prone to STA ([Tasi et al. 2009](http://dx.doi.org/10.4015/S1016237209001283),  [Akbarshahi et al. 2010](http://dx.doi.org/10.1016/j.jbiomech.2010.01.002))  and other tracking markers for the femur and tibia segments are preferable. Tools will be developed to ensure that data captured with the old markerset can be reprocessed to be as compatible as possible with the new model (e.g. a version of the CGM based on the old marker set but with the new hip joint centre regression equations will be provided).

Continuity with the old model will also be reinforced by introducing modifications sequentially rather than as a single step. Whenever modifications are introduced data will be collected to compare old and new models and any discrepancies will be rigorously documented.

Future proofing will be ensured by moving to a kinematic fitting (inverse kinematic) approach. The most important developments that the model is likely to need to incorporate will be an improved understanding of how soft-tissue artefact affects outputs and kinematic fitting will allow such understanding to be incorporated into the model. Inverse kinematic modelling is also more compatible with muscle length and function calculations than the current vector algebra approach.

## Transparency and standardisation
Despite there being good proprietary documentation of the CGM and reasonably comprehensive descriptions in the academic literature, many implementations of the CGM have developed a negative reputation for being black box applications. The new model will be developed by the team at the University of Salford and the Royal Children’s Hospital, Melbourne in [Python](https://www.python.org(/) and the code will be both be made available through [GitHub](https://github.com/) and lodged as an electronic appendix to the academic articles describing the model. Given Vicon's sponsorship we will focus first on implemenations specifically desinged to be used within the exisitng suite of Vicon products (Nexus and Polygon in particular)

The model itself is envisaged as a standard package with minimal options which will be used unmodified by the users for whom it is intended. Other groups, with the skills to work with the publically available code, will clearly be able to adapt it however they see fit.

## Ease of use and quality assurance
Quality assurance will be enhanced by separating between calibration and tracking markers (current versions of the CGM use many markers with both calibration and tracking function). Doing this makes repeatability studies within and between gait analysts and between services much easier as these can be confined to the placement of calibration markers for the static trial rather than for all makers for static and walking trials. Ease of use will be ensured by minimising the number of markers that are required, particularly calibration markers that are required to be placed accurately. A minimum of anthropometric parameters will be required.

The new model will also incorporate measures of quality of model fit to assist with quality assurance.

Whilst the project focuses on model development, manufacturers will be encouraged and supported to develop new and robust workflows to facilitate easy and robust collection of high quality data.
