import streamlit as st
st.write('Hello Everyone')

st.title('Diabetes prediction')
st.markdown('Diabetes prediction')
st.header('Diabetes prediction')
st.subheader('Diabetes prediction')


st.checkbox('Pick your option',['Yes','No'])
st.button('Do prediction')
st.radio('Gender',['Male','Female'])
st.selectbox('pick your option',['A','B','C'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])	

st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])

st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)


st.number_input('enter input',)