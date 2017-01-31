# This is for testing the SolidWorks installation
### BEFORE this script executes: test_i_user signs in
                                #mounts server for storage
### Setup necessary reporting environemnt for testing
import os
import datetime
from sikuli import *

#application testing dir
#test_results
#

##file structure for program
SOURCE_DIR = "K:\\\\QnA_Tests\\"
TEST_SCRIPTS_DIR = "K:\\\\QnQ_Test\\applications_to_test\\"
LOGFILES_DIR = "K:\\\\QnA_Tests\\results\\" #filename globallog.csv
#--- TEST SPECIFIC --- 
TEST_FILES_DIR = "K:\\\\QnA_Test\\Test_files\\"
TEST_RESULTS_DIR = "K:\\\\QnA_Test\\Test_results\\"
# AFTER THE HOSTNAME IS KNOWN
SCREENSHOTS_RESULTS_DIR = "K:\\QnA_Tests\\Test_results\\"+hostname+"\\"   
# EXAMPLE FILE: testname.png
# ONLY CREATE THIS DIRECTORY IF NECESSARY
SCREENSHOTS_REQUESTED_DIR = "K:\\QnA_Tests\\Test_results\\"+hostname+"\\"   #---- EXAMPLE FILE: specifiedscreenshot1 < increment the #




TESTNAME = "SolidWorks Graphics" 	### this should be the testname which is pulled from the script name

TARGET_IMAGE_DIR = "K:\\QnQ_Test\\Test_scripts\\script1\\target_images\\"
MAIN_SCRIPT_LOCATION = "K:\\QnQ_Test\\Test_scripts\\main.py"  #----?? What's the file extension for jython
TEST_SCRIPT_LOCATION = "K:\\QnQ_Test\\Test_scripts\\script1\\testname.py"
TARGET_IMAGE_LOCATION = "K:\\QnQ_Test\\Test_scripts\\script1\\script1_images\\"   #--- image1.png, image2.png, image3.png
LOG_DIR = O:\LabOutput\logs\"
LOG_FILE = t2073.txt


TEST_FILENAME = "SolidWorks Graphics" 	### this should be the testname


SNIP_TOOL_DIR = "C:\\Windows\\System32\\SnippingTool.exe"




### Test Utilities Class will contain the following functions
def getTS():    
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st

def createDir(inDir):
    if not os.path.exists(inDir):
        os.makedirs(inDir)
# Creation of Directories for Logging and Screenshots
createDir(LOG_DIR)
createDir(SCREENSHOT_DIR)
logFile = open(LOG_DIR + LOG_FILE, '+a')
def printLog(relevantMessage):
    timeStamp = getTS()    
    toFile = timeStamp + " --- " + TESTNAME + " " + relevantMessage + "\n"
    #temporary print 
    print toFile
    logFile.write(toFile)
def printFFError(relevantMessage):
    timeStamp = getTS() 
    toFile = timeStamp + " --- " + TESTNAME + " " + FFS + " " + relevantMessage + "\n"
    print toFile
    logFile.write(toFile)    


######    Start testing of application    ######
###    Map to network drive
def run():	
	printLog("------------- Beginning " + TESTNAME+ " test -------------" )
	openApp("cmd.exe")
	time.sleep(2)
	##This is going to be place in the master class
	if(exists("1469219620680.png", 5))
		type(SERVER_MAP_CMD + Key.ENTER)
		time.sleep(1)
		type("exit" + Key.ENTER)
	except FindFailed:
		printFFError("Couldn't find CMD window")
	##That is going to be placed in the master class
	
	
	###    Open main testing application(SolidWorks)
	

	#
	#
	#How are we going to specify the main app
	# Ideas: NameOfFile.CSV or first line in the file
	# 							We could use the first line int he file to take in more variables, but hte
	#								file format wouldn't be consistent
	mainApp = App(APP_EXE_DIR)
	mainApp.open()

#######
#######	Custom Testing Comes here
#######	


####### This is something that has a possibility of not appearing, but doesn't
	### negatively affect workflow
	#	logEntry = "Opening command prompt window"
	#	errorMessage = "License Agreement Error"
	#	inImage = "1467383157084.png"
	#	waitTime = 10
	#	areaToClick = "1467383172301.png"
	#
	#
	#  CSV : LogEntry, ErrorMessage, SearchForImage, WaitTimeForImage, SearchForSecondImage
	#		Function1, Function2, Function3, Function4, Function5, Function6
	#
	printLog("Checking for  SolidWorks EULA")
	if(exists(TARGET_IMAGE_DIR + "1467383157084.png", 10)):
	    click("1467383172301.png")
	else:
	    printFFError("Failed to agree to SolidWorks EULA")
#########################################################################################

####### This is something that has a possibility of not appearing, but doesn't
	### negatively affect workflow
	#
	#	logEntry = "Agreeing to EULA"
	#	errorMessage = "Simulation License Agreement, will wait til later in testing"
	#	imageToWaitFor = "1467383203996.png"
	#	waitTime = 10
	#	areaToClick = "1467383218122.png"
	#
	#  CSV : LogEntry, ErrorMessage, SearchForImage, WaitTimeForImage, SearchForSecondImage
	#		Function1, Function2, Function3, Function4, Function5, Function6
	#	
	printLog("Checking for SolidWorks Simulation Agreement")
	if(exists("1467383203996.png",10)):
		click("1467383218122.png")	
	else:
		printFFError("Simulation License Agreement not found")
#########################################################################################	

	#
	#	logEntry = "Waiting for solid works window"
	#	errorMessage = "Solidworks hasn't opened yet"
	#	imageToWaitFor = "1472157259399.png"
	#	waitTime = 30
	#	typeKeyCombo = Key.ALT + "f" + "o"
	#
	#  CSV : LogEntry, ErrorMessage, SearchForImage, WaitTimeForImage, SearchForSecondImage
	#		Function1, Function2, Function3, Function4, Function5, Function6
	#	
	printLog("Waiting for solid works window")	
	if(exists("1472157259399.png", 30)):    
	    type(Key.ALT + "f" + "o")
	else:
	    printFFError("Solidworks hasn't opened") 
#########################################################################################

	#
	#	logEntry = "Opening SolidWorks file"
	#	errorMessage = "Couldn't find open window for solid works"
	#	firstImageToWaitFor = "1471963744703.png"
	#	firstWaitTime = 10
	#	secondImageToWaitFor = "1471973716750.png"
	#	secondWaitTime = 
	#	areaToClick1 =
	#	typeKeyCombo = Key.ALT+d
	#	sleep = 2
	#	typeKeys = SOURCE_DIR + Key.Enter
	#	sleep = 2
	#	typeKeyCombo = Key.ALT+n
	#	typeKeys = FILENAME
	#	typeKeys = Key.ENTER
	#
	#  CSV : LogEntry, ErrorMessage, SearchForImage, WaitTimeForImage, SearchForSecondImage
	#		Function1, Function2, Function3, Function4, Function5, Function6
	#
	printLog("Opening SolidWorks file")	
	if(exists("1471963744703.png", 10)) or (exists("1471973716750.png")):      
			
			type("d", Key.ALT)
			time.sleep(2)
			type(SOURCE_DIR + Key.ENTER) 
			time.sleep(2)
			type("n", Key.ALT)
			type(FILENAME)
			type(Key.ENTER) 
	else:
		printFFError("Couldn't find open window for solid works")
#########################################################################################
	time.sleep(2)
#########################################################################################

	#
	#	logEntry = "Opening in read only mode"
	#	errorMessage = "Couldn't find open in read only mode window for solid works"
	#	firstImageToWaitFor ="1471014557163.png"
	#	firstWaitTime = 10
	#	typeKeys = 
	#
	#  CSV : LogEntry, ErrorMessage, SearchForImage, WaitTimeForImage, SearchForSecondImage
	#		Function1, Function2, Function3, Function4, Function5, Function6
	#

	printLog("Opening in read only mode")
	if(exists("1471014557163.png",10)):	
		type("r", Key.ALT)	
	else:
		printFFError("Couldn't find open in read only mode window for solid works")
#########################################################################################

#########################################################################################

	#
	#	logEntry = "Opened file in SolidWorks"
	#	errorMessage = "Couldn't find open test file"
	#	firstImageToWaitFor ="1472053455435.png"
	#	firstWaitTime = 30
	#	seconImageToWaitFor ="1472060933958.png"
	#	CheckSuccess = True
	#	
	#  CSV : LogEntry, ErrorMessage, SearchForImage, WaitTimeForImage, SearchForSecondImage
	#		Function1, Function2, Function3, Function4, Function5, Function6
	#

	printLog("Opened file in SolidWorks")
	if(exists("1472053455435.png",30) or exists("1472060933958.png")):
		programLoadedSuccessfully = 1
	else:
		printFFError("Couldn't find open test file")

#########################################################################################




#########################################################################################
#
#
#		Taking Screenshot for Results
#
#
#########################################################################################
	if(programLoadedSuccessfully):
		snippingApp = App(SNIP_TOOL_DIR)
		snippingApp.open()
	else:
		printLog("Program did not load successfully")
	
	printLog("Taking screenshot")	
	if(exists("1471890943545.png", 10) or exists("1471890870096.png", 10)):       
		type("n", Key.ALT)
		type("s")
	else:
		printFFError("Could not find snipping tool window")
		
	
	time.sleep(2)
	
	printLog("Waiting for snipping tool window")
	if(exists("1469219920351.png",10)):
		type("s", Key.CTRL)
		time.sleep(2)
	else:
		printFFError("Couldn't find snipping tool window")
		
	printLog("Mapping to screenshot saving area")	
	ifs(exists("1471964672610.png", 10) or exists("1471965794144.png")):
		type("d", Key.ALT)
		type(SCREENSHOT_DIR + Key.ENTER)
	else:
		printFFError("Couldn't find snipping tool save window")

	time.sleep(2)
	printLog("Titling screenshot file")

	type(Key.TAB)
	type("n", Key.ALT)
	type(HOSTNAME +"-"+TESTNAME )
	type(Key.ENTER)
	type("s", Key.ALT)
	
	if(exists("1472053783138.png",10)):
		type("y", Key.ALT)
	else:
		printFFError("Overwrite pop-up not found error")
		printLog("found popup")
	#########################################################################################
	#
	#		Close open applications ---- This might have to be something that is in a queue
	#										due to having several applications open
	#
	#########################################################################################            
	time.sleep(2)    
	snippingApp.focus()
	###    close solid works
	snippingApp.focus()
	time.sleep(2)
	if(exists("1471978522353.png")):
		type(Key.F4, Key.ALT)
		waitVanish("1471979176530.png")
	else:
		printFFError("Snipping Tool Windows") 
		printLog("Locating Snipping Tool window and closing")
	
	time.sleep(3)    
	if(exists("1472053455435.png",15) or exists("1472060933958.png",15)):
		type(Key.F4, Key.ALT)
	else:
		printFFError("Could not find SolidWorks window")
		printLog("Located SolidWorks window and closed")
### END
run()