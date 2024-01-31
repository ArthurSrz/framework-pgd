# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
from streamlit_elements import dashboard
from streamlit_elements import elements, mui, html, editor, lazy, sync

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Framework PGD",
        page_icon="🧑‍🔬",
    )

    st.title("Votre Sprint PGD")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Tadaaam !
    """
    )
    def update_content(value):
        st.session_state.content = value
    if "content" not in st.session_state:
        st.session_state.content = "Default value"
    with elements("dashboard"):
        # First, build a default layout for every element you want to include in your dashboard
        
        layout = [
            # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
            dashboard.Item("first_card", 1, 1, 2, 2, isDraggable=True, isResizable=False, moved = True),
            dashboard.Item("second_card", 1, 0, 2, 2, isDraggable=True, isResizable=False),
            dashboard.Item("third_card", 0, 2, 1, 2, isDraggable=True, isResizable=False),
        ]    

        
        
        def handle_layout_change(updated_layout):
            # You can save the layout in a file, or do anything you want with it.
            # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
            print(updated_layout)
        
        with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
            with mui.Card(key="first_card", sx={"maxWidth": 345}):
                children = [
                    editor.Monaco(
                    height=300,
                    defaultValue=st.session_state.content,
                    onChange=lazy(update_content)
    )
                ]
                

            with mui.Card(key="second_card", sx={"maxWidth": 345}):
                children = [
                    editor.Monaco(
                    height=300,
                    defaultValue=st.session_state.content,
                    onChange=lazy(update_content)
    )
                ]
            
            with mui.Card(key="third_card", sx={"maxWidth": 345}):
                children = [
                    editor.Monaco(
                    height=300,
                    defaultValue=st.session_state.content,
                    onChange=lazy(update_content),
                    options={"language": "markdown"}
    )
                ]
            
            
            
        
        
        

if __name__ == "__main__":
    run()
