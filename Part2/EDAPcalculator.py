#!/usr/bin/python
from optparse import OptionParser
import os
import sys
import re
import json
import types
import math
from xml.etree import ElementTree as ET

benchmarks = ["401bzip2", "429mcf", "456hmmer", "458sjeng", "470lbm"]
runs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "idealNew"]

with open("EDAPoutput.txt", "a") as o:
	for y in runs:
		o.write("- Machine #{} -".format(y) )
		for x in benchmarks:
			o.write("\n")
			o.write("Bench: {} | ".format(x) )
			a_file = open("EnergyPrinterOutput/output{}{}.txt".format(x, y))	#opens the Energy Printer Output
			lines_to_read = [3]							#line with the Energy Value
			for position, line in enumerate(a_file):
				if position in lines_to_read:
					line= line[10 : -3]					#targets the line segment with the value
					E = float(line)
					o.write("E = {} | ".format(E) )
			a_file = open("EnergyPrinterOutput/output{}{}.txt".format(x, y))	#re-opens the Energy Printer Output
			lines_to_read = [2]							#line with the Delay Value
			for position, line in enumerate(a_file):
				if position in lines_to_read:
					line= line[-12 : -5]					#targets the line segment with the value
					D = float(line)
					o.write("D = {} | ".format(D) )
			a_file = open("McPatOutput/results{}{}.txt".format(x, y))
			lines_to_read = [14]
			for position, line in enumerate(a_file):
				if position in lines_to_read:
					line= line[9 : -6]					#targets the line segment with the value
					A = float(line)
					o.write("A = {} | ".format(A) )
			EDAP = E * D * A
			o.write("EDAP = {}".format(EDAP) )
		o.write("\n")

	print('process is completed')

