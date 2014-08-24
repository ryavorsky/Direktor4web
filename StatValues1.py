# This sub-module computes values for the 1-st section of the report

import ParseInput
import StatValues
import BuildTexts

def ComputeAll(subFolder, statData) :

    computeAllBossTeacher(subFolder, statData)
    computeParticipatedManWomen(subFolder, statData)
    computeAge(subFolder, statData)
    computeEducation(subFolder, statData)
    computeWorkYears(subFolder, statData)
    computeWorkHereYears(subFolder, statData)
    computeTeachCat(subFolder, statData)


def computeAllBossTeacher(subFolder, statData) :
    values = ParseInput.extractAnswers(statData, [8])
    boss = values.count('201') + values.count('202')
    teacher = values.count('203')

    BuildTexts.addMacro(subFolder, 'nTotal', str(len(statData)))
    BuildTexts.addMacro(subFolder, 'numBoss', str(boss))
    BuildTexts.addMacro(subFolder, 'numTeacher', str(teacher))


def computeParticipatedManWomen(subFolder, statData) :
    values = ParseInput.extractAnswers(statData, [9])
    men = values.count('14')
    women = values.count('15')
    BuildTexts.addMacro(subFolder, 'nParticipated', str(men+women))
    BuildTexts.addMacro(subFolder, 'numMen', str(men))
    BuildTexts.addMacro(subFolder, 'numWomen', str(women))


def computeAge(subFolder, statData) :
    values = ParseInput.extractAnswers(statData, [14])
    years = map(StatValues.toNumber, values)
    print '\nYears:', years
    ages = [(2014 - y) for y in years]
    print 'Ages:', ages
    [young, mid, senior, old] = [0,0,0,0]
    for age in ages :
        if age < 25 and age > 12:
            young += 1
        elif age < 36 :
            mid += 1
        elif age < 56 :
            senior += 1
        elif age >= 56 and age < 120:
            old += 1 
    BuildTexts.addMacro(subFolder, 'numYoung', str(young))
    BuildTexts.addMacro(subFolder, 'numMidAge', str(mid))
    BuildTexts.addMacro(subFolder, 'numSenior', str(senior))
    BuildTexts.addMacro(subFolder, 'numOld', str(old))


def computeEducation(subFolder, statData) :
    values = ParseInput.extractAnswers(statData, [15])
    eduValues = []
    for v in values :
        v = v.replace('{','').replace('}','')
        eduList = v.split('=')
        for e in eduList :
            if len(e) > 1 :
                eduValues.append(e)

    keys = [str(i+16) for i in range(7)]
    eduStat = [eduValues.count(key) for key in keys]
    print 'Education values:', eduValues, eduStat
    BuildTexts.addMacrosList(subFolder, 'numEdu', eduStat)


def computeWorkYears(subFolder, statData) :
    values = ParseInput.extractAnswers(statData, [16])
    years = map(StatValues.toNumber, values)
    print '\nExperience:', values, years
    [expA, expB, expC, expD] = [0,0,0,0]
    for y in years :
        if y<0 :
            expA = expA
        elif y < 5 :
            expA += 1
        elif y < 11 :
            expB += 1
        elif y < 21 :
            expC += 1
        elif y>=21 and y<100:
            expD += 1 
    res = [expA, expB, expC, expD]
    BuildTexts.addMacrosList(subFolder, 'numExp', res)


def computeWorkHereYears(subFolder, statData):
    values = ParseInput.extractAnswers(statData, [17])
    years = map(StatValues.toNumber, values)
    print '\nExperience:', values, years
    [expA, expB, expC, expD] = [0,0,0,0]
    for y in years :
        if y<0 :
            expA = expA
        elif y < 5 :
            expA += 1
        elif y < 11 :
            expB += 1
        elif y < 21 :
            expC += 1
        elif y>=21 and y<100:
            expD += 1 
    res = [expA, expB, expC, expD]
    BuildTexts.addMacrosList(subFolder, 'numExpHere', res)


def computeTeachCat(subFolder, statData) :
    values = ParseInput.extractAnswers(statData, [19])
    keys = [str(i+55) for i in range(5)]
    stat = [values.count(key) for key in keys]
    print '\nTeacher categories:', values, stat
    BuildTexts.addMacrosList(subFolder, 'numTechCat', stat)

