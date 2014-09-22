
import os

import BuildTexts

def buildNamesListFile(subFolder, statData):

    resFileName =  os.path.join(subFolder, 'nameslist.tex')
    f = open(resFileName, 'w')

    localId = 0

    for line in statData :
        localId += 1
        data = line.split('\t')
        name = data[6].split('=')[1]
        position = data[7].split('=')[1]
        resLine = '\item [' + str(localId) + '] ' + name + ', ' + position + '\n'
        f.write(resLine) #.decode("CP1251").encode("UTF-8"))

    f.close()


def addNamesListToHtml(subFolder):

    names = extractNames(subFolder)
    
    res = ''

    for id in range(len(names)) :
        number = str(id+1)
        fullName = names[number][0]
        position = names[number][1]
        resLine = '<tr><td>&nbsp;'+number+'.</td><td>'+fullName+'</td><td>'+position+'</td></tr>'
        res = res + resLine

    templateFileName = os.path.join(subFolder,'Report_template.html')
    BuildTexts.replaceInFile(templateFileName,'<td>0</td><td>A</td><td>B</td>',res)
    

def addSizeComments(subFolder, numOfNodes) :
    
    if numOfNodes <= 7 :
        res = '\socioSizeTextA'
    elif numOfNodes <= 11 :
        res = '\socioSizeTextB'
    elif numOfNodes <= 16 :
        res = '\socioSizeTextC'
    elif numOfNodes <= 21 :
        res = '\socioSizeTextD'
    else :
        res = '\socioSizeTextE'

    fileName = os.path.join(subFolder, 'commands.tex')
    BuildTexts.replaceInFile(fileName,res,'\socioSizeComment')


def computeRating(subFolder, sectionId, G) :
    fileName = os.path.join(subFolder, 'table'+sectionId+'.tex')
    print '\nBuilding table ', fileName
    names = extractNames(subFolder)

    # TeX version
    f = open(fileName,'w')
    
    res = []
    for id in G.nodes() :
        fullName = names.get(id,['',''])[0]
        position = names.get(id,['',''])[1]
        score = G.in_degree(id)
        res.append([id,fullName,position,score])

    res.sort(cmp = cmp)

    for t in res :
        resLine = t[0] + ' & ' + t[1] + ' & ' + t[2] + ' & ' + str(t[3]) + '\\\\ \n'
        f.write(resLine)
    f.close()

    resHtml = ''
    for t in res :
        resLineHtml = '<tr><td class="right">'+t[0]+'.&nbsp;</td><td>'+t[1]+'</td><td>'+t[2]+'</td><td class="number">'+str(t[3])+'</td></tr>'
        resHtml = resHtml + resLineHtml 
    templateFileName = os.path.join(subFolder,'Report_template.html')
    BuildTexts.replaceInFile(templateFileName,'rating'+sectionId,resHtml)


def cmp(x, y) : 
    if x[3] < y[3] :
        return 1
    elif x[3] > y[3] :
        return -1
    elif int(x[0]) > int(y[0]) :
        return 1
    elif int(x[0]) < int(y[0]) :
        return -1
    else :
        return 0


def extractNames(subFolder) :
    names = dict()
    f = open(os.path.join(subFolder, 'nameslist.tex'),'r')

    for line in f.readlines() :
        p1 = line.find('[')
        p2 = line.find(']')
        p3 = line.find(',')
        p4 = len(line)
        p4a = line.find('(')
        if p4a > 0 :
            p4 = p4a
        num = line[(p1+1):p2]
        name = line[(p2+2):p3]
        position = line[(p3+2):(p4-1)]

        names[num] = [name,position]

    f.close()
    return names
