# Researcher content inventory

## Source and scope

- Source: `source/research-portfolio.pdf`, 17 pages, titled *Research Portfolio*.
- References below use 1-based PDF page numbers (the cover is page 1); printed page numbers on subsequent pages agree.
- This inventory records what the portfolio states. Linked papers, repositories, reports, and the thesis were not independently inspected. Publication and manuscript statuses are as reported in the PDF, not verified current statuses.
- Personal contributions are distinguished from broader team activities. Missing dates, qualifications, results, and statuses are not inferred.

## Profile

**Source: PDF pp. 1-3.**

- Display name: **Abigail A. Adjetey Bisa** (p. 1).
- Research focus: remote sensing, geographic information science (GIS), and artificial intelligence for agricultural and environmental applications (pp. 1-2).
- Experience described: UAV multispectral crop nutrient assessment; satellite land-use/land-cover (LULC) classification; deep learning for satellite image classification; GIS analysis of cocoa agroforestry landscapes (p. 2).
- Research trajectory: field data collection, remote sensing, geospatial processing, machine learning/deep learning, and spatial prediction and decision-support products (p. 2).
- Attribution principle: work by supervisors, co-authors, and other team members is not claimed as the researcher's own (p. 3).
- Current job title, employer, and current professional affiliation are not stated. KNUST is identified in the education context (pp. 1, 16).

## Research interests

**Source: PDF p. 2.**

| Theme | Stated interests |
| --- | --- |
| Remote sensing | Satellite and UAV multispectral imagery, image processing, vegetation indices, time-series analysis |
| Geospatial AI | Machine learning and deep learning for classification, prediction, and spatially explicit environmental applications |
| Agricultural applications | Crop nutrition, cocoa agroforestry, precision agriculture, landscape monitoring |
| Environmental applications | Deforestation monitoring, land-use/land-cover mapping, sustainable land management |

## Research status inventory

**Source: PDF pp. 4-16.**

| Work | Status supported by the PDF | References |
| --- | --- | --- |
| Cocoa nutrient assessment MSc research | Submitted thesis; thesis entry dated 2025. Related manuscript in preparation. No peer-reviewed publication is claimed for this nutrient study. | pp. 7-8, 16 |
| Shade canopy/agroforestry research | Co-authored research with a related published shade-tree optimisation paper. A separate related soil-quality/cocoa-yield manuscript is under review. The broader project's ongoing/completed status is unspecified. | pp. 10-11, 16 |
| Deforestation-Free Cocoa monitoring | Documented research experience and historical mapping outputs. No publication or ongoing/completed project designation is supplied. | pp. 12-13 |
| High Forest Zone LULC research | Documented contribution and classification outputs. No publication or ongoing/completed project designation is supplied. | pp. 14-15 |
| Proposed research | No explicitly proposed project, proposal, or future research plan is stated. General research interests are not classified as proposals. | Full PDF, pp. 1-17 |

## Projects

### 1. UAV Multispectral Remote Sensing and Machine Learning for Cocoa Nutrient Assessment

**Source: PDF pp. 3-9; related thesis and manuscript entries on p. 16.**

- **Context/location:** MSc research in the Juaboso cocoa landscape, Western North, Ghana; component of the FRAME-Cocoa Project, sponsored by the African Plant Nutrition Institute (APNI) (p. 4).
- **Problem:** declining soil fertility and limitations of blanket fertilizer recommendations for cocoa production (p. 4).
- **Objectives:** quantify relationships between soil and leaf nitrogen (N), phosphorus (P), and potassium (K); develop predictions of cocoa leaf nutrients from multispectral bands and vegetation indices (p. 4).
- **Research question:** whether UAV multispectral imagery and machine learning can estimate foliar N, P, and K and generate continuous spatial predictions across a cocoa landscape (p. 4).
- **Data/platform:** DJI Matrice 350 RTK at 150 m altitude and 3 m/s, with 65% image overlap; MicaSense RedEdge-P bands at blue 475 nm, green 560 nm, red 668 nm, red edge 717 nm, and NIR 842 nm; 59 composite soil samples/field sampling locations; ground-truth soil and foliar N, P, and K measurements (p. 4).
- **Processing:** MicaSense calibration-panel radiometric correction; Agisoft Metashape orthomosaic with 0.09 m ground sampling distance (GSD); spectral bands and vegetation indices extracted at sampling locations; vegetation-index predictors with inter-correlation greater than 0.95 excluded (p. 7).
- **Models listed in the methods text:** Random Forest (RF), Support Vector Regression (labelled SVM), Artificial Neural Network (ANN), Partial Least Squares Regression (PLSR), XGBoost, and Gradient Boosting Machine (GBM) (p. 7).
- **Workflow diagram:** soil sampling at 0-15 cm and 15-30 cm plus foliage; bivariate Pearson correlation; linear/PLS modelling and machine learning; 70/30 train-test split, LOOCV, and comparison using R-squared, RMSE, MAE, and AIC. The diagram also lists KNN and a 2 cm GSD, which are not reconciled with the methods text; see conflicts below (p. 6).
- **Individual contribution:** UAV and field-data components, multispectral predictor preparation, feature screening, soil-leaf statistical analysis, comparative machine-learning modelling, and interpretation of spectral predictors and model behaviour (pp. 3, 9).
- **Outputs:** study-area/UAV orthomosaic map (Figure 1, p. 5); workflow diagram (p. 6); observed/predicted foliar nutrient plots (Figure 2, p. 8); model-comparison chart (Figure 3, p. 9); nutrient modelling products (p. 16).
- **Limitations reported:** limited nutrient variability constrained spectral models; predictive behaviour differed by nutrient (p. 8). These results do not establish strong spectral predictive accuracy.
- **Status:** submitted MSc thesis dated 2025; related manuscript in preparation (pp. 7, 16). Fieldwork/project start and end dates are absent.

**Numerical results reported in the submitted-thesis summary (PDF pp. 7-8):**

| Target | Soil-to-leaf Random Forest R-squared | Spectral-variable results |
| --- | --- | --- |
| Leaf N | 0.17 | Very low/close to zero R-squared; no exact spectral value supplied in the prose |
| Leaf P | 0.55 | XGBoost best; R-squared approximately 0.09 |
| Leaf K | 0.52 | ANN best; R-squared approximately 0.10, with relatively high errors |

### 2. Geospatial Characterisation of Shade Canopy in Cocoa Agroforestry and Soil Resources

**Source: PDF pp. 3, 10-11; related research outputs on p. 16.**

- **Context/location:** co-authored research in Juaboso District, Ghana; remote-sensing component under FRAME-Cocoa (p. 10).
- **Aim/context:** characterise shade canopy in cocoa farms, recognising benefits within an optimal shade range and possible adverse productivity effects outside that range; broader work integrates remote sensing, field observations, and mathematical optimisation (p. 10).
- **Field research described:** soil sampling at multiple depths, identification and measurement of shade-tree canopy sizes, conducting/supporting soil laboratory analysis, and characterisation of shade cover and agroforestry structure (p. 10).
- **Individual contribution:** field collection plus remote sensing/GIS, Sentinel-derived predictor development, Random Forest analysis, shade-level classification, and spatial characterisation of cocoa shade conditions (pp. 10-11).
- **Predictors:** dry-season Sentinel-2 imagery; spectral bands and vegetation indices; GLCM texture metrics; biophysical variables including LAI, fAPAR, fCover, chlorophyll content, and canopy water content (p. 10).
- **Methods:** Random Forest predicts continuous canopy cover, then assigns no shade, low shade, moderate (optimal) shade, or high shade; backwards feature elimination; 10-fold cross-validation (pp. 10-11).
- **Output:** Juaboso landscape land-cover map with cocoa shade-canopy variations (Figure 4, p. 11).
- **Broader-team work:** integration of field tree and shade-tree species information, mathematical optimisation, site-specific tree-combination recommendations, and the overall agroforestry management framework. These are not all attributed to the researcher individually (p. 11).
- **Status:** related peer-reviewed publication and under-review manuscript listed on p. 16. Project dates, completion designation, canopy thresholds, and numerical validation scores are not supplied.

### 3. Satellite Time-Series Classification for Deforestation-Free Cocoa Monitoring

**Source: PDF pp. 3, 12-13.**

- **Context/location:** Deforestation-Free Cocoa Project, Ghana; hotspot intervention landscapes named as Sefwi-Wiawso Bibiani, Asunafo-Asutifi, and Juaboso-Bia (p. 12).
- **Aim:** support historical LULC mapping using temporal Earth observation information rather than only single-date imagery (p. 12).
- **Individual role:** led a field-data collection team; supervised training-coordinate collection for historical years 2015, 2020, and 2024; developed Python deep-learning and machine-learning satellite classifiers; supported historical LULC outputs; constructed physical 3D landscape models for stakeholder communication (p. 12).
- **CNN workflow shown:** Landsat imagery, cloud masking, temporal stacking/extraction, CNN deep learning, class assignment, and land-cover map output (p. 12).
- **Training/reference data:** systematic spatially distributed collection and preparation for historical classification (p. 13). The historical mapping years are not stated employment or project dates.
- **Outputs:** historical LULC maps, a landscape-change time-series map for 2015-2024 (Figure 5, p. 13), and physical 3D landscape models (pp. 12-13).
- **Status:** work and outputs are documented; ongoing/completed designation, publication status, model architecture, sample count, and accuracy scores are not stated.

### 4. Land-Use/Land-Cover Classification in Ghana's High Forest Zone

**Source: PDF pp. 3, 14-15.**

- **Context:** component of supervisor-led forest/land-cover research in Ghana's High Forest Zone (p. 14).
- **Research aim:** investigate which algorithm best distinguishes land-use classes in a highly heterogeneous landscape (p. 14).
- **Individual contribution:** assigned remote-sensing/GIS component; satellite imagery preparation and analysis; training/reference data for supervised classification; production and interpretation of LULC outputs; geospatial support for broader landscape research (pp. 3, 14).
- **Technical context:** medium-resolution Landsat and Sentinel datasets; comparison of traditional machine-learning classifiers and CNN deep learning; workflow includes preprocessing, reference data, classification, accuracy assessment, and spatial interpretation (p. 14).
- **Specific illustrated output:** comparison of RF, SVM, and CNN LULC maps for Juaboso-Bia HIA using Landsat 9 L2 imagery (Figure 6, p. 15).
- **Status:** documented contribution; project dates, ongoing/completed designation, publication status, supervisor identity, numerical accuracy results, and best-performing classifier are not supplied.

## Publications and research outputs

### Published peer-reviewed research

**Source: PDF p. 16; DOI link on p. 17.**

- Ashiagbor, G., Essah, I.S., Baiden, P.P.K., Adjetey Bisa, A.A., et al. (2026). **Modelling the number of shade tree species needed to reach the optimal canopy target in cocoa agroforestry systems.** *Agroforest Syst* 100, 36 (2026).
- DOI as supplied: https://doi.org/10.1007/s10457-025-01402-6
- Researcher listed as a co-author. The PDF supplies an abbreviated author list; omitted authors are not reconstructed.

### Ongoing publication work: manuscript under review

**Source: PDF p. 16.**

- Ashiagbor, G., Ahorlu, O., Enyinful-Andoh, G., Adjetey Bisa, A. A., Essah, I. S., Tawiah, W. B., Yeboah, E., Mutegi, J., Mugi-Ngenga, E., Amouzou, K. A., & Oberthür, T. (2026).
- **Shade Tree Structural Management Does Not Predict Soil Chemical Quality or Cocoa Yield in Smallholder Agroforestry: Plot-Level Evidence from Ghana.**
- Manuscript number: **AGEE58523**.
- Status in PDF: **under review at Agriculture, Ecosystems and Environment**. Not listed as accepted or published.

### Ongoing publication work: manuscript in preparation

**Source: PDF p. 16.**

- **Predicting Macronutrient Status in Mature Cocoa Using UAV Multispectral Imagery and Machine Learning**.
- Status in PDF: **in preparation**. Authors, target journal, date, and submission details are not supplied.

### MSc thesis

**Source: PDF p. 16; submitted-thesis results on pp. 7-8.**

- **Predicting Macronutrient Levels in Cocoa Soils Using Multispectral Unmanned Aerial Vehicles (UAV)**.
- Master of Science (MSc.), Geo-Information Science for Natural Resources Management, KNUST, **2025**.
- Described elsewhere as the submitted thesis. Degree-conferral date, thesis URL, supervisor, and repository identifier are not stated.

### Other research products

**Source: PDF p. 16; illustrations on pp. 5, 8-9, 11, 13, 15.**

- UAV multispectral orthomosaics and vegetation-index products.
- Cocoa foliar nutrient modelling outputs.
- Satellite time-series classification outputs.
- Sentinel-based cocoa shade classification maps.
- LULC and landscape classification products.
- Physical 3D landscape models are additionally documented on pp. 12-13.

## Education

**Source: PDF pp. 1, 16.**

- **Programme/qualification listed:** MSc Geo-Information Science for Natural Resources Management.
- **Institution:** Kwame Nkrumah University of Science and Technology (KNUST), Ghana.
- **Year associated with thesis:** 2025 (p. 16). This is not explicitly identified as the graduation or degree-conferral year.
- **Thesis title:** recorded in the thesis section above.
- No undergraduate qualification, attendance dates, academic grades, or explicit degree-conferral confirmation is provided.

## Experience and technical capabilities

**Research experience source: PDF pp. 2-3, 9-14.**

- MSc UAV/field research, nutrient modelling, and scientific interpretation.
- FRAME-Cocoa remote-sensing/GIS and shade-canopy research.
- Deforestation-Free Cocoa field-team leadership, training-data supervision, Python satellite classification, and stakeholder 3D models.
- Supervisor-assigned High Forest Zone remote-sensing and LULC classification research.
- These are research contributions, not verified employment appointments. Formal job titles, employers, contracts, and service dates are absent.

**Technical capabilities source: PDF pp. 3, 17.**

| Area | Capabilities/tools stated |
| --- | --- |
| Earth observation | Satellite and UAV multispectral remote sensing, preprocessing, vegetation indices, time-series analysis |
| GIS/spatial analysis | ArcGIS Pro, QGIS, raster and spatial analysis, kriging/interpolation, cartography |
| AI/machine learning | CNN, ANN, Random Forest, XGBoost, Support Vector Machines, Gradient Boosting, PLSR |
| Programming/analysis | Python, R/RStudio, Google Colab |
| Remote-sensing software | SNAP, Agisoft Metashape |
| UAV/field research | DJI Matrice 350 RTK, MicaSense RedEdge-P, field sampling, georeferenced observations, environmental/crop data collection |
| Research communication | Scientific writing, research communication, and publication (p. 3); physical 3D landscape models (pp. 12-13) |

## Awards

**Source reviewed: full PDF, pp. 1-17.**

- No personal awards, honours, scholarships, or prizes are listed.
- APNI sponsorship of FRAME-Cocoa is project funding (p. 4), not a stated personal award.

## Contact details and resource links

**Source: PDF p. 1 (contact); p. 17 (resource links).**

| Type | Value supplied | Page |
| --- | --- | --- |
| Email | abigailadjeleyadjeteybisa@gmail.com | 1 |
| LinkedIn | linkedin.com/in/abigail-adjeley-adjetey-bisa-b885a5216 | 1 |
| Repository (Google Drive) | https://drive.google.com/drive/folders/1oQW2PkMrRqszJHe6Tyt9hNYEWxkXkR0M?usp=drive_link | 17 |
| Published paper | https://doi.org/10.1007/s10457-025-01402-6 | 17 |
| Scientific writings/reports (Google Drive) | https://drive.google.com/drive/folders/1iTtz8tL972xv826KnH7IIDWEJrI1BXwJ?usp=drive_link | 17 |

No telephone number, postal address, ORCID, institutional email, or personal website is stated. Links are transcribed from the source; their availability and contents were not checked.

## Missing information

**Source reviewed: PDF pp. 1-17; relevant sections noted below.**

- Current job title, employer, current affiliation, professional location, and dated biography: absent from profile/experience material (pp. 1-3, 12-14).
- Degree attendance/conferral dates, undergraduate education, grades, and thesis supervision/repository details: absent from education entries (pp. 1, 16).
- Formal employment appointments and dates: absent from research experience (pp. 3-15).
- Project start/end dates and explicit ongoing/completed designations: absent from project descriptions (pp. 4-15). Historical imagery years do not supply these dates.
- Proposed research objectives or future project plans: none explicitly stated (pp. 1-17).
- Awards/honours: none listed (pp. 1-17).
- Full published-paper author list; authors and target journal for the in-preparation manuscript; status-as-of date and current manuscript decisions: absent from publication entries (p. 16).
- Numerical validation for shade classification, historical LULC mapping, and High Forest Zone classifier comparison; canopy-class thresholds; detailed CNN architecture/hyperparameters: absent from relevant project descriptions (pp. 10-15).
- Sampling dates and exact foliar sample count: not supplied with the stated 59 composite soil samples/locations (p. 4).
- Telephone/address, ORCID, institutional email, and personal website: not listed in contact/link sections (pp. 1, 17).

## Conflicts and ambiguities requiring clarification

1. **GSD discrepancy (pp. 6-7):** the Project 1 workflow diagram states 2 cm GSD, while the methods prose reports a 0.09 m (9 cm) orthomosaic. These may describe different products/resolutions, but the PDF does not explain the difference; neither is silently substituted for the other.
2. **Algorithm-list discrepancy (pp. 6-7):** the diagram includes KNN and labels an SVM-based machine-learning step, while the methods list includes ANN and XGBoost and does not list KNN. The intended final model set needs clarification. The diagram also specifies validation steps that are not repeated in the methods prose.
3. **Results/figure mismatch (pp. 7-9):** the final-thesis prose reports soil-based RF R-squared values of 0.17, 0.55, and 0.52 and weak spectral fits. Figure 2 on p. 8 visibly labels RF fits differently (including approximately 0.31 for Leaf N and 0.49 for Leaf K). The PDF does not clearly identify the predictor set or model version for that figure. The inventory preserves the explicitly identified final-thesis prose values; plotted values are not treated as interchangeable with them.
4. **Thesis-title versus described targets (pp. 4, 7-8, 16):** the formal thesis title refers to macronutrient levels in cocoa soils, whereas the detailed project objectives and models address foliar nutrients and soil-to-leaf relationships. Both descriptions are preserved; the thesis title has not been rewritten.
5. **Name expansion (pp. 1, 16):** the display name is Abigail A. Adjetey Bisa; publication entries use Adjetey Bisa, A.A. Contact identifiers contain "Adjeley". The middle initial is not expanded from account identifiers.
6. **Manuscript title versus Project 2 detail (pp. 10-11, 16):** the under-review soil-quality/cocoa-yield manuscript appears related to the agroforestry work, but the PDF does not explicitly map every project task to that manuscript or provide manuscript-specific contribution statements.
7. **Publication year and DOI (pp. 16-17):** the citation states 2026 while the DOI contains "025". A DOI suffix alone does not establish a conflicting publication year; retain 2026 as reported unless the publication is separately checked.
8. **Historical reference collection (p. 12):** the portfolio states supervision of training-coordinate collection for historical years 2015, 2020, and 2024, but does not explain retrospective reference-data generation. Do not infer that fieldwork itself occurred in all three years.
