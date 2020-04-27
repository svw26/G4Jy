# G4Jy

This is a repository for things related to the GLEAM 4-Jy Sample: https://arxiv.org/abs/1810.01226.

This sample is a collation of the brightest radio-sources across the southern sky (Dec. < 30 deg), which have an integrated flux-density > 4 Jy at 151 MHz (as measured in the GLEAM extragalactic catalogue, see https://arxiv.org/abs/1610.08318). The vast majority of these sources are active galactic nuclei (AGN) with powerful radio-jets, although the sample is also known to contain two nearby, star-forming galaxies, a cluster relic, a halo, and the Flame Nebula.

Once the paper is accepted, I will provide:
* A link to the catalogue
* A link to a server, which will distribute cutouts and overlays created for this sample
* A python script to aid the download of cutouts/overlays from the server

Stay tuned.

## The G4Jy Sample Server

A server for distributing the overlays, and component cutouts, for the G4Jy Sample:
http://mwa-web.icrar.org/gleam_4jy/q/form

The above interface is good for exploration of the sample, but users wishing to download images for multiple sources may wish to do this through a Python script. Please do the following.

1. ```cd``` into your chosen working directory
2. [Need to attached Python script? Is it not pulled at step 4?]
3. Type ```git init```
4. Type ```git pull https://github.com/ICRAR/gleamvo-client```
5. Download the demo input-file: 
```wget https://raw.githubusercontent.com/svw/G4Jy/master/server/demo_input_file.txt```
6. run the Python script like so:
```
python basic_G4Jy_download.py --input_source_list=demo_input_file.txt --search_radius=1.0 --output_dir=demo_downloads
```

Overlays, and the component .fits images from which they are made, will then be downloaded to the specified output-directory. Note that the demo input-file will download images for three GLEAM components, which in this case correspond to G4Jy sources. You can expect this to take up ~110 MB of space, whilst the images associated with 200 sources would require ~7.5 GB of space. You may want to tweak the Python script if you really want to download the images for all 1,863 sources belonging to the G4Jy Sample.  
 


  


