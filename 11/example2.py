from openpyxl import load_workbook

class MgmtExcel:

    def __init__(self, path_to_file):
        self.filename = path_to_file
        self.wb = load_workbook(filename=self.filename)

    def insert_data(self, sheet_name):
        
        #set sheet
        sheet = self.wb[sheet_name]
        info = (
            ('Colombia', '46,30 mi'),
            ('Chile', '18,73 mi')
        )
        for value in info:
            country, population = value
            print(f'adding values {country}/{population} to excel')
            #adding to sheet
            sheet.append((country, population))

        #save excel
        self.wb.save(self.filename)

if __name__ == '__main__':
    
    mgmt = MgmtExcel('11/example.xlsx')
    mgmt.insert_data('Sheet1')


    