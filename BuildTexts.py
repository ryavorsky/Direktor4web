import os

def CreateReport(subFolder, orgSize):

    if orgSize > 37 :
        splitTables(subFolder, orgSize)

    applyMacros(subFolder)


def applyMacros(subFolder):
    macrosFileName = os.path.join(subFolder, 'Tex', 'commands.tex')
    templateFileName = os.path.join(subFolder,'Report_template.html')

    # Extract macros
    macros = dict()
    macrosFile = open(macrosFileName,'r')
    for line in macrosFile.readlines() :
        size = len(line)
        if size > 12 :
            [var, value] = line[12:size-2].split('}{')
            macros[var] = value
    print '\n Macros:', macros
    macrosFile.close()

    # Substitute the macros into the report template
    htmlReport = open(templateFileName,'r')
    report = ''.join(htmlReport.readlines())
    for var in macros :
        print var, macros[var]
        report = report.replace(var, macros[var])
    htmlReport.close()
    htmlReport = open(templateFileName,'w')
    htmlReport.write(report)
    htmlReport.close()


# append a TeX macro definition to the commands.tex file
def addMacro(subFolder, command, value) :

    print 'Adding macro:', subFolder, command, value
    lineToAdd = '\\newcommand{\\' + command +'}{' + str(value) + '}\n'
    
    fName = os.path.join(subFolder, 'Tex', 'commands.tex')
    fileOfTexCommands = open(fName, 'a')
    fileOfTexCommands.write(lineToAdd)
    fileOfTexCommands.close()
    
    print 'Tex command added', '\\newcommand{\\' + command +'}{' + str(value) + '}\n'


def addMacrosList(subFolder, commandPrefix, values) :
    
    print 'Adding several macros:', commandPrefix, values
    suffix = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    size = len(values)

    for i in range(size) :
        command = commandPrefix + suffix[i]
        value = values[i]
        addMacro(subFolder, command, value)


def replaceInFile(fileName, oldValue, newValue):

    # read the current file into a variable
    f = open(fileName,'r')
    data = ''.join(f.readlines())
    f.close()

    data = data.replace(oldValue, newValue)

    # write the new data into the file
    f = open(fileName,'w')
    f.write(data)
    f.close()

def encodeNumber(number) :
    code = {
            '1' : 'A',
            '2' : 'B',
            '3' : 'C',
            '4' : 'D',
            '5' : 'E',
            '6' : 'F',
            '7' : 'G',
            '8' : 'H'
            }
    res = ''
    for symbol in str(number) :
        res = res + code[symbol]

    return res


def Alert(subFolder, msg):
    f = open(os.path.join(subFolder,'alerts.txt'),'a')
    f.write(msg + '\n')
    f.close


def splitTables(subFolder, orgSize):

    print '\nSplitting tables'

    files = ['table61.tex', 'table711.tex', 'table721.tex', 'table731.tex']
    files = [os.path.join(subFolder, 'Tex', name) for name in files]
    list_split = os.path.join(subFolder, 'Tex', 'list_split.tex')
    table_split = os.path.join(subFolder, 'Tex', 'table_split.tex')

    insertFileaAfterLine(os.path.join(subFolder, 'Tex', 'nameslist.tex'), list_split, 35)

    for fileName in files :
        insertFileaAfterLine(fileName, table_split, 35)

    if orgSize > 76 :
        insertFileaAfterLine(os.path.join(subFolder,'Tex','nameslist.tex'), list_split, 85)

        for fileName in files :
            insertFileaAfterLine(fileName, table_split, 105)

    # now insert the tables into the slides - TeX does not like neseted includes
    print '\nInserting tables'
    specs = [['slide1b.tex','nameslist.tex'],['slide6_3.tex','table61.tex'],['slide7_3a.tex','table711.tex'],['slide7_3b.tex','table721.tex'],['slide7_3c.tex','table731.tex'],]
    for spec in specs :
        (fileName, addFileName) = spec
        file_name = os.path.join(subFolder, 'Tex', fileName)
        oldValue = '\input{'+ addFileName + '}'
        data_file = open(os.path.join(subFolder, 'Tex', addFileName), 'r')
        newValue = ' '.join(data_file.readlines())
        data_file.close()
        replaceInFile(file_name, oldValue, newValue)


def insertFileaAfterLine(fileName, addFileName, lineNum):
    f1 = open(fileName, 'r')
    f2 = open(addFileName, 'r')
    data = []
    i = 1
    for line in f1.readlines() :
        if i <> lineNum :
            data.append(line)
            i += 1
        else :
            data.append(line)
            for additionalLine in f2.readlines() :
                data.append(additionalLine)
            i += 1

    f1.close()
    f2.close()

    f1 = open(fileName, 'w')
    for dataLine in data:
        f1.write(dataLine)
    f1.close()

def replaceLineWithFile(fileName, addFileName, lineNum):
    f1 = open(fileName, 'r')
    f2 = open(addFileName, 'r')
    print 'Replacing line with file:', fileName, addFileName, lineNum
    data = []
    i = 1
    for line in f1.readlines() :
        if i <> lineNum :
            data.append(line)
            i += 1
        else :
            for additionalLine in f2.readlines() :
                data.append(additionalLine)
            i += 1

    f1.close()
    f2.close()

    f1 = open(fileName, 'w')
    print 'Write result'
    for dataLine in data:
        print dataLine
        f1.write(dataLine)
    f1.close()
   
