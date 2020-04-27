#!/usr/bin/env python

"""
Script for passing multiple centroid positions to the GLEAM 4-Jy (G4Jy) Sample Server, and downloading all images relevant to the GLEAM components that are associated with each centroid position (i.e. *source*).

Dependency: gleam_4jy_client

Usage example
====

python basic_G4Jy_download.py --input_source_list=test_positions.txt --search_radius=1.0 --output_dir=G4Jy_downloads

====
Any issues, please contact: sarahwhite.astro@gmail.com or chenwuperth@gmail.com
"""

import gleam_4jy_client
from optparse import OptionParser
import os

# Enter input parameters
parser = OptionParser()
parser.add_option("--input_source_list", dest="INPUT_SOURCE_LIST", type="string", help='Input source list (headings: G4Jy_name G4Jy_component ncmp_GLEAM GLEAM_name centroid_RA centroid_Dec). Example of expected format: "G4Jy 1" - 1.0 "GLEAM J000057-105435" 0.24021 -10.90894. RA and Dec in deg.')
parser.add_option("--search_radius", dest="RADIUS", type="float", help="Search radius in arcmin, queried against the centroid positions within the G4Jy catalogue")
parser.add_option("--output_dir", dest="OUTPUT_DIR", type="string", help="Output directory")
(options, args) = parser.parse_args()
input_source_list=options.INPUT_SOURCE_LIST
radius=options.RADIUS
output_dir=options.OUTPUT_DIR

# Make output directory if it doesn't already exist
if os.path.isdir(output_dir):
    print 'Output directory already exists.'
else:
    os.system('mkdir '+output_dir)

# Run through the input list of positions
ncomp = 0
for line in open(input_source_list):
    columns = line.split()

    # Extract name and position from current line of the input file
    if columns[0] != '#':  # Ignore the line containing column headings
        name = columns[0] + columns[1]  # Although, this is not used 
        ra = columns[6] 
        dec = columns[7]
        ncomp = ncomp + 1

        # Run GLEAM 4-Jy client
        position_string = ra + ' ' + dec
        print 'position_string = ',position_string
        gleam_4jy_client.vo_get(position_string, sr=radius, download_dir=output_dir) # 'sr' is the search radius

print 'Number of GLEAM components = ',ncomp
exit()

