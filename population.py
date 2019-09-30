import string
def InputFromUser():
    '''Takes input from user'''
    file_name = input("Enter name of file: ")
    return file_name

def OpenFile(file_name):
    '''Opnar skrá, ef skrá er ekki til þá stoppar forritið með skilaboðum. '''
    try:
        file_object = open(file_name, "r")

        return file_object
    except FileNotFoundError:
        print("Filename "+file_name+" not found!")
    return False

def MakeList(file_object):
    '''Make a list of lines in file, takes out whitespace (exept the first) and taps'''
    file_list = [line.replace(" ", "", 1).strip() for line in file_object]
    return file_list

def main():
# Fáum inn skrárnafn.
    file_name = InputFromUser()
    file_object = OpenFile(file_name)
    file_list = MakeList(file_object)
    
    file_object.close()

#call the main function to run the program
main() 

