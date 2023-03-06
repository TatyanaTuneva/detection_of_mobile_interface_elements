# Detection of mobile interface elements

This project use yolov8 model for detection of mobile interface elements, such as burger menu, search icon and authorization icon. 

![project_image](https://user-images.githubusercontent.com/32728641/223195848-4b9855ff-6df6-41b6-8e5c-5cd85138a8bc.png)

## Dataset

Dataset was created by [download_dataset.ipynb](https://github.com/TatyanaTuneva/detection_of_mobile_interface_elements/blob/master/download_dataset.ipynb). 
At first, a list of the most visited sites was collected, then the mobile version of this site was opened using the library [Selenium](https://selenium-python.readthedocs.io/) 
and a screenshot of all of websites was taken. Almost 300 screenshots were collected.

The dataset was assembled from screenshots using the program [Label Studio](https://labelstud.io/). 
3 classes were marked on the images: burger menu, search icon and authorization icon. 
There was about 200 screenshot after markup in prepared dataset.

## Training

The ready-made model [yolov8](https://github.com/ultralytics/ultralytics) was used to detect interface elements. It was further trained using a prepared dataset.

![results](https://user-images.githubusercontent.com/32728641/223201522-79547641-721a-444f-ba0c-a24f6ecf4c41.png)

## Backend 

[Fast Api](https://fastapi.tiangolo.com/) web framework was used for the backend. 

## Frontend

For the frontend, the JavaScript language and the [jQuery](https://jquery.com/) web framework were used.
