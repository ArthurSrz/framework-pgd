import streamlit as st
from streamlit.logger import get_logger
from streamlit_elements import dashboard, elements, mui, lazy, sync
import pandas as pd
import time

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Framework PGD",
        page_icon="🧑‍🔬",
    )

    st.title("Adaptez votre Sprint PGD")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Découvrez le patchwork conçu par Datactivist et adaptez le.
    """
    )
    
    #Initialise st.session_state.df_base with empty dataframe
    if "df_base" not in st.session_state:
        st.session_state.df_base = pd.DataFrame()
    
    # Retrieve from 0_construction.py edited df
    df_base = st.session_state.df_base
    
    
    
    #make a list out of all elements inside the columns of the dataframe "nom de l'étape"
    etapes = df_base["nom de l'étape"].unique()
    pas = df_base["nomPas"]
    description = df_base["description"]
    #print(etapes)
    
    #create the layout of the app
    with st.container(border = True, height=300):
            tab1, tab2 = st.tabs(["👀 Consultation","📝 Modification"])
            with tab1:
                st.title(etapes[0])

                col1,col2,col3,col4,col5 = st.columns(5)

                with col1:
                    with st.container(border = True, height = 100):
                        st.write(pas[0])
                        st.markdown(description[0])
                with col2:
                    st.image("https://img.freepik.com/photos-gratuite/impression-floc-peinture-silhouette-eclabousse_1194-8202.jpg?w=900&t=st=1707141902~exp=1707142502~hmac=4951795c48392a58f5044521c1f6007a6953c90deadd3d1b8e8814da8765f44e")
                with col3:
                    with st.container(border = True, height = 100):
                        try:
                            st.write(pas[1])
                            st.markdown(description[1])
                        except:
                            st.info("Il n'y a pas de pas 2")
                with col4:
                    st.image("https://img.freepik.com/photos-gratuite/impression-floc-peinture-silhouette-eclabousse_1194-8202.jpg?w=900&t=st=1707141902~exp=1707142502~hmac=4951795c48392a58f5044521c1f6007a6953c90deadd3d1b8e8814da8765f44e")
                with col5:
                    with st.container(border = True, height = 100):
                        try:
                            st.write(pas[2])
                            st.markdown(description[2])
                        except:
                            st.info("Il n'y a pas de pas 3")
            with tab2:
                df_filtered = st.data_editor(df_base[df_base["nom de l'étape"] == str(etapes[0])], column_order=["nom de l'étape", "nomPas", "description"], hide_index=True)
                
                if st.button("Modifier", type="primary"):
                    st.session_state.df_base = df_filtered
                    st.success("Modifications enregistrées")
                    time.sleep(2)
                    st.rerun()
                    
                    
        

    with st.container(border = True, height=250):
        try : 
            st.title(etapes[1])
        except:
            st.info("Il n'y a pas d'étape 2")
        st.columns([1,1,1])
    
    with st.container(border = True, height=250):
        try : 
            st.title(etapes[2])
        except:
            st.info("Il n'y a pas d'étape 3")
        st.columns([1,1,1])
    
    with st.container(border = True, height=250):
        try : 
            st.title(etapes[3])
        except:
            st.info("Il n'y a pas d'étape 4")
        st.columns([1,1,1])
    
    with st.container(border = True, height=250):
        try : 
            st.title(etapes[4])
        except:
            st.info("Il n'y a pas d'étape 5")
        st.columns([1,1,1])
     
    

    
if __name__ == "__main__":
    run()
