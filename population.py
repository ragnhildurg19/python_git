# DESCRIPTION
# In this project, you develop a program, population.py, that reads population figures for US states 
# for a particular year and prints out the states that have the minimum and maximum population for the given year.
# The first row is a header row.  
# The population figures for each state are shown in three columns, for years 1990, 1980 and 1970.  
# Notice that the header years and the number of population columns (>= 1), 
# and of course the population figures, could be different in another input file.  
# The population figures only contain digits (no commas or periods). 
# Note also that the name of a state can possibly consist of two words (but not more).
# The input to the program is a name of a file in the above format 
# and the year the user is interested in. For example, 
# if the user enters the year 1980 she is only interested in data from that particular column.  
# The output of the program is information about the states that had the minimum and maximum population 
# for the given year.  Hint: The min() and max() funciton or sorted() function might come in handy!
# Note that the minimum and maximum are tuples.  
# This suggest that you could indeed use list of tuples in your implementation.

# Your program should print out an error message and quit if the input file is not found 
# (you should however not call the quit() function).  
# Moreover, it should ask the user, repeatedly, to input a valid year if an invalid year is given:

# 2. Biðja um ártal. 
# 3. Prenta út max og min (borg og fjölda)

import string

def OpenFile(file_name):
    '''Opnar skrá, ef skrá er ekki til þá stoppar forritið með skilaboðum. '''
    try:
        file_object = open(file_name, "r")

        return file_object
    except FileNotFoundError:
        print("Filename "+file_name+" not found!")
    return False


# Fáum inn skrárnafn.
file_name = input("Enter name of file: ")
file_object = OpenFile(file_name)

if file_object != False:
    file_list = []
    for line in file_object:
        file_list = [line]
        print(file_list)

    file_object.close()
