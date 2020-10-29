# -*- coding: utf-8 -*- 
from PlaceHoldMachine import PlaceHoldMachine #import class

i = PlaceHoldMachine() #create class instance
i.log_level = 2 #set log level to 2, so we can see errors

# set directories list, where all images will be replaced with placeholders
dirs = [
	'D:/Others Project/placeholdermaker/phd'
]

i.emulate_csshopper_placeholder() #emulate csshopper placeholder service
i.walk_recursive(dirs) #recursively find all images in given directories
i.start() #begin conversion process