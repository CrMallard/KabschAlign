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

	#Iterates through the query file line by line
	for i in range(0,len(querLines)-1):
		#if The line contains the word ATOM indicating it is an atom coordinate line 
		#print(querLines[i][:6])
		if "ATOM" in querLines[i][:6]:
			print("Found an atom line!")
			#if the line also contains 'CA' indicating that it is the alpha carbon
			if "CA" in querLines[i][12:17]:
				print("Found an alpha carbon line!")
				#Stores the line in which the above conditions are met into the qurList
				qurList.append(querLines[i])
		#print(querLines[i])

	#Iterates through the template file line by line
	for i in range(0,len(tempLines)-1):
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

	for i in range(0, len(qurList)-1):
		print(qurList[i])

	print("#############################################")
	print("############# BREAK BREAK BREAK #############")
	print("############# BREAK BREAK BREAK #############")
	print("############# BREAK BREAK BREAK #############")
	print("#############################################")

	#for i in range(0, len(temList)-1):
		#print(temList[i])

	print("Number of alpha carbons found in query: " + str(len(qurList)))
	print("Number of alpha carbons found in template: " + str(len(temList)))

aCarbonCoordMatrix("5gsm.pdb", "5gsl.pdb")
