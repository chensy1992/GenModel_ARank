import os
import sys
from os import path
import shutil

# info=os.getcwd()
# listfile=os.listdir(os.getcwd())
# info = raw_input("请输入要列举文件的目录：(如D:\\temp)")
#homepath = '/home/fany/Workplace/modis_feature/imgs'

#homepath = '/home/fany/Workplace/modis_feature/imgs'

def  read(homepath):	
	listclass = os.listdir(homepath)
	print('listclass', listclass)
	pointpath = 'Points'
	if path.exists(pointpath):
	    shutil.rmtree(pointpath)#删除
	os.mkdir(pointpath)
	["sea", "block ice", "paper cloud", "thick cloud", "trash ice"]
	for cla in listclass:
	    print(cla)
	    classpath = path.join(homepath, cla)
	    points = os.listdir(classpath)
	    for point in points:
	        #print('point', point)
	        line = point.split('_')
	        picname = path.join(pointpath, line[0] + '_' + line[1])
	        xcenter = line[3]
	        ycenter = line[4]
	        if not path.exists(picname):
	            f = open(picname, 'w')
	            f.write(xcenter + ',' + ycenter + ',' + cla + '\n')
	            f.close()
	        else:
	            f = open(picname, 'a')
	            f.write(xcenter + ',' + ycenter + ',' + cla + '\n')
	            f.close()


def main():
	homepath = '/home/chensy/桌面/imgs'
	read(homepath)

if __name__ == '__main__':
	main()
