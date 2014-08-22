# Check whether the input file and output folder exist, create subFolder
import sys
import time
import os

def TestDirs(inDir, outDir):
    try:
        os.chdir(inDir)
    except Exception:
        print('Failed to open the inDir\n\t' + inDir + '\n')
        sys.exit
    else:
        print('The intput folder is found:\n\t' + inDir + '\n')
        inputFiles = os.listdir(inDir)
        print(str(len(inputFiles)) + ' files to process')
        for inputFileName in inputFiles:
            print '\t' + inputFileName

    if os.path.exists(outDir): 
        t = time.localtime()
        outDir = outDir + '_' + str(t[3]) + str(t[4]) + str(t[5])
        os.mkdir(outDir)
        print('The output folder is created:\n\t' + outDir + '\n')
    else:
        os.mkdir(outDir)
        print('The output folder is created:\n\t' + outDir + '\n')

    return outDir

def _MakeSubfolder(inputFileName, outputDir) :
    # extract input file Id and create folder for the results
    inputId = os.path.basename(inputFileName).split('.')[0].split('_')[1]
    subFolder = outputDir + '\\' + inputId + '_files'
    os.mkdir(subFolder)
    print subFolder, ' is created for ', inputId

    BuildHtml.MoveFiles(subFolder, projectDir)  

    return [inputId, subFolder]

def MakeSubfolder(inputFileName, outputDir) :
    return ["",""]