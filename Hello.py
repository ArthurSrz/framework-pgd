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
        page_icon="🧑‍🔬"
    )

    st.title("Bienvenue sur le framework PGD")
    
    
    
    st.markdown(
        """
        Vous pourrez ici construire votre propre sprint PGD avec 
        les composants de votre choix.\n
        **Spoiler** : il y en a beaucoup !
    """
    )

    st.image("https://raw.githubusercontent.com/ArthurSrz/framework-pgd/main/media/images/logo.webp", width = 400)
    

    
    
        
        

if __name__ == "__main__":
    run()
