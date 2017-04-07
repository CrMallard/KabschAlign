"""
Date: 23 March 2017
Author: Chris Remillard
File: matrices.py
Description: A rough class for coordinate matrices in python 2.7 without using numpy
"""

#### LOOK INTO BASING OFF OF NUMPY PACKAGE
#### SIGNIFICANTLY FASTER THAN USUAL INDIRECT ARITHMETIC IN PYTHON

class coordinateMatrix(object):

	"""
	Function: __init__
	Description: Constructor for an index matrix containing x, y, and z coordinates. This function will initialize the matrix and fill it with coordinates
	Input: <self> : A reference to the object being created
		   <list> : A list of strings which are 24 characters long comprising the x, y, and z coordinates for a single molecule from the pdb file.
	"""
	def __init__(self, list):
		#calculates the length or in this case number of coordinates being added to the matrix
		ln = len(list)
		#Generates a list of lists. The first "super list" is ln long for each coordinate. The sub lists are all of length 3 for each coordinate they will store
		self.matrix = [[]*3 for i in range(ln)]
		#Iterates through the list passed into the constructor
		for i in range(0, ln):
			#Converts the string values into floats doubles which can be signed, may introduce precision errors if decimals end up truncated
			x = float(list[i][:7]) # Contains the first 8 characters of the string which represent the x coordinate
			y = float(list[i][8:16]) # Contains the second set of 8 characters which represent the y coordinate
			z = float(list[i][16:24]) # Contains an 8 character string cooresponding to the z coordinate of the molecule
			self.matrix[i][0]= x #X coordinate is stored into the matrix
			self.matrix[i][1]= y #Y coordinate is stored into the matrix
			self.matrix[i][2]= z #Z coordinate is stored into the matrix


	"""
	Function: toString
	Description: Prints the matrix object out to the command line
	"""
	def toString():
		for i in range(0, len(self.matrix)):
			print(matrix[i])

	"""
	Function: stripCoordToMat
	Description: Creates a list containing lists of length three to contain x, y, and z coordinates
	Input: <lst> : the list of text row coordinates as stripped directly from the pdb file. The input list will consist of strings
		 	 	   of length 24. These strings will contain the three coordinates. This function will then split each spring based 
		 	 	   on the 8 characters alloted to each coordinate as per the PDB 3.3 file format documentation and store them to 
		 	 	   one of the three cells (x, y, or z) to which they correspond.
	"""
	def coordMat(lst):
		#Matrix to be returned containing the coordinate sets for each alpha carbon
		retMat = []
		rows = len(lst)-1
		for i in range(0, rows):
