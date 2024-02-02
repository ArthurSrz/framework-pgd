import streamlit as st
from streamlit.logger import get_logger
from streamlit_elements import elements, mui

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Framework PGD",
        page_icon="🧑‍🔬",
    )

    st.title("Adaptez votre Sprint PGD")

    st.sidebar.success("Select a demo above.")

    st.markdown("""
        Ci-dessous
    """)

    

    with elements("dashboard"):
        if "my_data" not in st.session_state:
            st.session_state.my_data = {}

        def handle_cell_edit_stop(params):
            for card_key in st.session_state.my_data.keys():
                if st.session_state.my_data[card_key]["id"] == params["id"]:
                    st.session_state.my_data[card_key]["description"] = params["descriptionEtape"]
                    break
        
        # Display the DataGrid
        columns = [
            {"field": 'id', "headerName": 'Numéro', "width": 90},
            {"field": 'nomEtape', "headerName": 'nomEtape', "width": 150, "editable": True,},
            {"field": 'descriptionEtape', "headerName": 'descriptionEtape', "width": 150, "editable": True,},
        ]

        rows = [
            {"id": 1, "nomEtape": 'Identifier les produits de recherche', "descriptionEtape": 'Trouver les éléments à inscrire dans votre PGD avant de commencer sa rédaction.'},
            {"id": 2, "nomEtape": 'Expliquer si les données sont réutilisées ou collectées', "descriptionEtape": 'Classer les données recensées pour mieux rédiger votre PGD'},
            {"id": 3, "nomEtape": 'Choisir le meilleur format pour les données', "descriptionEtape": 'Assignez un format aux données recensées pour mieux rédiger votre PGD'}
        ]

        mui.DataGrid(
            sx={"maxHeight": 505, "maxWidth": 755},
            columns=columns,
            rows=rows,
            pageSize=5,
            checkboxSelection=True,
            disableSelectionOnClick=True,
            onCellEditStop=handle_cell_edit_stop,
        )

        # Display the Cards
        for row in rows:
            with mui.Card(key=f"card_{row['id']}"):
                mui.CardContent(
                    children=[
                        mui.Typography(
                            gutterBottom=True,
                            variant="h6",
                            component="div",
                            children=f"{row['nomEtape']}",
                        ),
                        mui.Typography(
                            variant="body2",
                            color="text.secondary",
                            children=f"{row['descriptionEtape']}",
                        )
                    ]
                )

if __name__ == "__main__":
    run()
