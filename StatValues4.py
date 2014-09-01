# Statistics for chapter 4

import ParseInput
import BuildTexts
import BuildCharts
import StatValues

def ComputeAll(subFolder, statData):
    
    compute41(subFolder, statData)

    compute42a(subFolder, statData)
    compute42b(subFolder, statData)
    compute42c(subFolder, statData)

def compute41(subFolder, statData): # one question 
    print '\nComputing values for slide 4.1.'
    values = ParseInput.extractAnswers(statData, [36])
    ansA = values.count('91') 
    ansB = values.count('92')
    ansC = values.count('93') 
    ansD = values.count('94')
    [ansAp, ansBp, ansCp, ansDp] = StatValues.percent([ansA, ansB, ansC, ansD])

    BuildTexts.addMacro(subFolder, 'valDAansAv', str(ansA))
    BuildTexts.addMacro(subFolder, 'valDAansBv', str(ansB))
    BuildTexts.addMacro(subFolder, 'valDAansCv', str(ansC))
    BuildTexts.addMacro(subFolder, 'valDAansDv', str(ansD))
    BuildTexts.addMacro(subFolder, 'valDAansAp', str(ansAp))
    BuildTexts.addMacro(subFolder, 'valDAansBp', str(ansBp))
    BuildTexts.addMacro(subFolder, 'valDAansCp', str(ansCp))
    BuildTexts.addMacro(subFolder, 'valDAansDp', str(ansDp))
    
    BuildCharts.Pie(subFolder,'pie41.svg', [ansAp, ansBp, ansCp, ansDp])


def compute42a(subFolder, statData): # one question 
    print '\nComputing values for slide 4.2.a'
    values = ParseInput.extractAnswers(statData, [37])
    ansA = values.count('95') 
    ansB = values.count('96')
    ansC = values.count('97') 
    ansD = values.count('98')
    [ansAp, ansBp, ansCp, ansDp] = StatValues.percent([ansA, ansB, ansC, ansD])

    BuildTexts.addMacro(subFolder, 'valDBAansAv', str(ansA))
    BuildTexts.addMacro(subFolder, 'valDBAansBv', str(ansB))
    BuildTexts.addMacro(subFolder, 'valDBAansCv', str(ansC))
    BuildTexts.addMacro(subFolder, 'valDBAansDv', str(ansD))
    BuildTexts.addMacro(subFolder, 'valDBAansAp', str(ansAp))
    BuildTexts.addMacro(subFolder, 'valDBAansBp', str(ansBp))
    BuildTexts.addMacro(subFolder, 'valDBAansCp', str(ansCp))
    BuildTexts.addMacro(subFolder, 'valDBAansDp', str(ansDp))
    
    BuildCharts.Pie(subFolder,'pie421.svg', [ansAp, ansBp, ansCp, ansDp])


def compute42b(subFolder, statData): # one question 
    print '\nComputing values for slide 4.2.b.'
    values = ParseInput.extractAnswers(statData, [45])
    ansA = values.count('107') 
    ansB = values.count('108')
    ansC = values.count('109') 
    ansD = values.count('110')
    ansE = values.count('111')
    [ansAp, ansBp, ansCp, ansDp, ansEp] = StatValues.percent([ansA, ansB, ansC, ansD, ansE])

    BuildTexts.addMacro(subFolder, 'valDBBansAv', str(ansA))
    BuildTexts.addMacro(subFolder, 'valDBBansBv', str(ansB))
    BuildTexts.addMacro(subFolder, 'valDBBansCv', str(ansC))
    BuildTexts.addMacro(subFolder, 'valDBBansDv', str(ansD))
    BuildTexts.addMacro(subFolder, 'valDBBansEv', str(ansE))
    BuildTexts.addMacro(subFolder, 'valDBBansAp', str(ansAp))
    BuildTexts.addMacro(subFolder, 'valDBBansBp', str(ansBp))
    BuildTexts.addMacro(subFolder, 'valDBBansCp', str(ansCp))
    BuildTexts.addMacro(subFolder, 'valDBBansDp', str(ansDp))
    BuildTexts.addMacro(subFolder, 'valDBBansEp', str(ansEp))
    
    BuildCharts.Pie(subFolder,'pie422.svg', [ansAp, ansBp, ansCp, ansDp, ansEp])


def compute42c(subFolder, statData): # one question 
    print '\nComputing values for slide 4.2.c.'
    values = ParseInput.extractAnswers(statData, [54])

    yesNum = values.count('87') + values.count('88')
    noNum = values.count('89') + values.count('90')
    [yesNumP, noNumP] = StatValues.percent([yesNum,noNum])

    BuildTexts.addMacro(subFolder, 'valDBCyesNum', str(yesNum))
    BuildTexts.addMacro(subFolder, 'valDBCnoNum', str(noNum))
    BuildTexts.addMacro(subFolder, 'valDBCyesNP', str(yesNumP))
    BuildTexts.addMacro(subFolder, 'valDBCnoNP', str(noNumP))

    BuildCharts.YesNoPieSVG(subFolder,'pie423.svg', yesNumP, noNumP)

