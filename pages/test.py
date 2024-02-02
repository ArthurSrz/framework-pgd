import streamlit as st
from streamlit.logger import get_logger
from streamlit_elements import dashboard, elements, mui

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
        Ci-dessous
    """
    )

    # Define the initial rows data for the DataGrid
    if "rows" not in st.session_state:
        st.session_state.rows = [
            {"id": 1, "nomEtape": 'Identifier les produits de recherche', "descriptionEtape": 'Trouver les éléments à inscrire dans votre PGD avant de commencer sa rédaction.'},
            {"id": 2, "nomEtape": 'Expliquer si les données sont réutilisées ou collectées', "descriptionEtape": 'Classer les données recensées pour mieux rédiger votre PGD'},
            {"id": 3, "nomEtape": 'Choisir le meilleur format pour les données', "descriptionEtape": 'Assignez un format aux données recensées pour mieux rédiger votre PGD'}
        ]

    # Define a state variable to track changes in Streamlit Elements
    if "element_state" not in st.session_state:
        st.session_state.element_state = {}

    # Display the Streamlit Elements dashboard
    with elements("dashboard"):
        # Define the layout for the dashboard
        layout = [
            dashboard.Item("first_card", 1, 4, 2, 2.3, isDraggable=True, isResizable=True, moved=False),
            dashboard.Item("second_card", 2, 0, 2, 2.3, isDraggable=True, isResizable=True, moved=False),
            dashboard.Item("third_card", 3, 2, 2, 2.3, isDraggable=True, isResizable=True, moved=False),
            dashboard.Item("test", 0, 0, 2, 2.3, isDraggable=True, isResizable=True, moved=False),
            dashboard.Item("data_test", 1, 0, 2, 2.3, isDraggable=True, isResizable=True, moved=False)
        ]

        # Handle layout changes
        def handle_layout_change(updated_layout):
            st.session_state.element_state["layout"] = updated_layout

        # Display the dashboard grid with layout
        with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
            # Display each card within the dashboard
            with mui.Card(key="first_card", sx={"maxHeight": 505, "maxWidth": 355}):
                mui.CardContent(
                    children=[
                        mui.Typography(gutterBottom=True, variant="h6", component="div", children="1. Identifier les produits de recherche"),
                        mui.Typography(variant="body2", color="text.secondary", children="Trouver les éléments à inscrire dans votre PGD avant de commencer sa rédaction.")
                    ]
                )

            # Display the editable DataFrame
            with mui.Card(key="data_test", sx={"maxHeight": 505, "maxWidth": 755}):
                # Display the editable DataFrame
                edited_data = st.data_editor(st.session_state.rows)

                # Update session state with edited data
                st.session_state.rows = edited_data

                # Display the Cards
                for row in st.session_state.rows:
                    with mui.Card():
                        mui.CardContent(
                            children=[
                                mui.Typography(gutterBottom=True, variant="h6", component="div", children=row['nomEtape']),
                                mui.Typography(variant="body2", color="text.secondary", children=row['descriptionEtape'])
                            ]
                        )

if __name__ == "__main__":
    run()
