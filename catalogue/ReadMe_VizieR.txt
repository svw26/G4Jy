VIII/105            The GLEAM 4-Jy (G4Jy) Sample                  (White+, 2020)
================================================================================
The GLEAM 4-Jy (G4Jy) Sample:
I. Definition and the catalogue.
II. Host-galaxy identification for individual sources.
    White S.V., Franzen T.M.O., Riseley C.J., Ivy Wong O., KapiNska A.D.,
    Hurley-Walker N., Callingham J.R., Thorat K., Wu C., Hancock P.,
    Hunstead R.W., Seymour N., Swan J., Wayth R., Morgan J., Chhetri R.,
    Jackson C., Weston S., Bell M., For B.-Q., Gaensler B.M.,
    Johnston-Hollitt M., Offringa A., Staveley-Smith L.
   <Publ. Astron. Soc. Australia, 37, 18 (2020)>
   <Publ. Astron. Soc. Australia, 37, 17 (2020)>
   =2020PASA...37...18W
   +2020PASA...37...17W
   =2020yCat.8105....0W
================================================================================
ADC_Keywords: Surveys ; Radio sources ; Galaxy catalogs ; Morphology
Keywords: catalogues - galaxies: active - galaxies: evolution -
          radio continuum: galaxies

Abstract:
    The Murchison Widefield Array (MWA) has observed the entire southern
    sky (Declination, {delta}<30{deg}) at low radio-frequencies, over the
    range 72-231MHz. These observations constitute the GaLactic and
    Extragalactic All-sky MWA (GLEAM) Survey, and we use the extragalactic
    catalogue (Galactic latitude, |b|>10{deg}) to define the GLEAM 4-Jy
    (G4Jy) Sample. This is a complete sample of the 'brightest'
    radio-sources (S_151MHz_>4Jy), the majority of which are active
    galactic nuclei with powerful radio-jets. Crucially, low-frequency
    observations allow the selection of such sources in an
    orientation-independent way (i.e. minimising the bias caused by
    Doppler boosting, inherent in high-frequency surveys). We then use
    higher-resolution radio images, and information at other wavelengths,
    to morphologically classify the brightest components in GLEAM. We also
    conduct cross-checks against the literature, and perform internal
    matching, in order to improve sample completeness (which is estimated
    to be >95.5%). This results in a catalogue of 1,863 sources, making
    the G4Jy Sample over 10 times larger than that of the revised Third
    Cambridge Catalogue of Radio Sources (3CRR; S_178MHz_>10.9Jy). Of
    these G4Jy sources, 78 are resolved by the MWA (Phase-I) synthesised
    beam (~2' at 200MHz), and we label 67% of the sample as 'single',
    26% as 'double', 4% as 'triple', and 3% as having 'complex'
    morphology at ~1GHz (45" resolution). We characterise the spectral
    behaviour of these objects in the radio, and find that the median
    spectral-index is {alpha}=-0.740+/-0.012 between 151MHz and 843MHz,
    and {alpha}=-0.786+/-0.006 between 151MHz and 1400MHz (assuming a
    power-law description, S_{nu}_{prop.to}{nu}^{alpha}^), compared to
    {alpha}=-0.829+/-0.006 within the GLEAM band. Alongside this, our
    value-added catalogue provides mid-infrared source associations
    (subject to 6" resolution at 3.4um) for the radio emission, as
    identified through visual inspection and thorough checks against the
    literature. As such, the G4Jy Sample can be used as a reliable
    training set for cross-identification via machine-learning algorithms.
    We also estimate the angular size of the sources, based on their
    associated components at ~1GHz, and perform a flux-density comparison
    for 67 G4Jy sources that overlap with 3CRR. Analysis of
    multi-wavelength data, and spectral curvature between 72MHz and 20GHz,
    will be presented in subsequent papers, and details for accessing all
    G4Jy overlays are provided at https://github.com/svw26/G4Jy.

Description:
    The construction of the G4Jy Sample draws on radio data from the GLEAM
    extragalactic catalogue (Hurley-Walker et al., 2017MNRAS.464.1146H,
    Cat. VIII/100), SUMSS (Mauch et al., 2003MNRAS.342.1117M, Cat.
    VIII/70; Murphy et al., 2007MNRAS.382..382M, Cat. VIII/82), NVSS
    (Condon et al., 1998AJ....115.1693C, Cat. VIII/65), TGSS ADR1 (Intema
    et al., 2017A&A...598A..78I, Cat. J/A+A/598/A78), and AT20G (Murphy et
    al., 2010MNRAS.402.2403M, Cat. J/MNRAS/402/2403). These datasets were
    used alongside mid-infrared information from AllWISE (Cutri et al.,
    2013, Cat. II/328) and optical positions from 6dFGS (Jones et al.,
    2004MNRAS.355..747J, see Cat. VII/259) for identifying the host
    galaxies of the 1,863 G4Jy radio-sources in the sample. Note that a
    .fits version of the G4Jy catalogue, with complete metadata, will be
    kept up-to-date at https://github.com/svw26/G4Jy.

File Summary:
--------------------------------------------------------------------------------
 FileName      Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe            80        .   This file
catalog.dat     4686     1960   G4Jy catalogue (18/01/2020)
catalog.fits  2880       1157   fits version of G4Jy catalogue (18/01/2020)
--------------------------------------------------------------------------------

See also:
          VIII/65 : 1.4GHz NRAO VLA Sky Survey (NVSS) (Condon+ 1998)
          VIII/78 : Sydney University Molonglo Sky Survey (SUMSS) (Mauch+ 2006)
          VIII/82 : 2nd Epoch Molonglo Galactic Plane Survey (MGPS-2)
                                                             (Murphy+, 2007)
          VII/259 : 6dF galaxy survey final redshift release (Jones+, 2009)
 J/A+A/598/A78    : The GMRT 150MHz all-sky radio survey (Intema+, 2017)
 J/MNRAS/402/2403 : Australia Telescope 20GHz Survey Catalog, AT20G
                                                             (Murphy+, 2010)

 VIII/100 : GaLactic and Extragalactic All-sky MWA survey (Hurley-Walker+, 2016)
 VIII/102 : GLEAM II. Galactic plane (Hurley-Walker+, 2019)

Byte-by-byte Description of file: catalog.dat
--------------------------------------------------------------------------------
   Bytes   Format Units     Label          Explanations
--------------------------------------------------------------------------------
    1-   4  A4    ---       ---            [G4Jy]
    6-   9  I4    ---       G4Jy           Name of source belonging to the
                                            G4Jy Sample, NNNN (G4Jy_name)
        11  A1    ---     m_G4Jy           [ABCDE-] Label for an individual
                                            GLEAM component (G4Jy_component)
        13  I1    ---       NGLEAM         [1/5] Number of GLEAM components for
                                            this G4Jy source (ncmp_GLEAM)
   15-  34  A20   ---       GLEAM          Name of the GLEAM component,
                                            GLEAM JHHMMSS+DDMMSS (GLEAM_name)
        36  I1    ---       rfitFlag       [0/3] Flag for sources with re-fitted
                                            GLEAM measurements
                                            (refitted_flag) (1)
   38-  47  F10.6 deg       RAdeg          Right ascension for the centroid
                                            position (J2000) (centroid_RAJ2000)
   49-  52  F4.2  arcsec  e_RAdeg          Error on RA for the centroid position
                                            (err_centroid_RAJ2000)
   54-  63  F10.6 deg       DEdeg          Declination for the centroid position
                                            (J2000) (centroid_DEJ2000)
   65-  68  F4.2  arcsec  e_DEdeg          Error on Dec for the centroid
                                            position (err_centroid_DEJ2000)
        70  I1    ---       fPos           [0/2] Flag for sources with an
                                            updated centroid-position
                                            (centroid_flag) (2)
   72-  78  A7    ---       Mtype          Morphology of the source in
                                            NVSS/SUMSS/TGSS (morphology)
   80-  81  I2    ---       Nradio         Number of NVSS/SUMSS components
                                            (ncmp_NVSSorSUMSS)
        83  I1    ---       cFlag          [0/1] Flag for sources affected by
                                            confusion in GLEAM
                                            (confusion_flag) (3)
        85  A1    arcsec  l_Size           Upper limit flag on angular size
                                            (angular_size_limit)
   87-  94  F8.3  arcsec    Size           Angular size in NVSS/SUMSS
                                            (angular_size)
   96- 102  F7.4  Jy        Sradio         Total flux-density in NVSS/SUMSS
                                            (S_NVSSorSUMSS)
  104- 109  F6.4  Jy      e_Sradio         Error on the total flux-density in
                                            NVSS/SUMSS (err_S_NVSSorSUMSS)
  111- 116  F6.1  MHz       Freq           Indicates whether NVSS (1400.0) or
                                            SUMSS (843.0) was used for Sradio
                                            (Freq)
  118- 129  F12.9 ---       alphaG4JyNVSS  ? Spectral index between 151 and
                                            1400MHz (G4Jy_NVSS_alpha)
  131- 142 F12.10 ---     e_alphaG4JyNVSS  ? Error on spectral index between
                                            151 and 1400MHz
                                            (err_G4Jy_NVSS_alpha)
  144- 154  F11.8 ---       alphaG4JySUMSS ? Spectral index between 151 and
                                            843MHz (G4Jy_SUMSS_alpha)
  156- 167 F12.10 ---     e_alphaG4JySUMSS ? Error on spectral index between
                                            151 and 843MHz
                                            (err_G4Jy_SUMSS_alpha)
  169- 180  F12.9 ---       alphaG4Jy      ? Fitted spectral-index using total
                                            GLEAM flux-densities (G4Jy_alpha)
  182- 192  F11.9 ---     e_alphaG4Jy      ? Error on fitted, G4Jy
                                            spectral-index (err_G4Jy_alpha)
  194- 204  F11.9 ---       rchi2G4Jy      ? Reduced chi^2 statistic for G4Jy
                                            spectral-index fit
                                            (reduced_chi2_G4Jy_alpha)
       206  A1    ---       hostFlag       [imnu] Flag for the type of
                                            host-galaxy identification
                                            (host_flag) (4)
  208- 226  A19   ---       AllWISE        Name of the host galaxy in AllWISE
                                            (AllWISE_name)
  228- 238  F11.7 deg       RAAdeg         ? Right ascension for the host galaxy
                                            (J2000) (AllWISE_RAJ2000)
  240- 250  F11.7 deg       DEAdeg         ? Declination for the host galaxy
                                            (J2000) (AllWISE_DEJ2000)
  252- 257  F6.3  mag       W1mag          ? W1 magnitude for the host galaxy
                                            (W1mag)
  259- 263  F5.3  mag     e_W1mag          ? Error on W1 magnitude for the
                                            host galaxy (err_W1mag)
  265- 270  F6.3  mag       W2mag          ? W2 magnitude for the host galaxy
                                            (W2mag)
  272- 276  F5.3  mag     e_W2mag          ? Error on W2 magnitude for the
                                            host galaxy (err_W2mag)
  278- 283  F6.3  mag       W3mag          ? W3 magnitude for the host galaxy
                                            (W3mag)
  285- 289  F5.3  mag     e_W3mag          ? Error on W3 magnitude for the
                                            host galaxy (err_W3mag)
  291- 296  F6.3  mag       W4mag          ? W4 magnitude for the host galaxy
                                            (W4mag)
  298- 302  F5.3  mag     e_W4mag          ? Error on W4 magnitude for the
                                            host galaxy (err_W4mag)
  304- 305  I2    h         RAGh           Right ascension for the GLEAM
                                            component (J2000) (GLEAM_ra_str_RAh)
       306  A1    ---       ---            [:]
  307- 308  I2    min       RAGm           Right ascension for the GLEAM
                                            component (J2000) (GLEAM_ra_str_RAm)
       309  A1    ---       ---            [:]
  310- 314  F5.2  s         RAGs           Right ascension for the GLEAM
                                            component (J2000) (GLEAM_ra_str_RAs)
       316  A1    ---       DEG-           Declination sign for the GLEAM
                                            component (J2000)
                                            (GLEAM_dec_str_DE-)
  317- 318  I2    deg       DEGd           Declination for the GLEAM component
                                            (J2000) (GLEAM_dec_str_DEd)
       319  A1    ---       ---            [:]
  320- 321  I2    arcmin    DEGm           Declination for the GLEAM component
                                            (J2000) (GLEAM_dec_str_DEm)
       322  A1    ---       ---            [:]
  323- 327  F5.2  arcsec    DEGs           Declination for the GLEAM component
                                            (J2000) (GLEAM_dec_str_DEs)
  329- 340  F12.8 deg       RAGdeg         Right ascension for the GLEAM
                                            component (J2000) (GLEAM_RAJ2000)
  342- 362 E21.19 deg     e_RAGdeg         Error on RA for the GLEAM
                                            component (err_GLEAM_RAJ2000)
  364- 377 F14.10 deg       DEGdeg         Declination for the GLEAM
                                            component (J2000) (GLEAM_DEJ2000)
  379- 399 E21.19 deg     e_DEGdeg         Error on Dec for the GLEAM
                                            component (err_GLEAM_DEJ2000)
  401- 413 E13.10 Jy/beam   bckwide        Background level in wide-band image
                                            (background_wide)
  415- 426 F12.10 Jy/beam   lrmswide       Local noise level in wide-band image
                                            (local_rms_wide)
  428- 439  F12.8 Jy/beam   Fpwide         Peak flux-density in wide-band image
                                            (peak_flux_wide)
  441- 452 F12.10 Jy/beam e_Fpwide         Uncertainty in fit for peak
                                            flux-density in wide-band  image
                                            (err_peak_flux_wide)
  454- 465  F12.8 Jy        Fintwide       Integrated flux-density in wide-band
                                            image (int_flux_wide)
  467- 478 F12.10 Jy      e_Fintwide       Uncertainty in fit for integrated
                                            flux-density in wide-band image
                                            (err_int_flux_wide)
  480- 488  F9.5  arcsec    awide          Fitted semi-major axis in wide-band
                                            image (a_wide)
  490- 501  F12.9 arcsec  e_awide          ? Uncertainty in fitted semi-major
                                            axis in wide-band image (err_a_wide)
  503- 511  F9.5  arcsec    bwide          Fitted semi-minor axis in wide-band
                                            image (b_wide)
  513- 524  F12.9 arcsec  e_bwide          ? Uncertainty in fitted semi-minor
                                            axis in wide-band image (err_b_wide)
  526- 539 F14.10 deg       pawide         Fitted position angle in wide-band
                                            image (pa_wide)
  541- 552 E12.10 deg     e_pawide         ? Uncertainty in fitted position
                                            angle in wide-band image
                                            (err_pa_wide)
  554- 566 E13.10 Jy/beam   resmwide       Mean value of data-model in wide-band
                                            image (residual_mean_wide)
  568- 579 F12.10 Jy/beam   resstdwide     Standard deviation of data-model in
                                            wide-band image (residual_std_wide)
  581- 589  F9.5  arcsec    psfawide       Semi-major axis of the point spread
                                            function in wide-band image
                                            (psf_a_wide)
  591- 599  F9.5  arcsec    psfbwide       Semi-minor axis of the point spread
                                            function in wide-band image
                                            (psf_b_wide)
  601- 613  F13.9 deg       psfpawide      Position angle of the point spread
                                            function in wide-band image
                                            (psf_pa_wide)
  615- 627 E13.10 Jy/beam   bck076         ? Background level in 72-80MHz image
                                            (background_076)
  629- 639  F11.9 Jy/beam   lrms076        ? Local noise level in 72-80MHz image
                                            (local_rms_076)
  641- 652  F12.8 Jy/beam   Fp076          ? Peak flux-density in 72-80MHz image
                                            (peak_flux_076)
  654- 664  F11.9 Jy/beam e_Fp076          ? Uncertainty in fit for peak
                                            flux-density in 72-80MHz image
                                            (err_peak_flux_076)
  666- 677  F12.8 Jy        Fint076        ? Integrated flux-density in 72-80MHz
                                            image (int_flux_076)
  679- 689  F11.9 Jy      e_Fint076        ? Uncertainty in fit for integrated
                                            flux-density in 72-80MHz image
                                            (err_int_flux_076)
  691- 699  F9.5  arcsec    a076           ? Fitted semi-major axis in 72-80MHz
                                            image (a_076)
  701- 709  F9.5  arcsec    b076           ? Fitted semi-minor axis in 72-80MHz
                                            image (b_076)
  711- 724 F14.10 deg       pa076          ? Fitted position angle in 72-80MHz
                                            image (pa_076)
  726- 739 E14.10 Jy/beam   resm076        ? Mean value of data-model in
                                            72-80MHz image (residual_mean_076)
  741- 751  F11.9 Jy/beam   resstd076      ? Standard deviation of data-model in
                                            72-80MHz image (residual_std_076)
  753- 761  F9.5  arcsec    psfa076        ? Semi-major axis of the point spread
                                            function in 72-80MHz image
                                            (psf_a_076)
  763- 771  F9.5  arcsec    psfb076        ? Semi-minor axis of the point spread
                                            function in 72-80MHz image
                                            (psf_b_076)
  773- 786 F14.10 deg       psfpa076       ? Position angle of the point spread
                                            function in 72-80MHz image
                                            (psf_pa_076)
  788- 800 E13.10 Jy/beam   bck084         ? Background level in 80-88MHz image
                                            (background_084)
  802- 812  F11.9 Jy/beam   lrms084        ? Local noise level in 80-88MHz image
                                            (local_rms_084)
  814- 825  F12.8 Jy/beam   Fp084          ? Peak flux-density in 80-88MHz image
                                            (peak_flux_084)
  827- 837  F11.9 Jy/beam e_Fp084          ? Uncertainty in fit for peak
                                            flux-density in 80-88MHz image
                                            (err_peak_flux_084)
  839- 850  F12.8 Jy        Fint084        ? Integrated flux-density in
                                            80-88MHz image (int_flux_084)
  852- 862  F11.9 Jy      e_Fint084        ? Uncertainty in fit for integrated
                                            flux-density in 80-88MHz image
                                            (err_int_flux_084)
  864- 872  F9.5  arcsec    a084           ? Fitted semi-major axis in 80-88MHz
                                            image (a_084)
  874- 882  F9.5  arcsec    b084           ? Fitted semi-minor axis in 80-88MHz
                                            image (b_084)
  884- 897 F14.10 deg       pa084          ? Fitted position angle in 80-88MHz
                                            image (pa_084)
  899- 911 E13.10 Jy/beam   resm084        ? Mean value of data-model in
                                            80-88MHz image (residual_mean_084)
  913- 923  F11.9 Jy/beam   resstd084      ? Standard deviation of data-model in
                                            80-88MHz image (residual_std_084)
  925- 933  F9.5  arcsec    psfa084        ? Semi-major axis of the point spread
                                            function in 80-88MHz image
                                            (psf_a_084)
  935- 943  F9.5  arcsec    psfb084        ? Semi-minor axis of the point spread
                                            function in 80-88MHz image
                                            (psf_b_084)
  945- 957  F13.9 deg       psfpa084       ? Position angle of the point spread
                                            function in 80-88MHz image
                                            (psf_pa_084)
  959- 972 E14.10 Jy/beam   bck092         ? Background level in 88-95MHz image
                                            (background_092)
  974- 984  F11.9 Jy/beam   lrms092        ? Local noise level in 88-95MHz image
                                            (local_rms_092)
  986- 997  F12.8 Jy/beam   Fp092          ? Peak flux-density in 88-95MHz image
                                            (peak_flux_092)
  999-1010  F12.9 Jy/beam e_Fp092          ? Uncertainty in fit for peak
                                            flux-density in 88-95MHz image
                                            (err_peak_flux_092)
 1012-1022  F11.7 Jy        Fint092        ? Integrated flux-density in 88-95MHz
                                            image (int_flux_092)
 1024-1035  F12.9 Jy      e_Fint092        ? Uncertainty in fit for integrated
                                            flux-density in 88-95MHz image
                                            (err_int_flux_092)
 1037-1045  F9.5  arcsec    a092           ? Fitted semi-major axis in 88-95MHz
                                            image (a_092)
 1047-1055  F9.5  arcsec    b092           ? Fitted semi-minor axis in 88-95MHz
                                            image (b_092)
 1057-1070 F14.10 deg       pa092          ? Fitted position angle in 88-95MHz
                                            image (pa_092)
 1072-1084 E13.10 Jy/beam   resm092        ? Mean value of data-model in
                                            88-95MHz image (residual_mean_092)
 1086-1096  F11.9 Jy/beam   resstd092      ? Standard deviation of data-model in
                                            88-95MHz image (residual_std_092)
 1098-1106  F9.5  arcsec    psfa092        ? Semi-major axis of the point spread
                                            function in 88-95MHz image
                                            (psf_a_092)
 1108-1116  F9.5  arcsec    psfb092        ? Semi-minor axis of the point spread
                                            function in 88-95MHz image
                                            (psf_b_092)
 1118-1131 F14.10 deg       psfpa092       ? Position angle of the point spread
                                            function in 88-95MHz image
                                            (psf_pa_092)
 1133-1145 E13.10 Jy/beam   bck099         ? Background level in 95-103MHz image
                                            (background_099)
 1147-1157  F11.9 Jy/beam   lrms099        ? Local noise level in 95-103MHz
                                            image (local_rms_099)
 1159-1170  F12.8 Jy/beam   Fp099          ? Peak flux-density in 95-103MHz
                                            image (peak_flux_099)
 1172-1183  F12.9 Jy/beam e_Fp099          ? Uncertainty in fit for peak
                                            flux-density in 95-103MHz image
                                            (err_peak_flux_099)
 1185-1196  F12.8 Jy        Fint099        ? Integrated flux-density in
                                            95-103MHz image (int_flux_099)
 1198-1209  F12.9 Jy      e_Fint099        ? Uncertainty in fit for integrated
                                            flux-density in 95-103MHz image
                                            (err_int_flux_099)
 1211-1219  F9.5  arcsec    a099           ? Fitted semi-major axis in 95-103MHz
                                            image (a_099)
 1221-1229  F9.5  arcsec    b099           ? Fitted semi-minor axis in 95-103MHz
                                            image (b_099)
 1231-1244 F14.10 deg       pa099          ? Fitted position angle in 95-103MHz
                                            image (pa_099)
 1246-1258 E13.10 Jy/beam   resm099        ? Mean value of data-model in
                                            95-103MHz image (residual_mean_099)
 1260-1270  F11.9 Jy/beam   resstd099      ? Standard deviation of data-model
                                            in 95-103MHz image
                                            (residual_std_099)
 1272-1280  F9.5  arcsec    psfa099        ? Semi-major axis of the point
                                            spread function in 95-103MHz image
                                            (psf_a_099)
 1282-1290  F9.5  arcsec    psfb099        ? Semi-minor axis of the point
                                            spread function in 95-103MHz image
                                            (psf_b_099)
 1292-1305 F14.10 deg       psfpa099       ? Position angle of the point
                                            spread function in 95-103MHz image
                                            (psf_pa_099)
 1307-1320 E14.10 Jy/beam   bck107         Background level in 103-111MHz image
                                            (background_107)
 1322-1332  F11.9 Jy/beam   lrms107        Local noise level in 103-111MHz image
                                            (local_rms_107)
 1334-1345  F12.8 Jy/beam   Fp107          Peak flux-density in 103-111MHz image
                                            (peak_flux_107)
 1347-1358  F12.9 Jy/beam e_Fp107          ? Uncertainty in fit for peak
                                            flux-density in 103-111MHz image
                                            (err_peak_flux_107)
 1360-1371  F12.8 Jy        Fint107        Integrated flux-density in 103-111MHz
                                            image (int_flux_107)
 1373-1385  F13.9 Jy      e_Fint107        ? Uncertainty in fit for integrated
                                            flux-density in 103-111MHz image
                                            (err_int_flux_107)
 1387-1395  F9.5  arcsec    a107           Fitted semi-major axis in 103-111MHz
                                            image (a_107)
 1397-1405  F9.5  arcsec    b107           Fitted semi-minor axis in 103-111MHz
                                            image (b_107)
 1407-1420 F14.10 deg       pa107          Fitted position angle in 103-111MHz
                                            image (pa_107)
 1422-1434 E13.10 Jy/beam   resm107        Mean value of data-model in
                                            103-111MHz image (residual_mean_107)
 1436-1446  F11.9 Jy/beam   resstd107      Standard deviation of data-model in
                                            103-111MHz image (residual_std_107)
 1448-1456  F9.5  arcsec    psfa107        Semi-major axis of the point spread
                                            function in 103-111MHz image
                                            (psf_a_107)
 1458-1466  F9.5  arcsec    psfb107        Semi-minor axis of the point spread
                                            function in 103-111MHz image
                                            (psf_b_107)
 1468-1481 F14.10 deg       psfpa107       Position angle of the point spread
                                            function in 103-111MHz image
                                            (psf_pa_107)
 1483-1495 E13.10 Jy/beam   bck115         ? Background level in 111-118MHz
                                            image (background_115)
 1497-1507  F11.9 Jy/beam   lrms115        ? Local noise level in 111-118MHz
                                            image (local_rms_115)
 1509-1520  F12.8 Jy/beam   Fp115          ? Peak flux-density in 111-118MHz
                                            image (peak_flux_115)
 1522-1533  F12.9 Jy/beam e_Fp115          ? Uncertainty in fit for peak
                                            flux-density in 111-118MHz image
                                            (err_peak_flux_115)
 1535-1546  F12.8 Jy        Fint115        ? Integrated flux-density in
                                            111-118MHz image (int_flux_115)
 1548-1559  F12.9 Jy      e_Fint115        ? Uncertainty in fit for integrated
                                            flux-density in 111-118MHz image
                                            (err_int_flux_115)
 1561-1569  F9.5  arcsec    a115           ? Fitted semi-major axis in
                                            111-118MHz image (a_115)
 1571-1579  F9.5  arcsec    b115           ? Fitted semi-minor axis in
                                            111-118MHz image (b_115)
 1581-1594 F14.10 deg       pa115          ? Fitted position angle in
                                            111-118MHz image (pa_115)
 1596-1608 E13.10 Jy/beam   resm115        ? Mean value of data-model in
                                            111-118MHz image (residual_mean_115)
 1610-1620  F11.9 Jy/beam   resstd115      ? Standard deviation of data-model in
                                            111-118MHz image (residual_std_115)
 1622-1630  F9.5  arcsec    psfa115        ? Semi-major axis of the point spread
                                            function in 111-118MHz image
                                            (psf_a_115)
 1632-1640  F9.5  arcsec    psfb115        ? Semi-minor axis of the point spread
                                            function in 111-118MHz image
                                            (psf_b_115)
 1642-1653  E12.9 deg       psfpa115       ? Position angle of the point spread
                                            function in 111-118MHz image
                                            (psf_pa_115)
 1655-1668 E14.10 Jy/beam   bck122         ? Background level in 118-126MHz
                                            image (background_122)
 1670-1680  F11.9 Jy/beam   lrms122        ? Local noise level in 118-126MHz
                                            image (local_rms_122)
 1682-1693  F12.8 Jy/beam   Fp122          ? Peak flux-density in 118-126MHz
                                            image (peak_flux_122)
 1695-1706  F12.9 Jy/beam e_Fp122          ? Uncertainty in fit for peak
                                            flux-density in 118-126MHz image
                                            (err_peak_flux_122)
 1708-1719  F12.8 Jy        Fint122        ? Integrated flux-density in
                                            118-126MHz image (int_flux_122)
 1721-1732  F12.9 Jy      e_Fint122        ? Uncertainty in fit for integrated
                                            flux-density in 118-126MHz image
                                            (err_int_flux_122)
 1734-1742  F9.5  arcsec    a122           ? Fitted semi-major axis in
                                            118-126MHz image (a_122)
 1744-1752  F9.5  arcsec    b122           ? Fitted semi-minor axis in
                                            118-126MHz image (b_122)
 1754-1767 F14.10 deg       pa122          ? Fitted position angle in
                                            118-126MHz image (pa_122)
 1769-1781 E13.10 Jy/beam   resm122        ? Mean value of data-model in
                                            118-126MHz image (residual_mean_122)
 1783-1793  F11.9 Jy/beam   resstd122      ? Standard deviation of data-model in
                                            118-126MHz image (residual_std_122)
 1795-1803  F9.5  arcsec    psfa122        ? Semi-major axis of the point spread
                                            function in 118-126MHz image
                                            (psf_a_122)
 1805-1813  F9.5  arcsec    psfb122        ? Semi-minor axis of the point spread
                                            function in 118-126MHz image
                                            (psf_b_122)
 1815-1827  F13.9 deg       psfpa122       ? Position angle of the point spread
                                            function in 118-126MHz image
                                            (psf_pa_122)
 1829-1841 E13.10 Jy/beam   bck130         Background level in 126-134MHz image
                                            (background_130)
 1843-1853  F11.9 Jy/beam   lrms130        Local noise level in 126-134MHz image
                                            (local_rms_130)
 1855-1866  F12.8 Jy/beam   Fp130          Peak flux-density in 126-134MHz image
                                            (peak_flux_130)
 1868-1879  F12.9 Jy/beam e_Fp130          ? Uncertainty in fit for peak
                                            flux-density in 126-134MHz image
                                            (err_peak_flux_130)
 1881-1892  F12.8 Jy        Fint130        Integrated flux-density in 126-134MHz
                                            image (int_flux_130)
 1894-1905  F12.9 Jy      e_Fint130        ? Uncertainty in fit for integrated
                                            flux-density in 126-134MHz image
                                            (err_int_flux_130)
 1907-1915  F9.5  arcsec    a130           Fitted semi-major axis in 126-134MHz
                                            image (a_130)
 1917-1925  F9.5  arcsec    b130           Fitted semi-minor axis in 126-134MHz
                                            image (b_130)
 1927-1940 F14.10 deg       pa130          Fitted position angle in 126-134MHz
                                            image (pa_130)
 1942-1954 E13.10 Jy/beam   resm130        Mean value of data-model in 126-
                                            134MHz image (residual_mean_130)
 1956-1966  F11.9 Jy/beam   resstd130      Standard deviation of data-model in
                                            126-134MHz image (residual_std_130)
 1968-1976  F9.5  arcsec    psfa130        Semi-major axis of the point spread
                                            function in 126-134MHz image
                                            (psf_a_130)
 1978-1986  F9.5  arcsec    psfb130        Semi-minor axis of the point spread
                                            function in 126-134MHz image
                                            (psf_b_130)
 1988-2000  F13.9 deg       psfpa130       Position angle of the point spread
                                            function in 126-134MHz image
                                            (psf_pa_130)
 2002-2014 E13.10 Jy/beam   bck143         Background level in 139-147MHz image
                                            (background_143)
 2016-2026  F11.9 Jy/beam   lrms143        Local noise level in 139-147MHz image
                                            (local_rms_143)
 2028-2039  F12.8 Jy/beam   Fp143          Peak flux-density in 139-147MHz image
                                            (peak_flux_143)
 2041-2052  F12.9 Jy/beam e_Fp143          ? Uncertainty in fit for peak
                                            flux-density in 139-147MHz image
                                            (err_peak_flux_143)
 2054-2065  F12.8 Jy        Fint143        Integrated flux-density in 139-147MHz
                                            image (int_flux_143)
 2067-2078  F12.9 Jy      e_Fint143        ? Uncertainty in fit for integrated
                                            flux-density in 139-147MHz image
                                            (err_int_flux_143)
 2080-2088  F9.5  arcsec    a143           Fitted semi-major axis in 139-147MHz
                                            image (a_143)
 2090-2098  F9.5  arcsec    b143           Fitted semi-minor axis in 139-147MHz
                                            image (b_143)
 2100-2113 F14.10 deg       pa143          Fitted position angle in 139-147MHz
                                            image (pa_143)
 2115-2127 E13.10 Jy/beam   resm143        Mean value of data-model in
                                            139-147MHz image (residual_mean_143)
 2129-2139  F11.9 Jy/beam   resstd143      Standard deviation of data-model in
                                            139-147MHz image (residual_std_143)
 2141-2149  F9.5  arcsec    psfa143        Semi-major axis of the point spread
                                            function in 139-147MHz image
                                            (psf_a_143)
 2151-2159  F9.5  arcsec    psfb143        Semi-minor axis of the point spread
                                            function in 139-147MHz image
                                            (psf_b_143)
 2161-2174 F14.10 deg       psfpa143       Position angle of the point spread
                                            function in 139-147MHz image
                                            (psf_pa_143)
 2176-2189 E14.10 Jy/beam   bck151         Background level in 147-154MHz image
                                            (background_151)
 2191-2201  F11.9 Jy/beam   lrms151        Local noise level in 147-154MHz image
                                            (local_rms_151)
 2203-2214  F12.8 Jy/beam   Fp151          Peak flux-density in 147-154MHz image
                                            (peak_flux_151)
 2216-2228 F13.10 Jy/beam e_Fp151          ? Uncertainty in fit for peak
                                            flux-density in 147-154MHz image
                                            (err_peak_flux_151)
 2230-2241  F12.8 Jy        Fint151        Integrated flux-density in 147-154MHz
                                            image (int_flux_151)
 2243-2254  F12.9 Jy      e_Fint151        ? Uncertainty in fit for integrated
                                            flux-density in 147-154MHz image
                                            (err_int_flux_151)
 2256-2264  F9.5  arcsec    a151           Fitted semi-major axis in 147-154MHz
                                            image (a_151)
 2266-2274  F9.5  arcsec    b151           Fitted semi-minor axis in 147-154MHz
                                            image (b_151)
 2276-2289 F14.10 deg       pa151          Fitted position angle in 147-154MHz
                                            image (pa_151)
 2291-2304 E14.10 Jy/beam   resm151        Mean value of data-model in
                                            147-154MHz image (residual_mean_151)
 2306-2316  F11.9 Jy/beam   resstd151      Standard deviation of data-model in
                                            147-154MHz image (residual_std_151)
 2318-2326  F9.5  arcsec    psfa151        Semi-major axis of the point spread
                                            function in 147-154MHz image
                                            (psf_a_151)
 2328-2336  F9.5  arcsec    psfb151        Semi-minor axis of the point spread
                                            function in 147-154MHz image
                                            (psf_b_151)
 2338-2349  E12.8 deg       psfpa151       Position angle of the point spread
                                            function in 147-154MHz image
                                            (psf_pa_151)
 2351-2364 E14.10 Jy/beam   bck158         Background level in 154-162MHz image
                                            (background_158)
 2366-2376  F11.9 Jy/beam   lrms158        Local noise level in 154-162MHz image
                                            (local_rms_158)
 2378-2389  F12.8 Jy/beam   Fp158          Peak flux-density in 154-162MHz image
                                            (peak_flux_158)
 2391-2403 F13.10 Jy/beam e_Fp158          ? Uncertainty in fit for peak
                                            flux-density in 154-162MHz image
                                            (err_peak_flux_158)
 2405-2416  F12.8 Jy        Fint158        Integrated flux-density in 154-162MHz
                                            image (int_flux_158)
 2418-2430 F13.10 Jy      e_Fint158        ? Uncertainty in fit for integrated
                                            flux-density in 154-162MHz image
                                            (err_int_flux_158)
 2432-2440  F9.5  arcsec    a158           Fitted semi-major axis in 154-162MHz
                                            image (a_158)
 2442-2450  F9.5  arcsec    b158           Fitted semi-minor axis in 154-162MHz
                                            image (b_158)
 2452-2465 F14.10 deg       pa158          Fitted position angle in 154-162MHz
                                            image (pa_158)
 2467-2480 E14.10 Jy/beam   resm158        Mean value of data-model in
                                            154-162MHz image (residual_mean_158)
 2482-2492  F11.9 Jy/beam   resstd158      Standard deviation of data-model in
                                            154-162MHz image (residual_std_158)
 2494-2502  F9.5  arcsec    psfa158        Semi-major axis of the point spread
                                            function in 154-162MHz image
                                            (psf_a_158)
 2504-2512  F9.5  arcsec    psfb158        Semi-minor axis of the point spread
                                            function in 154-162MHz image
                                            (psf_b_158)
 2514-2527 F14.10 deg       psfpa158       Position angle of the point spread
                                            function in 154-162MHz image
                                            (psf_pa_158)
 2529-2542 E14.10 Jy/beam   bck166         Background level in 162-170MHz image
                                            (background_166)
 2544-2555 F12.10 Jy/beam   lrms166        Local noise level in 162-170MHz image
                                            (local_rms_166)
 2557-2568  F12.8 Jy/beam   Fp166          Peak flux-density in 162-170MHz image
                                            (peak_flux_166)
 2570-2582 F13.10 Jy/beam e_Fp166          ? Uncertainty in fit for peak
                                            flux-density in 162-170MHz image
                                            (err_peak_flux_166)
 2584-2595  F12.8 Jy        Fint166        Integrated flux-density in 162-170MHz
                                            image (int_flux_166)
 2597-2609 F13.10 Jy      e_Fint166        ? Uncertainty in fit for integrated
                                            flux-density in 162-170MHz image
                                            (err_int_flux_166)
 2611-2619  F9.5  arcsec    a166           Fitted semi-major axis in 162-170MHz
                                            image (a_166)
 2621-2629  F9.5  arcsec    b166           Fitted semi-minor axis in 162-170MHz
                                            image (b_166)
 2631-2644 F14.10 deg       pa166          Fitted position angle in 162-170MHz
                                            image (pa_166)
 2646-2659 E14.10 Jy/beam   resm166        Mean value of data-model in
                                            162-170MHz image (residual_mean_166)
 2661-2671  F11.9 Jy/beam   resstd166      Standard deviation of data-model in
                                            162-170MHz image (residual_std_166)
 2673-2681  F9.5  arcsec    psfa166        Semi-major axis of the point spread
                                            function in 162-170MHz image
                                            (psf_a_166)
 2683-2691  F9.5  arcsec    psfb166        Semi-minor axis of the point spread
                                            function in 162-170MHz image
                                            (psf_b_166)
 2693-2706 F14.10 deg       psfpa166       Position angle of the point spread
                                            function in 162-170MHz image
                                            (psf_pa_166)
 2708-2720 E13.10 Jy/beam   bck174         ? Background level in 170-177MHz
                                            image (background_174)
 2722-2733 F12.10 Jy/beam   lrms174        ? Local noise level in 170-177MHz
                                            image (local_rms_174)
 2735-2746  F12.8 Jy/beam   Fp174          ? Peak flux-density in 170-177MHz
                                            image (peak_flux_174)
 2748-2760 F13.10 Jy/beam e_Fp174          ? Uncertainty in fit for peak
                                            flux-density in 170-177MHz image
                                            (err_peak_flux_174)
 2762-2773  F12.8 Jy        Fint174        ? Integrated flux-density in
                                            170-177MHz image (int_flux_174)
 2775-2787 F13.10 Jy      e_Fint174        ? Uncertainty in fit for integrated
                                            flux-density in 170-177MHz image
                                            (err_int_flux_174)
 2789-2798  F10.6 arcsec    a174           ? Fitted semi-major axis in
                                            170-177MHz image (a_174)
 2800-2809  F10.6 arcsec    b174           ? Fitted semi-minor axis in
                                            170-177MHz image (b_174)
 2811-2824 F14.10 deg       pa174          ? Fitted position angle in
                                            170-177MHz image (pa_174)
 2826-2838 E13.10 Jy/beam   resm174        ? Mean value of data-model in
                                            170-177MHz image (residual_mean_174)
 2840-2850  F11.9 Jy/beam   resstd174      ? Standard deviation of data-model in
                                            170-177MHz image (residual_std_174)
 2852-2860  F9.5  arcsec    psfa174        ? Semi-major axis of the point spread
                                            function in 170-177 MHz image
                                            (psf_a_174)
 2862-2871  F10.6 arcsec    psfb174        ? Semi-minor axis of the point spread
                                            function in 170-177MHz image
                                            (psf_b_174)
 2873-2885  F13.9 deg       psfpa174       ? Position angle of the point spread
                                            function in 170-177MHz image
                                            (psf_pa_174)
 2887-2899 E13.10 Jy/beam   bck181         ? Background level in 177-185MHz
                                            image (background_181)
 2901-2912 F12.10 Jy/beam   lrms181        ? Local noise level in 177-185MHz
                                            image (local_rms_181)
 2914-2925  F12.8 Jy/beam   Fp181          ? Peak flux-density in 177-185MHz
                                            image (peak_flux_181)
 2927-2939 F13.10 Jy/beam e_Fp181          ? Uncertainty in fit for peak
                                            flux-density in 177-185MHz image
                                            (err_peak_flux_181)
 2941-2952  F12.8 Jy        Fint181        ? Integrated flux-density in
                                            177-185MHz image (int_flux_181)
 2954-2966 F13.10 Jy      e_Fint181        ? Uncertainty in fit for integrated
                                            flux-density in 177-185MHz image
                                            (err_int_flux_181)
 2968-2977  F10.6 arcsec    a181           ? Fitted semi-major axis in
                                            177-185MHz image (a_181)
 2979-2988  F10.6 arcsec    b181           ? Fitted semi-minor axis in
                                            177-185MHz image (b_181)
 2990-3003 F14.10 deg       pa181          ? Fitted position angle in
                                            177-185MHz image (pa_181)
 3005-3017 E13.10 Jy/beam   resm181        ? Mean value of data-model in
                                            177-185MHz image (residual_mean_181)
 3019-3029  F11.9 Jy/beam   resstd181      ? Standard deviation of data-model in
                                            177-185MHz image (residual_std_181)
 3031-3040  F10.6 arcsec    psfa181        ? Semi-major axis of the point spread
                                            function in 177-185MHz image
                                            (psf_a_181)
 3042-3051  F10.6 arcsec    psfb181        ? Semi-minor axis of the point spread
                                            function in 177-185MHz image
                                            (psf_b_181)
 3053-3065  F13.9 deg       psfpa181       ? Position angle of the point spread
                                            function in 177-185MHz image
                                            (psf_pa_181)
 3067-3080 E14.10 Jy/beam   bck189         ? Background level in 185-193MHz
                                            image (background_189)
 3082-3093 F12.10 Jy/beam   lrms189        ? Local noise level in 185-193MHz
                                            image (local_rms_189)
 3095-3106  F12.8 Jy/beam   Fp189          ? Peak flux-density in 185-193MHz
                                            image (peak_flux_189)
 3108-3120 F13.10 Jy/beam e_Fp189          ? Uncertainty in fit for peak
                                            flux-density in 185-193MHz image
                                            (err_peak_flux_189)
 3122-3133  F12.8 Jy        Fint189        ? Integrated flux-density in
                                            185-193MHz image (int_flux_189)
 3135-3147 F13.10 Jy      e_Fint189        ? Uncertainty in fit for integrated
                                            flux-density in 185-193MHz image
                                            (err_int_flux_189)
 3149-3158  F10.6 arcsec    a189           ? Fitted semi-major axis in
                                            185-193MHz image (a_189)
 3160-3169  F10.6 arcsec    b189           ? Fitted semi-minor axis in
                                            185-193MHz image (b_189)
 3171-3184 F14.10 deg       pa189          ? Fitted position angle in
                                            185-193MHz image (pa_189)
 3186-3198 E13.10 Jy/beam   resm189        ? Mean value of data-model in
                                            185-193MHz image (residual_mean_189)
 3200-3210  F11.9 Jy/beam   resstd189      ? Standard deviation of data-model in
                                            185-193MHz image (residual_std_189)
 3212-3221  F10.6 arcsec    psfa189        ? Semi-major axis of the point spread
                                            function in 185-193MHz image
                                            (psf_a_189)
 3223-3232  F10.6 arcsec    psfb189        ? Semi-minor axis of the point spread
                                            function in 185-193MHz image
                                            (psf_b_189)
 3234-3247 F14.10 deg       psfpa189       ? Position angle of the point spread
                                            function in 185-193MHz image
                                            (psf_pa_189)
 3249-3261 E13.10 Jy/beam   bck197         ? Background level in 193-200MHz
                                            image (background_197)
 3263-3274 F12.10 Jy/beam   lrms197        ? Local noise level in 193-200MHz
                                            image (local_rms_197)
 3276-3287  F12.8 Jy/beam   Fp197          ? Peak flux-density in 193-200MHz
                                            image (peak_flux_197)
 3289-3301 F13.10 Jy/beam e_Fp197          ? Uncertainty in fit for peak
                                            flux-density in 193-200MHz image
                                            (err_peak_flux_197)
 3303-3314  F12.8 Jy        Fint197        ? Integrated flux-density in
                                            193-200MHz image (int_flux_197)
 3316-3328 F13.10 Jy      e_Fint197        ? Uncertainty in fit for integrated
                                            flux-density in 193-200MHz image
                                            (err_int_flux_197)
 3330-3339  F10.6 arcsec    a197           ? Fitted semi-major axis in
                                            193-200MHz image (a_197)
 3341-3350  F10.6 arcsec    b197           ? Fitted semi-minor axis in
                                            193-200MHz image (b_197)
 3352-3365 F14.10 deg       pa197          ? Fitted position angle in
                                            193-200MHz image (pa_197)
 3367-3379 E13.10 Jy/beam   resm197        ? Mean value of data-model in
                                            193-200MHz image (residual_mean_197)
 3381-3391  F11.9 Jy/beam   resstd197      ? Standard deviation of data-model in
                                            193-200MHz image (residual_std_197)
 3393-3402  F10.6 arcsec    psfa197        ? Semi-major axis of the point spread
                                            function in 193-200MHz image
                                            (psf_a_197)
 3404-3413  F10.6 arcsec    psfb197        ? Semi-minor axis of the point spread
                                            function in 193-200MHz image
                                            (psf_b_197)
 3415-3428 F14.10 deg       psfpa197       ? Position angle of the point spread
                                            function in 193-200MHz image
                                            (psf_pa_197)
 3430-3442 E13.10 Jy/beam   bck204         ? Background level in 200-208MHz
                                            image (background_204)
 3444-3455 F12.10 Jy/beam   lrms204        ? Local noise level in 200-208MHz
                                            image (local_rms_204)
 3457-3468  F12.8 Jy/beam   Fp204          ? Peak flux-density in 200-208MHz
                                            image (peak_flux_204)
 3470-3482 F13.10 Jy/beam e_Fp204          ? Uncertainty in fit for peak
                                            flux-density in 200-208MHz image
                                            (err_peak_flux_204)
 3484-3495  F12.8 Jy        Fint204        ? Integrated flux-density in
                                            200-208MHz image (int_flux_204)
 3497-3509 F13.10 Jy      e_Fint204        ? Uncertainty in fit for integrated
                                            flux-density in 200-208MHz image
                                            (err_int_flux_204)
 3511-3520  F10.6 arcsec    a204           ? Fitted semi-major axis in
                                            200-208MHz image (a_204)
 3522-3531  F10.6 arcsec    b204           ? Fitted semi-minor axis in
                                            200-208MHz image (b_204)
 3533-3546 F14.10 deg       pa204          ? Fitted position angle in
                                            200-208MHz image (pa_204)
 3548-3560 E13.10 Jy/beam   resm204        ? Mean value of data-model in
                                            200-208MHz image (residual_mean_204)
 3562-3573 F12.10 Jy/beam   resstd204      ? Standard deviation of data-model in
                                            200-208MHz image (residual_std_204)
 3575-3584  F10.6 arcsec    psfa204        ? Semi-major axis of the point spread
                                            function in 200-208MHz image
                                            (psf_a_204)
 3586-3595  F10.6 arcsec    psfb204        ? Semi-minor axis of the point spread
                                            function in 200-208MHz image
                                            (psf_b_204)
 3597-3609  F13.9 deg       psfpa204       ? Position angle of the point spread
                                            function in 200-208MHz image
                                            (psf_pa_204)
 3611-3624 E14.10 Jy/beam   bck212         ? Background level in 208-216MHz
                                            image (background_212)
 3626-3637 F12.10 Jy/beam   lrms212        ? Local noise level in 208-216MHz
                                            image (local_rms_212)
 3639-3650  F12.8 Jy/beam   Fp212          ? Peak flux-density in 208-216MHz
                                            image (peak_flux_212)
 3652-3664 F13.10 Jy/beam e_Fp212          ? Uncertainty in fit for peak
                                            flux-density in 208-216MHz image
                                            (err_peak_flux_212)
 3666-3677  F12.8 Jy        Fint212        ? Integrated flux-density in
                                            208-216MHz image (int_flux_212)
 3679-3691 F13.10 Jy      e_Fint212        ? Uncertainty in fit for integrated
                                            flux-density in 208-216MHz image
                                            (err_int_flux_212)
 3693-3702  F10.6 arcsec    a212           ? Fitted semi-major axis in
                                            208-216MHz image (a_212)
 3704-3713  F10.6 arcsec    b212           ? Fitted semi-minor axis in
                                            208-216MHz image (b_212)
 3715-3728 F14.10 deg       pa212          ? Fitted position angle in
                                            208-216MHz image (pa_212)
 3730-3742 E13.10 Jy/beam   resm212        ? Mean value of data-model in
                                            208-216MHz image (residual_mean_212)
 3744-3755 F12.10 Jy/beam   resstd212      ? Standard deviation of data-model in
                                            208-216MHz image (residual_std_212)
 3757-3766  F10.6 arcsec    psfa212        ? Semi-major axis of the point spread
                                            function in 208-216MHz image
                                            (psf_a_212)
 3768-3777  F10.6 arcsec    psfb212        ? Semi-minor axis of the point spread
                                            function in 208-216MHz image
                                            (psf_b_212)
 3779-3791  E13.9 deg       psfpa212       ? Position angle of the point spread
                                            function in 208-216MHz image
                                            (psf_pa_212)
 3793-3805 E13.10 Jy/beam   bck220         ? Background level in 216-223MHz
                                            image (background_220)
 3807-3818 F12.10 Jy/beam   lrms220        ? Local noise level in 216-223MHz
                                            image (local_rms_220)
 3820-3831  F12.8 Jy/beam   Fp220          ? Peak flux-density in 216-223MHz
                                            image (peak_flux_220)
 3833-3845 F13.10 Jy/beam e_Fp220          ? Uncertainty in fit for peak
                                            flux-density in 216-223MHz image
                                            (err_peak_flux_220)
 3847-3858  F12.8 Jy        Fint220        ? Integrated flux-density in
                                            216-223MHz image (int_flux_220)
 3860-3872 F13.10 Jy      e_Fint220        ? Uncertainty in fit for integrated
                                            flux-density in 216-223MHz image
                                            (err_int_flux_220)
 3874-3883  F10.6 arcsec    a220           ? Fitted semi-major axis in
                                            216-223MHz image (a_220)
 3885-3894  F10.6 arcsec    b220           ? Fitted semi-minor axis in
                                            216-223MHz image (b_220)
 3896-3909 F14.10 deg       pa220          ? Fitted position angle in
                                            216-223MHz image (pa_220)
 3911-3923 E13.10 Jy/beam   resm220        ? Mean value of data-model in
                                            216-223MHz image (residual_mean_220)
 3925-3935  F11.9 Jy/beam   resstd220      ? Standard deviation of data-model in
                                            216-223MHz image (residual_std_220)
 3937-3946  F10.6 arcsec    psfa220        ? Semi-major axis of the point spread
                                            function in 216-223MHz image
                                            (psf_a_220)
 3948-3957  F10.6 arcsec    psfb220        ? Semi-minor axis of the point spread
                                            function in 216-223MHz image
                                            (psf_b_220)
 3959-3971  F13.9 deg       psfpa220       ? Position angle of the point spread
                                            function in 216-223MHz image
                                            (psf_pa_220)
 3973-3986 E14.10 Jy/beam   bck227         ? Background level in 223-231MHz
                                            image (background_227)
 3988-3999 F12.10 Jy/beam   lrms227        ? Local noise level in 223-231MHz
                                            image (local_rms_227)
 4001-4012  F12.8 Jy/beam   Fp227          ? Peak flux-density in 223-231MHz
                                            image (peak_flux_227)
 4014-4026 F13.10 Jy/beam e_Fp227          ? Uncertainty in fit for peak
                                            flux-density in 223-231MHz image
                                            (err_peak_flux_227)
 4028-4039  F12.8 Jy        Fint227        ? Integrated flux-density in
                                            223-231MHz image (int_flux_227)
 4041-4053 F13.10 Jy      e_Fint227        ? Uncertainty in fit for integrated
                                            flux-density in 223-231MHz image
                                            (err_int_flux_227)
 4055-4064  F10.6 arcsec    a227           ? Fitted semi-major axis in
                                            223-231MHz image (a_227)
 4066-4075  F10.6 arcsec    b227           ? Fitted semi-minor axis in
                                            223-231MHz image (b_227)
 4077-4090 F14.10 deg       pa227          ? Fitted position angle in
                                            223-231MHz image (pa_227)
 4092-4104 E13.10 Jy/beam   resm227        ? Mean value of data-model in
                                            223-231MHz image (residual_mean_227)
 4106-4116  F11.9 Jy/beam   resstd227      ? Standard deviation of data-model in
                                            223-231MHz image (residual_std_227)
 4118-4127  F10.6 arcsec    psfa227        ? Semi-major axis of the point spread
                                            function in 223-231MHz image
                                            (psf_a_227)
 4129-4138  F10.6 arcsec    psfb227        ? Semi-minor axis of the point spread
                                            function in 223-231MHz image
                                            (psf_b_227)
 4140-4152  F13.9 deg       psfpa227       ? Position angle of the point spread
                                            function in 223-231MHz image
                                            (psf_pa_227)
 4154-4165  F12.9 ---       GLEAM-alpha    ? Fitted spectral-index using
                                            GLEAM-component flux-densities
                                            (GLEAM_alpha)
 4167-4177  F11.9 ---     e_GLEAM-alpha    ? Error on fitted, GLEAM
                                            spectral-index (err_GLEAM_alpha)
 4179-4189  F11.9 ---       rchi2GLEAM     ? Reduced chi^2 statistic for GLEAM
                                            spectral-index fit
                                            (reduced_chi2_GLEAM_alpha)
 4191-4201  F11.7 Jy        FintTot076     ? Total, integrated flux-density in
                                            72-80MHz image (total_int_flux_076)
 4203-4213  F11.9 Jy      e_FintTot076     ? Error on total, integrated
                                            flux-density in 72-80MHz image
                                            (err_total_int_flux_076)
 4215-4225  F11.7 Jy        FintTot084     ? Total, integrated flux-density in
                                            80-88MHz image (total_int_flux_084)
 4227-4237  F11.9 Jy      e_FintTot084     ? Error on total, integrated
                                            flux-density in 80-88MHz image
                                            (err_total_int_flux_084)
 4239-4249  F11.7 Jy        FintTot092     ? Total, integrated flux-density in
                                            88-95MHz image (total_int_flux_092)
 4251-4261  F11.9 Jy      e_FintTot092     ? Error on total, integrated
                                            flux-density in 88-95MHz image
                                            (err_total_int_flux_092)
 4263-4273  F11.7 Jy        FintTot099     ? Total, integrated flux-density in
                                            95-103MHz image (total_int_flux_099)
 4275-4285  F11.9 Jy      e_FintTot099     ? Error on total, integrated
                                            flux-density in 95-103MHz image
                                            (err_total_int_flux_099)
 4287-4297  F11.7 Jy        FintTot107     Total, integrated flux-density in
                                            103-111MHz image
                                            (total_int_flux_107)
 4299-4310  F12.9 Jy      e_FintTot107     Error on total, integrated
                                            flux-density in 103-111MHz image
                                            (err_total_int_flux_107)
 4312-4322  F11.7 Jy        FintTot115     ? Total, integrated flux-density in
                                            111-118MHz image
                                            (total_int_flux_115)
 4324-4335  F12.9 Jy      e_FintTot115     ? Error on total, integrated
                                            flux-density in 111-118MHz image
                                            (err_total_int_flux_115)
 4337-4347  F11.7 Jy        FintTot122     ? Total, integrated flux-density in
                                            118-126MHz image
                                            (total_int_flux_122)
 4349-4360  F12.9 Jy      e_FintTot122     ? Error on total, integrated
                                            flux-density in 118-126MHz image
                                            (err_total_int_flux_122)
 4362-4372  F11.7 Jy        FintTot130     Total, integrated flux-density in
                                            126-134MHz image
                                            (total_int_flux_130)
 4374-4385  F12.9 Jy      e_FintTot130     Error on total, integrated
                                            flux-density in 126-134MHz image
                                            (err_total_int_flux_130)
 4387-4397  F11.7 Jy        FintTot143     Total, integrated flux-density in
                                            139-147MHz image
                                            (total_int_flux_143)
 4399-4409  F11.9 Jy      e_FintTot143     Error on total, integrated
                                            flux-density in 139-147MHz image
                                            (err_total_int_flux_143)
 4411-4421  F11.7 Jy        FintTot151     Total, integrated flux-density in
                                            147-154MHz image
                                            (total_int_flux_151)
 4423-4433  F11.9 Jy      e_FintTot151     Error on total, integrated
                                            flux-density in 147-154MHz image
                                            (err_total_int_flux_151)
 4435-4445  F11.7 Jy        FintTot158     Total, integrated flux-density in
                                            154-162MHz image
                                            (total_int_flux_158)
 4447-4458 F12.10 Jy      e_FintTot158     Error on total, integrated
                                            flux-density in 154-162MHz image
                                            (err_total_int_flux_158)
 4460-4470  F11.7 Jy        FintTot166     Total, integrated flux-density in
                                            162-170MHz image
                                            (total_int_flux_166)
 4472-4484 F13.10 Jy      e_FintTot166     Error on total, integrated
                                            flux-density in 162-170MHz image
                                            (err_total_int_flux_166)
 4486-4496  F11.7 Jy        FintTot174     ? Total, integrated flux-density in
                                            170-177MHz image
                                            (total_int_flux_174)
 4498-4510 F13.10 Jy      e_FintTot174     ? Error on total, integrated
                                            flux-density in 170-177MHz image
                                            (err_total_int_flux_174)
 4512-4522  F11.7 Jy        FintTot181     ? Total, integrated flux-density in
                                            177-185MHz image
                                            (total_int_flux_181)
 4524-4536 F13.10 Jy      e_FintTot181     ? Error on total, integrated
                                            flux-density in 177-185MHz image
                                            (err_total_int_flux_181)
 4538-4548  F11.7 Jy        FintTot189     ? Total, integrated flux-density in
                                            185-193MHz image
                                            (total_int_flux_189)
 4550-4561 F12.10 Jy      e_FintTot189     ? Error on total, integrated
                                            flux-density in 185-193MHz image
                                            (err_total_int_flux_189)
 4563-4573  F11.7 Jy        FintTot197     ? Total, integrated flux-density in
                                            193-200MHz image
                                            (total_int_flux_197)
 4575-4586 F12.10 Jy      e_FintTot197     ? Error on total, integrated
                                            flux-density in 193-200MHz image
                                            (err_total_int_flux_197)
 4588-4598  F11.7 Jy        FintTot204     ? Total, integrated flux-density in
                                            200-208MHz image
                                            (total_int_flux_204)
 4600-4611 F12.10 Jy      e_FintTot204     ? Error on total, integrated
                                            flux-density in 200-208MHz image
                                            (err_total_int_flux_204)
 4613-4623  F11.7 Jy        FintTot212     ? Total, integrated flux-density in
                                            208-216MHz image
                                            (total_int_flux_212)
 4625-4636 F12.10 Jy      e_FintTot212     ? Error on total, integrated
                                            flux-density in 208-216MHz image
                                            (err_total_int_flux_212)
 4638-4648  F11.7 Jy        FintTot220     ? Total, integrated flux-density in
                                            216-223MHz image
                                            (total_int_flux_220)
 4650-4661 F12.10 Jy      e_FintTot220     ? Error on total, integrated
                                            flux-density in 216-223MHz image
                                            (err_total_int_flux_220)
 4663-4673  F11.7 Jy        FintTot227     ? Total, integrated flux-density in
                                            223-231MHz image
                                            (total_int_flux_227)
 4675-4686 F12.10 Jy      e_FintTot227     ? Error on total, integrated
                                            flux-density in 223-231MHz image
                                            (err_total_int_flux_227)
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

Acknowledgements:
    Sarah White, sarahwhite.astro(at)gmail.com

================================================================================
(End)                                        Patricia Vannier [CDS]  28-May-2020
