# Please enter the directory in line 14(in place of "./niki/")
# The code will print the phone numbers which have 10 digits and start with 9 , 8 or 7 only(as per the Indian format).

# System Libraries
import os

# Function Definitions
def is_indian(t):
    return ((t[0]=='9' or t[0]=='8' or t[0]=='7') and len(t)==10 and t.isdigit())


print("Displaying all the phone numbers ")

for directory_path, directories, filename in os.walk("./niki/"):
    #print(filename)
    #print directory_path
    for f in filename:
        file_path = os.path.join(directory_path,f)
        fl = file(file_path).read()
        for t in fl.split():
            if is_indian(t):
                print t
