import os 
import re 
import csv

setOfFunctions = {}


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def search_image(img1, img2, waitTime):
	print "search image"
	#if(img2):
		#find(img1)
	#	wait(waitTime)
		#find(img2)
	#else:
		#find(img1)

def wait(inWait):
	print inWait + ' wait'	


def click(inClick):
	print inClick + ' click'


def typekeys(inKey):
	print inKey + ' type keys'


def typekeycombo(inKeyCombo):	
	print inKeyCombo + ' type key combo'


def sleep(inSleep):
	print inSleep + ' sleep'

def checksuccess(inSuccessMessage):
	print inSuccessMessage + ' success!'
	
def run_function(inFunction, inValue):
	#the following functions need to be made here: 
	#TypeKeys, TypeKeyCombo, Sleep, CheckSuccess
	print "run_function called|arguement passed|inFunction"+str(inFunction)
	print "run_function called|arguement passed|inFunction"+str(inValue)
	if(inFunction == 'typekeys'):
		print "calling typekeys function"
		typekeys(inValue)
	elif(inFunction == 'sleep'):
		print "calling sleep function"
		sleep(inValue)
	elif(inFunction == 'typekeycombo'):
		print "calling typkeycombo function"
		typekeycombo(inValue)
	elif(inFunction == 'wait'):
		print "calling wait function"
		wait(inValue)
	elif(inFunction == 'sleep'):
		print "calling sleep function"
		sleep(inValue)
	elif(inFunction == 'checksuccess'):
		print "calling checksuccess function"
		checksuccess(inValue)
	else:
		print "instruction not defined in function titled: run_function"
	
	
def run_test_step(funcName, funcVal, logEntry, errorEntry):
	#this is where we start using sikuli code
	funcName = funcName.lower()
	#make log entry here
	#make error log entry here too
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
		
tests_dir = "/Users\/f002nx3/Documents/GitHub/gobblegobblegobble/windows_application_test_tool.sikuli\/application_tests/"

#find each testfile.csv and execute 
for test_folder in os.listdir(tests_dir):	

	test_file = test_folder + ".csv"
	test_dir = tests_dir + test_folder
	test_file = test_dir + "/" + test_file
	
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