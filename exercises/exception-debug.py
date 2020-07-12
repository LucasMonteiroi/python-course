import traceback as trace, datetime 

def createLogFile() :
    now = datetime.datetime.now()
    fileName = '/Users/lucasmonteiroi/git-repo/python-course/output-files/erro_log_%s.txt' % (now)
    logFile = open(fileName, 'a')
    return logFile

def makeBox(symbol, width, height) :
    if len(symbol) != 1 :
        raise Exception('"symbol" needs to be a string of 1 character')

    if (width < 2) or (height < 2) :
        raise Exception('"width" and "height" must to be greather or equal 2')

    print(symbol * width)
    
    for i in range(height - 2) :
        print(symbol + (' ' * (width - 2)) + symbol)
    
    print(symbol * width)

def logException(exception, file) :
    file.write(exception)
    print('The log was written in logfile')
    file.close()


errorFile = createLogFile()

try :
    makeBox('*', 4, 1)
except :
    exception = trace.format_exc()
    logException(exception, errorFile)