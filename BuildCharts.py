#from pylab import *
#import matplotlib
import shutil
import os
import math


def Pie(subFolder, fileName, data, size = 400):
    
    if data.count(0) == len(data) :
        shutil.copy2(os.path.join(subFolder,'SVG','empty.svg'), os.path.join(subFolder,'SVG',fileName))
    elif data.count(0) == len(data) - 1 :
        shutil.copy2(os.path.join(subFolder,'SVG','pie_yes.svg'), os.path.join(subFolder,'SVG',fileName))
    else :
        total = 0        
        for value in data :
            total = total + value

        cx = int(size/2.0)    # center x
        cy = int(size/2.0)    # center y
        r = int(size/2.0) - 5 # radius

        x1 = cx + r      # start point of the arc 
        y1 = cy          # 
        startAngle = 0

        f_out = open(os.path.join(subFolder, 'SVG', fileName), 'w')
        header = '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
        header = header + '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'
        header = header + '<svg height="' + str(size) + '" width="' + str(size) + '" version="1.1"'
        header = header + ' xmlns="http://www.w3.org/2000/svg">\n\t<desc>Pie chart</desc>\n'
        f_out.write(header)

        colors = ['#A03000','#0030A0','#A0A030','#703030','#1030F0','#209030',]
        for value in data :
            if value > 0 :
                angle = 2.0 * math.pi * value/total;
                endAngle = startAngle + angle
                x2 = cx + int (r * math.cos(endAngle))
                y2 = cy + int (r * math.sin(endAngle))

                if angle < math.pi :
                    flag = '0'
                else :
                    flag = '1'

                d = "M" + str(cx) + "," + str(cy) + " L" + str(x1) + "," + str(y1) + " A" + str(r) + "," + str(r)+ ",0," + flag + ",1," + str(x2) + "," + str(y2) + "Z";
                color = colors.pop()
                res = '\t<path fill="' + color + '" stroke="#000000" d="' + d + '"></path>\n'
                f_out.write(res)

                x1, y1, startAngle = x2, y2, endAngle

        f_out.write('</svg>\n')
        f_out.close()


def YesNoPieSVG(subFolder, fileName, yesNum, noNum, size = 400) :

    print '\nBuilding Yes/No pie:', yesNum, noNum, size
    if (yesNum == 0) and (noNum == 0) :
        shutil.copy2(os.path.join(subFolder,'SVG','empty.svg'), os.path.join(subFolder,'SVG',fileName))
    elif (yesNum == 0) :
        shutil.copy2(os.path.join(subFolder,'SVG','pie_no.svg'), os.path.join(subFolder,'SVG',fileName))
    elif (noNum == 0) :
        shutil.copy2(os.path.join(subFolder,'SVG','pie_yes.svg'), os.path.join(subFolder,'SVG',fileName))
    else :
        cx = int(size/2.0)     # center
        cy = int(size/2.0)
        r = int(size/2.0) - 5  # radius

        x1 = cx + r        # start point
        y1 = cy

        yesP = int(round(100.0 * yesNum/(yesNum + noNum)))
        noP = int(round(100.0 * noNum/(yesNum + noNum)))

        angle = 2.0 * math.pi * noNum/(yesNum + noNum); # the angle

        x2 = cx + int (r * math.cos(angle))
        y2 = cy + int (r * math.sin(angle))

        if angle < math.pi :
            flag0, flag1 = '0', '1'
        else :
            flag0, flag1 = '1', '0'

        # the red and the green parts
        d0 = "M" + str(cx) + "," + str(cy) + " L" + str(x1) + "," + str(y1) + " A" + str(r) + "," + str(r)+ ",0," + flag0 + ",1," + str(x2) + "," + str(y2) + "Z";
        d1 = "M" + str(cx) + "," + str(cy) + " L" + str(x2) + "," + str(y2) + " A" + str(r) + "," + str(r)+ ",0," + flag1 + ",1," + str(x1) + "," + str(y1) + "Z";

        # the text labels
        ang_no_label  = 0.5 * angle 
        ang_yes_label = 0.5 * angle + math.pi
        r_no = 0.7 * r
        r_yes = 0.7 * r  

        no_label_x = cx + int (r_no * math.cos(ang_no_label))
        no_label_y = cy + int (r_no * math.sin(ang_no_label)) + 10
        no_label_svg = '\t<text x="'+ str(no_label_x) +'" y="'+ str(no_label_y) +'" style="text-anchor: middle; font-family:arial; fill:black; font-size: 36px;">'+str(noP)+'%</text>\n'

        yes_label_x = cx + int (r_yes * math.cos(ang_yes_label))
        yes_label_y = cy + int (r_yes * math.sin(ang_yes_label)) + 10
        yes_label_svg = '\t<text x="'+ str(yes_label_x) +'" y="'+ str(yes_label_y) +'" style="text-anchor: middle; font-family:arial; fill:black; font-size: 36px;">'+str(yesP)+'%</text>\n'


        res = '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
        res = res + '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'

        res = res + '<svg height="' + str(size) + '" width="' + str(size) + '" version="1.1"'
        res = res + ' xmlns="http://www.w3.org/2000/svg">\n\t<desc>Yes-no pie chart</desc>\n'
        res = res + '\t<path fill="#FF0000" stroke="#000000" d="' + d0 + '"></path>\n'
        res = res + '\t<path fill="#00FF00" stroke="#000000" d="' + d1 + '"></path>\n'
        res = res + no_label_svg + yes_label_svg
        res = res + '</svg>\n'

        f_out = open(os.path.join(subFolder, 'SVG', fileName), 'w')
        f_out.write(res)
        f_out.close()


