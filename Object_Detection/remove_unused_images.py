import os
import os.path

train_dir = 'train'
test_dir = 'test' 

for f_name in os.listdir(train_dir):

	name, extension = f_name.split(".", 1)
	
	image_file = train_dir + "/" + name + ".jpg"
	xml_file = train_dir + "/" + name + ".xml"

	if (os.path.exists(image_file) and os.path.exists(xml_file)):
		pass
	else:
		os.remove(image_file)	


for f_name in os.listdir(test_dir):

	name, extension = f_name.split(".", 1)
	
	image_file = test_dir + "/" + name + ".jpg"
	xml_file = test_dir + "/" + name + ".xml"

	if (os.path.exists(image_file) and os.path.exists(xml_file)):
		pass
	else:
		os.remove(image_file)

print("Removed images without corresponding xml file from " + train_dir + " directory")
print("Removed images without corresponding xml file from " + test_dir + " directory")