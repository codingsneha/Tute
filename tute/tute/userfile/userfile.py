from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
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

for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
	print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
	file.GetContentFile(file['title'])