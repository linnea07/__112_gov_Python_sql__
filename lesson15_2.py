import streamlit as st

if 'content' not in st.session_state:
    st.session_state['count'] = 0

st.title("計數器")

increment = st.button('增加值',key="mybtn")
if increment:
    st.session_state.count += 1

st.write("計數器",st.session_state.count)
