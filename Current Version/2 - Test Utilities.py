
test_dir = ""
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
LOG_DIR = "O:\\LabOutput\\logs\\"
LOG_FILE = "t2073.txt"








class test_utilities:
	

	def logErrorMessage(messageIn):
		errorLog.write(messageIn)


	def getTS():    
	    ts = time.time()
	    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	    return st

	def createDir(inDir):
	    if not os.path.exists(inDir):
	        os.makedirs(inDir)
	# Creation of Directories for Logging and Screenshots
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