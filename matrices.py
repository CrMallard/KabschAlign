"""
Date: 23 March 2017
Author: Chris Remillard
File: matrices.py
Description: A rough class for coordinate matrices in python 2.7 without using numpy
"""

class coordinateMatrix(object):

	def __init__(self):
		

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
