# Statistics for chapter 5

import ParseInput
import BuildTexts
import BuildCharts
import StatValues

def  ComputeAll(subFolder, statData):

    compute51(subFolder, statData)
    compute52(subFolder, statData)
    compute53(subFolder, statData)
    compute54(subFolder, statData)

def compute51(subFolder, statData) :  # aggregate
    print '\nComputing values for slide 5.1.'
    values = ParseInput.extractAnswers(statData, [56,57])
    values = StatValues.joinLists(values)

    yesNum = values.count('87') + values.count('88')
    noNum = values.count('89') + values.count('90')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTexts.addMacro(subFolder, 'valGAyesNum', str(yesNum))
    BuildTexts.addMacro(subFolder, 'valGAnoNum', str(noNum))
    BuildTexts.addMacro(subFolder, 'valGAyesNP', str(yesNumP))
    BuildTexts.addMacro(subFolder, 'valGAnoNP', str(noNumP))

    BuildCharts.YesNoPie(subFolder,'pie51.png', yesNumP, noNumP)


def compute52(subFolder, statData): # by age - q14
    print '\nComputing values for slide 5.2.'
    values = ParseInput.extractAnswers(statData, [14, 56,57])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTexts.addMacro(subFolder, 'valGByesNumA', str(yesNum[0]))
    BuildTexts.addMacro(subFolder, 'valGByesNumB', str(yesNum[1]))
    BuildTexts.addMacro(subFolder, 'valGByesNumC', str(yesNum[2]))
    BuildTexts.addMacro(subFolder, 'valGByesNumD', str(yesNum[3]))
    BuildTexts.addMacro(subFolder, 'valGBnoNumA', str(noNum[0]))
    BuildTexts.addMacro(subFolder, 'valGBnoNumB', str(noNum[1]))
    BuildTexts.addMacro(subFolder, 'valGBnoNumC', str(noNum[2]))
    BuildTexts.addMacro(subFolder, 'valGBnoNumD', str(noNum[3]))

    BuildCharts.YesNoPie(subFolder,'pie52a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder,'pie52b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder,'pie52c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder,'pie52d.png', yesNum[3], noNum[3])


def compute53(subFolder, statData): # by category - q19
    print '\nComputing values for slide 5.3.'
    values = ParseInput.extractAnswers(statData, [19, 56,57])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTexts.addMacro(subFolder, 'valGCyesNumA', str(yesNum[0]))
    BuildTexts.addMacro(subFolder, 'valGCyesNumB', str(yesNum[1]))
    BuildTexts.addMacro(subFolder, 'valGCyesNumC', str(yesNum[2]))
    BuildTexts.addMacro(subFolder, 'valGCyesNumD', str(yesNum[3]))
    BuildTexts.addMacro(subFolder, 'valGCyesNumE', str(yesNum[4]))
    BuildTexts.addMacro(subFolder, 'valGCnoNumA', str(noNum[0]))
    BuildTexts.addMacro(subFolder, 'valGCnoNumB', str(noNum[1]))
    BuildTexts.addMacro(subFolder, 'valGCnoNumC', str(noNum[2]))
    BuildTexts.addMacro(subFolder, 'valGCnoNumD', str(noNum[3]))
    BuildTexts.addMacro(subFolder, 'valGCnoNumE', str(noNum[4]))

    BuildCharts.YesNoPie(subFolder,'pie53a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder,'pie53b.png', yesNum[1], noNum[1])
    BuildCharts.YesNoPie(subFolder,'pie53c.png', yesNum[2], noNum[2])
    BuildCharts.YesNoPie(subFolder,'pie53d.png', yesNum[3], noNum[3])
    BuildCharts.YesNoPie(subFolder,'pie53e.png', yesNum[4], noNum[4])


def compute54(subFolder, statData): # by question
    print '\nComputing values for slide 5.4.'
    values = ParseInput.extractAnswers(statData, [56,57])
    values = StatValues.joinListsByQuestion(values)

    yesNum = [ val.count('87') + val.count('88') for val in values ]
    noNum = [ val.count('89') + val.count('90') for val in values ]

    BuildTexts.addMacro(subFolder, 'valGDyesNumA', str(yesNum[0]))
    BuildTexts.addMacro(subFolder, 'valGDyesNumB', str(yesNum[1]))
    BuildTexts.addMacro(subFolder, 'valGDnoNumA', str(noNum[0]))
    BuildTexts.addMacro(subFolder, 'valGDnoNumB', str(noNum[1]))

    BuildCharts.YesNoPie(subFolder,'pie54a.png', yesNum[0], noNum[0])
    BuildCharts.YesNoPie(subFolder,'pie54b.png', yesNum[1], noNum[1])
