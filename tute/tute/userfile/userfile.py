"""
TO DO
	*f*
	- file fetch from frontend form (using flask)
		- text file
		- video file
	*f*
	uploadUserFile.py
		- file upload to google drive
		- generate/ store ID for the userID, txt and mp4 instance
		- insert the three valued ID tuple to userdata table
	- access file using ID (key = user ID)
		transcriptToAudioConverter.py
			- create audio from transcript 
		audioVideoMerger.py
			- merge audio and video
			- output file upload to google drive
			- generate/ store ID for output video
			- use flask to pass it to frontend
	*f*
	- render video to user on frontend.
	*f*
	- flush user data
"""

import pymysql
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def IDupload():
    conn = pymysql.connect(
        host='localhost',
        user='TUTE', 
        password = "pwd",
		db = 'tute'
        )
    cur = conn.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()
    print(output)
    conn.close()


def fileUpload():
	gauth = GoogleAuth()           
	drive = GoogleDrive(gauth)
	files = ["D:/Coding/Tute/tute/tute/userfile/test.txt"]
	for upload_file in files:
		gfile = drive.CreateFile({'parents': [{'id': '17SP1SxYaZNuQtAduw_AmTgpBqcYOUNdy'}]})
		gfile.SetContentFile(upload_file)
		gfile.Upload()

	file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('17SP1SxYaZNuQtAduw_AmTgpBqcYOUNdy')}).GetList()
	for file in file_list:
		print('title: %s, id: %s' % (file['title'], file['id']))

if __name__ == "__main__" :
    IDupload()




"""
for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
	print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
	file.GetContentFile(file['title'])


file1 = drive.CreateFile({'id': file['id']})
file1.GetContentString('test.txt')
"""

