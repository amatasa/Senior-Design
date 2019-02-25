import os
import os.path

"""
	Folder Structure should be the following...
	
	Images/
	|-- train/
	|	|-- train_1.jpg
	|	|-- train_1.csv
	|	|-- ...
	|-- test/
	|	|-- test_1.jpg
	|	|-- test_2.csv
	|	|-- ...
	|-- remove_unused_images.py
	
"""

def remove_unused_images(directory):

	for f_name in os.listdir(directory):

		remove_classes_file(directory)

		name, extension = f_name.split(".", 1)
	
		image_file = directory + "/" + name + ".jpg"
		xml_file = directory + "/" + name + ".xml"

		if (os.path.exists(image_file) and os.path.exists(xml_file)):
			pass
		else:
			os.remove(image_file)

	print("Removed images without corresponding xml file from " + 
		directory + " directory")


def remove_classes_file(directory):

	class_file = directory + "/classes.txt"

	if(os.path.exists(class_file)):
		os.remove(class_file)


def main():

	train_dir = "train"
	test_dir = "test"

	remove_unused_images(train_dir)
	remove_unused_images(test_dir)

main()

