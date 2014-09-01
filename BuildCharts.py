#from pylab import *
#import matplotlib
import shutil
import os
import math

def YesNoPie(subFolder, fileName, yesNum = 11, noNum = 5) :
    shutil.copy2(os.path.join(subFolder,'diag.png'), os.path.join(subFolder,fileName))
    return

def Pie(subFolder, fileName, data):
    shutil.copy2(os.path.join(subFolder,'empty.svg'), os.path.join(subFolder,fileName))
    return



def YesNoPieSVG(subFolder = 'c:\\tmp\\', fileName = 'pie1.svg', yesNum = 27, noNum = 5, size = 400) :

    print '\nBuilding Yes/No pie:', yesNum, noNum, size
    if (yesNum == 0) and (noNum == 0) :
        shutil.copy2(os.path.join(subFolder,'empty.svg'), os.path.join(subFolder,fileName))
    elif (yesNum == 0) :
        shutil.copy2(os.path.join(subFolder,'pie_no.svg'), os.path.join(subFolder,fileName))
    elif (noNum == 0) :
        shutil.copy2(os.path.join(subFolder,'pie_yes.svg'), os.path.join(subFolder,fileName))
    else :
        cx = int(size/2.0)
        cy = int(size/2.0)
        r = int(size/2.0) - 5

        x1 = cx + r
        y1 = cy

        angle = 2.0 * math.pi * noNum/(yesNum + noNum);

        x2 = cx + int (r * math.cos(angle))
        y2 = cy + int (r * math.sin(angle))

        if (x1 == x2) and (y1 == y2) :
            x2 = x1 - 1

        if angle < math.pi :
            flag0, flag1 = '0', '1'
        else :
            flag0, flag1 = '1', '0'

        d0 = "M" + str(cx) + "," + str(cy) + " L" + str(x1) + "," + str(y1) + " A" + str(r) + "," + str(r)+ ",0," + flag0 + ",1," + str(x2) + "," + str(y2) + "Z";
        d1 = "M" + str(cx) + "," + str(cy) + " L" + str(x2) + "," + str(y2) + " A" + str(r) + "," + str(r)+ ",0," + flag1 + ",1," + str(x1) + "," + str(y1) + "Z";

        res = '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
        res = res + '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'

        res = res + '<svg height="' + str(size) + '" width="' + str(size) + '" version="1.1"'
        res = res + ' xmlns="http://www.w3.org/2000/svg">\n\t<desc>Yes-no pie chart</desc>\n'
        res = res + '\t<path fill="#FF0000" stroke="#000000" d="' + d0 + '"></path>\n'
        res = res + '\t<path fill="#00FF00" stroke="#000000" d="' + d1 + '"></path>\n'
        res = res + '</svg>\n'

        f_out = open(os.path.join(subFolder, fileName), 'w')
        f_out.write(res)
        f_out.close()


