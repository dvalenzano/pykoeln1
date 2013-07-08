import sys
import pykoeln1

file = raw_input('What is the ped file you want to analyze?\n')

input = open(file, 'rU').read()

files = input.split('\n')[:-1]
filesf2 = files[5:]
a = pykoeln1.loopovermarkers(files, filesf2)
ofile = file[:-4]+'_output.csv'
z = open(ofile,'w')
z.write(a)
z.close()
