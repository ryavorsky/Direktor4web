import os

def CreateReport(subFolder):
    # BuildTex.MakeTitlePage(subFolder, statData)
    # BuildTex.buildNamesList(subFolder, statData)
    return


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
