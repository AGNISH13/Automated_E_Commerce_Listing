def transform(input_class = None, output_class = None):
    def compute(actual_func):
        def wrapper(*args, **kwargs):
            
            # collect the input using get function from input class
            # transcripts.get_tra
            # call the poc_function(*args, **kwargs)
            # write to cluster using write function of output class

            return None # return logs here
        return wrapper
    return compute

# Using in main function

# objk
# @transform(
#     input = keyframes
#     output = 
# )
# def actual_func(video_id, keyframe_id):
    # .....