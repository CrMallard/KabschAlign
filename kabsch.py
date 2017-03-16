"""
Author: Chris Remillard
Email: cxr5298@rit.edu
Date: 16 March 2017
File: kabsch.py
Description: Aligns the alpha carbons of two pdb files, a query file and a template. Using an implementation of Kabsch's algorithm it aligns
			 the query file agains the backbone of the template.
"""


#import sys # For reading commandline arguments, rough implementation may use getopts in the future -CR


"""
Function: aCarbonCoordMatrix

Input: queryFile - .pdb file of your query structure.
	   templateFile - .pdb file of template structure.

Output: queryMat - Three column matrix for the x y and z coordinates of each alpha carbon from the input query structure.
	    templateMat - Three column matrix for the x y and z coordinates of each alpha carbon from the input template structure.

Description: Reads two .pdb files, strips the x, y, and z coordinate value of each alpha carbon for each structure and returns two matrices containing
			 the coordinate sets of each alpha carbon in a new row.
"""
def aCarbonCoordMatrix(queryFile, templateFile): 

	#opens each input file
	queryFi = open(queryFile)
	templateFi = open(templateFile)

	#Reads each of the input files line by line into the variables querLines (query) and tempLines (template)
	querLines = queryFi.readlines()
	tempLines = templateFi.readlines()

	

	for i in range(0,len(querLines)-1):
		print(querLines[i])
	for i in range(0,len(tempLines)-1):
		print(tempLines[i])

	#print(querLines)
	#print(tempLines)

aCarbonCoordMatrix("5gsm.pdb", "5gsl.pdb")
