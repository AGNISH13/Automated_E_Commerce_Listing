# import sys
# import os
# import streamlit as st

# sys.path.append(os.path.abspath(os.path.join('..')))
# print(sys.path)

# from pipeline import Pipeline
# # from dummy_pipeline import Pipeline
# from stlit.dummy_display import Display

# def page():
#     st.set_page_config(page_title="SAM", page_icon="📹", layout="wide")
#     if 'pipeline' not in st.session_state:
#         st.session_state['pipeline'] = Pipeline()
#     if 'display' not in st.session_state:
#         st.session_state['display'] = Display()
#     # if 'count' not in st.session_state:
#     #     st.session_state.count = 0

#     header = st.container()
#     body = st.container()

#     with header:
#         st.write("# Running dummy pipelines")
#         file = st.file_uploader("choose videos", type=["mp4"], accept_multiple_files=False, label_visibility="hidden")

#     if file:
#         st.button("reset pipeline", key="reset_pipeline", type="secondary", on_click=st.session_state['pipeline'].reset) #, args=(test,))
#         with body:
#             col1, col2 = st.columns([1, 4])
#             with col1:
#                 st.write("The uploaded video")
#                 st.video(file, format="video/mp4")
#             file_data = file.getvalue()
#             with col2:
#                 st.write("Other data will be displayed here")
#                 while st.session_state['pipeline'].step != -1:
#                     st.session_state['pipeline'].auto_run()

#                     if st.session_state['pipeline'].flag_transcript:
#                         st.session_state['display'].display_transcript()
#                         st.session_state['pipeline'].flag_transcript = False

#                     if st.session_state['pipeline'].flag_katna:
#                         binaries = st.session_state['pipeline'].katna_keyframes
#                         st.session_state['display'].display_bnr_frames(binaries)
#                         st.session_state['pipeline'].flag_katna = False

#                     if st.session_state['pipeline'].flag_description:
#                         st.session_state['display'].display_description()
#                         st.session_state['pipeline'].flag_description = False

#                 if st.session_state['pipeline'].step == -1:
#                     st.write("Pipeline has ended")
#                     st.session_state['pipeline'].reset()
#                     st.session_state['display'].close()
#             st.write("not in column")

# page()

# # test = Pipeline()

# # # Add a selectbox to the sidebar:
# # add_selectbox = st.sidebar.selectbox(
# #     'How would you like to be contacted?',
# #     ('Email', 'Home phone', 'Mobile phone')
# # )

# # # Add a slider to the sidebar:
# # add_slider = st.sidebar.slider(
# #     'Select a range of values',
# #     0.0, 100.0, (25.0, 75.0)
# # )

# # def page():

# #     if 'pipeline' not in st.session_state:
# #         st.session_state['pipeline'] = Pipeline()
# #     if 'display' not in st.session_state:
# #         st.session_state['display'] = Display()
# #     if 'count' not in st.session_state:
# #         st.session_state.count = 0
    
# #     st.write("## Running dummy pipelines")
# #     st.button("Run pipeline", key="run_pipeline", type="primary", on_click=runner) #, args=(test,))
# #     st.button("Reset pipeline", key="reset_pipeline", type="secondary", on_click=reset) #, args=(test,))
# #     # st.button("End pipeline", key="end_pipeline")

# #     # if pipeline.step == 0:
# #     #     st.write("Pipeline has started")
# #     # if pipeline.step == 1:
# #     #     st.write("Running step 1")
# #     # if pipeline.step > 2:
# #     #     st.write(st.session_state['flag1_content'])

# #     # # while test.step!= -1:
# #     # if st.session_state['flag1']:
# #     #     st.write("Flag 1 is set")
# #     #     display.display1()
# #     # if st.session_state['flag2']:
# #     #     st.write("Flag 2 is set")
# #     #     display.display2()
            
# #     return None

# # def reset():
# #     st.session_state['pipeline'].reset()
# #     st.session_state['flag1'] = False
# #     st.session_state['flag2'] = False
# #     st.session_state.count = 0
# #     st.write("Pipeline has been reset")
# #     return None

# # def runner():

# #     # st.write(st.session_state['count'])
# #     # st.session_state.count += 1

# #     pipeline = st.session_state['pipeline']
# #     pipeline.auto_run()
# #     if pipeline.step == 1:
# #         st.write("Creating transcript...")
# #     if pipeline.step == 2:
# #         st.write("Creating description...")
# #     if pipeline.step > 2:
# #         st.write(pipeline.transcript)
# #     if pipeline.step > 3:
# #         st.write(pipeline.description)
# #     if pipeline.step>5:
# #         pipeline.end()