import openpyxl
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="bible"
)
 
mycursor = mydb.cursor()
sql = "INSERT INTO BibleData (Book, Chapter, Verse, Scripture) VALUES (%s, %s, %s, %s)"


# Define variable to load the dataframe
dataframe = openpyxl.load_workbook("kjv.xlsx")
 
# Define variable to read sheet
sheet = dataframe.active

headers = [cell.value for cell in sheet[1]]

def save_to_db(row):
    mycursor.execute(sql, row)

for i in range(2, sheet.max_row+1):
    row = [cell.value for cell in sheet[i]] # sheet[n] gives nth row (list of cells)
    save_to_db(row)

mydb.commit()
    

 