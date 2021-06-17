#importing the important libraries
from keras.models import load_model
import streamlit as st
from PIL import Image
import cv2 as cv
import tempfile
from keras.preprocessing import image
import numpy as np
import os

#Loading the model
model = load_model('minor_project_CNN.model')

#Loading the function to break down the video into frames
def FrameCapture(path):
    vidObj = cv.VideoCapture(path)
    count = 0
    success = 1
    while success:
        success, image = vidObj.read()
        try:
          cv.imwrite("frame%d.jpg" % count, image)
        except:
          pass
        count += 1

#Basic info and introduction
st.image('c2.jpg')
st.title("Facial Autism Recognition")


#Asking the user to upload the media files
st.header("Please upload the file you want to get predicted :")
st.set_option('deprecation.showfileUploaderEncoding', False)
choice = st.radio("File Types Available:",("Select","Image","Video"))
if(choice == 'Image'):
    st.write("Image Upload")
    img = st.file_uploader("",type=['jpg','jpeg', 'png'])
    if img is not None:
        pic = Image.open(img)
        st.image(pic)
        with open("image.jpg", "wb") as f:
            f.write(img.getbuffer())
        import numpy as np


        test_image = image.load_img('image.jpg', target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        if result[0][0] == 1:
            prediction = 'Non_Autistic'
        else:
            prediction = 'Autistic'
        st.subheader(prediction)

elif(choice == 'Video'):
    st.write("Video Upload")
    video = st.file_uploader("", type=['mp4', 'mkv'])
    if video is not None:
        st.write("This could take a while! Hold on.")
        st.write("Uploading...")
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video.read())
        st.write("Saving...")
        vf = cv.VideoCapture(tfile.name)
        with open("video.mp4", "wb") as f:
            f.write(video.getbuffer())
        st.write("Splitting into frames...")
        FrameCapture('video.mp4')
        from statistics import mean
        result_arr = []
        st.write("Processing...")
        for i in range(4708):
            img_cnt = "frame" + str(i) + ".jpg"
            test_image = image.load_img(img_cnt, target_size=(64, 64))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            result = model.predict(test_image)
            result_arr.append(result[0][0])
        avg_pred = mean(result_arr)
        if avg_pred >= 0.5:
            prediction = 'Predicted Response: Non_Autistic'
        else:
            prediction = 'Predicted Response: Autistic'
        st.title(prediction)