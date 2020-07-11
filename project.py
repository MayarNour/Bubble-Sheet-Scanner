import numpy as np
import cv2

nameimage = str(input("Enter image name:"))
image = cv2.imread(nameimage,0)
kernel =cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 5))
image = cv2.dilate(image,kernel) #we dilate image to remove pepper noise
gray = cv2.cvtColor(image, cv2.COLOR_BayerRG2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0) #blurring the image to have smooth edged using cannyy
cv2.imwrite("GaussianBlur.jpg",blurred)
edged = cv2.Canny(blurred, 75, 200) #output of canny edges
cv2.imwrite("edgesOfCanny.jpg",edged)
Result = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
Result1 = ["0","0","0"]
gray1 = cv2.bitwise_not(gray)

thresh1 = cv2.threshold(gray1, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] #thresholding the image to use it while rotating.
######rotating the imgage#######
coords = np.column_stack(np.where(thresh1 > 0))
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle
(h, w) = image.shape[:2]
center = tuple(np.array(image.shape[1::-1]) / 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
image = cv2.warpAffine(image, M,image.shape[1::-1],flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
gray = cv2.warpAffine(gray, M,image.shape[1::-1],flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
##################################
cv2.imwrite("Rotatedimage.png",image) #the result of rotating the original image
cv2.imwrite("Rotatedgrayimage.png",gray) #the resultof rotating  after converting to gray scale


gray_blurred = cv2.blur(gray, (3, 3)) #make blur by filter 3*3
#hought detection circle#
detected_circles = cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT, 1, 20, param1=50,param2=30, minRadius=1, maxRadius=25)
f=open("Resultfile.txt","w+")
i=0
y=0
if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        cv2.circle(image, (a, b), r, (255, 255, 255), 2)
        cv2.circle(image, (a, b), 1, (0, 0, 255), 3)
        # print x coorinateof detected circle
        cv2.putText(image,str(a), (a+30, b), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (80,170, 89), 2,1)
        # print y coorinateof detected circle
        cv2.putText(image, str(b), (a, b+30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (80,170, 89), 2, 1)
        if (a > 380 and b>580):
            ##ranges to detect from 1 to 5
                if(a>1100 and a<1200):
                    if (b > 950 and b < 999):
                        Result[0] = "Question 1.1:Strongly agree"
                    if (b > 999 and b < 1030):
                        Result[1] = "Question 1.2:Strongly agree"
                    if (b > 1030 and b < 1075):
                        Result[2] = "Question 1.3:Strongly agree"
                    if (b > 1075 and b < 1110):
                        Result[3] = "Question 1.4:Strongly agree"
                    if (b > 1110 and b < 1150):
                        Result[4] = "Question 1.5:Strongly agree"
                    if (b > 1150 and b < 1265):
                        Result[5] = "Question 2.1:Strongly agree"
                    if (b > 1265 and b < 1315):
                        Result[6] = "Question 2.2:Strongly agree"
                    if (b > 1315 and b < 1355):
                        Result[7] = "Question 2.3:Strongly agree"
                    if (b > 1355 and b < 1385):
                        Result[8] = "Question 2.4:Strongly agree"
                    if (b > 1385 and b < 1430):
                        Result[9] = "Question 2.5:Strongly agree"
                    if (b > 1430 and b < 1480):
                        Result[10] = "Question 2.6:Strongly agree"
                    if (b > 1480 and b < 1585):
                        Result[11] = "Question 3.1:Strongly agree"
                    if (b > 1585 and b < 1625):
                        Result[12] = "Question 3.2:Strongly agree"
                    if (b > 1625 and b < 1670):
                        Result[13] = "Question 3.3:Strongly agree"
                    if (b > 1670 and b < 1790):
                        Result[14] = "Question 4.1:Strongly agree"
                    if (b > 1790 and b < 1830):
                        Result[15] = "Question 4.2:Strongly agree"
                    if (b > 1830 and b < 1910):
                        Result[16] = "Question 4.3:Strongly agree"
                    if (b > 1910 and b < 2022):
                        Result[17] = "Question 5.1:Strongly agree"
                    if (b > 2022):
                        Result[18] = "Question 5.2:Strongly agree"
                if(a>1200 and a<1300):
                    if (b > 950 and b < 999):
                        Result[0] = "Question 1.1:agree"
                    if (b > 999 and b < 1030):
                        Result[1] = "Question 1.2:agree"
                    if (b > 1030 and b < 1075):
                        Result[2] = "Question 1.3:agree"
                    if (b > 1075 and b < 1110):
                        Result[3] = "Question 1.4:agree"
                    if (b > 1110 and b < 1150):
                        Result[4] = "Question 1.5:agree"
                    if (b > 1150 and b < 1265):
                        Result[5] = "Question 2.1:agree"
                    if (b > 1265 and b < 1315):
                        Result[6] = "Question 2.2:agree"
                    if (b > 1315 and b < 1355):
                        Result[7] = "Question 2.3:agree"
                    if (b > 1355 and b < 1385):
                        Result[8] = "Question 2.4:agree"
                    if (b > 1385 and b < 1430):
                        Result[9] = "Question 2.5:agree"
                    if (b > 1430 and b < 1480):
                        Result[10] = "Question 2.6:agree"
                    if (b > 1480 and b < 1585):
                        Result[11] = "Question 3.1:agree"
                    if (b > 1585 and b < 1625):
                        Result[12] = "Question 3.2:agree"
                    if (b > 1625 and b < 1670):
                        Result[13] = "Question 3.3:agree"
                    if (b > 1670 and b < 1790):
                        Result[14] = "Question 4.1:agree"
                    if (b > 1790 and b < 1830):
                        Result[15] = "Question 4.2:agree"
                    if (b > 1830 and b < 1910):
                        Result[16] = "Question 4.3:agree"
                    if (b > 1910 and b < 2022):
                        Result[17] = "Question 5.1:agree"
                    if (b > 2022):
                        Result[18] = "Question 5.2:agree"
                if (a > 1300 and a < 1400):
                    if (b > 950 and b < 999):
                        Result[0] = "Question 1.1:Neutral"
                    if (b > 999 and b < 1030):
                        Result[1] = "Question 1.2:Neutral"
                    if (b > 1030 and b < 1075):
                        Result[2] = "Question 1.3:Neutral"
                    if (b > 1075 and b < 1110):
                        Result[3] = "Question 1.4:Neutral"
                    if (b > 1110 and b < 1150):
                        Result[4] = "Question 1.5:Neutral"
                    if (b > 1150 and b < 1265):
                        Result[5] = "Question 2.1:Neutral"
                    if (b > 1265 and b < 1315):
                        Result[6] = "Question 2.2:Neutral"
                    if (b > 1315 and b < 1355):
                        Result[7] = "Question 2.3:Neutral"
                    if (b > 1355 and b < 1385):
                        Result[8] = "Question 2.4:Neutral"
                    if (b > 1385 and b < 1430):
                        Result[9] = "Question 2.5:Neutral"
                    if (b > 1430 and b < 1480):
                        Result[10] = "Question 2.6:Neutral"
                    if (b > 1480 and b < 1585):
                        Result[11] = "Question 3.1:Neutral"
                    if (b > 1585 and b < 1625):
                        Result[12] = "Question 3.2 :Neutral"
                    if (b > 1625 and b < 1670):
                        Result[13] = "Question 3.3:Neutral"
                    if (b > 1670 and b < 1790):
                        Result[14] = "Question 4.1:Neutral"
                    if (b > 1790 and b < 1830):
                        Result[15] = "Question 4.2:Neutral"
                    if (b > 1830 and b < 1910):
                        Result[16] = "Question 4.3:Neutral"
                    if (b > 1910 and b < 2022):
                        Result[17] = "Question 5.1:Neutral"
                    if (b > 2022):
                        Result[18] = "Question 5.2:Neutral"
                if (a > 1400 and a < 1500):
                    if (b > 950 and b < 999):
                        Result[0] = "Question 1.1: disagree"
                    if (b > 999 and b < 1030):
                        Result[1] = "Question 1.2:disagree"
                    if (b > 1030 and b < 1075):
                        Result[2] = "Question 1.3:disagree"
                    if (b > 1075 and b < 1110):
                        Result[3] = "Question 1.4: disagree"
                    if (b > 1110 and b < 1150):
                        Result[4] = "Question 1.5:disagree"
                    if (b > 1150 and b < 1265):
                        Result[5] = "Question 2.1:disagree"
                    if (b > 1265 and b < 1315):
                        Result[6] = "Question 2.2:disagree"
                    if (b > 1315 and b < 1355):
                        Result[7] = "Question 2.3:disagree"
                    if (b > 1355 and b < 1385):
                        Result[8] = "Question 2.4:disagree"
                    if (b > 1385 and b < 1430):
                        Result[9] = "Question 2.5:disagree"
                    if (b > 1430 and b < 1480):
                        Result[10] = "Question 2.6:disagree"
                    if (b > 1480 and b < 1585):
                        Result[11] = "Question 3.1:disagree"
                    if (b > 1585 and b < 1625):
                        Result[12] = "Question 3.2:disagree"
                    if (b > 1625 and b < 1670):
                        Result[13] = "Question 3.3:disagree"
                    if (b > 1670 and b < 1790):
                        Result[14] = "Question 4.1:disagree"
                    if (b > 1790 and b < 1830):
                        Result[15] = "Question 4.2:disagree"
                    if (b > 1830 and b < 1910):
                        Result[16] = "Question 4.3:disagree"
                    if (b > 1910 and b < 2022):
                        Result[17] = "Question 5.1:disagree"
                    if (b > 2022):
                        Result[18] = "Question 5.2:Disagree"
                if(a > 1500):
                    if (b > 950 and b < 999):
                        Result[0] = "Question 1.1:Strongly disagree"
                    if (b > 999 and b < 1030):
                        Result[1] = "Question 1.2:Strongly disagree"
                    if (b > 1030 and b < 1075):
                        Result[2] = "Question 1.3:Strongly disagree"
                    if (b > 1075 and b < 1110):
                        Result[3] = "Question 1.4:Strongly disagree"
                    if (b > 1110 and b < 1150):
                        Result[4] = "Question 1.5:Strongly disagree"
                    if (b > 1150 and b < 1265):
                        Result[5] = "Question 2.1:Strongly disagree"
                    if (b > 1265 and b < 1315):
                        Result[6] = "Question 2.2:Stronglydisagree"
                    if (b > 1315 and b < 1355):
                        Result[7] = "Question 2.3:Stronglydisagree"
                    if (b > 1355 and b < 1385):
                        Result[8] = "Question 2.4:Stronglydisagree"
                    if (b > 1385 and b < 1430):
                        Result[9] = "Question 2.5:Stronglydisagree"
                    if (b > 1430 and b < 1480):
                        Result[10] = "Question 2.6:Stronglydisagree"
                    if (b > 1480 and b < 1585):
                        Result[11] = "Question 3.1:Stronglydisagree"
                    if (b > 1585 and b < 1625):
                        Result[12] = "Question 3.2 :Stronglydisagree"
                    if (b > 1625 and b < 1670):
                        Result[13] = "Question 3.3:Strongly disagree"
                    if (b > 1670 and b < 1790):
                        Result[14] = "Question 4.1:Strongly disagree"
                    if (b > 1790 and b < 1830):
                        Result[15] = "Question 4.2:Strongly disagree"
                    if (b > 1830 and b < 1910):
                        Result[16] = "Question 4.3:Strongly disagree"
                    if (b > 1910 and b < 2022):
                        Result[17] = "Question 5.1:Strongly disagree"
                    if (b > 2022 ):
                        Result[18] = "Question 5.2:Strongly Disagree"
            ##ranges to detect above Question
        if(a>380 and b>260 and b<530):
                if(b>260 and b<350):
                    ##ranges to detect geneder Question
                    if(a>1200and a<1370):
                        Result1[0]="Gender:Male"
                    if(a>1370):
                        Result1[0] = "Gender:Female"
                if(b>355 and b<400):
                    ##ranges to detect semester Question
                    if(a>530 and a<600):
                        Result1[1] = "Semester:Fall"
                    elif(a>1070):
                        Result1[1] = "Semester:Summer"
                    else:
                        Result1[1] = "Semester:Spring"
                if (b > 440 and b < 475):
                    ##ranges to detect department Question
                    if (a>390 and a<560):
                        Result1[2] = "Department: MCTA"
                    if (a>560 and a<610):
                        Result1[2] = "Department: ENVER"
                    if (a>700 and a<740):
                        Result1[2] = "Department: BLDG"
                    if (a>740 and a<870):
                        Result1[2] = "Department: CESS"
                    if (a>870 and a<1000):
                        Result1[2] = "Department: ENRG"
                    if (a>1000 and a<1130):
                        Result1[2] = "Department: COMM"
                    if (a>1130):
                        Result1[2] = "Department: MANF"
                if (b > 475 and b < 520):
                    if (a > 390 and a < 560):
                        Result1[2] = "Department: LAAR"
                    if (a > 560 and a < 610):
                        Result1[2] = "Department: MATL"
                    if (a > 700 and a < 740):
                        Result1[2] = "Department: CISE"
                    if (a>740 and a<870):
                        Result1[2] = "Department: HAUD"

        cv2.imwrite("Hough answers.png", image)
        #putting result of array in the file
for x in Result1:
  f.write (Result1[y]+"\n")
  y=y+1
for x in Result:
  f.write (Result[i]+"\n")
  i=i+1
f.close()
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
img = cv2.dilate(image, kernel3)
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
img = cv2.erode(image, kernel2)
cv2.imwrite("hough answers.png", image)
cv2.waitKey()
