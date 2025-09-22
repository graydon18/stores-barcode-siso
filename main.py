import time

currEmp = ""
currTool = None
checkoutState = False

while True:    
    print("Hello, welcome to the OS equipment SISO system")
    currEmp, currTool = getInputs()
    checkoutState = setSISOState()
    if checkoutState:
        checkOutTool(currEmp, currTool)
    else:
        checkInTool(currEmp, currTool)
    time.sleep(3)
