##########################################################################################################################
######                                     STEP1: TWO FIXED MAKERS                                                  ######
##########################################################################################################################

def countgt(input1, input2): #input1 is the string named 'provafs', input2 is the string named 'provafsf2'
  header = ['markers','aaaa', 'aaab', 'aabb', 'abaa', 'abab', 'abbb', 'bbaa',  'bbab', 'bbbb'] #this will be the header of the big matrix
  l0  = input1[0].split(',') 
  row = [l0[9]+'-'+l0[10]]
  ls = []
  for i in input2:
    ls.append(i.split(',')[9]+i.split(',')[10])
  row.append(str(ls.count('aaaa')))
  row.append(str(ls.count('aaab')))
  row.append(str(ls.count('aabb')))
  row.append(str(ls.count('abaa')))
  row.append(str(ls.count('abab')))
  row.append(str(ls.count('abbb')))
  row.append(str(ls.count('bbaa')))
  row.append(str(ls.count('bbab')))
  row.append(str(ls.count('bbbb')))
  return ','.join(header)+'\n'+','.join(row)+'\n'

##########################################################################################################################
######                           STEP2: ONE MAKER FIXED, LOOPING OVER ALL THE MARKERS                               ######
##########################################################################################################################

def loopovertab(input1, input2): #this will allow me to build a genotype*genotype markers for all the markers with marker1
  ls = []
  header = ['markers','aaaa', 'aaab', 'aabb', 'abaa', 'abab', 'abbb', 'bbaa',  'bbab', 'bbbb'] #this will be the header of the big matrix
  for i in range(9, len(input2[0].split(','))):
    ls.append(countgt2(input1, input2, i))
  return ','.join(header)+'\n'+ ','.join(ls).replace('\n,','\n')

def countgt2(input1, input2, n): #input1 is the string named 'provafs', input2 is the string named 'provafsf2'
  l0  = input1[0].split(',') 
  row = [l0[9]+'-'+l0[n]]
  ls = []
  for i in input2:
    ls.append(i.split(',')[9]+i.split(',')[n])
  row.append(str(ls.count('aaaa')))
  row.append(str(ls.count('aaab')))
  row.append(str(ls.count('aabb')))
  row.append(str(ls.count('abaa')))
  row.append(str(ls.count('abab')))
  row.append(str(ls.count('abbb')))
  row.append(str(ls.count('bbaa')))
  row.append(str(ls.count('bbab')))
  row.append(str(ls.count('bbbb')))
  return ','.join(row)+'\n'

##########################################################################################################################
######                       STEP3: BIGGER LOOP: ALL THE MARKERS VS ALL THE MARKERS                                 ######
##########################################################################################################################

def loopovermarkers(input1, input2): #Description: calculates genotype by genotype cosegregation, looping through all the markers within a family
                                     #input1 is the first row of the file that contains the column names in the processed ped file
                                     #input2 is the subfile that contains only F2 ped files (including pheno-genot) from the processed ped file
                                     #specifically, input1 is the string named 'provafs', input2 is the string named 'provafsf2'

  ls = []
  header = ['markers','aaaa', 'aaab', 'aabb', 'abaa', 'abab', 'abbb', 'bbaa',  'bbab', 'bbbb'] #this will be the header of the big matrix
  for j in range(9, len(input2[0].split(','))):
    ls.append(loopovertab3(j, input1, input2))
  return ','.join(header)+'\n'+','.join(ls).replace('\n,','\n')
   
def loopovertab3(j, input1, input2): 
  ls = []
  for n in range(9, len(input2[0].split(','))):
    ls.append(countgt3(j, input1, input2, n))
  return ','.join(ls).replace('\n,','\n')

def countgt3(j, input1, input2, n): 
  l0  = input1[0].split(',') 
  row = [l0[j]+'-'+l0[n]]
  ls = []
  for i in input2:
    ls.append(i.split(',')[j]+i.split(',')[n])
  row.append(str(ls.count('aaaa')))
  row.append(str(ls.count('aaab')))
  row.append(str(ls.count('aabb')))
  row.append(str(ls.count('abaa')))
  row.append(str(ls.count('abab')))
  row.append(str(ls.count('abbb')))
  row.append(str(ls.count('bbaa')))
  row.append(str(ls.count('bbab')))
  row.append(str(ls.count('bbbb')))
  return ','.join(row)+'\n'

##########################################################################################################################
######                 STEP4: BIGGER LOOP - ALL THE MARKERS VS ALL THE MARKERS, BUT FASTER                          ######
##########################################################################################################################

def loopovermarkers4(input1, input2): #Description: calculates genotype by genotype cosegregation, looping through all the markers within a family
                                     #input1 is the first row of the file that contains the column names in the processed ped file
                                     #input2 is the subfile that contains only F2 ped files (including pheno-genot) from the processed ped file
                                     #specifically, input1 is the string named 'provafs', input2 is the string named 'provafsf2'

  ls = []
  header = ['markers','aaaa', 'aaab', 'aabb', 'abaa', 'abab', 'abbb', 'bbaa',  'bbab', 'bbbb'] #this will be the header of the big matrix
  for j in range(9, len(input2[0].split(','))):
    ls.append(loopovertab4(j, input1, input2))
  return ','.join(header)+'\n'+','.join(ls).replace('\n,','\n')
   
def loopovertab4(j, input1, input2): 
  ls = []
  for n in range(j, len(input2[0].split(','))): # I just changed "9" to "j". This avoids redundancy and should do the trick
    ls.append(countgt4(j, input1, input2, n))
  return ','.join(ls).replace('\n,','\n')

def countgt4(j, input1, input2, n): 
  l0  = input1[0].split(',') 
  row = [l0[j]+'-'+l0[n]]
  ls = []
  for i in input2:
    ls.append(i.split(',')[j]+i.split(',')[n])
  row.append(str(ls.count('aaaa')))
  row.append(str(ls.count('aaab')))
  row.append(str(ls.count('aabb')))
  row.append(str(ls.count('abaa')))
  row.append(str(ls.count('abab')))
  row.append(str(ls.count('abbb')))
  row.append(str(ls.count('bbaa')))
  row.append(str(ls.count('bbab')))
  row.append(str(ls.count('bbbb')))
  return ','.join(row)+'\n'


