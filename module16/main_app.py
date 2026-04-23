import streamlit as st

if st.button("Click Me"):
    st.write("Ec hup")

if st.checkbox("tick ok"):
    st.write("ok")

user_inputs = st.text_input("Enter Text", "sample")
st.write(user_inputs)

age = st.number_input("entr ag", min_value=0, max_value=100)
st.write(age)
if age > 80:
    st.write("rrenc")

message = st.text_area("Entr a msg")
st.write(message)

choice = st.radio("pik one", ["Ok","ok2","Cooler ok"])
if choice == "Cooler ok":
    st.write(f"you choose 😎: {choice}")


if st.button("Success"):
    st.success("operaniotn wsa sucesufla")

try:
    1/0
except Exception as e:
    st.exception(e)