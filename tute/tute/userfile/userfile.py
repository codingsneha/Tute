from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)
files = ['test.txt']
for upload_file in files:
	gfile = drive.CreateFile({'parents': [{'id': '17SP1SxYaZNuQtAduw_AmTgpBqcYOUNdy'}]})
	gfile.SetContentFile(upload_file)
	gfile.Upload()