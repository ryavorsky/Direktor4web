import time
import os
import shutil
import sys

import ParseInput
import StatValues
import BuildTexts
import BuildGraphs
import BuildCharts

#inputFileName = "c:\\Direktor4web\\upload\\export_912.txt"
templateDir = "templates\\"
outputDir = "c:\\Direktor4web\\reports\\"
todoFileName = "c:\\Direktor4web\\todo.txt"

def Main(): 

    print 'Make subfolders. '
    [subFolder, rawData] = MakeSubfolder()
    if rawData == '' :
        print 'No data to process. '

    else :

        print 'Parse input. '
        [graphData, statData] = ParseInput.DataFromFile(rawData, subFolder)

        print 'Compute the statistics values and build the charts for the report. '
        StatValues.ComputeValues(subFolder, statData)
        BuildGraphs.BuildAllGraphs(subFolder, graphData)

        print 'Create the final report. '
        BuildTexts.CreateReport(subFolder)


# Create subfolder for the report files (charts, graphs, lists, texts etc)
def MakeSubfolder() :

    # Get the input data file name from the top in todo.txt
    todoFile = open(todoFileName,'r')
    inputFileName = todoFile.readline().strip()
    todoList = todoFile.readlines()
    todoFile.close()

    todoFile = open(todoFileName,'w')
    todoFile.writelines(todoList)
    todoFile.close()

    if len(inputFileName) < 5 : 
        print 'No file to process'
        return ['', ''] 
    else :
        # Read the input file into the rawData variable
        f = open(inputFileName, 'r')
        rawData = f.readlines()
        f.close()

        # create subfolder for the report
        t = time.localtime()
        timestamp = str(t[0]) + '-' + str(t[1]) + '-' + str(t[2]) + '_' + str(t[3]) + 'h' + str(t[4]) + 'm' + str(t[5]) + 's'
        inputFileName_ = os.path.basename(inputFileName).replace('.','_') + '_'
        subFolder = os.path.join(outputDir, 'Res_' + inputFileName_ + timestamp)
        os.mkdir(subFolder)
        print('\nThe output folder is created:\n\t' + subFolder + '\n')

        # move the template files into the subfolder
        inputFiles = os.listdir(templateDir)
        print str(inputFiles)
        for fileName in inputFiles:
            fullFileName = os.path.join(templateDir, fileName)
            shutil.copy2(fullFileName, subFolder)

        shutil.copy2(inputFileName, os.path.join(subFolder, 'InputData'+ '_' + timestamp + '.txt'))
        print('\nTemplate files copied to ' + subFolder + '\n')

        return [subFolder, rawData]


Main()
