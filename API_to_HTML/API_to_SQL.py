import pyodbc 
import json
import requests

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-XXXXXXX;"
                      "Database=Test;"
                      "Trusted_Connection=yes;")

r = requests.get('https://samples.openweathermap.org/data/2.5/forecast/daily?id=524901&lang=zh_cn&appid=b6907d289e10d714a6e88b30761fae22')

data = r.text
json3 = json.loads(data)
i = 0
query = "INSERT INTO Test.dbo.Weather (DT, DayTemp, LowTemp, HighTemp, NightTemp, EveningTemp, MorningTemp, Pressure, Humidity, WeatherDescription, Speed, Deg, Clouds, Snow)\n VALUES "
while i <= len(json3["list"]) - 1:
    query += "('"
    query += str(json3["list"][i]["dt"]) + "', '"
    query += str(json3["list"][i]["temp"]["day"]) + "', '"
    query += str(json3["list"][i]["temp"]["min"]) + "', '"
    query += str(json3["list"][i]["temp"]["max"]) + "', '"
    query += str(json3["list"][i]["temp"]["night"]) + "', '"
    query += str(json3["list"][i]["temp"]["eve"]) + "', '"
    query += str(json3["list"][i]["temp"]["morn"]) + "', '"
    query += str(json3["list"][i]["pressure"]) + "', '"
    query += str(json3["list"][i]["humidity"]) + "', '"
    query += str(json3["list"][i]["weather"][0]["description"]) + "', '"
    query += str(json3["list"][i]["speed"]) + "', '"
    query += str(json3["list"][i]["deg"]) + "', '"
    query += str(json3["list"][i]["clouds"]) + "', '"
    if "snow" in json3["list"][i]:
        query += str(json3["list"][i]["snow"]) + "'"
    else:
        query += "No Snowfall" + "'"
    if i < len(json3["list"]) - 1:
        query += "), "
    else:
        query += ");"
    i += 1

cursor = cnxn.cursor()
cursor.execute(query)
cnxn.commit()