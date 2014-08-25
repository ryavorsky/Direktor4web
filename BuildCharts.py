from pylab import *
import matplotlib
import shutil
import os

def YesNoPie(subFolder, fileName, yesNum = 11, noNum = 5) :

    print '\nBuilding Yes/No pie:', yesNum, noNum, fileName

    if (yesNum == 0) and (noNum == 0) :
        shutil.copy2(os.path.join(subFolder,'empty.png'), os.path.join(subFolder,fileName))
    else :

        matplotlib.rcParams['font.size'] = 32.0
        matplotlib.rcParams['font.family'] = 'Times New Roman'
        fig = figure(1, figsize=(5.5,5.5))

        yes = int(yesNum * 100/(yesNum + noNum))
        fracs = [100 - yes, yes]
        labels = [str(fracs[0]) + '%',str(fracs[1]) + '%']

        if fracs[0] == 0 :
            labels[0] = ''
        if fracs[1] == 0 :
            labels[1] = ''

        colors=['#FF0000' ,'#9BBB00']

        pie(fracs, labels = labels, colors=colors, startangle=90)
        savefig(os.path.join(subFolder,fileName))
        close(1)


def Pie(subFolder, fileName, data):
    print '\nBuilding big pie for:', data, fileName
    matplotlib.rcParams['font.size'] = 32.0
    matplotlib.rcParams['font.family'] = 'Times New Roman'
    fig = figure(1, figsize=(5.5,5.5))

    s = 0.0
    for val in data :
        s = s + int(val)

    if (int(s) == 0) :
        shutil.copy2('empty.png', fileName)
    else :
        fracs = [int(val*100.0/s) for val in data]
        print fracs
        labels = [str(p) + '%' for p in fracs ]

        for i in range(len(fracs)) :
            if fracs[i] == 0 :
                labels[i] = ''
             
        colors=['#997300','#5B9BD5','#ED7D31','#A5A5A5','#FFC000']
        pie(fracs, labels = labels, colors=colors, startangle=90)
        savefig(os.path.join(subFolder,fileName))
    close(1)

