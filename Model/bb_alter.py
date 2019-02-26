import os
import os.path
import xml.etree.ElementTree as ET

def vertical_flip(directory):

	for f_name in os.listdir(directory):

		name, extension = f_name.split(".", 1)

		path = directory + "/" + f_name

		tree = ET.parse(path)
		root = tree.getroot()

		height = int(root.find("size").find("height").text)
		width = int(root.find("size").find("width").text)

		for object in root.findall('object'):

			bound_box = object.find('bndbox')
			bound_box.find('xmin').text = str(width - int(bound_box.find('xmin').text))
			bound_box.find('xmax').text = str(width - int(bound_box.find('xmax').text))

		tree.write("flipped/" + name + "(v_flip).xml")


def main():
	
	vertical_flip("xml")

main()