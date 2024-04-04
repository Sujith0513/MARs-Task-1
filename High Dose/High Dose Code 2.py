import cv2
image=cv2.imread('test.png')
for i in range(len(image)):
    for j in range(len(image[i])):
        br=(0.21*image[i][j][0] +0.72*image[i][j][1] + 0.02*image[i][j][2])/3
        if br>50:
            image[i][j]=[0,0,0]
        else:
            image[i][j]=[255,255,255]
cv2.imshow("image",image)
cv2.waitKey(0)

