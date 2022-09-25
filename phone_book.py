import time


def lookUp(phoneBook):
    teleNum = input("Enter the telephone number you want to find:")
    extNum = extNumConverter(teleNum)
    name = phoneBook.get(extNum)
    # name is returned through the phoneBook object's method
   
    if name == None:
        # if name doesn't exist then the number doesn't
        print("This phone number is not on the phone book")
    else:
        # else output who the telephone number belongs to
        print(f"{teleNum} belongs to {name}")
    return phoneBook

def extNumConverter(teleNum):
    # converts a whole telephone number into an extension number by taking the last two digits
    # Then converts these 2 digits into an integer
    extNum = teleNum[-2:]
    return int(extNum)
       
def addNew(phoneBook):
    name = input("Enter the name you want to add:")
    teleNum = input("Enter the telephone number you want to add:")
    extNum = extNumConverter(teleNum)
    phoneBook[extNum] = name
    # Adds the new number with the new name to the dictionary
    return phoneBook

def edit(phoneBook):
    teleNum = input("Enter the telephone number you want to edit:")
    newNum = input(f"What would you like to change {teleNum} to:")
    extOldNum = extNumConverter(teleNum)
    extNewNum = extNumConverter(newNum)
    phoneBook[extNewNum] = phoneBook[extOldNum]
    # The new number takes the name value of the old number
    del phoneBook[extOldNum]
    # Deletes the old number entry from the dictionary
    return phoneBook

def delete(phoneBook):
    teleNum = input("Which number would you like to delete:")
    extNum = extNumConverter(teleNum)
    del phoneBook[extNum]
    # Finds and deletes the number from the dictionary
    return phoneBook

def output(phoneBook):
    sorted_names = sorted(phoneBook.values())
    # Sorts the names alphabetically (default)
    keys = list(phoneBook.keys())
    # Gets all the keys from the phoneBook object using the keys method and converts this data...
    # type into a list
    sorted_Book = {}
    for i in range(0, len(sorted_names)):
        # For every name in the sorted_names list
        for k in range (0, len(keys)):          
            if phoneBook[keys[k]] == sorted_names[i]:
                # For every key in the phoneBook
                sorted_Book[keys[k]] = phoneBook[keys[k]]
                # If phoneBook value associated with the key is the same as the sorted name (which is being looped through in order),
                # then the sorted book has this value and key added to it, thus sorting the dictionary in
                # alphabetical order.
    for i in sorted_Book:
        # Every key value pair in sorted_Book is outputted
        print(f"Name: {phoneBook[i]:20} Ext number: {i}")
    return phoneBook



def main(phoneBook):
    choices = {
        1 : lookUp,
        2 : addNew,
        3 : edit,
        4 : delete,
        5 : output}
   
    # choices is a dictionary containing functions, much more efficient than using if else statements
    choice = int(input("""1. Look up a telephone number
2. Add a new name and telephone number
3. Edit a telephone number
4. Delete an entry
5. Output directory
6. Quit\n: """))
   
    if choice == 6:
        END = True
        return END
        # If you select the quit option, END is set to True and returned, breaking the while loop
    else:
        phoneBook = choices[choice](phoneBook)
        # The choice selected is used as the key for the choices dictionary...
        # The function from choices then takes in the phoneBook as an argument
        # PhoneBook is then set to what is returned depending on the users choice
        print("\n================RESTARTING================\n")
        time.sleep(1)
        # pauses the program for 1 second to make the output more readable
        END = False
        return END, phoneBook
        # END is set to false and returned, thus meeting the condition of the while loop...
        # allowing it to continue

END = False
phoneBook = {
            44:"zbc",
            55:"bfg"
        }

while END == False:
    END, phoneBook = main(phoneBook)