import os
from GetPoint import GetPoint

def getrank(picpath):
    crop_size = 20
    box_size = crop_size * 10
    homepath = 'Points'
    listpic = os.listdir(homepath)
    fi = open('ranks.txt', 'w')
    for pic in listpic:
        xlist = []
        ylist = []
        labellist = []
        filename = os.path.join(homepath, pic)
        f = open(filename, 'r')
        for line in f:
            ls = line.strip().split(',')
            xlist.append(int(ls[0]))
            ylist.append(int(ls[1]))
            labellist.append(ls[2])
        f.close()

        imgname_list = []
        pic_split = pic.split('_')
        w_picname = os.path.join(picpath, pic_split[0] + '_band1_8bit.tif')
        imgname_list.append(w_picname)

        pic_split = pic.split('_')
        w_picname2 = os.path.join(picpath, pic_split[0] + '_band2_8bit.tif')
        imgname_list.append(w_picname2)
        gp = GetPoint(imgname_list, xlist, ylist, labellist, fi)
        gp.sampling()

def main():
  picpath = '//home/chensy/SouthPoleFile/tiff'
  getrank(picpath)


if __name__ == '__main__':
    main()
