import streamlit as st
import langchain_cafe

st.title("Cafe Name Generator")

country = st.sidebar.selectbox("Pick a Country", ("India", "Italy", "China", "Iran","Dubai", "America", "Mexico", "Brazil","Russia"))

if country:
    response = langchain_cafe.generate_cafe_name_and_items(country)
    st.header(response['cafe_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)