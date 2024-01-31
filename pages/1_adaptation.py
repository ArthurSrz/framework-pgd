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
from streamlit_monaco import st_monaco

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="🧑‍🔬",
    )

    st.title("Adaptez le template")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Adaptez selon les spécificités de l'équipe que vous accompagnez
    """
    )
    
    # Initialize session state
    if "content" not in st.session_state:
        st.session_state.content = {}
    
    if "edit" not in st.session_state:
        st.session_state.edit = {}
    
    st.title("Streamlit Markdown Editor")

    

    with elements("dashboard"):
        # First, build a default layout for every element you want to include in your dashboard
        
        layout = [
            dashboard.Item("editor1", 1, 1, 2, 3, isDraggable=True, isResizable=True, moved=False),
            dashboard.Item("editor2", 3, 1, 2, 3, isDraggable=True, isResizable=True, moved=False),
            dashboard.Item("editor3", 1, 0, 2, 2, isDraggable=True, isResizable=True, moved=False),
            dashboard.Item("editor4", 1, 2, 1, 1, isDraggable=True, isResizable=True, moved=False),
        ]   

        def update_content(value):
            st.session_state.content = value
        
        if "edit" not in st.session_state:
            st.session_state.edit = False
        
        def handle_layout_change(updated_layout):
            # You can save the layout in a file, or do anything you want with it.
            # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
            print(updated_layout)
        
        with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
            with mui.Paper(key="editor1", sx={"maxWidth": 345}):
                mui.Typography("Pas 1", variant="h6")
                if st.session_state.edit:
                    editor.Monaco(
                    height=50,
                    defaultValue=st.session_state.content,
                    defaultLanguage="markdown",
                    onChange=lazy(update_content),
                    options={"language": "markdown"}
                )
                else:
                    mui.Button("Editer", onClick=sync())
                
            with mui.Paper(key="editor2", sx={"maxWidth": 345}):
                mui.Typography("Pas 2", variant="h6")
                if st.session_state.edit:
                    editor.Monaco(
                    height=50,
                    defaultValue=st.session_state.content,
                    defaultLanguage="markdown",
                    onChange=lazy(update_content),
                    options={"language": "markdown"}
                )
                else:
                    mui.Button("Editer", onClick=sync())
            
            with mui.Paper(key="editor3", sx={"maxWidth": 345}):
                mui.Typography("Pas 3", variant="h6")
                if st.session_state.edit:
                    editor.Monaco(
                    height=50,
                    defaultValue=st.session_state.content,
                    defaultLanguage="markdown",
                    onChange=lazy(update_content),
                    options={"language": "markdown"}
                )
                else:
                    mui.Button("Editer", onClick=sync())
            
            with mui.Paper(key="editor4", sx={"maxWidth": 345}):
                mui.Typography("Pas 4", variant="h6")
                if st.session_state.edit:
                    editor.Monaco(
                    height=50,
                    defaultValue=st.session_state.content,
                    defaultLanguage="markdown",
                    onChange=lazy(update_content),
                    options={"language": "markdown"}
                )
                else:
                    mui.Button("Editer", onClick=sync())
            
            
            
        
        
        

if __name__ == "__main__":
    run()
