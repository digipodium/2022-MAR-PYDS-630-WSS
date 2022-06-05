# TO Run - streamlit run app_example\app_2.py
import streamlit as st

st.title("Streamlit App Example : Widgets")

c1,c2 = st.columns(2)
c1.text("This is One section")
c2.text("This is Second section")
mopt = ['Option 1','Option 2','Option 3']
choice = c1.selectbox('Select an option',mopt)
c1.write(f'You selected {choice}')

fruits = ['Apple','Orange','Mango','Banana']
fav_fruit = c2.radio("your favourite fruit",fruits)
c2.success(f'You selected {fav_fruit}') 

st.header("Form example")
name = st.text_input("Enter your name")
address = st.text_area("Enter your address")
age = st.number_input("Enter your age",min_value=0,max_value=100)
pic = st.camera_input("Upload your pic")
if st.button("Submit"):
    st.success(f'Hello {name}')
    st.markdown(f'''
    ### Your name is {name}
    #### Your age is {age}
    ''')
