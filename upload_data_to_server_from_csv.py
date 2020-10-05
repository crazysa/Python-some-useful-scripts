import csv
import pyodbc

server = #servername inside ''
database = #database name inside ''
username = #username  inside ''
password = #password inside ''
driver= #servername inside '{ }'

reader = csv.DictReader(open("csv_name.csv"))
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
count = 0
for raw in reader:
   
    cursor.execute ("sql query" )
	
            
    conn.commit()
        


    
conn.close()

