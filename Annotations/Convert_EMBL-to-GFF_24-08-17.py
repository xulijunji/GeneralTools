#!usr/usr/bin/python

###################
# Import packages #
###################

import sys
from BCBio import GFF
from Bio import SeqIO

# Python script to convert from EMBL to GFF format
# Author: Joseph Crispell
# Created: 24-08-17

# REQUIRES:
# bcbio-gff		pip install bcbio-gff
# biopython		pip install biopython

# Command line structure:
# python Convert_EMBL-to-GFF.py input.embl output.gff

# Code taken from to-gff tool. Available here: https://github.com/mscook/to-gff
# Note that if converting EMBL file from RATT then you'll need to substitute the first line from the original EMBL file

###############
# Check input #
###############

if len(sys.argv) != 3:
	print "Python script to convert EMBL formatted file into GFF formatted file\n"
	print "Command line structure:"
	print "\tpython Convert_EMBL-to-GFF.py input.embl output.gff"
	print "\t\tinput.embl\tPath to input file in EMBL format"
	print "\t\toutput.gff\tPath to output file (will be in GFF format)\n"
	print "Requires:"
	print "\tbcbio-gff\tTo install use: pip install bcbio-gff"
	print "\tbiopython\tTo install use: pip install biopython"
	sys.exit()

##################################
# Get the input and output files #
##################################

input = open(sys.argv[1])
output = open(sys.argv[2], 'w')

#########################################
# Convert input EMBL to output GFF file #
#########################################

GFF.write(SeqIO.parse(input, "embl"), output)