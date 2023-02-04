import mysql.connector
import ffmpeg

mydb = mysql.connector.connect(
    host = "localhost",
    database = "tute"
)

print(mydb)
cursor = mydb.cursor()
#cursor.execute("CREATE DATABASE tute;")
#cursor.execute("

 
for x in cursor:
  print(x)

""" 
input_video = ffmpeg.input("D:/Coding/Tute/tute/video/test.mp4")

input_audio = ffmpeg.input("D:/Coding/Tute/tute/video/test.mp3")

ffmpeg.concat(input_video, input_audio, v=1, a=1).output("output.mp4").run()
 """