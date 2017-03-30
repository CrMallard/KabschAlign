
#Author: Chris Remillard
#File: alphaCarbonTest.R
#Date: 17 March 2017
#Description: Rscript used to pull alpha carbons and their coordinates from a .pdb file
#             used to test the python equivalent method : aCarbonCoordMatrix in the kabsch.py file


#Function: alphaStrip
#Description: Strips the ATOM lines containing CA for atom type in the input .pdb file
#Input: filename - file name or file path to .pdb file
#       ignore - Number of rows to skip. NOTE: This will be the rownumber of the first instance of ATOM minus 2
#       rows - Total number of rows to read. NOTE: Difference between first row in which ATOM appears and last row in which ATOM appears
#Returns: Data frame containing strings for each value in an ATOM row containing CA
alphaStrip <- function(filename, ignore, rows){
    fil <- read.table(filename, skip = ignore, nrows = rows, fill = T, row.names = NULL)
    atoms <- fil[which(fil$V1=="ATOM"), ]
    colnames(atoms) <- c("Type", "SerialNo", "AtomType", "Residue", "Chain", "SeqNo", "X", "Y", "Z", "Occup", "TFactor", "Element", "Charge")
    alpha <- atoms[which(atom$AtomType=='CA'),]
    return(alpha)
}