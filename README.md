# G4Jy

This is a repository for things related to the GLEAM 4-Jy (G4Jy) Sample.

This sample is a collation of the brightest radio-sources across the southern sky (Dec. < 30 deg), which have an integrated flux-density > 4 Jy at 151 MHz (as measured in the GLEAM extragalactic catalogue, see https://arxiv.org/abs/1610.08318). The vast majority of these sources are active galactic nuclei (AGN) with powerful radio-jets, although the sample is also known to contain two nearby, star-forming galaxies, a cluster relic, a halo, and the Flame Nebula.

* For an overview of the sample, see https://arxiv.org/abs/1810.01226
* Paper I details how the sample and catalogue were constructed -- https://arxiv.org/abs/tbc1
* Paper II provides details of cross-identification for the sample -- https://arxiv.org/abs/tbc2 \\
Given the length of Papers I and II, please consider the environment and save trees by not printing... :innocent:

The value-added G4Jy catalogue will be submitted to VizieR but, in the meantime, you can find a copy here: \
https://github.com/svw26/G4Jy/tree/master/catalogue/G4Jy_catalogue_18012020.fits


## The G4Jy Sample Server

A server for distributing the overlays, and component cutouts, for the G4Jy Sample: \
http://mwa-web.icrar.org/gleam_4jy/q/form

The above interface is good for exploration of the sample, but users wishing to download images for multiple sources may prefer to do this through a Python script. In which case, please do the following.

1. ```cd``` into your chosen working directory
2. Type ```git init```
3. Type ```git pull https://github.com/ICRAR/gleamvo-client```
4. Download the Python script:
```
wget https://raw.githubusercontent.com/svw/G4Jy/master/server/basic_G4Jy_download.py
```
5. Download the demo input-file: 
```
wget https://raw.githubusercontent.com/svw/G4Jy/master/server/demo_input_file.txt
```
6. Run the Python script like so, where the search radius is in units of arcmin:
```
python basic_G4Jy_download.py --input_source_list=demo_input_file.txt --search_radius=1.0 --output_dir=demo_downloads
```

Overlays, and the component .fits images from which they are made, will then be downloaded to the specified output-directory. Note that the demo input-file will download images for *three* GLEAM components, which in this case correspond to *two* G4Jy sources. You can expect this to take up 110 MB of space, whilst the images associated with 200 sources would require ~7.5 GB of space. You may want to tweak the gleam_4jy_client.py script if you really would like to download the images for all 1,863 sources belonging to the G4Jy Sample, since the mid-infrared images from AllWISE are the largest files. If all else fails, get in touch!


## Seminars/colloquia

As an astrophysicist concerned about the climate crisis, I have both hosted and delivered numerous online talks, resulting in a reduced carbon footprint. Please email (sarahwhite.astro@gmail.com) if you would like me to give a talk on this work for your institution, either remotely or the next time I am in your part of the world. :earth_americas: :earth_africa: :earth_asia:

Finally, feel free to use the conference poster made available here: \
https://github.com/svw26/G4Jy/tree/master/poster/SarahWhite_G4Jy_portrait_poster.pdf



 
 


 


  


