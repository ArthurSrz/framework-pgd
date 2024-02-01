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
import webbrowser

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
    
    with elements("dashboard"):
        # First, build a default layout for every element you want to include in your dashboard
        
       
            
        
        layout = [
            
            # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
            dashboard.Item("first_card", 1, 4, 2, 2.3, isDraggable=True, isResizable=True, moved = False),
            dashboard.Item("second_card", 2, 0, 2, 2.3, isDraggable=True, isResizable=True, moved = False),
            dashboard.Item("third_card", 3, 2,2, 2.3, isDraggable=True, isResizable=True, moved = False),
            dashboard.Item("test", 0, 0, 2, 2.3, isDraggable=True, isResizable=True, moved = False),
            dashboard.Item("data_test", 1, 0, 2, 2.3, isDraggable=True, isResizable=True, moved = False)
            
        ]    

        
        
        def handle_layout_change(updated_layout):
            # You can save the layout in a file, or do anything you want with it.
            # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
            print(updated_layout)
        #create a function that opens link in new tab
        def open_link(link):
            webbrowser.open_new_tab(link)
        
        
        
        with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
            
            with mui.Card(key="first_card", sx={"maxHeight": 505,"maxWidth": 355}):
                mui.CardMedia(
                    sx = {"height": 140},
                    image="https://github.com/ArthurSrz/framework-pgd/blob/main/media/images/images.png?raw=true",
                    title="Random image",
                )
                mui.CardContent(
                    children=[
                        mui.Typography(
                            gutterBottom=True,
                            variant="h6",
                            component="div",
                            children="1.Identifier les produits de recherche",
                        ),
                        mui.Typography(
                            variant="body2",
                            color="text.secondary",
                            children="Trouver les éléments à inscrire dans votre PGD avant de commencer sa rédaction.",
                            
                        ),
                    ]
                )
                
                mui.CardActions(
                        mui.Button(
                            #open link in new tab
                            href="https://google.com",
                            target = "_blank",
                            variant="contained",
                            size="small",
                            children="Editer",
                        ),
                    
                )

            with mui.Card(key="second_card", sx={"maxHeight":505,"maxWidth": 355}):
                mui.CardMedia(
                    sx = {"height": 140},
                    image="https://github.com/ArthurSrz/framework-pgd/blob/main/media/images/images2.png?raw=true",
                    title="Random image",
                )
                mui.CardContent(
                    children=[
                        mui.Typography(
                            gutterBottom=True,
                            variant="h6",
                            component="div",
                            children="2.Expliquer si les données sont réutilisées ou collectées",
                        ),
                        mui.Typography(
                            variant="body2",
                            color="text.secondary",
                            children="Classer les données recensées pour mieux rédiger votre PGD",
                        ),
                    ]
                )
                mui.CardActions(
                        mui.Button(
                            variant="contained",
                            size="small",
                            children="Editer",
                        ),
                    
                )
            
            with mui.Card(key="third_card", sx={"maxHeight":505,"maxWidth": 355}):
                mui.CardMedia(
                    sx = {"height": 140},
                    image="https://github.com/ArthurSrz/framework-pgd/blob/main/media/images/images3.png?raw=true",
                    title="Random image",
                )
                mui.CardContent(
                    children=[
                        mui.Typography(
                            gutterBottom=True,
                            variant="h6",
                            component="div",
                            children="3.Choisir le meilleur format pour les données",
                        ),
                        mui.Typography(
                            variant="body2",
                            color="text.secondary",
                            children="Assignez un format aux données recensées pour mieux rédiger votre PGD",
                        ),
                    ]
                )
                mui.CardActions(
                        mui.Button(
                            variant="contained",
                            size="small",
                            children="Editer",
                        )
                    
                )
            
            with mui.Card(key="test", sx={"maxHeight":505,"maxWidth": 355}):
                mui.CardMedia(
                    sx = {"height": 140},
                    image="https://github.com/ArthurSrz/framework-pgd/blob/main/media/images/images3.png?raw=true",
                    title="Random image",
                )
                mui.CardContent(
                    children=[
                        mui.Typography(
                            gutterBottom=True,
                            variant="h6",
                            component="div",
                            children="Test",
                        ),
                        mui.Typography(
                            variant="body2",
                            color="text.secondary",
                            children="Test",
                        )
                    ]
                )
                mui.CardActions(
                        mui.Button(
                            variant="contained",
                            size="small",
                            children="Editer",
                        )
                
                )
            columns = [
                { "field": 'id', "headerName": 'Numéro', "width": 90 },
                { "field": 'nomEtape', "headerName": 'nomEtape', "width": 150, "editable": True, },
                { "field": 'descriptionEtape', "headerName": 'descriptionEtape', "width": 150, "editable": True, },
                
            ]   
            rows = [
                { "id": 1, "nomEtape": 'Identifier les produits de recherche', "descriptionEtape": 'Trouver les éléments à inscrire dans votre PGD avant de commencer sa rédaction.' },
                { "id": 2, "nomEtape": 'Expliquer si les données sont réutilisées ou collectées', "descriptionEtape": 'Classer les données recensées pour mieux rédiger votre PGD'},
                { "id": 3, "nomEtape": 'Choisir le meilleur format pour les données', "descriptionEtape": 'Assignez un format aux données recensées pour mieux rédiger votre PGD'}
          
            ]
            mui.DataGrid(
                    sx={"maxHeight":505,"maxWidth": 755},
                    key = "data_test",
                    columns=columns,
                    rows=rows,
                    pageSize=5,
                    checkboxSelection=True,
                    disableSelectionOnClick=True,
                )
                
                

            
        
        
        

if __name__ == "__main__":
    run()
