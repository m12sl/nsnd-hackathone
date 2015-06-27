import cv2, cv
import numpy as np
from matplotlib import pyplot as plt


def main():
    img = cv2.imread('7.png')
    cv2.imshow('in', img)
    r,g,b = cv2.split(img)
    gray = cv2.cvtColor(img, cv.CV_BGR2GRAY)
    cv2.imshow('gray',gray)
    cv2.imshow('r', r)
    cv2.imshow('g', g)
    cv2.imshow('b', b)
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    histr = cv2.calcHist([gray],[0],None,[256],[0,256])
    plt.hist(gray.ravel(),256,[0,256])
    plt.show()


    #conv(img)



def conv(img, size = 4):
    x,y,_ = img.shape
    r,g,b = cv2.split(img)
    _,b_t = cv2.threshold(b,50,255,cv2.THRESH_BINARY)
    #cv2.imshow('b_t',b_t)
    out = np.zeros((x,y))
    for i in range(0,x,size):
        for j in range(0,y,size):
            #print i,j
            out[i:i+size,j:j+size] += r[i:i+size,j:j+size]
            out[i:i+size,j:j+size] += b_t[i:i+size,j:j+size]
            out[i:i+size,j:j+size] += b[i:i+size,j:j+size]
    print out
    out = (out/3.0).astype(np.uint8)
    #cv2.imshow('out',out)

def main2():
    img3 = cv2.imread('3.png')
    img4 = cv2.imread('4.png')
    img6 = cv2.imread('6.png')
    img7 = cv2.imread('7.png')
    fuse(img3,img4,img6,img7)


def fuse(img3,img4,img6,img7):
    img3 = cv2.cvtColor(img3, cv.CV_BGR2GRAY).astype(float)
    img4 = cv2.cvtColor(img4, cv.CV_BGR2GRAY).astype(float)
    img6 = cv2.cvtColor(img6, cv.CV_BGR2GRAY).astype(float)
    img7 = cv2.cvtColor(img7, cv.CV_BGR2GRAY).astype(float)


    img4 = 255-img4
    img4[img4 > 240] = 0

    img6 = 255-img6
    img6[img6 > 240] = 0    

    cv2.imshow('img3',img3)
    cv2.imshow('img4',img4)
    cv2.imshow('img6',img6)
    cv2.imshow('img7',img7)

    out = img3 + img4 + img6 + img7

    out -= 300
    out[out<1] =0
    out = (255 * (out) / 385.0).astype(np.uint8)

    return 

if __name__ == "__main__":
    main2()
    cv2.waitKey(0)
    cv2.destroyAllWindows()