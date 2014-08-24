# Convert the inputraw data into the internal data representation
import os

def DataFromFile(rawData, subFolder):
    print '\nParsing data. Folder:', subFolder

    # Get questions specs from key.txt
    keys = extractKeys(subFolder)
    dataFileName = os.path.join(subFolder, 'data.txt')
    f_data = open(dataFileName, 'w')

    graphData = []
    statData = []

    toprow = rawData[0]
    N = len(rawData) - 1
    localId = 0

    for line in rawData[1:N] :
        dataline = extractDataLine(line, keys)
        statData.append(dataline)
        f_data.write(dataline + '\n')

        localId += 1
        graphline = extractGraphDataBlock(dataline, localId)
        graphData.append(graphline)

    f_data.close()

    # Filter graph data according to the Nodes number
    graphData = restrictOutEdges(graphData)

    return [graphData, statData]


def extractGraphDataBlock(dataline, localId) :

    id = extractAnswers([dataline], [5])[0]
    name = extractAnswers([dataline], [6])[0]
    position = extractAnswers([dataline], [7])[0]
    year = extractAnswers([dataline], [14])[0]
    if len(year) == 4 :
        age = 2014 - int(year)
    else :
        age = 0
        print 'Age is unknown for', id, name

    edgeGroups = extractEdgeGroups(dataline)

    return [ id, str(localId), name + position, age, edgeGroups ]


# nine sequences of edge targets for the nine questions
def extractEdgeGroups(dataline):
    data = dataline.split('\t')
    res = []
    for i in range(9) : # there are 9 quesions
        group = []
        for k in range(5) : # max 5 answers
            questionId = 62 + 10*i + k*2 + 1
            node = data[questionId].split('=')[1]
            if len(node) > 1 :
                group.append(node)
        res.append(group)
    print '\nEdge groups', res
    return res


# for small schools truncate the socio answers
def restrictOutEdges(graphData):
    # first, compute the restriction  
    numOfNodes = len(graphData)
    if numOfNodes <= 7 :
        maxNumOfEdges = 0
    elif numOfNodes <= 11 :
        maxNumOfEdges = 2
    elif numOfNodes <= 16 :
        maxNumOfEdges = 3
    elif numOfNodes <= 21 :
        maxNumOfEdges = 4
    else :
        maxNumOfEdges = 5

    for node in range(len(graphData)):
        for question in range(9) :
            graphData[node][4][question] = graphData[node][4][question][0:(maxNumOfEdges)]

    return graphData


def extractKeys(subFolder) :

    print '\nExtracting keys'
    res = []    
    fileName = os.path.join(subFolder, 'key.txt')
    f = open (fileName, 'r')
    line = f.readline() # skip the table header
    for line in f.readlines() :
        res.append( line.split('\t') )
    f.close()
    return res


def extractDataLine(line, keys):
    res = line.split(';')

    if len(res) == len(keys) :
        for i in range(len(res)) :
            res[i] = extractDataValue(res[i], keys[i])
        print '\nExtracted data line', res
        return '\t'.join(res)
    else :
        print 'Keys lenght is wrong', len(res), len(keys)


def extractDataValue(value, key):
    listId = int(key[2])
    questionId = 'q' + key[0]

    res = value.strip()
    if listId != 0 and value != '':
        options = key[3].strip().split(';')
        optionId = [option.split(':')[0] for option in options]
        optionVal = [option.split(':')[1].strip() for option in options]
        for i in range(len(options)) :
            if res == optionVal[i] :
                res = optionId[i]
        
    return questionId + '=' + res

def extractAnswers(statData, questionNumbers) :
    res = []
    for line in statData :
        ans = []
        for n in questionNumbers :
            que = 'q'+str(n)+ '='
            pos1 = line.find(que) + len(que)
            value = line[pos1:(pos1+10)].split('\t')[0]
            ans.append(value)
        if len(questionNumbers) == 1 :
            res.append(ans[0])
        else :
            res.append(ans)

    print 'Extracted answers for', questionNumbers, ':\n', res
    return res


