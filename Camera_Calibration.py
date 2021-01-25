import cv2
import matplotlib.pyplot as plt
#import pylab
import numpy as np
import close_window
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((8*11,3), np.float32)
objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space #有定位real world的坐標系從(0,0,0)
imgpoints = [] # 2d points in image plane.

img = []
gray = []
for i in range(1,16) :
    tmp = cv2.imread(r'./Datasets/Q2_Image/'+ str(i) + '.bmp' )
    img.append(tmp)

    gray_tmp = cv2.cvtColor(img[i-1],cv2.COLOR_BGR2GRAY)
    gray.append(gray_tmp)
    
    ret , corner = cv2.findChessboardCorners(img[i-1],(11,8),None)

    if ret == True :
        objpoints.append(objp)
        #corner2 = cv2.cornerSubPix(gray[i-1],corner,(11,8),(-1,-1),criteria)
        imgpoints.append(corner)
        cv2.drawChessboardCorners(img[i-1],(11,8),corner,ret)

def find_corners() :
    plt.ion()
    for i in range(1,16) :
        plt.imshow(img[i-1])
        plt.show()
        plt.pause(1)      
        plt.clf()

"""        cv2.namedWindow("find corner" , cv2.WINDOW_NORMAL)
        cv2.resizeWindow('find corner',img[i-1].shape[0],img[i-1].shape[1])
        cv2.imshow('find corner',img[i-1])
        close_window.close()
        cv2.destroyAllWindows()"""

ret, intrisic_mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray[0].shape[::-1], None, None) ##可得intrinsic matrix

def find_intrinsic() :
    np.set_printoptions(suppress=True)
    print("intrinsic_matrix : \n" , np.around(intrisic_mtx , decimals = 5))

def find_extrinsic(number) :
    rvecs_3x3  , jacobian = cv2.Rodrigues(rvecs[number-1],None,None) ##可得extrinsic matrix 之 rotation matrix
    extrinsic_mtx = np.hstack((rvecs_3x3,tvecs[number-1]))
    print("extrinsic matrix : \n" , extrinsic_mtx)

def find_distortion() :
    print("distortion matrix : " , dist)
