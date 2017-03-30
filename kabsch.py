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

	#Lists for each ATOM line from the respective input file
	qurList = []
	temList = []

	#Distance variable created for more optimized iteration
	dist = len(querLines)-1
	#Iterates through the query file line by line
	for i in range(0,dist):
		#if The line contains the word ATOM indicating it is an atom coordinate line 
		#print(querLines[i][:6])
		if "ATOM" in querLines[i][:6]:
			#print("Found an atom line!")
			#if the line also contains 'CA' indicating that it is the alpha carbon
			if "CA" in querLines[i][12:17]:
				#print("Found an alpha carbon line!")
				#Stores the line in which the above conditions are met into the qurList
				qurList.append(querLines[i])
		#print(querLines[i])


	#Distance variable created for more optimized iteration
	dist = len(tempLines)-1
	#Iterates through the template file line by line
	for i in range(0,dist):
		#if The line contains the word ATOM indicating it is an atom coordinate line 
		#if "ATOM" == tempLines[i].index(tempLines):
		if "ATOM" in tempLines[i][:6]:
			#print("Found an atom at line: "+ str(i))
			#if the line also contains 'CA' indicating that it is the alpha carbon
			if "CA" in tempLines[i][12:17]:
				#print("Found an alpha carbon at line: " + str(i))
				#Stores the line in which the above conditions are met into the qurList
				temList.append(tempLines[i])
		#print(tempLines[i])


	#List of alpha carbon coordinates from the query protein
	qCoords = []
	#Distance variable created for more optimized iteration
	dist = len(qurList)-1
	#Iterate through alpha carbons in the qurList
	for i in range(0, dist):
		qCoords.append(qurList[i][31:55])

	#List of alpha carbon coordinates from the template protein
	tCoords = []
	#Distance variable cread for more optimized iteration
	dist = len(temList)-1
	#Iterate through the alpha carbons in the temList
	for i in range(0, dist):
		tCoords.append(temList[i][31:55])

	for i in range(0, len(qCoords)-1):
		print(qCoords[i])

	print("#############################################")
	print("############# BREAK BREAK BREAK #############")
	print("############# BREAK BREAK BREAK #############")
	print("############# BREAK BREAK BREAK #############")
	print("#############################################")

	for i in range(0, len(tCoords)-1):
		print(tCoords[i])

	#Line for debugging
	#for i in range(0, len(qurList)-1):
	#	print(qurList[i])

	


	#for i in range(0, len(temList)-1):
		#print(temList[i])

	#iterates through each of the list stripping the x, y, and z values from each line
	#for i in range(0, len(qurList)-1):
		

	print("Number of alpha carbons found in query: " + str(len(qurList)))
	print("Number of alpha carbons found in template: " + str(len(temList)))

aCarbonCoordMatrix("5gsm.pdb", "5gsl.pdb")
