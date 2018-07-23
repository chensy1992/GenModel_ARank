import numpy as np
from PIL import Image
import os
from os import path

# this is a test
labels = ["sea", "block ice", "paper cloud", "thick cloud", "trash ice"]

img_path = "imgs"
if not path.exists(img_path):
    os.mkdir(img_path)

img_path_pri = "imgs_pri"
if not path.exists(img_path_pri):
    os.mkdir(img_path_pri)

for label in labels:
    label_img_path = path.join(img_path, label)
    if not path.exists(label_img_path):
        os.mkdir(label_img_path)


for label in labels:
    label_img_path_pri = path.join(img_path_pri, label)
    if not path.exists(label_img_path_pri):
        os.mkdir(label_img_path_pri)

class GetPoint():
    """docstring for """
    def __init__(self, imgname_list, xlist, ylist, labellist, file, angs = [0,15,30,45,60,75,90], crop_size = 20, box_size = 200):
        self.imgname_list = imgname_list
        self.xlist = xlist
        self.ylist = ylist
        self.box_size = box_size
        self.crop_size = crop_size
        self.angs = angs
        self.labellist = labellist
        self.file = file

    def camsvd(self, cropimg):
        #aimg = np.array(cropimg.convert('L'))
        aimg = np.array(cropimg)
        U, s, V = np.linalg.svd(aimg)
        s90 = 0
        c90 = 0
        sums = sum(s)
        for ss in s:
            s90 += ss
            c90 += 1
            if s90 >= sums * 0.95:
            	break
        return c90

    def circle(self, img, sx, sy, ex, ey):

        color = int('0xFFFF00', 16)
        for i in range(sx, ex):
            try:
                img.putpixel([i, sy], color)
            except Exception as e:
                print('i', i, 'sy', sy)
                exit()

        for i in range(sx, ex):
            img.putpixel([i, ey], color)

        for i in range(sy, ey):
            img.putpixel([sx, i], color)

        for i in range(sy, ey):
            img.putpixel([ex, i], color)
        return img

    def camcolor(self, cropimg):
        aimg = np.array(cropimg)
        gray = np.mean(aimg)
        colar_var = np.std(aimg)
        return gray, colar_var

    def sampling(self):

        csx = int(self.box_size/2 - self.crop_size / 2)
        csy = int(self.box_size/2 - self.crop_size / 2)
        cex = csx + self.crop_size
        cey = csy + self.crop_size
        cbox = (csx, csy, cex, cey)

        imgs = []
        iii = 0
        for imgname in self.imgname_list:
            print('imgname: ', imgname)
            imgs.append(Image.open(imgname).convert('L'))
            p, filename = os.path.split(imgname)

            # imgs[iii].save(filename)
            iii += 1
        #file = open('ranks.txt', 'w')

        for ii in range(len(self.xlist)):
                feature = []
                i = int(self.xlist[ii])
                vec = np.zeros(7, int)
                j = int(self.ylist[ii])
                cla = self.labellist[ii].strip()
                if cla == 'sea':
                    label = 1
                elif cla == 'paper cloud' or cla == 'trash ice':
                    label = 2
                elif cla == "thick cloud" or cla == "block ice":
                    label = 3
                for ni in range(len(self.imgname_list)):
                    imgname = self.imgname_list[ni]
                    img = imgs[ni]
                    p, filename = os.path.split(imgname)

                    oneimagepath = path.join(img_path, cla, filename +
                            "_{}_{}".format(i, j))
                    # print('oneimagepath', oneimagepath)
                    if not path.exists(oneimagepath):
                        os.mkdir(oneimagepath)

                    oneimagepath_pri = path.join(img_path_pri, cla, filename +
                            "_{}_{}_pri".format(i, j))

                    if not path.exists(oneimagepath_pri):
                        os.mkdir(oneimagepath_pri)

                    bsx = int(i - self.box_size / 2)
                    bex = int(i + self.box_size / 2)
                    bsy = int(j - self.box_size / 2)
                    bey = int(j + self.box_size / 2)
                    box = (bsx, bsy, bex, bey)

                    img_box = img.crop(box)
                    '''
                    loc = imgname + '_' + str(bsx) + '_' + str(bsy) + '_' + str(bex) + '_' + str(bey)
                    spath = path.join(oneimagepath, loc)
                    if not path.exists(spath):
                        os.mkdir(spath)
                    spath_pri = path.join(oneimagepath_pri, loc)
                    if not path.exists(spath_pri):
                        os.mkdir(spath_pri)
                    spath_pri_img = path.join(spath_pri, imgname)
                    # img_box.save(spath_pri_img)

                    '''
                    a = 0
                    for ang in self.angs:


                        rimg = img_box.rotate(ang)
                        cropimg = rimg.crop(cbox)
                        '''
                        save_path = path.join(spath, str(ang) + '.jpg')
                        save_path_pri = path.join(spath_pri, str(ang) + '.jpg')

                        # cropimg.save(save_path)
                        pixmap = self.circle(rimg, csx, csy, cex, cey)
                        # pixmap.save(save_path_pri)
                        # savepath = path.join(spath, str(ang) + '.jpg')
                        # cropimg.save(savepath)
                        # cropimg = Image.open(savepath)
                        # savepath_pri = path.join(spath_pri, str(ang) + '.jpg')
                        # cropimg.save(savepath_pri)
                        '''
                        vec[a] = self.camsvd(cropimg)

                        if a == 0:
                            gray, color_var = self.camcolor(cropimg)
                        a += 1

                    feature.extend(vec)
                    feature.append(gray)
                    feature.append(color_var)
                feature.append(label)
                self.file.writelines(["%s " % item for item in feature])
                self.file.write('\n')
