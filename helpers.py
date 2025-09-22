from tool import Tool
from workbook import ws

def findTool(tool):
    for row in ws.iter_rows(min_row = 2):
        cell = row[0]
        if cell.value == tool:
            return Tool(row[0].value, row[1].value, row[2].value, row[3].value, cell.row) 
    return None
    
def getInputs():
    scan1 = str(input('Please enter your employee email (not including @onshipyards.com): '))
    emp = scan1 + "@onshipyards.com"

    scan2 = str(input('Please scan the tool barcode: '))
    tool = findTool(scan2)
    
    while tool is None:
        scan2 = str(input('Sorry, that barcode is invalid. Please try again: '))
        tool = findTool(scan2)
    
    return emp, tool