import CheckFolders
import ParseInput
import StatValues
import BuildHtml
import BuildGraphs

def Main():
    inputFileName = "c:\\DirekWeb\\upload\\export_912.txt"
    outputDir = "c:\\DirekWeb\\reports\\"

    [subFolder, rawData] = CheckFolders.MakeSubfolder(inputFileName, outputDir)
    [graphData, statData] = ParseInput.DataFromFile(rawData, subFolder)

    # Compute the statistics values and build the charts for the report
    StatValues.ComputeValues(subFolder, statData)
    BuildGraphs.BuildAllGraphs(subFolder, graphData)
    BuildHtml.CreateReport(subFolder)

    print('Hello World')


Main()