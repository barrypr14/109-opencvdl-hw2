import cv2
import numpy as np
import close_window
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pylab

def augmented_reality() :
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((8*11,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)


    axis = np.float32([[3,3,-3]])
 
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space #有定位real world的坐標系從(0,0,0)
    imgpoints = [] # 2d points in image plane.

    img = []
    gray = []
    for i in range(1,6) :
        tmp = cv2.imread(r'./Datasets/Q3_Image/'+ str(i) + '.bmp' )
        img.append(tmp)

        gray_tmp = cv2.cvtColor(img[i-1],cv2.COLOR_BGR2GRAY)
        gray.append(gray_tmp)
        
        ret , corner = cv2.findChessboardCorners(img[i-1],(11,8),None)

        if ret == True :
            objpoints.append(objp)
            corner2 = cv2.cornerSubPix(gray[i-1],corner,(11,11),(-1,-1),criteria)

            imgpoints.append(corner2)


    ret, intrinsic_mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray[0].shape[::-1], None, None) ##可得intrinsic matrix

    def draw(img, corners, imgpts):
        #corner = tuple(corners[0].ravel()) #取real world的原點為起點開始畫
        img = cv2.line(img, tuple(corners[12].ravel()), tuple(corners[58].ravel()), (0,0,255), 5)
        img = cv2.line(img, tuple(corners[58].ravel()), tuple(corners[16].ravel()), (0,0,255), 5)
        img = cv2.line(img, tuple(corners[16].ravel()), tuple(corners[12].ravel()), (0,0,255), 5)

        img = cv2.line(img, tuple(corners[12].ravel()), tuple(imgpts.ravel()), (0,0,255), 5)
        img = cv2.line(img, tuple(corners[58].ravel()), tuple(imgpts.ravel()), (0,0,255), 5)
        img = cv2.line(img, tuple(corners[16].ravel()), tuple(imgpts.ravel()), (0,0,255), 5)
        return img

    i = 0
    while(True) :
        if i == 6 :
            break
        else :
            imgpts, jac = cv2.projectPoints(axis, rvecs[i-1], tvecs[i-1], intrinsic_mtx, dist)

            tmp = draw(img[i-1],imgpoints[i-1],imgpts)  
            plt.imshow(tmp)
            plt.pause(1)
            plt.clf()
            i += 1
    
    #ani = animation.ArtistAnimation(fig,ims,interval=500,repeat_delay=1000)   
    #plt.show()

"""    for i in range(1,6) : 
        imgpts, jac = cv2.projectPoints(axis, rvecs[i-1], tvecs[i-1], intrinsic_mtx, dist)

        tmp = draw(img[i-1],imgpoints[i-1],imgpts)
        cv2.namedWindow("img" , cv2.WINDOW_NORMAL)
        cv2.resizeWindow('img',tmp.shape[0],tmp.shape[1])
        cv2.imshow('img',tmp)
        cv2.waitKey(500)
        cv2.destroyAllWindows()"""
