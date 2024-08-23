import streamlit as st
import pickle

st.title("🎈 Cars")
f1=st.number_input('feature 1',min_value=1,max_value=10,value=1)
f2=st.number_input('feature 2',min_value=1,max_value=10,value=1)
f3=st.number_input('feature 3',min_value=1,max_value=100,value=1)


with open('model (1).pkl','rb') as file:
  model = pickle.load(file)
res=model.predict([[f1,f2,f3]])


st.write('Result : ',res[0][0])
