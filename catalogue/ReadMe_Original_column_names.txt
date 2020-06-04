VIII/105   CDS/The GLEAM 4-Jy (G4Jy) Sample         (White et al., 2020a, 2020b)
================================================================================

The GLEAM 4-Jy (G4Jy) Sample: 
I. Definition and the catalogue (arxiv.org/abs/2004.13125)                       
II. Host-galaxy identification for individual sources (arxiv.org/abs/2004.13025)

    Sarah V. White, Thomas M.O. Franzen, Chris J. Riseley, O. Ivy Wong,    Anna D. Kapińska, Natasha Hurley–Walker, Joseph R. Callingham, 
    Kshitij Thorat, Chen Wu, Paul Hancock, Richard W. Hunstead, Nick Seymour, 
    Jesse Swan, Randall Wayth, John Morgan, Rajan Chhetri, Carole Jackson, 
    Stuart Weston, Martin Bell, Bi-Qing For, B.M. Gaensler, 
    Melanie Johnston–Hollitt, André Offringa, and Lister Staveley–Smith

As Papers I and II were completed in conjunction with another, please cite both
when making use of the G4Jy Sample and/or the associated catalogue. The abstract
below refers to Paper I (White et al., 2020a).

================================================================================

Keywords: 
catalogues – galaxies: active – galaxies: evolution – radio continuum: galaxies

Abstract:
    The Murchison Widefield Array (MWA) has observed the entire southern sky 
(Declination, δ < 30◦) at low radio-frequencies, over the range 72–231 MHz. 
These observations constitute the GaLactic and Extragalactic All-sky MWA (GLEAM) 
Survey, and we use the extragalactic catalogue (Galactic latitude, |b| > 10◦) to 
define the GLEAM 4-Jy (G4Jy) Sample. This is a complete sample of the 
‘brightest’ radio-sources (S_151MHz > 4 Jy), the majority of which are active 
galactic nuclei with powerful radio-jets. Crucially, low-frequency observations 
allow the selection of such sources in an orientation-independent way (i.e. 
minimising the bias caused by Doppler boosting, inherent in high-frequency 
surveys). We then use higher-resolution radio images, and information at other 
wavelengths, to morphologically classify the brightest components in GLEAM. We 
also conduct cross-checks against the literature, and perform internal matching,
in order to improve sample completeness (which is estimated to be > 95.5%). This 
results in a catalogue of 1,863 sources, making the G4Jy Sample over 10 times 
larger than that of the revised Third Cambridge Catalogue of Radio Sources 
(3CRR; S_178MHz > 10.9 Jy). Of these G4Jy sources, 78 are resolved by the MWA 
(Phase-I) synthesised beam (∼2’ at 200 MHz), and we label 67% of the sample as 
‘single’, 26% as ‘double’, 4% as ‘triple’, and 3% as having ‘complex’ morphology 
at ∼1 GHz (45” resolution). We characterise the spectral behaviour of these 
objects in the radio, and find that the median spectral-index is α = −0.740 ± 
0.012 between 151 MHz and 843 MHz, and α = −0.786 ± 0.006 between 151 MHz and 
1400 MHz (assuming a power-law description, S_ν ∝ ν^α), compared to α = −0.829 ± 
0.006 within the GLEAM band. Alongside this, our value-added catalogue provides 
mid-infrared source associations (subject to 6” resolution at 3.4 μm) for the 
radio emission, as identified through visual inspection and thorough checks 
against the literature. As such, the G4Jy Sample can be used as a reliable 
training set for cross-identification via machine-learning algorithms. We also 
estimate the angular size of the sources, based on their associated components
at ∼1 GHz, and perform a flux-density comparison for 67 G4Jy sources that 
overlap with 3CRR. Analysis of multi-wavelength data, and spectral curvature 
between 72 MHz and 20 GHz, will be presented in subsequent papers, and details 
for accessing all G4Jy overlays are provided at https://github.com/svw26/G4Jy.

Data description:
    The construction of the G4Jy Sample draws on radio data from the GLEAM 
extragalactic catalogue (Hurley-Walker et al., 2016; arxiv.org/abs/1610.08318), 
SUMSS (Mauch et al., 2003; Murphy et al., 2007), NVSS (Condon et al., 1998),
TGSS ADR1 (Intema et al., 2017), and AT20G (Murphy et al., 2010). These datasets
were used alongside mid-infrared information from AllWISE (Cutri et al., 2013) 
and optical positions from 6dFGS (Jones et al., 2004) for identifying the
host galaxies of the 1,863 G4Jy radio-sources in the sample. Note that a .fits 
version of the G4Jy catalogue, with complete metadata, will be kept up-to-date 
at https://github.com/svw26/G4Jy. The catalogue is also available at CDS via 
anonymous ftp to cdsarc.u-strasbg.fr (130.79.128.5) or 
via http://cdsarc.u-strasbg.fr/viz-bin/qcat?VIII/105.


File Summary:
--------------------------------------------------------------------------------
 FileName                    Lrecl  Records  Explanations
--------------------------------------------------------------------------------
ReadMe.longstrings.txt          80        .  This file
G4Jy_catalogue_18012020.dat   4686     1960  table title



Byte-by-byte Description of file: G4Jy_catalogue_18012020.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  9   A9      --- G4Jy_name                [ 0123456789GJy] Name of source belonging to the G4Jy Sample
  11- 11   A1      --- G4Jy_component           [-ABCDE] Label for an individual GLEAM component
  13- 13   I1      --- ncmp_GLEAM               [1-5] Number of GLEAM components for this G4Jy source
  15- 34   A20     --- GLEAM_name               [ +-0123456789AEGJLM] Name of the GLEAM component
  36- 36   I1      --- refitted_flag            [0-3] Flag for sources with re-fitted GLEAM measurements
  38- 47   F10.6   --- centroid_RAJ2000         Right ascension for the centroid position (J2000), in deg
  49- 52   F4.2    --- err_centroid_RAJ2000     Error on RA for the centroid position, in arcsec
  54- 63   F10.6   --- centroid_DEJ2000         Declination for the centroid position (J2000), in deg
  65- 68   F4.2    --- err_centroid_DEJ2000     Error on Dec for the centroid position, in arcsec
  70- 70   I1      --- centroid_flag            [0-2] Flag for sources with an updated centroid-position
  72- 78   A7      --- morphology               [bcdegilmnoprstux] Morphology of the source in NVSS/SUMSS/TGSS
  80- 81   I2      --- ncmp_NVSSorSUMSS         [1/2/3/4/5/6/7/8/9/10/11/17/23] Number of NVSS/SUMSS components
  83- 83   I1      --- confusion_flag           [01] Flag for sources affected by confusion in GLEAM
  85- 85   A1      --- angular_size_limit       ? [<] Indicates that the angular size is an upper limit
  87- 94   F8.3    --- angular_size             Angular size in NVSS/SUMSS, in arcsec
  96-102   F7.4    --- S_NVSSorSUMSS            Total flux-density in NVSS/SUMSS, in Jy
 104-109   F6.4    --- err_S_NVSSorSUMSS        Error on the total flux-density in NVSS/SUMSS, Jy
 111-116   F6.1    --- Freq                     Indicates whether NVSS or SUMSS was used, in MHz
 118-129   F12.9   --- G4Jy_NVSS_alpha          ? Spectral index between 151 and 1400 MHz
 131-142   F12.10  --- err_G4Jy_NVSS_alpha      ? Error on spectral index between 151 and 1400 MHz
 144-154   F11.8   --- G4Jy_SUMSS_alpha         ? Spectral index between 151 and 843 MHz
 156-167   F12.10  --- err_G4Jy_SUMSS_alpha     ? Error on spectral index between 151 and 843 MHz
 169-180   F12.9   --- G4Jy_alpha               ? Fitted spectral-index using total GLEAM flux-densities
 182-192   F11.9   --- err_G4Jy_alpha           ? Error on fitted, G4Jy spectral-index
 194-204   F11.9   --- reduced_chi2_G4Jy_alpha  ? Reduced chi^2 statistic for G4Jy spectral-index fit
 206-206   A1      --- host_flag                [imnu] Flag for the type of host-galaxy identification
 208-226   A19     --- AllWISE_name             ? [+-.0123456789J] Name of the host galaxy in AllWISE
 228-238   F11.7   --- AllWISE_RAJ2000          ? Right ascension for the host galaxy (J2000), in deg
 240-250   F11.7   --- AllWISE_DEJ2000          ? Declination for the host galaxy (J2000), in deg
 252-257   F6.3    --- W1mag                    ? W1 magnitude for the host galaxy, in mag
 259-263   F5.3    --- err_W1mag                ? Error on W1 magnitude for the host galaxy, in mag
 265-270   F6.3    --- W2mag                    ? W2 magnitude for the host galaxy, in mag
 272-276   F5.3    --- err_W2mag                ? Error on W2 magnitude for the host galaxy, in mag
 278-283   F6.3    --- W3mag                    ? W3 magnitude for the host galaxy, in mag
 285-289   F5.3    --- err_W3mag                ? Error on W3 magnitude for the host galaxy, in mag
 291-296   F6.3    --- W4mag                    ? W4 magnitude for the host galaxy, in mag
 298-302   F5.3    --- err_W4mag                ? Error on W4 magnitude for the host galaxy, in mag
 304-314   A11     --- GLEAM_ra_str             [.0123456789:] Right ascension for the GLEAM component (J2000), h:m:s
 316-327   A12     --- GLEAM_dec_str            [+-.0123456789:] Declination for the GLEAM component (J2000), d:m:s
 329-340   F12.8   --- GLEAM_RAJ2000            Right ascension for the GLEAM component (J2000), in deg
 342-362   E21.19  --- err_GLEAM_RAJ2000        Error on RA for the GLEAM component, in deg
 364-377   F14.10  --- GLEAM_DEJ2000            Declination for the GLEAM component (J2000), in deg
 379-399   E21.19  --- err_GLEAM_DEJ2000        Error on Dec for the GLEAM component, in deg
 401-413   E13.10  --- background_wide          Background level in wide-band image, in Jy/beam
 415-426   F12.10  --- local_rms_wide           Local noise level in wide-band image, in Jy/beam
 428-439   F12.8   --- peak_flux_wide           Peak flux-density in wide-band image, in Jy/beam
 441-452   F12.10  --- err_peak_flux_wide       Uncertainty in fit for peak flux-density in wide-band image, in Jy/beam
 454-465   F12.8   --- int_flux_wide            Integrated flux-density in wide-band image, in Jy
 467-478   F12.10  --- err_int_flux_wide        Uncertainty in fit for integrated flux-density in wide-band image, in Jy
 480-488   F9.5    --- a_wide                   Fitted semi-major axis in wide-band image, in arcsec
 490-501   F12.9   --- err_a_wide               Uncertainty in fitted semi-major axis in wide-band image, in arcsec
 503-511   F9.5    --- b_wide                   Fitted semi-minor axis in wide-band image, in arcsec
 513-524   F12.9   --- err_b_wide               Uncertainty in fitted semi-minor axis in wide-band image, in arcsec
 526-539   F14.10  --- pa_wide                  Fitted position angle in wide-band image, in deg
 541-553   E13.10  --- err_pa_wide              Uncertainty in fitted position angle in wide-band image, in deg
 555-567   E13.10  --- residual_mean_wide       Mean value of data-model in wide-band image, in Jy/beam
 569-580   F12.10  --- residual_std_wide        Standard deviation of data-model in wide-band image, in Jy/beam
 582-590   F9.5    --- psf_a_wide               Semi-major axis of the point spread function in wide-band image, in arcsec
 592-600   F9.5    --- psf_b_wide               Semi-minor axis of the point spread function in wide-band image, in arcsec
 602-614   F13.9   --- psf_pa_wide              Position angle of the point spread function in wide-band image, in deg
 616-628   E13.10  --- background_076           ? Background level in 72-80 MHz image, in Jy/beam
 630-640   F11.9   --- local_rms_076            ? Local noise level in 72-80 MHz image, in Jy/beam
 642-653   F12.8   --- peak_flux_076            ? Peak flux-density in 72-80 MHz image, in Jy/beam
 655-665   F11.9   --- err_peak_flux_076        ? Uncertainty in fit for peak flux-density in 72-80 MHz image, in Jy/beam
 667-678   F12.8   --- int_flux_076             ? Integrated flux-density in 72-80 MHz image, in Jy
 680-690   F11.9   --- err_int_flux_076         ? Uncertainty in fit for integrated flux-density in 72-80 MHz image, in Jy
 692-700   F9.5    --- a_076                    ? Fitted semi-major axis in 72-80 MHz image, in arcsec
 702-710   F9.5    --- b_076                    ? Fitted semi-minor axis in 72-80 MHz image, in arcsec
 712-725   F14.10  --- pa_076                   ? Fitted position angle in 72-80 MHz image, in deg
 727-740   E14.10  --- residual_mean_076        ? Mean value of data-model in 72-80 MHz image, in Jy/beam
 742-752   F11.9   --- residual_std_076         ? Standard deviation of data-model in 72-80 MHz image, in Jy/beam
 754-762   F9.5    --- psf_a_076                ? Semi-major axis of the point spread function in 72-80 MHz image, in arcsec
 764-772   F9.5    --- psf_b_076                ? Semi-minor axis of the point spread function in 72-80 MHz image, in arcsec
 774-787   F14.10  --- psf_pa_076               ? Position angle of the point spread function in 72-80 MHz image, in deg
 789-801   E13.10  --- background_084           ? Background level in 80-88 MHz image, in Jy/beam
 803-813   F11.9   --- local_rms_084            ? Local noise level in 80-88 MHz image, in Jy/beam
 815-826   F12.8   --- peak_flux_084            ? Peak flux-density in 80-88 MHz image, in Jy/beam
 828-838   F11.9   --- err_peak_flux_084        ? Uncertainty in fit for peak flux-density in 80-88 MHz image, in Jy/beam
 840-851   F12.8   --- int_flux_084             ? Integrated flux-density in 80-88 MHz image, in Jy
 853-863   F11.9   --- err_int_flux_084         ? Uncertainty in fit for integrated flux-density in 80-88 MHz image, in Jy
 865-873   F9.5    --- a_084                    ? Fitted semi-major axis in 80-88 MHz image, in arcsec
 875-883   F9.5    --- b_084                    ? Fitted semi-minor axis in 80-88 MHz image, in arcsec
 885-898   F14.10  --- pa_084                   ? Fitted position angle in 80-88 MHz image, in deg
 900-912   E13.10  --- residual_mean_084        ? Mean value of data-model in 80-88 MHz image, in Jy/beam
 914-924   F11.9   --- residual_std_084         ? Standard deviation of data-model in 80-88 MHz image, in Jy/beam
 926-934   F9.5    --- psf_a_084                ? Semi-major axis of the point spread function in 80-88 MHz image, in arcsec
 936-944   F9.5    --- psf_b_084                ? Semi-minor axis of the point spread function in 80-88 MHz image, in arcsec
 946-958   F13.9   --- psf_pa_084               ? Position angle of the point spread function in 80-88 MHz image, in deg
 960-973   E14.10  --- background_092           ? Background level in 88-95 MHz image, in Jy/beam
 975-985   F11.9   --- local_rms_092            ? Local noise level in 88-95 MHz image, in Jy/beam
 987-998   F12.8   --- peak_flux_092            ? Peak flux-density in 88-95 MHz image, in Jy/beam
 1000-1011   F12.9   --- err_peak_flux_092        ? Uncertainty in fit for peak flux-density in 88-95 MHz image, in Jy/beam
 1013-1023   F11.7   --- int_flux_092             ? Integrated flux-density in 88-95 MHz image, in Jy
 1025-1036   F12.9   --- err_int_flux_092         ? Uncertainty in fit for integrated flux-density in 88-95 MHz image, in Jy
 1038-1046   F9.5    --- a_092                    ? Fitted semi-major axis in 88-95 MHz image, in arcsec
 1048-1056   F9.5    --- b_092                    ? Fitted semi-minor axis in 88-95 MHz image, in arcsec
 1058-1071   F14.10  --- pa_092                   ? Fitted position angle in 88-95 MHz image, in deg
 1073-1085   E13.10  --- residual_mean_092        ? Mean value of data-model in 88-95 MHz image, in Jy/beam
 1087-1097   F11.9   --- residual_std_092         ? Standard deviation of data-model in 88-95 MHz image, in Jy/beam
 1099-1107   F9.5    --- psf_a_092                ? Semi-major axis of the point spread function in 88-95 MHz image, in arcsec
 1109-1117   F9.5    --- psf_b_092                ? Semi-minor axis of the point spread function in 88-95 MHz image, in arcsec
 1119-1132   F14.10  --- psf_pa_092               ? Position angle of the point spread function in 88-95 MHz image, in deg
 1134-1146   E13.10  --- background_099           ? Background level in 95-103 MHz image, in Jy/beam
 1148-1158   F11.9   --- local_rms_099            ? Local noise level in 95-103 MHz image, in Jy/beam
 1160-1171   F12.8   --- peak_flux_099            ? Peak flux-density in 95-103 MHz image, in Jy/beam
 1173-1184   F12.9   --- err_peak_flux_099        ? Uncertainty in fit for peak flux-density in 95-103 MHz image, in Jy/beam
 1186-1197   F12.8   --- int_flux_099             ? Integrated flux-density in 95-103 MHz image, in Jy
 1199-1210   F12.9   --- err_int_flux_099         ? Uncertainty in fit for integrated flux-density in 95-103 MHz image, in Jy
 1212-1220   F9.5    --- a_099                    ? Fitted semi-major axis in 95-103 MHz image, in arcsec
 1222-1230   F9.5    --- b_099                    ? Fitted semi-minor axis in 95-103 MHz image, in arcsec
 1232-1245   F14.10  --- pa_099                   ? Fitted position angle in 95-103 MHz image, in deg
 1247-1259   E13.10  --- residual_mean_099        ? Mean value of data-model in 95-103 MHz image, in Jy/beam
 1261-1271   F11.9   --- residual_std_099         ? Standard deviation of data-model in 95-103 MHz image, in Jy/beam
 1273-1281   F9.5    --- psf_a_099                ? Semi-major axis of the point spread function in 95-103 MHz image, in arcsec
 1283-1291   F9.5    --- psf_b_099                ? Semi-minor axis of the point spread function in 95-103 MHz image, in arcsec
 1293-1306   F14.10  --- psf_pa_099               ? Position angle of the point spread function in 95-103 MHz image, in deg
 1308-1321   E14.10  --- background_107           Background level in 103-111 MHz image, in Jy/beam
 1323-1333   F11.9   --- local_rms_107            Local noise level in 103-111 MHz image, in Jy/beam
 1335-1346   F12.8   --- peak_flux_107            Peak flux-density in 103-111 MHz image, in Jy/beam
 1348-1359   F12.9   --- err_peak_flux_107        Uncertainty in fit for peak flux-density in 103-111 MHz image, in Jy/beam
 1361-1372   F12.8   --- int_flux_107             Integrated flux-density in 103-111 MHz image, in Jy
 1374-1385   F12.9   --- err_int_flux_107         Uncertainty in fit for integrated flux-density in 103-111 MHz image, in Jy
 1387-1395   F9.5    --- a_107                    Fitted semi-major axis in 103-111 MHz image, in arcsec
 1397-1405   F9.5    --- b_107                    Fitted semi-minor axis in 103-111 MHz image, in arcsec
 1407-1420   F14.10  --- pa_107                   Fitted position angle in 103-111 MHz image, in deg
 1422-1434   E13.10  --- residual_mean_107        Mean value of data-model in 103-111 MHz image, in Jy/beam
 1436-1446   F11.9   --- residual_std_107         Standard deviation of data-model in 103-111 MHz image, in Jy/beam
 1448-1456   F9.5    --- psf_a_107                Semi-major axis of the point spread function in 103-111 MHz image, in arcsec
 1458-1466   F9.5    --- psf_b_107                Semi-minor axis of the point spread function in 103-111 MHz image, in arcsec
 1468-1481   F14.10  --- psf_pa_107               Position angle of the point spread function in 103-111 MHz image, in deg
 1483-1495   E13.10  --- background_115           ? Background level in 111-118 MHz image, in Jy/beam
 1497-1507   F11.9   --- local_rms_115            ? Local noise level in 111-118 MHz image, in Jy/beam
 1509-1520   F12.8   --- peak_flux_115            ? Peak flux-density in 111-118 MHz image, in Jy/beam
 1522-1533   F12.9   --- err_peak_flux_115        ? Uncertainty in fit for peak flux-density in 111-118 MHz image, in Jy/beam
 1535-1546   F12.8   --- int_flux_115             ? Integrated flux-density in 111-118 MHz image, in Jy
 1548-1559   F12.9   --- err_int_flux_115         ? Uncertainty in fit for integrated flux-density in 111-118 MHz image, in Jy
 1561-1569   F9.5    --- a_115                    ? Fitted semi-major axis in 111-118 MHz image, in arcsec
 1571-1579   F9.5    --- b_115                    ? Fitted semi-minor axis in 111-118 MHz image, in arcsec
 1581-1594   F14.10  --- pa_115                   ? Fitted position angle in 111-118 MHz image, in deg
 1596-1608   E13.10  --- residual_mean_115        ? Mean value of data-model in 111-118 MHz image, in Jy/beam
 1610-1620   F11.9   --- residual_std_115         ? Standard deviation of data-model in 111-118 MHz image, in Jy/beam
 1622-1630   F9.5    --- psf_a_115                ? Semi-major axis of the point spread function in 111-118 MHz image, in arcsec
 1632-1640   F9.5    --- psf_b_115                ? Semi-minor axis of the point spread function in 111-118 MHz image, in arcsec
 1642-1654   E13.9   --- psf_pa_115               ? Position angle of the point spread function in 111-118 MHz image, in deg
 1656-1669   E14.10  --- background_122           ? Background level in 118-126 MHz image, in Jy/beam
 1671-1681   F11.9   --- local_rms_122            ? Local noise level in 118-126 MHz image, in Jy/beam
 1683-1694   F12.8   --- peak_flux_122            ? Peak flux-density in 118-126 MHz image, in Jy/beam
 1696-1707   F12.9   --- err_peak_flux_122        ? Uncertainty in fit for peak flux-density in 118-126 MHz image, in Jy/beam
 1709-1720   F12.8   --- int_flux_122             ? Integrated flux-density in 118-126 MHz image, in Jy
 1722-1733   F12.9   --- err_int_flux_122         ? Uncertainty in fit for integrated flux-density in 118-126 MHz image, in Jy
 1735-1743   F9.5    --- a_122                    ? Fitted semi-major axis in 118-126 MHz image, in arcsec
 1745-1753   F9.5    --- b_122                    ? Fitted semi-minor axis in 118-126 MHz image, in arcsec
 1755-1768   F14.10  --- pa_122                   ? Fitted position angle in 118-126 MHz image, in deg
 1770-1782   E13.10  --- residual_mean_122        ? Mean value of data-model in 118-126 MHz image, in Jy/beam
 1784-1794   F11.9   --- residual_std_122         ? Standard deviation of data-model in 118-126 MHz image, in Jy/beam
 1796-1804   F9.5    --- psf_a_122                ? Semi-major axis of the point spread function in 118-126 MHz image, in arcsec
 1806-1814   F9.5    --- psf_b_122                ? Semi-minor axis of the point spread function in 118-126 MHz image, in arcsec
 1816-1828   F13.9   --- psf_pa_122               ? Position angle of the point spread function in 118-126 MHz image, in deg
 1830-1842   E13.10  --- background_130           Background level in 126-134 MHz image, in Jy/beam
 1844-1854   F11.9   --- local_rms_130            Local noise level in 126-134 MHz image, in Jy/beam
 1856-1867   F12.8   --- peak_flux_130            Peak flux-density in 126-134 MHz image, in Jy/beam
 1869-1880   F12.9   --- err_peak_flux_130        Uncertainty in fit for peak flux-density in 126-134 MHz image, in Jy/beam
 1882-1893   F12.8   --- int_flux_130             Integrated flux-density in 126-134 MHz image, in Jy
 1895-1906   F12.9   --- err_int_flux_130         Uncertainty in fit for integrated flux-density in 126-134 MHz image, in Jy
 1908-1916   F9.5    --- a_130                    Fitted semi-major axis in 126-134 MHz image, in arcsec
 1918-1926   F9.5    --- b_130                    Fitted semi-minor axis in 126-134 MHz image, in arcsec
 1928-1941   F14.10  --- pa_130                   Fitted position angle in 126-134 MHz image, in deg
 1943-1955   E13.10  --- residual_mean_130        Mean value of data-model in 126-134 MHz image, in Jy/beam
 1957-1967   F11.9   --- residual_std_130         Standard deviation of data-model in 126-134 MHz image, in Jy/beam
 1969-1977   F9.5    --- psf_a_130                Semi-major axis of the point spread function in 126-134 MHz image, in arcsec
 1979-1987   F9.5    --- psf_b_130                Semi-minor axis of the point spread function in 126-134 MHz image, in arcsec
 1989-2001   F13.9   --- psf_pa_130               Position angle of the point spread function in 126-134 MHz image, in deg
 2003-2015   E13.10  --- background_143           Background level in 139-147 MHz image, in Jy/beam
 2017-2027   F11.9   --- local_rms_143            Local noise level in 139-147 MHz image, in Jy/beam
 2029-2039   F11.8   --- peak_flux_143            Peak flux-density in 139-147 MHz image, in Jy/beam
 2041-2052   F12.9   --- err_peak_flux_143        Uncertainty in fit for peak flux-density in 139-147 MHz image, in Jy/beam
 2054-2065   F12.8   --- int_flux_143             Integrated flux-density in 139-147 MHz image, in Jy
 2067-2078   F12.9   --- err_int_flux_143         Uncertainty in fit for integrated flux-density in 139-147 MHz image, in Jy
 2080-2088   F9.5    --- a_143                    Fitted semi-major axis in 139-147 MHz image, in arcsec
 2090-2098   F9.5    --- b_143                    Fitted semi-minor axis in 139-147 MHz image, in arcsec
 2100-2113   F14.10  --- pa_143                   Fitted position angle in 139-147 MHz image, in deg
 2115-2127   E13.10  --- residual_mean_143        Mean value of data-model in 139-147 MHz image, in Jy/beam
 2129-2139   F11.9   --- residual_std_143         Standard deviation of data-model in 139-147 MHz image, in Jy/beam
 2141-2149   F9.5    --- psf_a_143                Semi-major axis of the point spread function in 139-147 MHz image, in arcsec
 2151-2159   F9.5    --- psf_b_143                Semi-minor axis of the point spread function in 139-147 MHz image, in arcsec
 2161-2174   F14.10  --- psf_pa_143               Position angle of the point spread function in 139-147 MHz image, in deg
 2176-2189   E14.10  --- background_151           Background level in 147-154 MHz image, in Jy/beam 
 2191-2201   F11.9   --- local_rms_151            Local noise level in 147-154 MHz image, in Jy/beam
 2203-2214   F12.8   --- peak_flux_151            Peak flux-density in 147-154 MHz image, in Jy/beam
 2216-2228   F13.10  --- err_peak_flux_151        Uncertainty in fit for peak flux-density in 147-154 MHz image, in Jy/beam
 2230-2241   F12.8   --- int_flux_151             Integrated flux-density in 147-154 MHz image, in Jy
 2243-2254   F12.9   --- err_int_flux_151         Uncertainty in fit for integrated flux-density in 147-154 MHz image, in Jy
 2256-2264   F9.5    --- a_151                    Fitted semi-major axis in 147-154 MHz image, in arcsec
 2266-2274   F9.5    --- b_151                    Fitted semi-minor axis in 147-154 MHz image, in arcsec
 2276-2289   F14.10  --- pa_151                   Fitted position angle in 147-154 MHz image, in deg
 2291-2304   E14.10  --- residual_mean_151        Mean value of data-model in 147-154 MHz image, in Jy/beam
 2306-2316   F11.9   --- residual_std_151         Standard deviation of data-model in 147-154 MHz image, in Jy/beam
 2318-2326   F9.5    --- psf_a_151                Semi-major axis of the point spread function in 147-154 MHz image, in arcsec
 2328-2336   F9.5    --- psf_b_151                Semi-minor axis of the point spread function in 147-154 MHz image, in arcsec
 2338-2349   E12.8   --- psf_pa_151               Position angle of the point spread function in 147-154 MHz image, in deg
 2351-2364   E14.10  --- background_158           Background level in 154-162 MHz image, in Jy/beam  
 2366-2376   F11.9   --- local_rms_158            Local noise level in 154-162 MHz image, in Jy/beam   
 2378-2389   F12.8   --- peak_flux_158            Peak flux-density in 154-162 MHz image, in Jy/beam 
 2391-2403   F13.10  --- err_peak_flux_158        Uncertainty in fit for peak flux-density in 154-162 MHz image, in Jy/beam 
 2405-2416   F12.8   --- int_flux_158             Integrated flux-density in 154-162 MHz image, in Jy 
 2418-2430   F13.10  --- err_int_flux_158         Uncertainty in fit for integrated flux-density in 154-162 MHz image, in Jy 
 2432-2440   F9.5    --- a_158                    Fitted semi-major axis in 154-162 MHz image, in arcsec
 2442-2450   F9.5    --- b_158                    Fitted semi-minor axis in 154-162 MHz image, in arcsec 
 2452-2465   F14.10  --- pa_158                   Fitted position angle in 154-162 MHz image, in deg 
 2467-2480   E14.10  --- residual_mean_158        Mean value of data-model in 154-162 MHz image, in Jy/beam
 2482-2492   F11.9   --- residual_std_158         Standard deviation of data-model in 154-162 MHz image, in Jy/beam
 2494-2502   F9.5    --- psf_a_158                Semi-major axis of the point spread function in 154-162 MHz image, in arcsec
 2504-2512   F9.5    --- psf_b_158                Semi-minor axis of the point spread function in 154-162 MHz image, in arcsec
 2514-2527   F14.10  --- psf_pa_158               Position angle of the point spread function in 154-162 MHz image, in deg  
 2529-2542   E14.10  --- background_166           Background level in 162-170 MHz image, in Jy/beam 
 2544-2555   F12.10  --- local_rms_166            Local noise level in 162-170 MHz image, in Jy/beam 
 2557-2568   F12.8   --- peak_flux_166            Peak flux-density in 162-170 MHz image, in Jy/beam 
 2570-2582   F13.10  --- err_peak_flux_166        Uncertainty in fit for peak flux-density in 162-170 MHz image, in Jy/beam 
 2584-2595   F12.8   --- int_flux_166             Integrated flux-density in 162-170 MHz image, in Jy 
 2597-2609   F13.10  --- err_int_flux_166         Uncertainty in fit for integrated flux-density in 162-170 MHz image, in Jy 
 2611-2619   F9.5    --- a_166                    Fitted semi-major axis in 162-170 MHz image, in arcsec 
 2621-2629   F9.5    --- b_166                    Fitted semi-minor axis in 162-170 MHz image, in arcsec 
 2631-2644   F14.10  --- pa_166                   Fitted position angle in 162-170 MHz image, in deg 
 2646-2659   E14.10  --- residual_mean_166        Mean value of data-model in 162-170 MHz image, in Jy/beam
 2661-2671   F11.9   --- residual_std_166         Standard deviation of data-model in 162-170 MHz image, in Jy/beam
 2673-2681   F9.5    --- psf_a_166                Semi-major axis of the point spread function in 162-170 MHz image, in arcsec
 2683-2691   F9.5    --- psf_b_166                Semi-minor axis of the point spread function in 162-170 MHz image, in arcsec
 2693-2706   F14.10  --- psf_pa_166               Position angle of the point spread function in 162-170 MHz image, in deg
 2708-2720   E13.10  --- background_174           ? Background level in 170-177 MHz image, in Jy/beam
 2722-2733   F12.10  --- local_rms_174            ? Local noise level in 170-177 MHz image, in Jy/beam
 2735-2746   F12.8   --- peak_flux_174            ? Peak flux-density in 170-177 MHz image, in Jy/beam
 2748-2760   F13.10  --- err_peak_flux_174        ? Uncertainty in fit for peak flux-density in 170-177 MHz image, in Jy/beam
 2762-2773   F12.8   --- int_flux_174             ? Integrated flux-density in 170-177 MHz image, in Jy
 2775-2787   F13.10  --- err_int_flux_174         ? Uncertainty in fit for integrated flux-density in 170-177 MHz image, in Jy
 2789-2798   F10.6   --- a_174                    ? Fitted semi-major axis in 170-177 MHz image, in arcsec
 2800-2809   F10.6   --- b_174                    ? Fitted semi-minor axis in 170-177 MHz image, in arcsec
 2811-2824   F14.10  --- pa_174                   ? Fitted position angle in 170-177 MHz image, in deg
 2826-2838   E13.10  --- residual_mean_174        ? Mean value of data-model in 170-177 MHz image, in Jy/beam
 2840-2850   F11.9   --- residual_std_174         ? Standard deviation of data-model in 170-177 MHz image, in Jy/beam
 2852-2860   F9.5    --- psf_a_174                ? Semi-major axis of the point spread function in 170-177 MHz image, in arcsec
 2862-2871   F10.6   --- psf_b_174                ? Semi-minor axis of the point spread function in 170-177 MHz image, in arcsec
 2873-2885   F13.9   --- psf_pa_174               ? Position angle of the point spread function in 170-177 MHz image, in deg
 2887-2899   E13.10  --- background_181           ? Background level in 177-185 MHz image, in Jy/beam
 2901-2912   F12.10  --- local_rms_181            ? Local noise level in 177-185 MHz image, in Jy/beam
 2914-2925   F12.8   --- peak_flux_181            ? Peak flux-density in 177-185 MHz image, in Jy/beam
 2927-2939   F13.10  --- err_peak_flux_181        ? Uncertainty in fit for peak flux-density in 177-185 MHz image, in Jy/beam
 2941-2952   F12.8   --- int_flux_181             ? Integrated flux-density in 177-185 MHz image, in Jy
 2954-2966   F13.10  --- err_int_flux_181         ? Uncertainty in fit for integrated flux-density in 177-185 MHz image, in Jy
 2968-2977   F10.6   --- a_181                    ? Fitted semi-major axis in 177-185 MHz image, in arcsec
 2979-2988   F10.6   --- b_181                    ? Fitted semi-minor axis in 177-185 MHz image, in arcsec
 2990-3003   F14.10  --- pa_181                   ? Fitted position angle in 177-185 MHz image, in deg
 3005-3017   E13.10  --- residual_mean_181        ? Mean value of data-model in 177-185 MHz image, in Jy/beam
 3019-3029   F11.9   --- residual_std_181         ? Standard deviation of data-model in 177-185 MHz image, in Jy/beam
 3031-3040   F10.6   --- psf_a_181                ? Semi-major axis of the point spread function in 177-185 MHz image, in arcsec
 3042-3051   F10.6   --- psf_b_181                ? Semi-minor axis of the point spread function in 177-185 MHz image, in arcsec
 3053-3065   F13.9   --- psf_pa_181               ? Position angle of the point spread function in 177-185 MHz image, in deg
 3067-3080   E14.10  --- background_189           ? Background level in 185-193 MHz image, in Jy/beam
 3082-3093   F12.10  --- local_rms_189            ? Local noise level in 185-193 MHz image, in Jy/beam
 3095-3106   F12.8   --- peak_flux_189            ? Peak flux-density in 185-193 MHz image, in Jy/beam
 3108-3120   F13.10  --- err_peak_flux_189        ? Uncertainty in fit for peak flux-density in 185-193 MHz image, in Jy/beam
 3122-3133   F12.8   --- int_flux_189             ? Integrated flux-density in 185-193 MHz image, in Jy
 3135-3147   F13.10  --- err_int_flux_189         ? Uncertainty in fit for integrated flux-density in 185-193 MHz image, in Jy
 3149-3158   F10.6   --- a_189                    ? Fitted semi-major axis in 185-193 MHz image, in arcsec
 3160-3169   F10.6   --- b_189                    ? Fitted semi-minor axis in 185-193 MHz image, in arcsec
 3171-3184   F14.10  --- pa_189                   ? Fitted position angle in 185-193 MHz image, in deg
 3186-3198   E13.10  --- residual_mean_189        ? Mean value of data-model in 185-193 MHz image, in Jy/beam
 3200-3210   F11.9   --- residual_std_189         ? Standard deviation of data-model in 185-193 MHz image, in Jy/beam
 3212-3221   F10.6   --- psf_a_189                ? Semi-major axis of the point spread function in 185-193 MHz image, in arcsec
 3223-3232   F10.6   --- psf_b_189                ? Semi-minor axis of the point spread function in 185-193 MHz image, in arcsec
 3234-3247   F14.10  --- psf_pa_189               ? Position angle of the point spread function in 185-193 MHz image, in deg
 3249-3261   E13.10  --- background_197           ? Background level in 193-200 MHz image, in Jy/beam
 3263-3274   F12.10  --- local_rms_197            ? Local noise level in 193-200 MHz image, in Jy/beam
 3276-3287   F12.8   --- peak_flux_197            ? Peak flux-density in 193-200 MHz image, in Jy/beam
 3289-3301   F13.10  --- err_peak_flux_197        ? Uncertainty in fit for peak flux-density in 193-200 MHz image, in Jy/beam
 3303-3314   F12.8   --- int_flux_197             ? Integrated flux-density in 193-200 MHz image, in Jy
 3316-3328   F13.10  --- err_int_flux_197         ? Uncertainty in fit for integrated flux-density in 193-200 MHz image, in Jy
 3330-3339   F10.6   --- a_197                    ? Fitted semi-major axis in 193-200 MHz image, in arcsec
 3341-3350   F10.6   --- b_197                    ? Fitted semi-minor axis in 193-200 MHz image, in arcsec
 3352-3365   F14.10  --- pa_197                   ? Fitted position angle in 193-200 MHz image, in deg
 3367-3379   E13.10  --- residual_mean_197        ? Mean value of data-model in 193-200 MHz image, in Jy/beam
 3381-3391   F11.9   --- residual_std_197         ? Standard deviation of data-model in 193-200 MHz image, in Jy/beam
 3393-3402   F10.6   --- psf_a_197                ? Semi-major axis of the point spread function in 193-200 MHz image, in arcsec
 3404-3413   F10.6   --- psf_b_197                ? Semi-minor axis of the point spread function in 193-200 MHz image, in arcsec
 3415-3428   F14.10  --- psf_pa_197               ? Position angle of the point spread function in 193-200 MHz image, in deg
 3430-3442   E13.10  --- background_204           ? Background level in 200-208 MHz image, in Jy/beam
 3444-3455   F12.10  --- local_rms_204            ? Local noise level in 200-208 MHz image, in Jy/beam
 3457-3468   F12.8   --- peak_flux_204            ? Peak flux-density in 200-208 MHz image, in Jy/beam
 3470-3482   F13.10  --- err_peak_flux_204        ? Uncertainty in fit for peak flux-density in 200-208 MHz image, in Jy/beam
 3484-3495   F12.8   --- int_flux_204             ? Integrated flux-density in 200-208 MHz image, in Jy
 3497-3509   F13.10  --- err_int_flux_204         ? Uncertainty in fit for integrated flux-density in 200-208 MHz image, in Jy
 3511-3520   F10.6   --- a_204                    ? Fitted semi-major axis in 200-208 MHz image, in arcsec
 3522-3531   F10.6   --- b_204                    ? Fitted semi-minor axis in 200-208 MHz image, in arcsec
 3533-3546   F14.10  --- pa_204                   ? Fitted position angle in 200-208 MHz image, in deg
 3548-3560   E13.10  --- residual_mean_204        ? Mean value of data-model in 200-208 MHz image, in Jy/beam
 3562-3573   F12.10  --- residual_std_204         ? Standard deviation of data-model in 200-208 MHz image, in Jy/beam
 3575-3584   F10.6   --- psf_a_204                ? Semi-major axis of the point spread function in 200-208 MHz image, in arcsec
 3586-3595   F10.6   --- psf_b_204                ? Semi-minor axis of the point spread function in 200-208 MHz image, in arcsec
 3597-3609   F13.9   --- psf_pa_204               ? Position angle of the point spread function in 200-208 MHz image, in deg
 3611-3624   E14.10  --- background_212           ? Background level in 208-216 MHz image, in Jy/beam
 3626-3637   F12.10  --- local_rms_212            ? Local noise level in 208-216 MHz image, in Jy/beam
 3639-3650   F12.8   --- peak_flux_212            ? Peak flux-density in 208-216 MHz image, in Jy/beam
 3652-3664   F13.10  --- err_peak_flux_212        ? Uncertainty in fit for peak flux-density in 208-216 MHz image, in Jy/beam
 3666-3677   F12.8   --- int_flux_212             ? Integrated flux-density in 208-216 MHz image, in Jy
 3679-3691   F13.10  --- err_int_flux_212         ? Uncertainty in fit for integrated flux-density in 208-216 MHz image, in Jy
 3693-3702   F10.6   --- a_212                    ? Fitted semi-major axis in 208-216 MHz image, in arcsec
 3704-3713   F10.6   --- b_212                    ? Fitted semi-minor axis in 208-216 MHz image, in arcsec
 3715-3728   F14.10  --- pa_212                   ? Fitted position angle in 208-216 MHz image, in deg
 3730-3742   E13.10  --- residual_mean_212        ? Mean value of data-model in 208-216 MHz image, in Jy/beam
 3744-3755   F12.10  --- residual_std_212         ? Standard deviation of data-model in 208-216 MHz image, in Jy/beam
 3757-3766   F10.6   --- psf_a_212                ? Semi-major axis of the point spread function in 208-216 MHz image, in arcsec
 3768-3777   F10.6   --- psf_b_212                ? Semi-minor axis of the point spread function in 208-216 MHz image, in arcsec
 3779-3791   E13.9   --- psf_pa_212               ? Position angle of the point spread function in 208-216 MHz image, in deg
 3793-3805   E13.10  --- background_220           ? Background level in 216-223 MHz image, in Jy/beam
 3807-3818   F12.10  --- local_rms_220            ? Local noise level in 216-223 MHz image, in Jy/beam
 3820-3831   F12.8   --- peak_flux_220            ? Peak flux-density in 216-223 MHz image, in Jy/beam
 3833-3845   F13.10  --- err_peak_flux_220        ? Uncertainty in fit for peak flux-density in 216-223 MHz image, in Jy/beam
 3847-3858   F12.8   --- int_flux_220             ? Integrated flux-density in 216-223 MHz image, in Jy
 3860-3872   F13.10  --- err_int_flux_220         ? Uncertainty in fit for integrated flux-density in 216-223 MHz image, in Jy
 3874-3883   F10.6   --- a_220                    ? Fitted semi-major axis in 216-223 MHz image, in arcsec
 3885-3894   F10.6   --- b_220                    ? Fitted semi-minor axis in 216-223 MHz image, in arcsec
 3896-3909   F14.10  --- pa_220                   ? Fitted position angle in 216-223 MHz image, in deg
 3911-3923   E13.10  --- residual_mean_220        ? Mean value of data-model in 216-223 MHz image, in Jy/beam
 3925-3935   F11.9   --- residual_std_220         ? Standard deviation of data-model in 216-223 MHz image, in Jy/beam
 3937-3946   F10.6   --- psf_a_220                ? Semi-major axis of the point spread function in 216-223 MHz image, in arcsec
 3948-3957   F10.6   --- psf_b_220                ? Semi-minor axis of the point spread function in 216-223 MHz image, in arcsec
 3959-3971   F13.9   --- psf_pa_220               ? Position angle of the point spread function in 216-223 MHz image, in deg
 3973-3986   E14.10  --- background_227           ? Background level in 223-231 MHz image, in Jy/beam
 3988-3999   F12.10  --- local_rms_227            ? Local noise level in 223-231 MHz image, in Jy/beam
 4001-4012   F12.8   --- peak_flux_227            ? Peak flux-density in 223-231 MHz image, in Jy/beam
 4014-4026   F13.10  --- err_peak_flux_227        ? Uncertainty in fit for peak flux-density in 223-231 MHz image, in Jy/beam
 4028-4039   F12.8   --- int_flux_227             ? Integrated flux-density in 223-231 MHz image, in Jy
 4041-4053   F13.10  --- err_int_flux_227         ? Uncertainty in fit for integrated flux-density in 223-231 MHz image, in Jy
 4055-4064   F10.6   --- a_227                    ? Fitted semi-major axis in 223-231 MHz image, in arcsec
 4066-4075   F10.6   --- b_227                    ? Fitted semi-minor axis in 223-231 MHz image, in arcsec
 4077-4090   F14.10  --- pa_227                   ? Fitted position angle in 223-231 MHz image, in deg
 4092-4104   E13.10  --- residual_mean_227        ? Mean value of data-model in 223-231 MHz image, in Jy/beam
 4106-4116   F11.9   --- residual_std_227         ? Standard deviation of data-model in 223-231 MHz image, in Jy/beam
 4118-4127   F10.6   --- psf_a_227                ? Semi-major axis of the point spread function in 223-231 MHz image, in arcsec
 4129-4138   F10.6   --- psf_b_227                ? Semi-minor axis of the point spread function in 223-231 MHz image, in arcsec
 4140-4152   F13.9   --- psf_pa_227               ? Position angle of the point spread function in 223-231 MHz image, in deg
 4154-4165   F12.9   --- GLEAM_alpha              ? Fitted spectral-index using GLEAM-component flux-densities
 4167-4177   F11.9   --- err_GLEAM_alpha          ? Error on fitted, GLEAM spectral-index
 4179-4189   F11.9   --- reduced_chi2_GLEAM_alpha ? Reduced chi^2 statistic for GLEAM spectral-index fit
 4191-4201   F11.7   --- total_int_flux_076       ? Total, integrated flux-density in 72-80 MHz image, in Jy
 4203-4213   F11.9   --- err_total_int_flux_076   ? Error on total, integrated flux-density in 72-80 MHz image, in Jy
 4215-4225   F11.7   --- total_int_flux_084       ? Total, integrated flux-density in 80-88 MHz image, in Jy
 4227-4237   F11.9   --- err_total_int_flux_084   ? Error on total, integrated flux-density in 80-88 MHz image, in Jy
 4239-4249   F11.7   --- total_int_flux_092       ? Total, integrated flux-density in 88-95 MHz image, in Jy
 4251-4261   F11.9   --- err_total_int_flux_092   ? Error on total, integrated flux-density in 88-95 MHz image, in Jy
 4263-4273   F11.7   --- total_int_flux_099       ? Total, integrated flux-density in 95-103 MHz image, in Jy
 4275-4285   F11.9   --- err_total_int_flux_099   ? Error on total, integrated flux-density in 95-103 MHz image, in Jy
 4287-4297   F11.7   --- total_int_flux_107       Total, integrated flux-density in 103-111 MHz image, in Jy
 4299-4310   F12.9   --- err_total_int_flux_107   Error on total, integrated flux-density in 103-111 MHz image, in Jy
 4312-4322   F11.7   --- total_int_flux_115       ? Total, integrated flux-density in 111-118 MHz image, in Jy
 4324-4335   F12.9   --- err_total_int_flux_115   ? Error on total, integrated flux-density in 111-118 MHz image, in Jy
 4337-4347   F11.7   --- total_int_flux_122       ? Total, integrated flux-density in 118-126 MHz image, in Jy
 4349-4360   F12.9   --- err_total_int_flux_122   ? Error on total, integrated flux-density in 118-126 MHz image, in Jy
 4362-4372   F11.7   --- total_int_flux_130       Total, integrated flux-density in 126-134 MHz image, in Jy
 4374-4385   F12.9   --- err_total_int_flux_130   Error on total, integrated flux-density in 126-134 MHz image, in Jy
 4387-4397   F11.7   --- total_int_flux_143       Total, integrated flux-density in 139-147 MHz image, in Jy
 4399-4409   F11.9   --- err_total_int_flux_143   Error on total, integrated flux-density in 139-147 MHz image, in Jy
 4411-4421   F11.7   --- total_int_flux_151       Total, integrated flux-density in 147-154 MHz image, in Jy
 4423-4433   F11.9   --- err_total_int_flux_151   Error on total, integrated flux-density in 147-154 MHz image, in Jy
 4435-4445   F11.7   --- total_int_flux_158       Total, integrated flux-density in 154-162 MHz image, in Jy
 4447-4458   F12.10  --- err_total_int_flux_158   Error on total, integrated flux-density in 154-162 MHz image, in Jy
 4460-4470   F11.7   --- total_int_flux_166       Total, integrated flux-density in 162-170 MHz image, in Jy
 4472-4484   F13.10  --- err_total_int_flux_166   Error on total, integrated flux-density in 162-170 MHz image, in Jy
 4486-4496   F11.7   --- total_int_flux_174       ? Total, integrated flux-density in 170-177 MHz image, in Jy
 4498-4510   F13.10  --- err_total_int_flux_174   ? Error on total, integrated flux-density in 170-177 MHz image, in Jy
 4512-4522   F11.7   --- total_int_flux_181       ? Total, integrated flux-density in 177-185 MHz image, in Jy
 4524-4536   F13.10  --- err_total_int_flux_181   ? Error on total, integrated flux-density in 177-185 MHz image, in Jy
 4538-4548   F11.7   --- total_int_flux_189       ? Total, integrated flux-density in 185-193 MHz image, in Jy
 4550-4561   F12.10  --- err_total_int_flux_189   ? Error on total, integrated flux-density in 185-193 MHz image, in Jy
 4563-4573   F11.7   --- total_int_flux_197       ? Total, integrated flux-density in 193-200 MHz image, in Jy
 4575-4586   F12.10  --- err_total_int_flux_197   ? Error on total, integrated flux-density in 193-200 MHz image, in Jy
 4588-4598   F11.7   --- total_int_flux_204       ? Total, integrated flux-density in 200-208 MHz image, in Jy
 4600-4611   F12.10  --- err_total_int_flux_204   ? Error on total, integrated flux-density in 200-208 MHz image, in Jy
 4613-4623   F11.7   --- total_int_flux_212       ? Total, integrated flux-density in 208-216 MHz image, in Jy
 4625-4636   F12.10  --- err_total_int_flux_212   ? Error on total, integrated flux-density in 208-216 MHz image, in Jy
 4638-4648   F11.7   --- total_int_flux_220       ? Total, integrated flux-density in 216-223 MHz image, in Jy
 4650-4661   F12.10  --- err_total_int_flux_220   ? Error on total, integrated flux-density in 216-223 MHz image, in Jy
 4663-4673   F11.7   --- total_int_flux_227       ? Total, integrated flux-density in 223-231 MHz image, in Jy
 4675-4686   F12.10  --- err_total_int_flux_227   ? Error on total, integrated flux-density in 223-231 MHz image, in Jy
--------------------------------------------------------------------------------
Note (1): refitted_flag as follows:
   0 = GLEAM component was not re-fitted
   1 = GLEAM component is the result of unconstrained re-fitting
   2 = GLEAM component required further work following unconstrained re-fitting
   3 = GLEAM component is the result of priorised re-fitting
Note (2): centroid_flag as follows:
   0 = original brightness-weighted centroid position is provided
   1 = centroid position was recalculated, using the correct number of
        NVSS/SUMSS components
   2 = centroid position was recalculated, using only the NVSS/SUMSS
        components closest to the radio core
Note (3): confusion_flag as follows:
   0 = low-frequency flux-densities are unlikely to be affected by confusion
   1 = low-frequency flux-densities may be affected by confusion
Note (4): host_flag as follows:
   i = a host galaxy has been identified in the AllWISE catalogue
   m = identification of the host galaxy is limited by the mid-infrared data
   n = no AllWISE source should be specified, given the type of radio
        emission involved
   u = it is unclear which AllWISE source is the most-likely host galaxy
--------------------------------------------------------------------------------
================================================================================
(End)    CDS/SARAH WHITE, sarahwhite.astro(at)gmail.com               2020-06-03
