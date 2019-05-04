import os
import re

folders = os.listdir('./bbc')
for folder in folders:
	path = './bbc/'+str(folder)
	if(os.path.isdir(path)):
		files = os.listdir(path)
		for file in files:
			file_item = open(path+'/'+file)
			content = file_item.read()
			ans = re.findall(r"[A-Z]+[a-z]+(?: |\-)[A-Z]+[a-z]+",content)
			for item in ans:
				print(item)
