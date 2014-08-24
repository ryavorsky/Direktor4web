# Check whether the input file and output folder exist, create subFolder
import time
import os
import shutil

def MakeSubfolder(inputFileName, outputDir) :
    # Read the input file into the rawData variable
    f = open(inputFileName, 'r')
    rawData = f.readlines()
    f.close()

    # create subfolder for the report
    t = time.localtime()
    timestamp = str(t[0]) + '-' + str(t[1]) + '-' + str(t[2]) + '_' + str(t[3]) + 'h' + str(t[4]) + 'm' + str(t[5]) + 's'
    subFolder = outputDir + 'Report_' + timestamp + '\\'
    os.mkdir(subFolder)
    print('\nThe output folder is created:\n\t' + subFolder + '\n')

    # move the template files into the subfolder
    shutil.copy2('Report_template.html', subFolder)
    shutil.copy2('key.txt', subFolder)
    shutil.copy2(inputFileName, subFolder + 'InputData'+ '_' + timestamp + '.txt')
    print('\nTemplate files copied to ' + subFolder + '\n')

    return [subFolder, rawData]
