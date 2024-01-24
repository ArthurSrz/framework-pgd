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


df = pd.DataFrame(
    [
        {"nom de l'étape":"Etape 1","img": "https://images.unsplash.com/photo-1617854818583-09e7f077a156?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","description":"ceci"},
        {"nom de l'étape":"Etape 2","img": "https://plus.unsplash.com/premium_photo-1691784080844-8300ab4c6790?q=80&w=2968&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","description":"cela"},
        {"nom de l'étape":"Etape 3","img": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=3028&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","description":"ceci et cela"},
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



print(edited_df)