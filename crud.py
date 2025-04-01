from bson import ObjectId
from pymongo.errors import PyMongoError

from connection import get_collection
from constants import Constant  

# I'm lazy, plugged in the error response here
get_error_response = {
    "status"    : 400,
    "response"  : None
}

# For storing video links
class video:
    def __init__(self):
        self.db = get_collection(Constant.video_collection_name.value)

    def create(self, video_link, user_id="Default"):
        if self.db is None:
            print("Database connection not found")
            return None

        if video_link is None:
            print("Video link found empty")
            return None

        try:
            input_doc = {
                "_id": ObjectId(),
                "user_id": user_id,
                "video_link": video_link
            }

            result = self.db.insert_one(input_doc)
            return result.inserted_id

        except PyMongoError as e:
            print(f"Error occurred while inserting the document: {e}")
            return None    

    def get_video(self, video_id):
        
        if self.db is None:
            print("Database connection not found")
            return get_error_response
        
        if video_id is None:
            print("Video id found empty")
            return get_error_response
        try:
            res = self.db.find_one({"_id": video_id})
            
            if res is None:
                print(f"No video found with id: {video_id}")
                return get_error_response
            
            return {
                "status": 200,
                "response": res["video_link"]
            }
        
        except PyMongoError as e:
            print(f"Database error: {e}")
            return get_error_response

# For storing keyframes
class keyframes:
    def __init__(self):
        self.db = get_collection(Constant.keyframes_collection_name.value)
    
    def create(self, video_id, keyframes):
        if self.db is None:
            print("Database connection not found")
            return None
        
        if video_id is None or keyframes is None or not keyframes :
            print(f"Values incomplete keyframes: {keyframes}\n video_id: {video_id}")
            return None
        
        returing_keyframes = []
        try:
            keyframe_list = []
            for keyframe in keyframes:
                if keyframe is None:
                    continue
                id = ObjectId()
                returing_keyframes.append(id)
                keyframe_list.append({
                    "_id": id,
                    "keyframe": keyframe
                }) 
            input_doc = {
                "_id": ObjectId(),
                "video_id": video_id,
                "keyframes": keyframe_list # [{id: bnr}, ...]
            }

            result = self.db.insert_one(input_doc) # currently not returning the inserted id
            return returing_keyframes
        
        except PyMongoError as e:
            print(f"Error occurred while inserting the document: {e}")
            return None
            
    def get_all_keyframes(self, video_id):
        if self.db is None:
            print("Database connection not found")
            return get_error_response
        
        if video_id is None:
            print("Video id found empty")
            return get_error_response
        
        try:
            result = self.db.find_one({"video_id": video_id})
            
            if result is None:
                print(f"No keyframes found for video with id: {video_id}")
                return get_error_response
            
            return {
                "status": 200,
                "response": result["keyframes"]
            }
        except PyMongoError as e:
            print(f"Database error: {e}")
            return get_error_response
    
    def update_keyframes(self, video_id, new_list):
        if self.db is None:
            print("Database connection not found")
            return get_error_response
        
        if video_id is None:
            print("Video id found empty")
            return get_error_response
        
        try:
            old = self.db.find_one({"video_id": video_id})
            old_list = old["keyframes"]

            if len(old_list)==len(new_list):
                print("no change needed")
                return None
            
            self.db.find_one_and_update(
                {"video_id": video_id},
                {"$set": {"keyframes": new_list}}
            )
            print(f"{video_id} instance updated with filtered keyframes")
            return None
        
        except PyMongoError as e:
            print(f"Database error: {e}")
            return get_error_response

# For storing transcripts
class transcripts:
    def __init__(self):
        self.db = get_collection(Constant.transcripts_collection_name.value)

    def create(self, video_id, transcript):
        if self.db is None:
            print("Database connection not found")
            return None

        if transcript is None or video_id is None:
            print(f"Values incomplete transcript: {transcript}\n video_id: {video_id}")
            return None

        try:
            input_doc = {
                "_id": ObjectId(),
                "video_id": video_id,
                "transcript": transcript
            }

            result = self.db.insert_one(input_doc)
            return result.inserted_id

        except PyMongoError as e:
            print(f"Error occurred while inserting the document: {e}")
            return None
        
    def get_transcripts(self, video_id):
        if self.db is None:
            print("Database connection not found")
            return get_error_response
        
        if video_id is None:
            print("Video id found empty")
            return get_error_response
        
        try:
            result = self.db.find_one({"video_id": video_id})
            
            if result is None:
                print(f"No video found with id: {video_id}")
                return get_error_response
            
            return {
                "status": 200,
                "response": result["transcript"]
            }
        
        except PyMongoError as e:
            print(f"Database error: {e}")
            return get_error_response

# For storing classes of keyframes
class keyframe_classes:
    def __init__(self):
        self.db = get_collection(Constant.keyframe_classes_collection_name.value)

    def create(self, video_id, keyframe_id, classes):
        if self.db is None:
            print("Database connection not found")
            return None
        
        if keyframe_id is None or classes is None or video_id is None:
            print(f"Values incomplete classes: {classes}\n keyframe_id: {keyframe_id}\n video_id: {video_id}")
            return None

        # !FIX - empty array if no classes detected 
        
        try:
            input_doc = {
                "_id": ObjectId(),
                "video_id": video_id,
                "keyframe_id": keyframe_id,
                "classes": classes
            }

            result = self.db.insert_one(input_doc)
            return result.inserted_id

        except PyMongoError as e:
            print(f"Error occurred while inserting the document: {e}")
            return None
        
    def get_classes(self, video_id=None): # -> list[str]

        if self.db is None:
            print("Database connection not found")
            return None
        if video_id is None:
            print(f"arguments empty\n -- video_id: {video_id}")
            return None

        try:
            matched_frames = self.db.find(
                { "video_id": video_id }
            )
            class_names = []
            for row in matched_frames:
                for d in row["classes"]:
                    if d["class_name"] not in class_names:
                        class_names.append(d["class_name"])

            return {
                "status": 200,
                "response": class_names
            }
        
        except PyMongoError as e:
            print(f"error occured while fetching documents:\n{e}")
            return None
        

# For storing final class of product
class final_class:
    def __init__(self):
        self.db = get_collection(Constant.confirmed_classes_collection_name.value)

    def create(self, video_id, classes):
        if self.db is None:
            print("Database connection not found")
            return None
        
        if classes is None or video_id is None:
            print(f"Values incomplete classes: {classes}\n video_id: {video_id}")
            return None

        # !FIX - empty array if no classes detected 
        
        try:
            input_doc = {
                "_id": ObjectId(),
                "video_id": video_id,
                "classes": classes
            }

            result = self.db.insert_one(input_doc)
            return result.inserted_id

        except PyMongoError as e:
            print(f"Error occurred while inserting the document: {e}")
            return None
        
    def get_final_classes(self, video_id):
        if self.db is None:
            print("Database connection not found")
            return get_error_response
        
        if video_id is None:
            print("Video id found empty")
            return get_error_response
        
        try:
            result = self.db.find_one({"video_id": video_id})
            
            if result is None:
                print(f"No video found with id: {video_id}")
                return get_error_response
            
            return {
                "status": 200,
                "response": result["classes"]
            }
        
        except PyMongoError as e:
            print(f"Database error: {e}")
            return get_error_response