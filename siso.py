def setSISOState():
    choice = str(input('Please enter A for signing out equipment, or B for signing back in: '))
    while not (choice == "A" or choice == "B"):
        choice = str(input('Sorry, that is invald. Please try again: '))

    return choice == "A"


def checkOutTool(currEmp, currTool):
    if not currTool.taken:
        currTool.checkOut(currEmp)
        print("You've checked out " + currTool.name + ". Please return it at the end of the day.")
    else:
        print("This has already been checked out by: " + currTool.email)
        choice = str(input('If you would like to take overwrite this sign out, enter A. Otherwise, enter any key and please return the equipment to its current user: '))
        if choice == "A":
            currTool.checkOut(currEmp)
            print("You've checked out " + currTool.name + "! Please return it at the end of the day.")

def checkInTool(currEmp, currTool):
    if currTool.taken:
        currTool.checkIn()
        print("You've returned " + currTool.name + ". Thank you very much!")
    else:
        print("This tool was never checked out to begin with. Please return it and ensure you're checking out all tools you take for the day.")