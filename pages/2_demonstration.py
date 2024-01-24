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
from streamlit_elements import elements, mui, html

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
    
    with elements("dashboard"):
        # First, build a default layout for every element you want to include in your dashboard
        
        layout = [
            # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
            dashboard.Item("first_card", 1, 1, 2, 2, isDraggable=False, isResizable=False, moved = True),
            dashboard.Item("second_card", 1, 0, 2, 2, isDraggable=False, isResizable=False),
            dashboard.Item("third_card", 0, 2, 1, 2, isDraggable=False, isResizable=False),
        ]    

        
        
        def handle_layout_change(updated_layout):
            # You can save the layout in a file, or do anything you want with it.
            # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
            print(updated_layout)
        
        with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
            with mui.Card(key="first_card", sx={"maxWidth": 345}):
                mui.CardMedia(
                    sx={"height": 140},
                    image="https://images.unsplash.com/photo-1617854818583-09e7f077a156?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                )
                mui.CardContent("Etape 1")
                mui.CardActions(
                    [
                        mui.Button(size="small", children="Question"),
                        mui.Button(size="small", children="Adapter"),
                    ]
                )

            with mui.Card(key="second_card", sx={"maxWidth": 345}):
                mui.CardMedia(
                    sx={"height": 140},
                    image="https://plus.unsplash.com/premium_photo-1691784080844-8300ab4c6790?q=80&w=2968&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                )
                mui.CardContent("Etape 2")
                mui.CardActions(
                    [
                        mui.Button(size="small", children="Question"),
                        mui.Button(size="small", children="Adapter"),
                    ]
                )
            
            with mui.Card(key="third_card", sx={"maxWidth": 345}):
                mui.CardMedia(
                    sx={"height": 140},
                    image="https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=3028&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                )
                mui.CardContent("Etape 3")
                mui.CardActions(
                    [
                        mui.Button(size="small", children="Question"),
                        mui.Button(size="small", children="Adapter"),
                    ]
                )
            
            
            
        
        
        

if __name__ == "__main__":
    run()
