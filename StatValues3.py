# Statistics for chapter 3

import ParseInput
import BuildTexts
import BuildCharts
import StatValues

def ComputeAll(subFolder, statData):

    compute31a(subFolder, statData)
    compute31b(subFolder, statData)
    compute31c(subFolder, statData)

    compute32a(subFolder, statData)
    compute32b(subFolder, statData)
    compute32c(subFolder, statData)
    compute32d(subFolder, statData)


def compute31a(subFolder, statData): # aggregate
    print '\nComputing values for slide 3.1.1.'
    values = ParseInput.extractAnswers(statData, [43])

    yesNum = values.count('103') + values.count('104')
    noNum = values.count('105') + values.count('106')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTexts.addMacro(subFolder, 'valCAAyesNum', str(yesNum))
    BuildTexts.addMacro(subFolder, 'valCAAnoNum', str(noNum))
    BuildTexts.addMacro(subFolder, 'valCAAyesNP', str(yesNumP))
    BuildTexts.addMacro(subFolder, 'valCAAnoNP', str(noNumP))

    BuildCharts.YesNoPieSVG(subFolder, 'pie311.svg', yesNumP, noNumP)


def compute31b(subFolder, statData): # by age - q14
    print '\nComputing values for slide 3.1.2.'
    values = ParseInput.extractAnswers(statData, [14, 43])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('103') + val.count('104') for val in values ]
    noNum = [ val.count('105') + val.count('106') for val in values ]

    BuildTexts.addMacro(subFolder, 'valCAByesNumA', str(yesNum[0]))
    BuildTexts.addMacro(subFolder, 'valCAByesNumB', str(yesNum[1]))
    BuildTexts.addMacro(subFolder, 'valCAByesNumC', str(yesNum[2]))
    BuildTexts.addMacro(subFolder, 'valCAByesNumD', str(yesNum[3]))
    BuildTexts.addMacro(subFolder, 'valCABnoNumA', str(noNum[0]))
    BuildTexts.addMacro(subFolder, 'valCABnoNumB', str(noNum[1]))
    BuildTexts.addMacro(subFolder, 'valCABnoNumC', str(noNum[2]))
    BuildTexts.addMacro(subFolder, 'valCABnoNumD', str(noNum[3]))

    BuildCharts.YesNoPieSVG(subFolder, 'pie312a.svg', yesNum[0], noNum[0])
    BuildCharts.YesNoPieSVG(subFolder, 'pie312b.svg', yesNum[1], noNum[1])
    BuildCharts.YesNoPieSVG(subFolder, 'pie312c.svg', yesNum[2], noNum[2])
    BuildCharts.YesNoPieSVG(subFolder, 'pie312d.svg', yesNum[3], noNum[3])


def compute31c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 3.1.3.'
    values = ParseInput.extractAnswers(statData, [19, 43])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('103') + val.count('104') for val in values ]
    noNum = [ val.count('105') + val.count('106') for val in values ]

    BuildTexts.addMacro(subFolder, 'valCACyesNumA', str(yesNum[0]))
    BuildTexts.addMacro(subFolder, 'valCACyesNumB', str(yesNum[1]))
    BuildTexts.addMacro(subFolder, 'valCACyesNumC', str(yesNum[2]))
    BuildTexts.addMacro(subFolder, 'valCACyesNumD', str(yesNum[3]))
    BuildTexts.addMacro(subFolder, 'valCACyesNumE', str(yesNum[4]))
    BuildTexts.addMacro(subFolder, 'valCACnoNumA', str(noNum[0]))
    BuildTexts.addMacro(subFolder, 'valCACnoNumB', str(noNum[1]))
    BuildTexts.addMacro(subFolder, 'valCACnoNumC', str(noNum[2]))
    BuildTexts.addMacro(subFolder, 'valCACnoNumD', str(noNum[3]))
    BuildTexts.addMacro(subFolder, 'valCACnoNumE', str(noNum[4]))

    BuildCharts.YesNoPieSVG(subFolder, 'pie313a.svg', yesNum[0], noNum[0])
    BuildCharts.YesNoPieSVG(subFolder, 'pie313b.svg', yesNum[1], noNum[1])
    BuildCharts.YesNoPieSVG(subFolder, 'pie313c.svg', yesNum[2], noNum[2])
    BuildCharts.YesNoPieSVG(subFolder, 'pie313d.svg', yesNum[3], noNum[3])
    BuildCharts.YesNoPieSVG(subFolder, 'pie313e.svg', yesNum[4], noNum[4])


def compute32a(subFolder, statData): # aggregate
    print '\nComputing values for slide 3.2.1.'
    values = ParseInput.extractAnswers(statData, [40,41,42])
    values = StatValues.joinLists(values)

    yesNum = values.count('99') + values.count('100')
    noNum = values.count('101') + values.count('102')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTexts.addMacro(subFolder, 'valCBAyesNum', str(yesNum))
    BuildTexts.addMacro(subFolder, 'valCBAnoNum', str(noNum))
    BuildTexts.addMacro(subFolder, 'valCBAyesNP', str(yesNumP))
    BuildTexts.addMacro(subFolder, 'valCBAnoNP', str(noNumP))

    BuildCharts.YesNoPieSVG(subFolder, 'pie321.svg', yesNumP, noNumP)


def compute32b(subFolder, statData): # by age - q14
    print '\nComputing values for slide 3.2.2.'
    values = ParseInput.extractAnswers(statData, [14, 40,41,42])
    values = StatValues.joinListsByAge(values)

    yesNum = [ val.count('99') + val.count('100') for val in values ]
    noNum = [ val.count('101') + val.count('102') for val in values ]

    BuildTexts.addMacro(subFolder, 'valCBByesNumA', str(yesNum[0]))
    BuildTexts.addMacro(subFolder, 'valCBByesNumB', str(yesNum[1]))
    BuildTexts.addMacro(subFolder, 'valCBByesNumC', str(yesNum[2]))
    BuildTexts.addMacro(subFolder, 'valCBByesNumD', str(yesNum[3]))
    BuildTexts.addMacro(subFolder, 'valCBBnoNumA', str(noNum[0]))
    BuildTexts.addMacro(subFolder, 'valCBBnoNumB', str(noNum[1]))
    BuildTexts.addMacro(subFolder, 'valCBBnoNumC', str(noNum[2]))
    BuildTexts.addMacro(subFolder, 'valCBBnoNumD', str(noNum[3]))

    BuildCharts.YesNoPieSVG(subFolder, 'pie322a.svg', yesNum[0], noNum[0])
    BuildCharts.YesNoPieSVG(subFolder, 'pie322b.svg', yesNum[1], noNum[1])
    BuildCharts.YesNoPieSVG(subFolder, 'pie322c.svg', yesNum[2], noNum[2])
    BuildCharts.YesNoPieSVG(subFolder, 'pie322d.svg', yesNum[3], noNum[3])



def compute32c(subFolder, statData): # by category - q19
    print '\nComputing values for slide 3.2.3.'
    values = ParseInput.extractAnswers(statData, [19, 40,41,42])
    values = StatValues.joinListsByCategory(values)

    yesNum = [ val.count('99') + val.count('100') for val in values ]
    noNum = [ val.count('101') + val.count('102') for val in values ]

    BuildTexts.addMacro(subFolder, 'valCBCyesNumA', str(yesNum[0]))
    BuildTexts.addMacro(subFolder, 'valCBCyesNumB', str(yesNum[1]))
    BuildTexts.addMacro(subFolder, 'valCBCyesNumC', str(yesNum[2]))
    BuildTexts.addMacro(subFolder, 'valCBCyesNumD', str(yesNum[3]))
    BuildTexts.addMacro(subFolder, 'valCBCyesNumE', str(yesNum[4]))
    BuildTexts.addMacro(subFolder, 'valCBCnoNumA', str(noNum[0]))
    BuildTexts.addMacro(subFolder, 'valCBCnoNumB', str(noNum[1]))
    BuildTexts.addMacro(subFolder, 'valCBCnoNumC', str(noNum[2]))
    BuildTexts.addMacro(subFolder, 'valCBCnoNumD', str(noNum[3]))
    BuildTexts.addMacro(subFolder, 'valCBCnoNumE', str(noNum[4]))

    BuildCharts.YesNoPieSVG(subFolder, 'pie323a.svg', yesNum[0], noNum[0])
    BuildCharts.YesNoPieSVG(subFolder, 'pie323b.svg', yesNum[1], noNum[1])
    BuildCharts.YesNoPieSVG(subFolder, 'pie323c.svg', yesNum[2], noNum[2])
    BuildCharts.YesNoPieSVG(subFolder, 'pie323d.svg', yesNum[3], noNum[3])
    BuildCharts.YesNoPieSVG(subFolder, 'pie323e.svg', yesNum[4], noNum[4])


def compute32d(subFolder, statData): # by question
    print '\nComputing values for slide 3.2.4.'
    values = ParseInput.extractAnswers(statData, [40,41,42])
    values = StatValues.joinListsByQuestion(values)

    yesNum = [ val.count('99') + val.count('100') for val in values ]
    noNum = [ val.count('101') + val.count('102') for val in values ]

    BuildTexts.addMacro(subFolder, 'valCBDyesNumA', str(yesNum[0]))
    BuildTexts.addMacro(subFolder, 'valCBDyesNumB', str(yesNum[1]))
    BuildTexts.addMacro(subFolder, 'valCBDyesNumC', str(yesNum[2]))
    BuildTexts.addMacro(subFolder, 'valCBDnoNumA', str(noNum[0]))
    BuildTexts.addMacro(subFolder, 'valCBDnoNumB', str(noNum[1]))
    BuildTexts.addMacro(subFolder, 'valCBDnoNumC', str(noNum[2]))

    BuildCharts.YesNoPieSVG(subFolder, 'pie324a.svg', yesNum[0], noNum[0])
    BuildCharts.YesNoPieSVG(subFolder, 'pie324b.svg', yesNum[1], noNum[1])
    BuildCharts.YesNoPieSVG(subFolder, 'pie324c.svg', yesNum[2], noNum[2])
