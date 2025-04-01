from enum import Enum
import os
from dotenv import load_dotenv 

class Constant(Enum):
    load_dotenv()
    username = os.getenv('username')
    password = os.getenv('password')
    cluster_name = 'cluster0'
    db_name = 'test'
    
    # username = os.getenv('db_username')
    # password = os.getenv('db_password')
    # cluster_name = os.getenv('db_cluster_name')
    # db_name = os.getenv('db_name')
    uri = f"mongodb+srv://{username}:{password}@{cluster_name}.8n9ij.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    
    video_collection_name = 'testCollection'
    transcripts_collection_name = 'testCollection2'
    keyframes_collection_name = 'testCollection3'
    keyframe_classes_collection_name = 'testCollection4'
    confirmed_classes_collection_name = 'confirmed_classes'
    description_collection_name = 'product_description'