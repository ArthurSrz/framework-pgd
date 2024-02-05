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

from typing import Any

import numpy as np

import streamlit as st
from streamlit_elements import elements, mui, html, lazy, sync
from streamlit_elements import editor
from typing import Any
import numpy as np
import streamlit as st
from streamlit_elements import elements, mui, html, lazy, sync
from streamlit_elements import editor
import pandas as pd

st.title("Construction du sprint PGD")

if "df_base" not in st.session_state:
    st.session_state.df_base = pd.DataFrame()

df = pd.DataFrame(
    [
        {"nom de l'étape":"Etape 1 - Acquisition des données","img": "https://github.com/ArthurSrz/framework-pgd/blob/main/media/images/images.png?raw=true","nomPas":"Identifier les produits de recherche","description":"ceci","versClient":True},
        {"nom de l'étape":"Etape 1 - Acquisition des données","img": "https://github.com/ArthurSrz/framework-pgd/blob/main/media/images/image4.png?raw=true","nomPas":"Expliquer si les données sont réutilisées ou collectées","description":"ceci","versClient":True},
        {"nom de l'étape":"Etape 2 - Traitement des données","img": "https://github.com/ArthurSrz/framework-pgd/blob/main/media/images/image6.png?raw=true","nomPas":"Décrire les métadonnées","description":"cela","versClient":False},
        {"nom de l'étape":"Etape 3 - Accès et partage des données","img": "https://github.com/ArthurSrz/framework-pgd/blob/main/media/images/image7.png?raw=true","nomPas":"Prévoir l'attribution d'identifiant pérenne","description":"ceci et cela","versClient":False},
        {"nom de l'étape":"Etape 4 - Conservation et archivage des données","img": "https://github.com/ArthurSrz/framework-pgd/blob/main/media/images/image8.png?raw=true","nomPas":"Déterminer la durée et le lieu d'archivage","description":"Jojo","versClient":False},
        {"nom de l'étape":"Etape 5 - Réutilisation des données","img": "https://github.com/ArthurSrz/framework-pgd/blob/main/media/images/image9.png?raw=true","nomPas":"Déterminer la licence appliquée aux données","description":"Jiji","versClient":False},
        
    ]
)


edited_df = st.data_editor(df,
                           column_config={
                               "img": st.column_config.ImageColumn(
                                "img", help="Streamlit app preview screenshots"
                                )
                               },
                           hide_index=True
                           ) # 👈 An editable dataframe



#store the edited dataframe in a state variable

if st.button("Sauvegarder", type="primary"):
    st.session_state.df_base = edited_df[edited_df["versClient"] == True]
    st.success("Envoyé !")

print(st.session_state.df_base)
