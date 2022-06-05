# to run - streamlit run app_example\app_1.py
import streamlit as st

st.title("Streamlit App Example")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("lorem ipsum dolor sit amet")
st.write('This is a write')
a = 10
b = 20
c = a + b
st.write(f'{a} + {b} = {c}')
st.success('This is a success message')
st.info('This is an info message')
st.warning('This is a warning message')
st.error('This is an error message')
st.exception('This is an exception message')
st.markdown('This is a markdown message')