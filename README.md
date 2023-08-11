# CPS_Group8

VISDrone dataset has been used for the aerial object detection using YOLOv8 algorithm
Attached link for the online repositary of the dataset. We have specifically used Object Detection in Images data - https://github.com/VisDrone/VisDrone-Dataset
For reference - https://docs.ultralytics.com/datasets/detect/visdrone/#dataset-yaml

The format of the annotated images in the given dataset was in Pascal format which we have changed into YOLO format (original format of the VISDrone dataset annotations is incompatible with YOLO) using the visdrone_to_YOLO.py script. 

Due to the hardware and time constraints we had to convert our images to smaller size - 
Hardware Constraints: Depending on the hardware you're using, such as GPUs or CPUs, you might have limitations on memory and processing power. Large aerial images can consume a significant amount of memory during both forward and backward passes through the neural network, which can lead to slowdowns or even crashes if the hardware is not capable of handling it.

To overcome the above issue we followed downsampling - 
Downsampling: Downsampling involves reducing the resolution of images to a smaller size. This is a common strategy to make images fit into memory and speed up processing. However, downsampling too much can lead to loss of fine details, which may be crucial for detecting small objects in aerial images.


NOTE: All the scripts need to be kept in the same folder where you have the training and validation aerial images from the VISDrone dataset

Steps to run the code : 

1) Change the train image directory and the validation image directory inside the data.yaml with respective folder where the VISdrone images are kept.
2) Change the annotations in the VISDrone dataset by running the visdrone_to_YOLO.py script which will give you the images in YOLO annotated format. Also, keep note to change the directory path in the script with the directory where you have kept the VISdrone annotations.
3) In case you are facing hardware issues which are not letting you run the model easily, you can change the image sizes by running image_resize.py to resize the images. Note to change the directory as well as your resired size in the script. 
4) Check if your GPU,CUDA and YOLO are configured properly by running check_gpu.py.
5) Finally, run the model.sh script which will first train and validate the model using VISDrone dataset using the pre trained weights of the YOLOv8x.pt model. For your reference, more about YOLOv8 can be found here - https://github.com/ultralytics/ultralytics
