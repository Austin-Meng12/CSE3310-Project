'''
title: Search and Sort Superheros
author: Austin Meng
date: 2023 - 02 - 23
'''

def getRawData(fileName):
	import csv
	tempLi = []
	fil = open(fileName)
	text = csv.reader(fil)
	for line in text:
		tempLi.append(line)
	var = tempLi.pop(0)
	return tempLi, var

rawArr, headers = getRawData('comicBookCharData_mixed.csv')

# rawArr is a 2D arrays holding all the Superhero data
# headers is a variable that holds the List of all the column headers.

# Using insertion sort as my sorting program
def insertSort(LIST):
	"""
	    takes the lowest value in the unsorted half of the list and
	    inserts it into the relative position within the sorted list
	    :param LIST:
	    :return:
	    """
	for i in range(1, len(LIST)):
		INDEX_VALUE = LIST[i]  # saving the VALUE of the lowest index in the unsorted section of the list
		SORTED_INDEX = i - 1  # identify the largest index of the sorted section of the list

		while SORTED_INDEX >= 0 and INDEX_VALUE < LIST[SORTED_INDEX]:
			# while traversing tail-to-head in the sorted section
			LIST[SORTED_INDEX + 1] = LIST[SORTED_INDEX]
			# overwrite the right value
			SORTED_INDEX = SORTED_INDEX - 1  # move one to the left
		# STOP when SORTED_INDEX reaches 0 or the LIST[SORTED_INDEX] is smaller than the INDEX_VALUE

		LIST[SORTED_INDEX + 1] = INDEX_VALUE  # Replace the SORTED INDEX position with the INDEX VALUE
	# NOTE: One is added to the SORTED_INDEX to adjust for the minus one at the end of the while loop.


# Using binary search as my searching program for my iterative part.

def binarySearch(LIST, VALUE):
    """
    :param LIST: List (int)
    :param VALUE: int
    :return: bool
    """

    SMALL_IND = 0
    LARGE_IND = len(LIST) - 1

    while SMALL_IND < LARGE_IND:
        MIDPOINT_IND = (SMALL_IND + LARGE_IND) // 2
        if LIST[MIDPOINT_IND][0] == VALUE:
            return MIDPOINT_IND
        elif VALUE > LIST[MIDPOINT_IND][0]:
            SMALL_IND = MIDPOINT_IND + 1
        else:
                LARGE_IND = MIDPOINT_IND

    return False



# using linear serach to search through the list of names

def namesearch(LIST, VALUE):
	'''

	:param LIST: list(int)
	:param VALUE: int
	:return: index value or false
	'''
	for i in range(len(LIST)):
		if LIST[i][1] == VALUE:
			return i
			break
	else:
		return False
def namelower():
	'''

	:return: name with lower case letters (the names within rawarr all have lower case)
	'''

	# changes every name within the superhero list to have lower case
	# letters instead of the first letter of the first name and last name having upper.
	for i in range(len(rawArr)):
		rawArr[i][1] = rawArr[i][1].lower()
# getting the value you entered for your superhero ID
def Getname():  #user enters the name they want to find
	'''

	:return: name with lowe case letters
	'''
	NAMEID = str(input("What is your superhero Name:"))
	return NAMEID.lower()
def getID(SUPERHERO):
	'''
	making the first letter a capital
	:param SUPERHERO: string
	:return: the string but with the first letter capatalized
	'''

	# getting the input value of your function
	if len(SUPERHERO) == 3:  # Check if the length of the ID is 3, where 1 of the zeros is missing
		SUPERHERO = SUPERHERO[0] + "0" + SUPERHERO[1:]

	elif len(SUPERHERO) == 2: # Check if the length of the ID is 2, where 2 of zeros are missing
		SUPERHERO = SUPERHERO[0] + "0" + "0" + SUPERHERO[1:]

	return SUPERHERO.upper()  # returns the ID, but with the First letter an uppercase (just in case you entered the M or D a lower case)


def askID():
	# Asking the user what their ID is
	ID = input("WHAT IS YOUR SUPERHERO ID: ")
	return ID


# printing the superheros data
def SuperheroPrint(MIDPOINT):
	if MIDPOINT == False:
		return print("Invalid Input")
	else:

		print(f"""SUPERHERO ID: {rawArr[MIDPOINT][0]}
name: {rawArr[MIDPOINT][1]}
ID: {rawArr[MIDPOINT][2]}
ALIGN: {rawArr[MIDPOINT][3]}
EYE: {rawArr[MIDPOINT][4]}
HAIR: {rawArr[MIDPOINT][5]}
ALIVE: {rawArr[MIDPOINT][6]}
APPEARANCES: {rawArr[MIDPOINT][7]}
FIRST APPEARANCE: {rawArr[MIDPOINT][8]}
YEAR: {rawArr[MIDPOINT][9]}
brand: {rawArr[MIDPOINT][10]}""")
# start menu
def menu():
	print("WELCOME TO SUPERHERO SEARCH")
	print('''1. ENTER your SUPERHERO ID
2. Search by Superhero Name
3. EXIT ''')
	Selection = int(input("Enter your selection:"))
	if Selection == 1:    # My search for the superhero ID
		HERO = askID()
		ID = getID(HERO)
		BSEARCH  = binarySearch(rawArr, ID)
		SuperheroPrint(BSEARCH)
		searchagain()
	elif Selection == 2:   # search for the superhero name
		namelower()
		NAME  = Getname()
		namelower()
		OUTPUT = namesearch(rawArr,NAME)
		SuperheroPrint(OUTPUT)
		searchagain()
	else:
		exit()

def searchagain(): # Used to ask the user if they want to use the function again
	Selection1  = int(input("Do you want to search again (ENTER 1 to continue and 2 to exit): "))

	if Selection1 == 1:
		menu()
	else:
		exit()

# Filtering between Marvel and DC



# printing my data
if __name__ == "__main__":
	rawArr, headers = getRawData('comicBookCharData_mixed.csv')
	insertSort(rawArr)
	menu()







































