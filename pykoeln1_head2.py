import sys
import pykoeln1
import time

starttime = time.time()

file = raw_input('What is the ped file you want to analyze?\n')

input = open(file, 'rU').read()

files = input.split('\n')[:-1]
filesf2 = files[5:]
a = pykoeln1.loopovermarkers4(files, filesf2)
ofile = file[:-4]+'_output.csv'
z = open(ofile,'w')
z.write(a)
z.close()
print "Time taken = %0.2f min" %((time.time()-starttime)/60.0)
