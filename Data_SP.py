import cv2 
import numpy as np 
import matplotlib.pyplot as plt 


img_loc = "./images/vivs1.png"

font = cv2.FONT_HERSHEY_COMPLEX


image = cv2.imread(img_loc, 0) 




img = cv2.imread( img_loc, cv2.IMREAD_GRAYSCALE)
img = cv2.GaussianBlur(img,(5,5),0)

img = cv2.blur(img,(5,5))
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


scale  = []

for cnt in contours:
	approx = cv2.approxPolyDP(cnt, 0.0001*cv2.arcLength(cnt, True), True)

	if (len(approx) == 4 )  and (not ((approx.ravel()[0] == 0) and ( approx.ravel()[1]  == 0))):

		print(approx)

		# top  left corner x coordinate 
		#x1 = approx.ravel()[0] 
		#y1 = approx.ravel()[1]  

		# coordinates of bottom left 

		#x2 = approx.ravel()[2]  
		#y2 = approx.ravel()[3] 


		# coordinates of bottom right  

		#x3 = approx.ravel()[4]  
		#y3 = approx.ravel()[5] 



		# coordinates of top right 

		#x4 = approx.ravel()[6]  
		#y4 = approx.ravel()[7] 

		#         1_______3
		#         |       |
		#         |_______|
        #         2       4

		len_of_y = approx.ravel()[3] - approx.ravel()[1]
		len_of_x = approx.ravel()[6] - approx.ravel()[2]




		for k in range(0,8,2):

			x = approx.ravel()[k]
			y = approx.ravel()[k+1]
			scale.append((x,y))





        #cv2.drawContours(img, [approx], 0, (0), 5)
 

 

        #cv2.putText(img, "Rectangle", (x, y), font, 1, (0))

        

     

#cv2.imshow("shapes", img)
#cv2.imshow("Threshold", threshold)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

  
# Set our filtering parameters 
# Initialize parameter settiing using cv2.SimpleBlobDetector 
params = cv2.SimpleBlobDetector_Params() 
  
# Set Area filtering parameters 
params.filterByArea = True
params.minArea = 50
  
# Set Circularity filtering parameters 
#params.filterByCircularity = True 
#params.minCircularity = 0.8
  
# Set Convexity filtering parameters 
params.filterByConvexity = True
params.minConvexity = 0.8
      
# Set inertia filtering parameters 
params.filterByInertia = True
params.minInertiaRatio = 0.1

#params.filterByCircularity = True 
#params.minCircularity = 0.6
  
# Create a detector with the parameters 
detector = cv2.SimpleBlobDetector_create(params) 
      
# Detect blobs 
keypoints = detector.detect(image) 
  
# Draw blobs on our image as red circles 
blank = np.zeros((1, 1))  
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), 
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
   

l=[]
L = []


  
for k in keypoints :
	#print(k.pt)
	L.append((int(k.pt[0])   , int(k.pt[1])  ))
	Xx = ((int(k.pt[0]) - scale[1][0])/len_of_x)*100

	Yy = (-(int(k.pt[-1]) - scale[1][1] )/len_of_y)*100

	if Xx >= 0 and Yy >=0 :
		l.append((Xx , Yy ))

	


print(L)
print(l)


cv2.imshow("Filtering Circular Blobs Only", blobs) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

 