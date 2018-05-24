import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import os

def process_image(image):
    # image = mpimg.imread('test_images/solidWhiteRight.jpg')

    #printing out some stats and plotting
    # print('This image is:', type(image), 'with dimensions:', image.shape)
    # plt.imshow(image)  # if you wanted to show a single color channel image called 'gray', for example, call as plt.imshow(gray, cmap='gray')
    # listdir = os.listdir("test_images/")
    # # print(listdir)
    # index = listdir[5]
    # image = mpimg.imread("test_images/" + index)
    image = image
    # Read in and grayscale the image
    # image = mpimg.imread('exit-ramp.jpg')
    # print("image shape:{}".format(image.shape))
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Define a kernel size and apply Gaussian smoothing
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

    # Define our parameters for Canny and apply
    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

    # Next we'll create a masked edges image using cv2.fillPoly()
    mask = np.zeros_like(edges)  # blank image
    ignore_mask_color = 255

    # This time we are defining a four sided polygon to mask
    imshape = image.shape
    vertices = np.array([[(0, imshape[0]),(450, 320), (490, 310), (imshape[1], imshape[0])]], dtype=np.int32)
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_edges = cv2.bitwise_and(edges, mask)
    # plt.imshow(masked_edges)
    # Define the Hough transform parameters
    # Make a blank the same size as our image to draw on
    rho = 1 # distance resolution in pixels of the Hough grid
    theta = np.pi/180 # angular resolution in radians of the Hough grid
    threshold = 15     # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 40 #minimum number of pixels making up a line
    max_line_gap = 20    # maximum gap in pixels between connectable line segments
    line_image = np.copy(image)*0 # creating a blank to draw lines on

    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                                min_line_length, max_line_gap)

    # Iterate over the output "lines" and draw lines on a blank image
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,20,147),20)
    # plt.imshow(line_image)
    # Create a "color" binary image to combine with line image
    color_edges = np.dstack((edges, edges, edges))

    # Draw the lines on the edge image
    lines_edges = cv2.addWeighted(image, 0.8, line_image, 1, 0)
    # cv2.imwrite("test_images_output/"+index, lines_edges)
    # plt.imshow(lines_edges)
    # plt.show()
    return lines_edges

def process_videos(image=None):
    list = os.listdir("test_videos/")
    indext = list[1]
    cap = cv2.VideoCapture("test_videos/" + indext)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # print("fps:{}, size:{}".format(fps, size))

    # 初始化一个video writer
    # video_writer = cv2.VideoWriter("test_videos_output/solidYellowLeft.mp4", cv2.VideoWriter_fourcc(*'mpeg'), fps, size)
    video_writer = cv2.VideoWriter("test_videos_output/" + indext, fourcc=fourcc, fps=fps, frameSize=size)
    while frame_count:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        frame_count -= 1
        print("frame count:{}, ret:{}".format(frame_count, ret))
        if ret:
            lines_edges = process_image(frame)
            # Display the resulting frame
            # cv2.imshow(str(frame_count), lines_edges)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            video_writer.write(lines_edges)
        else: #判断视频读取完成
            break
    # When everything done, release the capture
    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()

def play_videos():
    list = os.listdir("test_videos_output/")
    index = list[0]
    cap = cv2.VideoCapture("test_videos_output/" + index)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # frame = cv2.flip(frame, 0)

            # write the flipped frame
            cv2.imshow('play', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # process_videos()
    play_videos()

