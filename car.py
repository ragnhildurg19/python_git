# DESCRIPTION
# Skrifið Python forrit, car_sensors.py, sem biður um nafn skrár til að lesa, t.d. 'data.txt', sem inniheldur mælingar frá skynjurum sem staðsettir eru í nýlegum rafbíl.
# Hver lína í skránni táknar nýjustu mælingar frá skynjurunum.

# Í bílnum eru staðsettir 5 skynjarar sem skrá gögn í skránna; 4 fjarlægðarmælar (einn á hverri hlið bílsins), og svo úrkomumælir.

# Hver fjarlægðarmælir hefur sitt auðkenni, og skrifar gögn á stöðluðu formi.

# Skynjarinn að framan hefur auðkennið "SF", skynjarinn að aftan hefur auðkennið "SB", skynjari á vistri hlið hefur auðkennið "SL" og skynjarinn á hægri hlið hefur auðkennið "SR".
# Fjarlægðarskynjararnir skrifa gögn á eftirfarandi formi:
# [Auðkenni]:[Fjarlægð í metrum].
# Dæmi: SF:100 táknar að að séu 100m í næstu fyrirstöðu fyrir framan.
# Ef engin fyrirstaða mælist, þá er skrifað -1, t.d. SF:-1.

# Úrkomumælirinn hefur eftirfarandi uppbyggingu skeytis:
# P:[Magn úrkomu], þar sem magn úrkomu er táknað með NONE, MIST, DRIZZLE, eða RAIN.

# Forritið skal:

# Lesa mæligildin úr skránni og halda utan um stöðu allra skynjara á hverjum tímapunkti.
# Skrifa út villumeldingu ef skráin finnst ekki.
# Sannreyna að uppbygging skeyta sé rétt, annars prenta út villuskilaboð í úttakinu.
# Prenta út hverja mælingu sem er lesin sem upplýsingaskilaboð í úttakinu.
# Prenta út stöðu skynjarana í lok keyrslu.
# Einungis má nota það efni sem búið er að fara yfir í bókinni í lausninni sem er skilað.
# Hafið í huga yfirferðalyklana sem hafa verið gefnir út á canvas.


def open_file(filename):
    ''' Opens file and checks if that file exicts '''
    try:
        file_object = open(filename, "r")

        return file_object
    except FileNotFoundError:
        print("File '{}' not found!".format(filename))
        return False


def read_lint(filename):
    '''Reads each line of the object '''
    file_object = filename.readlines()
    return file_object

def split_line(filename):
    ''' Splitst the lines '''
    for line in filename:
        new_line = line.strip().split(";")

        for index in new_line:
            index1, index2 = index.split(":")
            if index1 == "P" and (index2 == "NONE" or index2 == "MIST" or index2 == "DRIZZLE" or index2 == "RAIN" or index2.isdigit):
                print_line(index1, index2) # Calling the print line function
            elif index1 == "SF" or index1 == "SB" or index1 == "SL" or index1 == "SR": 
                if index2.isdigit() or index2.isalpha() == False:
                    print_line(index1, index2) # Calling the print line function
                else:
                    print_error(index1, index2)
            else:
                print_error(index1, index2)

    return new_line

def print_line(x, y):
    ''' Print out every line '''
    print("Info: Parsed part: {:<2} with value: {}".format(x, y))
    
def print_error(x, y):
    ''' Print out if there is an error in the line '''
    print("Error: Failed to parse part '{}:{}'".format(x, y))

def last_line(new_line):
    emt_str = ""
    for index in new_line:
        print(new_line)
        index1, index2 = index.split(":")
        emt_str += index2 + ":"
        emt_something = emt_str.split(":")
    print(emt_something)
    return emt_something

def print_last_line(new_line):
    ''' Print last line '''
 
    print()
    print("------ CURRENT STATE ------")
    print('{:<20}{:>4}.0m'.format("FRONT:", new_line[0])) # þetta þarf líka að prentast út sem FLOAT
    print('{:<20}{:>4}.0m'.format("BACK:", new_line[1])) # þetta þarf líka að prentast út sem FLOAT
    print('{:<20}{:>4}.0m'.format("LEFT:", new_line[3])) # þetta þarf líka að prentast út sem FLOAT
    print('{:<20}{:>6}m'.format("RIGHT:", new_line[2])) # þetta þarf líka að prentast út sem FLOAT
    print('{:<20}{:>7}'.format("PRECIPITATION:", new_line[4]))

# Main program starts here

filename = input("Enter name of file: ")
file_object = open_file(filename)
if file_object != False:

    file_line = read_lint(file_object)
    one_line = split_line(file_line)
    some_str = last_line(one_line)
    print_last_line(some_str)
    file_object.close()
