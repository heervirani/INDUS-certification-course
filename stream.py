import streamlit as st
st.title("Example")
no=st.text_input("Enter no")
if(st.button("Clickme")):
    if int(no)%2==0:
        st.write("ans is")
        st.write("no is even")
        st.balloons()
    else:
        st.write("ans is")
        st.warning("no is odd")