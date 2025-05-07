import sys
import os
import streamlit as st

print(sys.path)
sys.path.append(os.path.abspath(os.path.join('..')))
print("--------------------------")
for path in sys.path:
    print(path)

from dummy_pipeline import Pipeline

st.set_page_config(page_title="SAM", page_icon=None, layout="wide")
# st.set_page_config(page_title="Video Upload", page_icon="📹", layout="wide")

file = st.file_uploader("choose videos", type=["mp4"], accept_multiple_files=False, label_visibility="hidden")
if file:
    file_data = file.getvalue()
    col1, col2 = st.columns([1, 9])
    with col1:
        st.write("The uploaded video")
        st.video(file, format="video/mp4")
    with col2:
        st.write("Other data will be displayed here")

    st.write("not in column")

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

# test = Pipeline()
# print(test.step)