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

    st.title("Bienvenue sur le framework PGD")
    
    
    
    st.markdown(
        """
        Vous pourrez ici construire votre propre sprint PGD avec 
        les composants de votre choix.
    """
    )

    st.image("https://science-ouverte.univ-artois.fr/wp-content/uploads/2022/06/DMP.png")
    
    st.title("Test Monaco editor")
    
    with elements("monaco_editors"):

        if "content" not in st.session_state:
            st.session_state.content = "Default value"

        #mui.Typography("Content: ", st.session_state.content)

        def update_content(value):
            st.session_state.content = value
        
        st.markdown(st.session_state.content)

        if st.button("Edit"):
            editor.Monaco(
            height=300,
            defaultValue=st.session_state.content,
            defaultLanguage="markdown",
            onChange=lazy(update_content),
            options={"language": "markdown"}
        )

            mui.Button("Editer", onClick=sync())

       

    
    
        
        

if __name__ == "__main__":
    run()
