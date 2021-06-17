# FacialAutismDetection
We use facial expressions of the test subjects to detect autism.  Autistic people have difficulty making appropriate facial expressions at the right times. We are training the model on the dataset which has images of both Autistic and non-Autistic people. The model uses CNN algorithm with a 2 layer architecture, and have achieved a max of 86% accuracy.
## Testing and Predictions
In order to process the video and make predictions out of it, we decided to break down the video into its frames.
Then we have a directory of images with us consisting of the video.
Proceeding with this, we predicted the outcome for all the frames of the given Video and recorded the response.
Applying statistics on the responses, we got a mean prediction of the video.
## UserInterface
The User Interface was designed using the Streamlit module from Python.
It is a minimalistic web app, where users can upload, either an image or a video.
The app can make predictions for both image as well as a video.
The time taken for prediction from Video can be improved, by using a GPU based processor.

![image](https://user-images.githubusercontent.com/43439398/122372015-f39dd180-cf7d-11eb-8063-373c267b3863.png)
