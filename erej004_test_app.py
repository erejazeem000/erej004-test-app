import streamlit as st
from PIL import Image


st.markdown("""
# Simple Calculator
""")
st.subheader("""This is basic calculator application
   """)
image = Image.open('calc.jpeg')
st.image(image)


options = ["Addition", "Subtraction", "Multiplication", "Division"]
choice = st.radio("Choose the Operation", options)
if choice == "Addition":
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        c = a+b
        st.text("The result of addition is")
        st.write(c)
elif choice == "Subtraction":
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        c = a - b
        st.text("The result of Subtraction is")
        st.write(c)
elif choice == "Multiplication":
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        c = a * b
        st.text("The result of Multiplication is")
        st.write(c)
elif choice == "Division":
        st.warning("Must enter Some value Otherwise You'll get Error!")
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        remainder = a % b
        modulus = a / b
        st.write("Results are : ")
        st.write(" Reminder is ", remainder)
        st.write(" Modulus is ", modulus)


st.header("Advanced Calculator")
options = ["Factorial", "Exponent", "Square Root"]
choice = st.selectbox("Option", options)
    # if choice == "Addition":
    #     a = st.number_input("Please input First Number")
    #     b = st.number_input("Please input Second Number")
    #     c = a+b
    #     st.text("The result of addition is")
    #     st.write(c)
if choice == "Factorial":
        a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)
        factorial = 1
        if a < 0:
            st.write("Sorry!!, factorial does not exist for negative numbers")
        elif a == 0:
            st.write("The factorial of 0 is 1")
        else:
            for i in range(1, a + 1):
                factorial = factorial * i
            st.write("The factorial of", a, "is", factorial)
    #
elif choice == "Exponent":
        a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)
        b = st.number_input("Enter a Exponential value: ", min_value=0, max_value=100, value=1, step=1)

        result = a ** b
        st.write("Result is : ", result)


elif choice == "Square Root":
        a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)
        square_root = a * a
        st.write("Sruare of", a, "is", square_root)

        # x = int(input('Enter your number'))
        # z = x * x
        # print(z)




