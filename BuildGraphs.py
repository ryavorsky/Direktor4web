import shutil
import os

def BuildAllGraphs(subFolder, graphData):
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph61.svg'))
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph62.svg'))
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph711.svg'))
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph712.svg'))
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph721.svg'))
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph722.svg'))
