import pyodbc 
import json
import collections

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-XXXXXXX;"
                      "Database=Test;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Test.dbo.Weather')

rows = cursor.fetchall()

objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['WeatherID'] = row.WeatherID
    d['DayID'] = row.DT
    d['Day Temperature'] = row.DayTemp
    d['Temperature Low'] = row.LowTemp
    d['Temperature High'] = row.HighTemp
    d['Night Temperature'] = row.NightTemp
    d['Evening Temperature'] = row.EveningTemp
    d['Morning Temperature'] = row.MorningTemp
    d['Pressure'] = row.Pressure
    d['Humidity %'] = row.Humidity
    d['Weather Description'] = row.WeatherDescription
    d['Wind Speed'] = row.Speed
    d['Wind Direction'] = row.Deg
    d['Cloudiness %'] = row.Clouds
    d['Snowfall'] = row.Snow
    objects_list.append(d)
j = json.dumps(objects_list)
objects_file = 'SqlWeather.txt'
f = open(objects_file,'w')
print (j, end="", file=f) 
    
cnxn.close()