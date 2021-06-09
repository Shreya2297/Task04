#!/usr/bin/env python
# coding: utf-8

# In[21]:


#importing libraries
import numpy as np
import cv2 as cv


# In[23]:


#creating a blank black colored image
blank=np.zeros((500,500,3),dtype='uint8') 
#creating a rectangle on left side vertically
blank=cv.rectangle(blank,(0,0),(250,500),(49,99,53),thickness=-1)
#creating a rectangle on right side vertically
blank=cv.rectangle(blank,(250,0),(500,500),(99,53,49),thickness=-1)
#drawing a big circle
blank=cv.circle(blank,(250,250),250,(255,255,255),thickness=-1)
#drawing a small circle
blank=cv.circle(blank,(250,250),125,(27,27,27),thickness=-1)
# Drawing an orange line top-left
cv.line(blank, (0,250), (250,0), (0,100,255), (5))
# Drawing an orange line bottom-right
cv.line(blank, (500,250), (250,500), (0,100,255), (5))
# Drawing an orange line top-right
cv.line(blank, (250,0), (500,250), (0,100,255), (5))
# Drawing an orange line bottom-right
cv.line (blank, (0,250), (250,500), (0,100,255), (5))
#drawing a smaller circle
cv.circle(blank,(250,250),50,(255,255,255),thickness=-1)
cv.imshow('Custom image', blank)
cv.waitKey(0) #to hold the photo
cv.destroyAllWindows() #to close the window


# In[25]:


img1 = cv.imread('starry.jpg')
img2 = cv.imread('mlisa.jpg')
print(img1.shape)
print(img2.shape)

    


# In[26]:


#extracting starry image by cropping
s_night=img1[20:180,50:200]
cv.imshow('picture cropped image', s_night)
cv.waitKey(0) #to hold the photo
cv.destroyAllWindows() #to close the window


# In[27]:


#resizing s_night image
s_night=cv.resize(s_night,(100, 100))
#swaping it with one of the legs in the other picture
img2[100:200,0:100]=s_night
cv.imshow('Swapped image', img2)
cv.waitKey(0) #to hold the photo
cv.destroyAllWindows() #to close the window


# In[ ]:


img1 = cv.imread('rightimage.jpg')
img2 = cv.imread('leftimage.jpg')
horizontal = np.hstack((img2,img1))
cv.imshow("Collage",horizontal)
cv.waitKey(0)
cv.destroyAllWindows() #making collage


# In[ ]:





# In[ ]:





# In[ ]:




