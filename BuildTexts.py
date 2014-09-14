import os

def CreateReport(subFolder):

    applyMacros(subFolder)


def applyMacros(subFolder):
    macrosFileName = os.path.join(subFolder,'commands.tex')
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
    report = '\n'.join(htmlReport.readlines())
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
    
    fName = os.path.join(subFolder, 'commands.tex')
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
    data = '\n'.join(f.readlines())
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
