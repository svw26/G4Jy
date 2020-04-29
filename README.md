# G4Jy

This is a repository for things related to the GLEAM 4-Jy (G4Jy) Sample.

This sample is a compilation of the brightest radio-sources across the southern sky (Dec. < 30 deg), which have an integrated flux-density > 4 Jy at 151 MHz (as measured in the GLEAM extragalactic catalogue, see https://arxiv.org/abs/1610.08318). The vast majority of these sources are active galactic nuclei (AGN) with powerful radio-jets, although the sample is also known to contain two nearby, star-forming galaxies, a cluster relic, a halo, and the Flame Nebula. The Orion Nebula is excluded for the GLEAM catalogue, and thus the G4Jy Sample, but we provide new low-frequency flux-density measurements for this object in Appendix A of Paper I.

* For an overview of the sample, see https://arxiv.org/abs/1810.01226
* Paper I details how the sample and catalogue were constructed -- https://arxiv.org/abs/2004.13125 -- with supplementary material for Appendix F available here: https://github.com/svw26/G4Jy/tree/master/G4Jy_PaperI_AppendixF
* Paper II provides details of cross-identification for the sample -- https://arxiv.org/abs/2004.13025 

Given the length of Papers I and II, please consider the environment and save trees by not printing... :innocent:

The value-added G4Jy catalogue will be submitted to VizieR but, in the meantime, you can find a copy here: \
https://github.com/svw26/G4Jy/tree/master/catalogue/G4Jy_catalogue_18012020.fits


## The G4Jy Sample Server

A server for distributing the overlays, and component cutouts, for the G4Jy Sample can be found here: \
http://mwa-web.icrar.org/gleam_4jy/q/form

The above interface is good for exploring the sample, but users wishing to download images for several sources may prefer to do this through a Python script. In which case, please try the following.

1. ```cd``` into your chosen working directory
2. Type ```git init```
3. Type ```git pull https://github.com/ICRAR/gleamvo-client```
4. Download the Python script:
```
wget https://raw.githubusercontent.com/svw26/G4Jy/master/server/basic_G4Jy_download.py
```
5. Download the demo input-file: 
```
wget https://raw.githubusercontent.com/svw26/G4Jy/master/server/demo_input_file.txt
```
6. Run the Python script like so, where the search radius is in units of arcmin:
```
python basic_G4Jy_download.py --input_source_list=demo_input_file.txt --search_radius=1.0 --output_dir=demo_downloads
```

Overlays, and the component .fits images from which they are made, will then be downloaded to the specified output-directory. Note that the demo input-file will download images for *three* GLEAM components, which in this case correspond to *two* G4Jy sources. You can expect this to take up 110 MB of space, whilst the images associated with 200 sources would require ~7.5 GB of space. 

For your ease (given the required formatting), also provided within https://github.com/svw26/G4Jy/tree/master/server is an input file that lists all 1,960 GLEAM components associated with the G4Jy Sample. You may want to tweak the gleam_4jy_client.py script (downloaded as part of step '3') if you would like to obtain overlays/images for the 1,863 G4Jy sources that these components correspond to. This is because the mid-infrared images from AllWISE are the largest files (each 27.4 MB in size), so you could avoid these being downloaded by default. If you are having problems, please do get in touch via email or by opening an issue on this repository!


## Seminars/colloquia

As an astrophysicist concerned about the climate crisis, I have both hosted and delivered numerous online talks, resulting in a reduced carbon footprint. Please email (sarahwhite.astro@gmail.com) if you would like me to give a talk on the G4Jy Sample for your institution, either remotely or the next time I am in your part of the world. :earth_americas::earth_africa::earth_asia:

Finally, feel free to use the conference poster made available here: \
https://github.com/svw26/G4Jy/tree/master/poster/SarahWhite_G4Jy_portrait_poster.pdf
(The font size has been chosen so that the poster works equally well for A0 to A4 paper sizes.)


 
 


 


  


