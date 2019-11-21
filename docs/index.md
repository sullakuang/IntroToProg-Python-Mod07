# Working with Pickling and Error Handling Script
**Dev:** *QKuang*  
**Date:** *11.20.2019*
## Introduction
In this Assignment, I will go over how I use pickle to save and load data in a binary format. I will also go over how I conduct error handling in this program. I learned how to create custom Exception class.
## Process Performing
### Created new Folder and new file
First, I created a new folder called “Assignment07” and added the file called “Assignment07.py” into the “Assignment07” folder.
### Working with Pickling
#### Step one
First, I import pickle through command in the following (Listing 01).
```
# ------------------------------------------------- #
# Title: Listing 01
# Description: importing pickle
# ChangeLog: (Who, When, What)
# QKuang,11.20.2019,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!
```
##### Listing 01
#### Step two
Then, I write a custom function to save the data to a file with a binary format. I use pickle to dump the data object to the file object. Meanwhile, I write another custom function to read data from a file, and in this function, I use pickle to load the data object from the file object. That’s two main methods of pickle (https://pythontips.com/2013/08/02/what-is-pickle-in-python/
).  When I open the file, I also specify the mode as ‘ab’ and ‘rb’, and then I could save and read the data as a binary file. The following code is my custom functions to use pickle.dump method and pickle.load method (Listing 02).

```
# ------------------------------------------------- #
# Title: Listing 02
# Description: Using pickle to dump and load data
# ChangeLog: (Who, When, What)
# QKuang,11.20.2019,Created Script
# ------------------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, 'ab')
    pickle.dump(list_of_data, objFile)
    objFile.close()

def read_data_from_file(file_name):
    objFile = open(file_name, 'rb')
    objFileData = pickle.load(objFile)
    objFile.close()
    print(objFileData)
```
##### Listing 02
#### Step three
Then, I write the processing code which I could get the ID and name from the user, and use the two custom functions to save and read the data (Listing 03).
```
# ------------------------------------------------- #
# Title: Listing 03
# Description: Store and save data
# ChangeLog: (Who, When, What)
# QKuang,11.20.2019,Created Script
# ------------------------------------------------- #

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
```
##### Listing 03
### Working with Error Handling
At those three steps, I need to deal with some errors which might be caused by the user. Thus, I used Try-Except to handle those bugs.

In step one, I add a Try-Except to deal with the condition which the user input incorrect ID number instead of letting python show error to the user, for example, some user might type float number by mistake, then it would tell the user that he/she should input integer number here(Listing 04). 
```
# ------------------------------------------------- #
# Title: Listing 04
# Description: Error handling with integer ID number
# ChangeLog: (Who, When, What)
# QKuang,11.20.2019,Created Script
# ------------------------------------------------- #
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
```
#### Listing 04
In step two, If the user does not have the permission to edit the file, thus he/she would not save their new data to the file, and thus I use another Try-Except block of code (Listing 05).
```
# ------------------------------------------------- #
# Title: Listing 05
# Description: Error handling with permission of the file
# ChangeLog: (Who, When, What)
# QKuang,11.20.2019,Created Script
# ------------------------------------------------- #
try:
    objFile = open('AppData.dat', 'ab')
    pickle.dump(lstCustomer, objFile)
    objFile.close()

except Exception as e:
    print("There was an error! Try to get the permission of the file. << Custom Message")
    print(e, e.__doc__, type(e), sep='\n')
```
#### Listing 05
In step three, I create a custom Exception class which is called “FileNotDatError” to block if the user reading the file which is not “dat” format. Meanwhile, I also use Exception class to block if the file is not existed (Lising 06).
```
# ------------------------------------------------- #
# Title: Listing 06
# Description: Error handling when reading data from the file
# ChangeLog: (Who, When, What)
# QKuang,11.20.2019,Created Script
# ------------------------------------------------- #
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
```
#### Listing 06
### Running Script in PyCharm and Terminal
Then, I run the script in PyCharm and Terminal(Figure 01).
![A screenshot of running script](https://github.com/sullakuang/IntroToProg-Python-Mod07/blob/master/docs/Picture%2001.png "A screenshot of running script")
#### Figure 01. A screenshot of running script
### Verify the data 
Next, I opened the folder and checked that the data is saved in the file(Figure 02).
![Verify the data](https://github.com/sullakuang/IntroToProg-Python-Mod07/blob/master/docs/Picture%2002.png "Verify the data")
#### Figure 02. Verify the data
### Create github repository
Finally, I upload all of my assignment work in my github website(Figure 03).
![Assignment uploading on the github](https://github.com/sullakuang/IntroToProg-Python-Mod07/blob/master/docs/Picture%2003.png "Assignment uploading on the github")
#### Figure 03. Assignment uploading on the github
## Summary
In this assignment, I have learned how to use pickle to dump and load data, and also how to use Try-Except to handling with errors.
