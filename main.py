'''
This is the main file, it contains all the imports and calls other modules to
compute the result::
'''
###############################  General Imports   ######################################

import math
import random

###############################  Sorting Imports   ######################################

from Sorting.Selection_Sort import selection_sort
from Sorting.Bubble_Sort import bubble_sort

###############################  Challenge Imports   ######################################

#from Challenges import Incture_Challenge

###########################################################################################################

''' Writing ramdon data to a file'''
def data_generator():
    with open('data_set.txt','w') as fid:
        for i in range(20000):
            n = random.randint(-200,20000)
            fid.write(str(n))
            fid.write(',')
            if((i+1)%15==0):
                fid.write('\n')
        fid.close()
# Warning: Un-comment below function only if you need to generate new data set
#data_generator()
###########################################################################################################
''' Reading data raw data from the externael file '''
data = []
with open('data_set.txt','r') as f:
    rawData = [line.strip().split(',') for line in f]
    for datum in rawData:
        data = data + datum

for i in range(data.count('')):
    data.remove('')
    
data = list(map(int , data[:500]))

############################################################################################################

#print("Data to feed :\n", data)
#print("Total values in the data:\n",len(data))
#print("\n")
###############################  Calling Selection Sort   #######################################

#print("Running Selection Sort")
#print(selection_sort(data))

###############################  Calling Bubble Sort   ##########################################

print("Running Bubble Sort")
print(bubble_sort([-234,1,0,23,90,-23,-23]))

##################################################################################################
