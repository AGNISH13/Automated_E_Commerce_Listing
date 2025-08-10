# Automated-E-Commerce-Product-Listing

## Problem Description
In today's fast-paced e-commerce landscape, sellers face significant challenges in creating and maintaining compelling product listings. The traditional process is labor-intensive and slow, requiring manual effort to extract product details from marketing content, write descriptions, and select appropriate images. This manual workflow is a bottleneck for sellers, especially those who want to leverage popular social media trends and influencer content.

This project presents an innovative, AI-driven pipeline that automates the creation of high-quality Amazon product listings directly from social media content. By leveraging a suite of advanced models, we transform raw video and audio data into a ready-to-publish listing, significantly reducing the time, effort, and cost associated with product listing creation.

## Solution
Our tool automates the creation of Amazon product listings from social media content by processing audio and visual data. The entire pipeline can be segregated as follows:
- `The user's input video to be listed is saved in the database`
- `Audio is transcribed to text using Whisper`
- `Keyframe extraction from video using Katna`
- `Filtering the vulgar keyframes using NudeNet and MiddleFingerDetection`
- `Filtered frames are analyzed with YOLO v11 for object detection`
- `The transcript and YOLO object IDs as passed through Gemini to get the identified product`
- `Final frames to be listed are selected using BLIP, which takes the identified product and filtered frames as input`
- `The product description to be displayed is generated using Gemini`
   
The result is a high-quality product listing, ready for e-commerce platforms.


## Tech Stack
This project has used the following tech stack
- `Python`
OpenCV 	(open source)
Hugging Face	(open source)
AWS EKS 	(open source)
Traefik proxy 	(open source)
Whisper 	(open source)
YOLO v8	(open source)
BLIP 		(open source)
CLIP 		(open source)
Gemini 		(proprietary)

## Flowchart
-     GoogleNet using KNN classifier
     ![image](https://github.com/user-attachments/assets/587a0a0a-d1ab-4a1a-9ff2-d4f58a29b23f)



## Dependencies
Since the entire project is based on `Python` programming language, it is necessary to have Python installed in the system. It is recommended to use Python with version `>=3.7`.
There are a number of Python packages which are in use in this project. All these dependencies can be installed just by the following command line argument
- pip install `requirements.txt`

## Code implementation
- ### Data paths :
      Current directory -------> data
                                  |
                                  |
                                  |               
                                  --------------------->  train
                                  |                         |
                                  |             -------------------------
                                  |             |        |              |
                                  |             V        V              V
                                  |           class_1  class_2 ...... class_n
                                  |
                                  |
                                  |              
                                  --------------------->   val
                                                            |
                                                -------------------------
                                                |        |              |
                                                V        V              V
                                              class_1  class_2 ...... class_n
                                              
                               
- Where the folders `train` and `val` contain the folders `benign` and `malignant`, which include the original histopathological images of respective type of human breast tumor tissue in `.jpg`/`.png` format.

- ### Training and Evaluation :

          usage: main.py [-h] [-data DATA_FOLDER] [-classes NUM_CLASSES]
                         [-ext EXTRACTOR_TYPE] [-classif CLASSIFIER_TYPE]

          Application of Genetic Algorithm

          optional arguments:
            -h, --help            show this help message and exit
            -data DATA_FOLDER, --data_folder DATA_FOLDER
                                  Path to data
            -classes NUM_CLASSES, --num_classes NUM_CLASSES
                                  Number of data classes
            -ext EXTRACTOR_TYPE, --extractor_type EXTRACTOR_TYPE
                                  Choice of deep feature extractor
            -classif CLASSIFIER_TYPE, --classifier_type CLASSIFIER_TYPE
                                  Choice of classifier for GA
        
-  ### Run the following for training and validation :
  
      `python main.py -data data`
