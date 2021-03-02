from urllib.request import urlopen
from io import StringIO
import csv
import schedule
import time 

import mysql.connector

def update_bd():
	db = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="admin",
		database="testing",
		auth_plugin="mysql_native_password")

	mycursor = db.cursor()
	# eventID int PRIMARY KEY AUTO_INCREMENT,
	# mycursor.execute("CREATE TABLE Eventos (FECHA_INICIO DATE, FECHA_FIN DATE, DURACION_DIAS int UNSIGNED, TIPO_EVENTO VARCHAR(150), ISLA VARCHAR(150), MUNICIPIO VARCHAR(150), DENOMINACION_ESPACIO VARCHAR(150), LUGAR VARCHAR(150), TITULO VARCHAR(150), DESCRIPCION VARCHAR(200), HORA VARCHAR(10), MINUTO VARCHAR(10), MAS_INFO VARCHAR(150) PRIMARY KEY, URL_IMAGEN VARCHAR(150))")
	#FECHA_INICIO DATE, FECHA_FIN DATE, DURACION_DIAS int UNSIGNED, TIPO_EVENTO VARCHAR, ISLA, MUNICIPIO, DENOMINACION_ESPACIO, LUGAR, TITULO, DESCRIPCION, HORA, MINUTO, MAS_INFO, URL_IMAGEN
	data = urlopen("https://datos.canarias.es/catalogos/general/dataset/11dc9d88-b456-4ae2-bcf9-07ad624fd025/resource/d179079c-a2ed-40dc-a748-7b64d093c342/download/agendaproxima.csv").read().decode('utf-8','ignore')
	datafile = StringIO(data)
	csvReader = list(csv.reader(datafile))

	# for row in csvReader:
	# 	print(row)

	for row in csvReader[1:]:
		print(row)
		mycursor.execute("INSERT IGNORE INTO Eventos "
	               "(FECHA_INICIO, FECHA_FIN, DURACION_DIAS, TIPO_EVENTO, ISLA, MUNICIPIO, DENOMINACION_ESPACIO, LUGAR, TITULO, DESCRIPCION, HORA, MINUTO, MAS_INFO, URL_IMAGEN) "
	               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
	# print()
	# mycursor.execute("DESCRIBE Eventos")
	# mycursor.execute("SELECT * from Eventos")

	# for row in mycursor:
	# 	print(row)

	db.commit()
	mycursor.close()
	db.close()

schedule.every().day.at("00:00").do(update_bd)

while True: 
	# Checks whether a scheduled task  
	# is pending to run or not 
	schedule.run_pending() 
	time.sleep(3600) 