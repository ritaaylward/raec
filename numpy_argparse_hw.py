import sys, os
import numpy as np
import pickle
import argparse

# local imports
from shared import my_module as mymod
from importlib import reload
reload(mymod)

'-----------------------------------------------------------------------------------'

# Make some arrays

arr_1 = np.array([45, 6, 94, 11, 33, 79, 103, 62]) # 1D array. 8 elements.
arr_2 = np.array(np.arange(16)).reshape(8,2) # 2D array using arange. 16 integer elemets starting from 0: 8 rows, 2 columns
arr_3 = np.array(np.linspace(8, 23, 16)).reshape(2, 8) # 2D array using linspace. 14 float elements between 7 and 23 (inclusive): 2 rows, 8 columns.
arr_4 = np.zeros((4,4)) # a 2D array of 0s. 4 rows, 4 columns.
arr_5 = np.ones((2,3,4))# 3D array of ones. an array of 3 elements(?), each of which is a 4 x 5 array of 1s. 60 total elemts.

print("We made 5 arrays. Do you want to see them printed? (If so, type 'yes')")
if input('> ').lower() == 'yes':
    print(f'\n1st array:\n {arr_1}, \n2nd array:\n {arr_2}, \n3rd array:\n {arr_3}, \n4th array:\n {arr_4}, \n5th array:\n {arr_5}')
else:
    print("You said something other than 'Yes' so we won't print the arrays. :(")

'-----------------------------------------------------------------------------------'

# use argparse to add command-line arguments

# create the parser object
parser = argparse.ArgumentParser()

parser.add_argument('-a', '--a_string', default='not "no"', type=str) # anything other than "no" (not case sensitive) will cause some info about the arrays to print
parser.add_argument('-b', '--b_integer', default=1, type=int) # must be an integer from from 0 to 7 because arr_3 has 8 columns
parser.add_argument('-c', '--c_float', default=900, type=float) # recommend an input such that 500 < c < 3000

# get the arguments
args = parser.parse_args()

'-----------------------------------------------------------------------------------'

# try some methods on the arrays (using the arguments from the command-line)

    # Print some basic info about the arrays
if args.a_string.lower() !=  'no':
    print('\nYour string input for -a is', args.a_string, 'so we will print some basic info about the arrays\n',
    '\tThe shape of arr_3 is:', arr_3.shape,
    '\n\tThe size of arr_4 is:', arr_4.size,
    '\n\tThe mean of arr_1 is:', (arr_1).mean(),
    '\n\tThe minimum value in arr_2 is:', arr_2.min())
else:
    print(f"\nYour string input for -a is '{args.a_string}' so we won't print the basic info about the arrays. :(")

    # do some math with the arrays

    # take a slice out of arr_2 (1st column) and a slice out of arr_3 ('bth' row) and add them to arr_1
arr_new = arr_1 + arr_2[:, 1] + arr_3[0, args.b_integer]
    # re-shape the resulting list into an array of 4 rows, two columns, then multiply it by the transposition of arr_2
arr_new = np.reshape(arr_new, (4, 2)) @ (arr_2.T)

print(f'\nDo some math and get a new array (note you chose to use row {args.b_integer} of arr_3):\n', arr_new)

    # make a new list out of the values greater than -c in array arr_new

arr_new_large_values = []
for i in range(len(arr_new)):
    for j in range(len(arr_new[i])):
        if arr_new[i,j] > args.c_float:
            arr_new_large_values.append(arr_new[i,j])
print(f'The values in the new array that are > {args.c_float} are:\n', arr_new_large_values)

    # change some of the values in arr_4
for i in range(len(arr_4)):
    arr_4[i, i] = i
print('Change the values along the diagonal in arr_4:\n', arr_4)

    # check if the values along the diagonal are less than 2
print('Are the values along the diagonal of arr_4 less than 2?')
for i in range(len(arr_4)):
    if arr_4[i,i] < 2:
        print('\tthe value at position', [i,i], 'is less than 2')
    else:
        print('\tthe value at position', [i,i], 'is not less than 2')

'-----------------------------------------------------------------------------------'

# save some output as a pickle file

    # make an output directory if needed

this_dir = os.path.abspath('.').split('/')[-1] #  path is split at each '/'. this_dir is assigned the last object [-1] in the path. not sure why the '.' is there in abspath.
print("This is the directory we're in now:", this_dir)
out_dir = '../' + this_dir + '_output/'
print(f'We create an output directory "{out_dir}" in line with "{this_dir}" if needed, then save arr_4 as a pickle file in that output directory')
mymod.make_dir(out_dir) # calling on function from mymod that creates a directory


# save it as a pickle file
out_fn = out_dir + 'pickled_output.p'
pickle.dump(arr_4, open(out_fn, 'wb')) # 'wb' is for write binary


# read the file back in
b = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary
