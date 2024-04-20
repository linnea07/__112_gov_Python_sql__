import streamlit as st 

st.title("Sessin_state基礎")
st.write(st.session_state)
number:int = st.slider("數值",min_value=1,max_value=10,key='mySlider')
st.write("加入slider",st.session_state)

col1, buff ,col2 =st.columns([1,0.5,3])

next = st.button("下一個選項")
if next:
    if st.session_state.radio_option == "a":
        st.session_state.radio_option = "b"
    elif st.session_state.radio_option == "b":
        st.session_state.radio_option = "c"
    else: 
        st.session_state.radio_option = "a"

with col1:
    option_names =["a","b","c"]
    option = st.radio("請選擇1個",option_names,key="radio_option")
    st.write("加入radio後",st.session_state)

with col2:
    if option == 'a':
        st.write("你選擇的是a :smile:")
    elif option == 'b':
        st.write("你選擇的是b :smile:")
    elif option == 'c':
        st.write("你選擇的是b :smile:")



    