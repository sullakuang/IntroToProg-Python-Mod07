# ------------------------------------------------- #
# Title: Assignment07
# Description: Working with Pickling and Error Handling
# ChangeLog: (Who, When, What)
# QKuang,11.20.2019,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, 'ab')
    pickle.dump(list_of_data, objFile)
    objFile.close()

def read_data_from_file(file_name):
    objFile = open(file_name, 'rb')
    objFileData = pickle.load(objFile)
    objFile.close()
    print(objFileData)

# Presentation ------------------------------------ #
# Get ID and NAME From user, then store it in a list object
intID = int(input("Enter your ID here: "))
strFirstName = str(input("Enter your first name here: "))
strLastName = str(input("Enter your last name here: "))
strName = strFirstName + " " + strLastName
lstCustomer = [intID, strName]
print(lstCustomer)

# store the list object into a binary file
Save_data = save_data_to_file(strFileName, lstCustomer)

# Read the data from the file into a new list object and display the contents
Read_data = read_data_from_file(strFileName)

# Error Handling------------------------------------ #

# Get ID and NAME From user, then store it in a list object
try:
    intID = int(input("Enter your ID here: "))
    strFirstName = str(input("Enter your first name here: "))
    strLastName = str(input("Enter your last name here: "))
    strName = strFirstName + " " + strLastName
    lstCustomer = [intID, strName]
    print(lstCustomer)
except Exception as e:
    print("Please enter ID as integer number! <<< Custom Message!\n")
    print(e, e.__doc__, type(e), sep='\n')

# store the list object into a binary file
try:
    objFile = open('AppData.dat', 'ab')
    pickle.dump(lstCustomer, objFile)
    objFile.close()

except Exception as e:
    print("There was an error! Try to get the permission of the file. << Custom Message")
    print(e, e.__doc__, type(e), sep='\n')

# Read the data from the file into a new list object and display the contents
class FileNotDatError(Exception):
    """ File extension must end with dat to indicate it is a dat file """
    def __str__(self):
        return 'File extension not dat'
try:
    file_name = input("Enter the name of the file you want to read: ")
    if file_name.endswith('dat') == False:
        raise FileNotDatError
    objFile = open(file_name, 'rb')
    objFileData = pickle.load(objFile)
    objFile.close()
    print(objFileData)

except FileNotFoundError as e:
    print("The file must exist before running this script!")
    print(e, e.__doc__, type(e), sep='\n')

except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
