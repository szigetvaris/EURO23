import streamlit as st

st.set_page_config(
    page_title='Multipage App',
    page_icon='🔥'
)

st.title("Home")
st.sidebar.info('select a page above.')

st.selectbox('Team selection', ['England', 'Germany', 'Spain'])

col1, col2, col3 = st.columns(3)
col2.image('./images/flags/eng.png', )
col1.markdown('<font size= "7">**Ranking '+str(5)+'**</font>', unsafe_allow_html=True)
col3.markdown('<font size= "7">**Score '+str(5)+'**</font>', unsafe_allow_html=True)

