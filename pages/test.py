import streamlit as st

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

    # Define the initial rows data
    if "rows" not in st.session_state:
        st.session_state.rows = [
            {"id": 1, "nomEtape": 'Identifier les produits de recherche', "descriptionEtape": 'Trouver les éléments à inscrire dans votre PGD avant de commencer sa rédaction.'},
            {"id": 2, "nomEtape": 'Expliquer si les données sont réutilisées ou collectées', "descriptionEtape": 'Classer les données recensées pour mieux rédiger votre PGD'},
            {"id": 3, "nomEtape": 'Choisir le meilleur format pour les données', "descriptionEtape": 'Assignez un format aux données recensées pour mieux rédiger votre PGD'}
        ]

    # Display the editable DataFrame
    edited_data = st.data_editor(st.session_state.rows)

    # Update session state with edited data
    st.session_state.rows = edited_data

    # Display the Cards
    for row in st.session_state.rows:
        st.write(f"## {row['nomEtape']}")
        st.write(row['descriptionEtape'])

if __name__ == "__main__":
    run()
