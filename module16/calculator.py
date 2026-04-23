import streamlit as st

def calculate(num1 , num2, operation):

    if operation == " ＋ ":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == ":":
        result = num1 * num2
    elif operation == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Smunesh haver me 0"

    return result

def main():
    st.title("kalkulator")

    num1 = st.number_input("numri i par", step=1)
    num2 = st.number_input("numri dyte", step=1)


    operation = st.radio("select number", [" ＋ ","-",":","/"])

    result = calculate(num1, num2, operation)

    st.write(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()