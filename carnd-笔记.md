hsv = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)  
lower_red = np.array([20, 20, 20])  
upper_red = np.array([200, 200, 200])  
# mask -> 1 channel  
mask = cv2.inRange(hsv, lower_red, upper_red) #lower20===>0,upper200==>0 

numpy as np
np.plotfit()
 np.meshgrid
cv2.imwrite(path, image)

 # Do all the relevant imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in the image and convert to grayscale
# Note: in the previous example we were reading a .jpg 
# Here we read a .png and convert to 0,255 bytescale
image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# Define a kernel size for Gaussian smoothing / blurring
kernel_size = 5 # Must be an odd number (3, 5, 7...)
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

# Define our parameters for Canny and run it
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Display the image
plt.imshow(edges, cmap='Greys_r')


#coding=utf-8  
import cv2.cv as cv  
#获取视频，capture   
capture = cv.CaptureFromFile('myvideo.mp4')  
#获取视频的帧集合对象个数  
frames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))  
  
#CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream 视频流帧的宽度  
#CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream 视频流帧的高度  
#获取帧率  
fps = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS)  
#两帧间的间隔时间  
wait = int(1/fps * 1000/1)  
#视频的时间长度  
duration = (frames * fps) / 1000  
  
print 'Num. Frames = ', frames  
print 'Frame Rate = ', fps, 'fps'  
print 'Duration = ', duration, 'sec'  
#遍历所有的帧  
for f in xrange( frames ):  
#抓取后，capture被指向下一帧  
    frameImg = cv.QueryFrame(capture)  
#获取当前帧的位置,并且写入图片中  
    num= cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_POS_FRAMES)  
    #创建一个矩形，来让我们在图片上写文字，参数依次定义了文字类型，高，宽，字体厚度等。。  
    font=cv.InitFont(cv.CV_FONT_HERSHEY_SCRIPT_SIMPLEX, 1, 1, 0, 3, 8)  
    text='%d' %num;  
    cv.PutText(frameImg, text, (30,30), font, (0,255,0))  
#显示当前帧  
        cv.ShowImage("The Video", frameImg)  
    cv.WaitKey(wait)  