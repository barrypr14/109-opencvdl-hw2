import cv2
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage , AnnotationBbox , TextArea
import numpy as np

def stereo_disparity_map() :
    imgL = cv2.imread(r'./Datasets/Q4_Image/imgL.png',0)
    imgR = cv2.imread(r'./Datasets/Q4_Image/imgR.png',0)

    stereo = cv2.StereoBM_create(numDisparities=256, blockSize=15)
    disparity = stereo.compute(imgL,imgR)

    disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    print(disp.shape)
    fig,ax = plt.subplots()
    xy = (2500,1800)
    def onclick(event):
        #print("xdata : " , event.ydata)
        #print("ydata : " , event.xdata)
        
        dd = disp[int(event.ydata)][int(event.xdata)]
        baseline = 178
        focal = 2826
        depth = baseline*focal/(dd+123)
        #print("dd : " , dd)
        if dd == 0 :
            offsetbox = TextArea("disparity : " + str(dd) + "    \ndepth : " + str(int(depth)))
        elif dd > 9 and dd < 99 :
            offsetbox = TextArea("disparity : " + str(dd) + "  \ndepth : " + str(int(depth)))
        else :
            offsetbox = TextArea("disparity : " + str(dd) + "\ndepth : " + str(int(depth)))

        ab = AnnotationBbox(offsetbox,xy)
        ax.add_artist(ab)

        fig.canvas.draw()
    fig.canvas.mpl_connect('button_press_event',onclick)
    plt.imshow(disp,'gray')
    plt.show()