import os
import shutil

path = os.path.expanduser("~/Desktop")

subdirs = filter(os.path.isdir, [os.path.join(path,x) for x in os.listdir(path)])
folder_list = list()
file_list = list()

for folderpath in subdirs:
	folder_list.append(folderpath)

print("Folders List: ", folder_list)


file_paths = filter(os.path.isfile,[os.path.join(path,x) for x in os.listdir(path)])
for f in file_paths:
	file_list.append( f )
	
print("Files List: ", file_list)
list = file_list

def file_extension(path): 
	return os.path.splitext(path)[1] 

def getGroupsDict(Files):
	key_dict = {}
	for file in Files:
		key_dict[file_extension(file)] = []
	for file in Files:
		key_dict[file_extension(file)].append(file)
	return key_dict
	
dict = getGroupsDict(list)
print("dict",dict)

for key,value in dict.items():
	Key = key.upper()
	try:
		os.mkdir(path+'/'+Key)
	except:
		pass
for key,value in dict.items():
	for file in dict[key]:
		try:
			shutil.move(file,path+'/'+key.upper()) 
		except:
			pass
		

