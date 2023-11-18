import openpyxl

class WriterXL:
    book = openpyxl.Workbook()
    book.save("catalog.xlsx")
    sheet = book.active
    def __init__(self):
        self.sheet["A1"] = "Title company"
        self.sheet["B1"] = "Percent"

    book.save("catalog.xlsx")
    book.close()