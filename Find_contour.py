import cv2
import close_window


coin01 = cv2.imread(r'Datasets/Q1_Image/Coin01.jpg')
coin02 = cv2.imread(r'Datasets/Q1_Image/Coin02.jpg')

coin_gray01 = cv2.cvtColor(coin01,cv2.COLOR_BGR2GRAY)
coin_gray02 = cv2.cvtColor(coin02,cv2.COLOR_BGR2GRAY)

coin_blurred01 = cv2.GaussianBlur(coin_gray01,(19,19),0)
coin_blurred02 = cv2.GaussianBlur(coin_gray02,(17,17),0)

coin_binary01 = cv2.Canny(coin_blurred01,30,150)
coin_binary02 = cv2.Canny(coin_blurred02,30,150)

contours01 = cv2.findContours(coin_binary01,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours02 = cv2.findContours(coin_binary02,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 

coin_num01 = len(contours01[1][0])
coin_num02 = len(contours02[1][0])

coin01_marked = coin01.copy()
coin02_marked = coin02.copy()

cv2.drawContours(coin01_marked , contours01[0] , -1 , (0,0,255),1)
cv2.drawContours(coin02_marked , contours02[0] , -1 , (0,0,255) ,1 )
"""for i in range(1,len(contours01[1])) :
    if contours01[2][0][i][3] != -1 :
        cv2.drawContours(coin01_marked,contours01[1],i,(0,0,255),1)
        coin_num01 = coin_num01 + 1

for i in range(1,len(contours02[1])) :
    if contours02[2][0][i][3] != -1 :
        cv2.drawContours(coin02_marked,contours02[1],i,(0,0,255),1)
        coin_num02 = coin_num02 + 1"""


def draw_contours() :
    cv2.imshow('origin Coin01.jpg',coin01)
    cv2.imshow('draw contours Coin01.jpg',coin01_marked)
    cv2.imshow('origin Coin02.jpg',coin02)
    cv2.imshow('draw contours Coin02.jpg',coin02_marked)
    close_window.close()
    cv2.destroyAllWindows()

def count_contours() :
    return coin_num01 , coin_num02


    
