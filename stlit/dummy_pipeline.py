import streamlit as st
import time
class Pipeline:
    def __init__(self):
        self.step = 0
        self.transcript = ""
        self.description = ""

    def run(self):
        if self.step>5:
            self.end()
            return self.step
        self.step += 1
        if self.step==2:
            self.transcript = "Transcript -->\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nibh mauris, posuere a laoreet in, malesuada sit amet est. Vivamus id efficitur libero. Mauris luctus sem quis arcu vehicula gravida. Nunc ac imperdiet mauris. Vivamus elementum varius libero. Praesent consequat eros a leo posuere, at efficitur dolor bibendum. Sed eget rutrum tortor, quis dictum dolor. Fusce vitae enim arcu. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi in nulla id velit facilisis ultrices. Fusce et tellus ornare, eleifend velit id, lobortis dui. Ut eleifend sodales metus et sodales. Suspendisse tincidunt lacus at tincidunt dapibus. Curabitur consequat orci tortor, ut."
        if self.step==3:
            self.description = "Description -->\nflag2_content"
    
    def auto_run(self):
        if self.step == 0:
            st.write("Pipeline has started")
            time.sleep(2)
        if self.step != -1:
            time.sleep(2)
            self.run()

    def reset(self):
        self.step = 0
        st.session_state['flag1'] = False
        st.session_state['flag2'] = False
    
    def end(self):
        self.step = -1