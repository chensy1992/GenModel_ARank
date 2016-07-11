from   read_point import  read
from getrank import getrank
from model import  model_SVM_RBF
from model import model_SVM_linear
 
 
homepath = '/home/chensy/python_workspace/SouthPole/modis_read/imgs'
read(homepath)
picpath = '/home/chensy/SouthPoleFile/EnhancedTrainingMODIS'
getrank(picpath)
model_SVM_RBF()
model_SVM_linear()