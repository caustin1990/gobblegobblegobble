import os 
import re 
import csv
import time

setOfFunctions = {}
"""
Global Variables
"""
base_dir = 	'C:\Users\\f002nx3\Documents\GitHub\gobblegobblegobble\simple_test.sikuli'
current_test_dir = ''
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
	
def prependImageURL(inImg):
	inImg = current_test_dir + '\\target_images\\' + inImg
	return inImg

def search_image(img1, img2, waitTime):
	img1_path = prependImageURL(img1)
	img2_path = prependImageURL(img2)
	print "in search image function"
	if(img1): print "image one exists" + img1
	if(waitTime): print "this is your wait time" + waitTime
	if(img2): print "image two exists" + img2	
	try:
		#find(img1_path)
		find(img1_path, waitTime)
	except FindFailed:
		print "there's something happening here"
	#if(img2):
		#find(img1)
	#	wait(waitTime)
		#find(img2)
	#else:
		#find(img1)

def wait(inWait):
	print inWait + ' wait'	


def click(inClickImage):
	inClickImage = prependImageURL(inClickImage)
	print 'we are totally clicking this image'
	
	click(inClickImage)
	print 'we must have totally clicked this image'
	print inClickImage + ' click'


def typekeys(inKey):
	print inKey + ' type keys'


def typekeycombo(inKeyCombo):	
	print inKeyCombo + ' type key combo'


def sikuli_sleep(inSleep):
	time.sleep(int(inSleep))
	print 'this is that sleep thang you were thinking about'
	#time.sleep(inSleep)

def checksuccess(inSuccessMessage):
	print inSuccessMessage + ' success!'
	
def run_function(inFunction, inValue):
	#the following functions need to be made here: 
	#TypeKeys, TypeKeyCombo, Sleep, CheckSuccess
	print "run_function | function called -> "+str(inFunction)
	print "run_function | value passed in -> "+str(inValue)
	if(inFunction == 'typekeys'):
		print "calling typekeys function"
		typekeys(inValue)
	elif(inFunction == 'sleep'):
		print "calling sleep function"
		print "VALUE | " + inValue
		print "TYPE  | " + inValue
		sikuli_sleep(inValue)
	elif(inFunction == 'typekeycombo'):
		print "calling typkeycombo function"
		typekeycombo(inValue)
	elif(inFunction == 'wait'):
		print "calling wait function"
		wait(inValue)
	elif(inFunction == 'checksuccess'):
		print "calling checksuccess function"
		checksuccess(inValue)
	else:
		print "instruction not defined in function titled: run_function"
	
	
def run_test_step(funcName, funcVal, logEntry, errorEntry):
	#this is where we start using sikuli code
	funcName = funcName.lower()
	#TODO:make log entry here
	#TODO:make error log entry here too
	#TOTO:make error handling try catch statement
	run_function(funcName, funcVal)


#execute through application specific instructions from list
def run_test(instructions_from_file):
	for instruction in instructions_from_file:
		#if there is an image to search for
		#translate array element to variable
		comment = instruction[0] #goes to log file
		failure = instruction[1] #if failed write this to log
		image1 = instruction[2] #first image to search for
		waitTime = instruction[3] #time to wait for image to appear
		image2 = instruction[4] #second image to search for, optional
		functionToCall = instruction[5] #function to be called
		args = instruction[6] #argument(s) for function
		
		if(image1):
			print "calling search_image"
			search_image(image1,image2,waitTime)
		print "calling run_test_step"
		run_test_step(functionToCall,args,comment,failure)

		
	

tests_dir = base_dir + '\\application_tests'
#find each testfile.csv and execute 
for test_folder in os.listdir(tests_dir):	

	test_file = test_folder + ".csv"
	test_dir = tests_dir + "\\" + test_folder
	global current_test_dir 
	current_test_dir 	= test_dir
	test_file = test_dir + "\\" + test_file
	print test_file
	print str(os.path.isdir(test_dir))
	#find test files in test folder exclude OSX's .DS_Store file
	if(os.path.isdir(test_dir) and not re.match("\.DS_Store", test_dir)): 
		#the test folder and file have the same name
		#get test parameters
		try:
			instructions = []
			with open(test_file, "r") as file:
				test_file_csv_read = csv.reader(file, delimiter=',')
				for row in test_file_csv_read:
					instructions.append(row)
			run_test(instructions)
		except ValueError:
			print ValueError
			print 'test failed, onto the next one'