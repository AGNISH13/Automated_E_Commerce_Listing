# Automated-E-Commerce-Product-Listing

## Problem Description
In today's fast-paced e-commerce landscape, sellers face significant challenges in creating and maintaining compelling product listings. The traditional process is labor-intensive and slow, requiring manual effort to extract product details from marketing content, write descriptions, and select appropriate images. This manual workflow is a bottleneck for sellers, especially those who want to leverage popular social media trends and influencer content.

This project presents an innovative, AI-driven pipeline that automates the creation of high-quality product listings directly from social media content. By leveraging a suite of advanced models, we transform raw video and audio data into a ready-to-publish listing, significantly reducing the time, effort, and cost associated with product listing creation.

## Proposed Solution
Our tool automates the creation of E-Commerce product listings from social media content by processing audio and visual data. The entire pipeline can be segregated as follows:
- `The user's input video to be listed is saved in the database`
- `Audio is transcribed to text using Whisper`
- `Keyframe extraction from video using Katna`
- `Filtering the vulgar keyframes using NudeNet and MiddleFingerDetection`
- `Filtered frames are analyzed with YOLO v11 for object detection`
- `The transcript and YOLO object IDs as passed through Gemini to get the identified product`
- `Final frames to be listed are selected using BLIP, which takes the identified product and filtered frames as input`
- `The product description to be displayed is generated using Gemini`
   
The result is a high-quality product listing, ready for e-commerce platforms.

## Flowchart
-     GoogleNet using KNN classifier
     ![image](<img width="1772" height="789" alt="flowchart" src="https://github.com/user-attachments/assets/30115475-a8e5-4098-ad9c-b5956ccb4106" />)

## Tools Used
This project has used the following tools:
- Python
- OpenCV
- [Whisper](https://github.com/openai/whisper)
- [Katna](https://github.com/keplerlab/katna)
- [NudeNet](https://github.com/vladmandic/nudenet)
- [YOLOv11](https://github.com/ultralytics/ultralytics)
- Gemini
- [BLIP](https://github.com/salesforce/BLIP)
- [PyMongo](https://pypi.org/project/pymongo/)

## Dependencies
Since the entire project is based on `Python` programming language, it is necessary to have Python installed in the system. It is recommended to use Python with version `>=3.7`.
There are a number of Python packages which are in use in this project. All these dependencies can be installed just by the following command line argument
- `pip install requirements.txt`

## Code Implementation
- ### Code paths :
      main.py --------------------------------------------------------------------------------> top_ids.py
                                  |                                                                 |  
                                  |                                                                 V 
                                  |                                                             load_llm.py
                                  |
                                  |               
                                  ------------------------------------------------------------> crud.py
                                  |                                                                |
                                  |                                                     -------------------------
                                  |                                                     |                       |
                                  |                                                     V                       V
                                  |                                                connection.py           constants.py
                                  |
                                  |
                                  |              
                                  ------------------------------------------------------------> utils
                                                                                                  |
                                               -------------------------------------------------------------------------------------------------------
                                               |                  |              |             |          |                   |                      |
                                               V                  V              V             V          V                   V                      V
                                     mp4_mp3_conversion.py    whisper.py    filtering.py    katna.py    yolo.py    caption_matching_blip.py    description.py
                                                                                                          |                                          |
                                                                                                          V                                          V
                                                                                                  image_conversion.py                            load_llm.py
                                              
                               
        
-  ### How to run the pipeline?
   To store the path to the video input, assign the file path as a string to the `video_path` variable within the main function of `main.py` file:
   -  `video_path = None  # Your file path`

   Run the following command in your terminal:
   -  `python main.py -data data`
