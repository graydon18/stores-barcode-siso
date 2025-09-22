from workbook import wb, ws

class Tool: 
    def __init__(self, id: str, name: str, taken: bool, email: str, row: int):
        self.id = id
        self.name = name
        self.taken = taken
        self.email = email
        self.row = row
        
    def checkIn(self):
        self.taken = False
        self.email = ""
        ws.cell(row=self.row, column=3, value=self.taken)
        ws.cell(row=self.row, column=4, value=self.email)
        wb.save("EquipmentInventory.xlsx")
    
    def checkOut(self, email):
        self.taken = True
        self.email = email
        ws.cell(row=self.row, column=3, value=self.taken)
        ws.cell(row=self.row, column=4, value=self.email)
        wb.save("EquipmentInventory.xlsx")
