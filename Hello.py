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
        page_title="Hello",
        page_icon="🧑‍🔬",
    )

    st.title("Bienvenue sur le framework PGD")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Vous pourrez ici construire votre propre sprint PGD avec 
        les composants de votre choix.
    """
    )
    
    with elements("dashboard"):
        # First, build a default layout for every element you want to include in your dashboard
        with mui.Button:
            mui.icon.EmojiPeople()
            mui.icon.DoubleArrow()
            mui.Typography("Button with multiple children")
        
        
        
        with mui.Card:
            key = "8"
            sx={"maxWidth": 345},
            children=[
                mui.CardMedia(
                    sx={"height": 140},
                    image="https://fastly.picsum.photos/id/404/200/300.jpg?hmac=1i6ra6DJN9kJ9AQVfSf3VD1w08FkegBgXuz9lNDk1OM"
                ),
                mui.CardContent("Card content"),
                mui.CardActions(
                    [
                        mui.Button(size="small", children="Share"),
                        mui.Button(size="small", children="Learn More"),
                    ]
                )
            ]

            
        
        
        layout = [
            # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
            dashboard.Item("first_item", 0, 0, 2, 2),
            dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=True, moved=False),
            dashboard.Item("third_item", 0, 2, 1, 1, isResizable=True),
        ]    

        
        
        def handle_layout_change(updated_layout):
            # You can save the layout in a file, or do anything you want with it.
            # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
            print(updated_layout)
        
        with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
            with mui.Card:
                key = "8"
                sx={"maxWidth": 345},
                children=[
                    mui.CardMedia(
                        sx={"height": 140},
                        image="https://images.unsplash.com/photo-1617854818583-09e7f077a156?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                    ),
                    mui.CardContent("Card content"),
                    mui.CardActions(
                        [
                            mui.Button(size="small", children="Share"),
                            mui.Button(size="small", children="Learn More"),
                        ]
                    )
                ]
            with mui.Card:
                key = "8"
                sx={"maxWidth": 345},
                children=[
                    mui.CardMedia(
                        sx={"height": 140},
                        image="https://images.unsplash.com/photo-1617854818583-09e7f077a156?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                    ),
                    mui.CardContent("Card content"),
                    mui.CardActions(
                        [
                            mui.Button(size="small", children="Share"),
                            mui.Button(size="small", children="Learn More"),
                        ]
                    )
                ]
            with mui.Card:
                key = "8"
                sx={"maxWidth": 345},
                children=[
                    mui.CardMedia(
                        sx={"height": 140},
                        image="https://images.unsplash.com/photo-1617854818583-09e7f077a156?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                    ),
                    mui.CardContent("Card content"),
                    mui.CardActions(
                        [
                            mui.Button(size="small", children="Share"),
                            mui.Button(size="small", children="Learn More"),
                        ]
                    )
                ]
            
            mui.Card("Second item", key="second_item")
            mui.Card("Third item", key="third_item")
            
        
        
        

if __name__ == "__main__":
    run()
