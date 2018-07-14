"""
Author: CHIRAG SHAH
Created On: 7th July 2018
Modified On: 14th July 2018
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mimg

def get_path():
	"""
	Helper utility to get the base paths
	"""
	
	P = str(Path().resolve().parent)
	CLASS_DIAGRAM_PATH = P + "\\diagrams\\"
	CODE_RESULT_PATH = P + "\\results\\"
	return CLASS_DIAGRAM_PATH, CODE_RESULT_PATH

def class_diagram(name):
	"""
	Get class diagram for specific class pattern
	
	@params: name of class diagram
	"""

	NAME = name
	BASE_PATH, _ = get_path()
	PATH = BASE_PATH + NAME

	diagram = mimg.imread(PATH)
	plt.axis('off')
	plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
	plt.suptitle(NAME.split('.')[0], fontsize = 18)
	result = plt.imshow(diagram)
	return result

def output_image(name):
	"""
	Get output image for specific class pattern

	@params: name of output image
	"""

	NAME = name
	_, BASE_PATH = get_path()
	PATH = BASE_PATH + NAME

	diagram = mimg.imread(PATH)
	plt.axis('off')
	plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
	plt.suptitle(NAME.split('.')[0], fontsize = 18)
	result = plt.imshow(diagram)
	return result