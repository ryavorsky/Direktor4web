# Statistics for chapter 2

import ParseInput
import BuildTexts
import BuildCharts
import StatValues

def  ComputeAll(subFolder, statData):

    compute21a(subFolder, statData)
    compute21b(subFolder, statData)
    compute21c(subFolder, statData)
    compute21d(subFolder, statData)

    compute22a(subFolder, statData)
    compute22b(subFolder, statData)
    compute22c(subFolder, statData)
    compute22d(subFolder, statData)
    compute22e(subFolder, statData)

    compute23a(subFolder, statData)
    compute23b(subFolder, statData)
    compute23c(subFolder, statData)
    compute23d(subFolder, statData)


def compute21a(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.1.1.'
    values = ParseInput.extractAnswers(statData, [38,39])
    values = StatValues.joinLists(values)

    yesNum = values.count('87') + values.count('88')
    noNum = values.count('89') + values.count('90')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTexts.addMacro(subFolder, 'valBAAyesNumP', str(yesNumP))
    BuildTexts.addMacro(subFolder, 'valBAAnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder, 'pie211.png', yesNumP, noNumP)


def compute21b(subFolder, statData): # by age - q14
    print '\nComputing values for slide 2.1.2.'
    values = ParseInput.extractAnswers(statData, [14, 38,39])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTexts.addMacrosList(subFolder, 'valBAByesNum', yesNum)
    BuildTexts.addMacrosList(subFolder, 'valBABnoNum', noNum)

    BuildCharts.YesNoPie(subFolder, 'pie212a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder, 'pie212b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder, 'pie212c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder, 'pie212d.png', yesNum[3], noNum[3])

def compute21c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 2.1.3.'
    values = ParseInput.extractAnswers(statData, [19, 38,39])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTexts.addMacrosList(subFolder, 'valBACyesNum', yesNum)
    BuildTexts.addMacrosList(subFolder, 'valBACnoNum', noNum)

    BuildCharts.YesNoPie(subFolder, 'pie213a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder, 'pie213b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder, 'pie213c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder, 'pie213d.png', yesNum[3], noNum[3])
    BuildCharts.YesNoPie(subFolder, 'pie213e.png', yesNum[4], noNum[4])

def compute21d(subFolder, statData): # by question
    print '\nComputing values for slide 2.1.4.'
    values = ParseInput.extractAnswers(statData, [35,38,39,50,55])
    values = StatValues.joinListsByQuestion(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTexts.addMacrosList(subFolder, 'valBADyesNum', yesNum)
    BuildTexts.addMacrosList(subFolder, 'valBADnoNum', noNum)

    BuildCharts.YesNoPie(subFolder, 'pie214a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder, 'pie214b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder, 'pie214c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder, 'pie214d.png', yesNum[3], noNum[3])
    BuildCharts.YesNoPie(subFolder, 'pie214e.png', yesNum[4], noNum[4])

def compute22a(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.2.1.'
    values = ParseInput.extractAnswers(statData, [28,29,46,47])
    values = StatValues.joinLists(values)

    yesNum = values.count('83') + values.count('84')
    noNum = values.count('85') + values.count('86')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTexts.addMacro(subFolder, 'valBBAyesNumP', str(yesNumP))
    BuildTexts.addMacro(subFolder, 'valBBAnoNumP', str(noNumP))

    BuildCharts.YesNoPie(subFolder, 'pie221.png', yesNumP, noNumP)


def compute22b(subFolder, statData): # by age
    print '\nComputing values for slide 2.2.2.'
    values = ParseInput.extractAnswers(statData, [14, 28,29,46,47])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('83') + val.count('84') for val in values ]
    noNum = [ val.count('85') + val.count('86') for val in values ]

    BuildTexts.addMacrosList(subFolder, 'valBBByesNum', yesNum)
    BuildTexts.addMacrosList(subFolder, 'valBBBnoNum', noNum)

    BuildCharts.YesNoPie(subFolder, 'pie222a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder, 'pie222b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder, 'pie222c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder, 'pie222d.png', yesNum[3], noNum[3])


def compute22c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 2.2.3.'
    values = ParseInput.extractAnswers(statData, [19, 28,29,46,47])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('83') + val.count('84') for val in values ]
    noNum = [ val.count('85') + val.count('86') for val in values ]

    BuildTexts.addMacrosList(subFolder, 'valBBCyesNum', yesNum)
    BuildTexts.addMacrosList(subFolder, 'valBBCnoNum', noNum)

    BuildCharts.YesNoPie(subFolder, 'pie223a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder, 'pie223b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder, 'pie223c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder, 'pie223d.png', yesNum[3], noNum[3])
    BuildCharts.YesNoPie(subFolder, 'pie223e.png', yesNum[4], noNum[4])


def compute22d(subFolder, statData): # by question
    print '\nComputing values for slide 2.2.4.'
    values = ParseInput.extractAnswers(statData, [28,29,46,47])
    values = StatValues.joinListsByQuestion(values)

    yesNum = [ val.count('83') + val.count('84') for val in values ]
    noNum = [ val.count('85') + val.count('86') for val in values ]

    BuildTexts.addMacrosList(subFolder, 'valBBDyesNum', yesNum)
    BuildTexts.addMacrosList(subFolder, 'valBBDnoNum', noNum)

    BuildCharts.YesNoPie(subFolder, 'pie224a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder, 'pie224b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder, 'pie224c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder, 'pie224d.png', yesNum[3], noNum[3])


def compute22e(subFolder, statData): # aggregate (1 question)
    print '\nComputing values for slide 2.2.5.'
    values = ParseInput.extractAnswers(statData, [49])

    ansA = values.count('115') 
    ansB = values.count('116')
    ansC = values.count('117') 
    ansD = values.count('118')
    [ansAp, ansBp, ansCp, ansDp] = StatValues.percent([ansA, ansB, ansC, ansD])

    BuildTexts.addMacro(subFolder, 'valBBEansA', str(ansA))
    BuildTexts.addMacro(subFolder, 'valBBEansB', str(ansB))
    BuildTexts.addMacro(subFolder, 'valBBEansC', str(ansC))
    BuildTexts.addMacro(subFolder, 'valBBEansD', str(ansD))
    BuildTexts.addMacro(subFolder, 'valBBEansAp', str(ansAp))
    BuildTexts.addMacro(subFolder, 'valBBEansBp', str(ansBp))
    BuildTexts.addMacro(subFolder, 'valBBEansCp', str(ansCp))
    BuildTexts.addMacro(subFolder, 'valBBEansDp', str(ansDp))
    
    BuildCharts.Pie(subFolder, 'pie225.png', [ansAp, ansBp, ansCp, ansDp])


def compute23a(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.3.1.'
    values = ParseInput.extractAnswers(statData, [23])

    yesNum = values.count('61')
    noNum = values.count('62')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTexts.addMacro(subFolder, 'valBCAyesNum', str(yesNum))
    BuildTexts.addMacro(subFolder, 'valBCAnoNum', str(noNum))
    BuildTexts.addMacro(subFolder, 'valBCAyesNP', str(yesNumP))
    BuildTexts.addMacro(subFolder, 'valBCAnoNP', str(noNumP))

    BuildCharts.YesNoPie(subFolder, 'pie231.png', yesNumP, noNumP)


def compute23b(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.3.2.'
    values = ParseInput.extractAnswers(statData, [52])

    yesNum = values.count('99') + values.count('100')
    noNum = values.count('101') + values.count('102')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTexts.addMacro(subFolder, 'valBCByesNum', str(yesNum))
    BuildTexts.addMacro(subFolder, 'valBCBnoNum', str(noNum))
    BuildTexts.addMacro(subFolder, 'valBCByesNP', str(yesNumP))
    BuildTexts.addMacro(subFolder, 'valBCBnoNP', str(noNumP))

    BuildCharts.YesNoPie(subFolder, 'pie232.png', yesNumP, noNumP)


def compute23c(subFolder, statData): # aggregate (1 question)
    print '\nComputing values for slide 2.3.3.'
    values = ParseInput.extractAnswers(statData, [53])

    ansA = values.count('120') 
    ansB = values.count('121')
    ansC = values.count('122') 
    [ansAp, ansBp, ansCp] = StatValues.percent([ansA, ansB, ansC])

    BuildTexts.addMacro(subFolder, 'valBCCansA', str(ansA))
    BuildTexts.addMacro(subFolder, 'valBCCansB', str(ansB))
    BuildTexts.addMacro(subFolder, 'valBCCansC', str(ansC))
    BuildTexts.addMacro(subFolder, 'valBCCanAp', str(ansAp))
    BuildTexts.addMacro(subFolder, 'valBCCanBp', str(ansBp))
    BuildTexts.addMacro(subFolder, 'valBCCanCp', str(ansCp))
    
    BuildCharts.Pie(subFolder, 'pie233.png', [ansAp, ansBp, ansCp])


def compute23d(subFolder, statData): # aggregate
    print '\nComputing values for slide 2.3.4.'
    values = ParseInput.extractAnswers(statData, [30])

    yesNum = values.count('83') + values.count('84')
    noNum = values.count('85') + values.count('86')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTexts.addMacro(subFolder, 'valBCDyesNum', str(yesNum))
    BuildTexts.addMacro(subFolder, 'valBCDnoNum', str(noNum))
    BuildTexts.addMacro(subFolder, 'valBCDyesNP', str(yesNumP))
    BuildTexts.addMacro(subFolder, 'valBCDnoNP', str(noNumP))

    BuildCharts.YesNoPie(subFolder, 'pie234.png', yesNumP, noNumP)


