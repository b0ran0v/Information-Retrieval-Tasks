import os
import re

files = os.listdir('./data/dev')
for item in files:
	file_item = open('./data/dev/'+item)
	content = file_item.read()
	tags = re.findall(r"(?:([0-9]{3}-[0-9]{3}-[0-9]{4})|([a-z]+@.*\.(?:com|edu)))",content)
	for tag in tags:
		if(tag[0]==''):
			print(tag[1].split('\"')[0].split('>')[0])
		else:
			print(tag[0])
