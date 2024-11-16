import  streamlit as st


st.title("Cars 24 second hand car price prediction")

st.header("My Calculator")

def square(x):
    return x**2

x = st.number_input("Enter the number")

if st.button("Submit"):
    res = square(x)
    st.write(res)

