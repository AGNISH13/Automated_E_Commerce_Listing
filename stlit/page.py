import sys
import os
import streamlit as st

# print(sys.path)
# sys.path.append(os.path.abspath(os.path.join('..')))
# print("--------------------------")
# for path in sys.path:
#     print(path)

from dummy_pipeline import Pipeline
from dummy_display import Display

def page():
    st.write("## Running dummy pipelines")
    test = Pipeline()
    display = Display()
    st.button("Run pipeline", key="run_pipeline", type="primary", on_click=runner, args=(test,))
    # st.button("Reset pipeline", key="reset_pipeline")
    # st.button("End pipeline", key="end_pipeline")

    while test.step!= -1:
        if st.session_state['flag1']:
            st.write("Flag 1 is set")
            display.display1()
        if st.session_state['flag2']:
            st.write("Flag 2 is set")
            display.display2()
            
    return None
    

def runner(pipeline):
    pipeline.run()
    if pipeline.step>5:
        pipeline.end()

page()
# def runner(pipeline):
#     if pipeline.step == -1:
#         st.write("Pipeline has ended")
#         return None
#     else:
#         while pipeline.step < 5:
#             # if st.button(f"Run step {pipeline.step}") or st.session_state['flag1'] or st.session_state['flag2']:
#             #     if pipeline.step == 0:
#             #         st.write("Pipeline has started")
#             #     elif pipeline.step == 1:
#             #         st.write("Running step 1")
#             #     elif pipeline.step == 2:
#             #         st.write("Running step 2")
#             #     elif pipeline.step == 3:
#             #         st.write("Running step 3")
#             #     elif pipeline.step == 4:
#             #         st.write("Running step 4")
#             #     else:
#             #         st.write("Pipeline has ended")
#             #         return None
#             st.write(f"Running step {pipeline.step}")
#             if st.session_state['flag1']:
#                 st.write("Flag 1 is set")
#             if st.session_state['flag2']:
#                 st.write("Flag 2 is set")
#             pipeline.run()
#         return None

# st.set_page_config(page_title="SAM", page_icon=None, layout="wide")
# # st.set_page_config(page_title="Video Upload", page_icon="📹", layout="wide")
# def page():
#     st.write("# Running dummy pipelines")

#     file = st.file_uploader("choose videos", type=["mp4"], accept_multiple_files=False, label_visibility="hidden")
#     if file:
#         file_data = file.getvalue()
#         col1, col2 = st.columns([1, 9])
#         with col1:
#             st.write("The uploaded video")
#             st.video(file, format="video/mp4")
#         with col2:
#             st.write("Other data will be displayed here")

#         st.write("not in column")

# test = Pipeline()

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )