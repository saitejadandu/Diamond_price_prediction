import streamlit as st
import pickle
import numpy as np

with open("diamond_prediction_model.pkl","rb") as file:
    model=pickle.load(file)

st.title("Diamond Price Prediction")

carat=st.number_input("Carat Weight", min_value=0.0, step=0.01)
cut=st.selectbox("Cut Quality", ["Fair","Good","Very Good","Premium","Ideal"])
color=st.selectbox("Color Grade", ["J","I","H","G","F","E","D"])
clarity=st.selectbox("Clarity Grade", ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"])
depth=st.number_input("Depth Percentage", min_value=0.0, step=0.1)
table=st.number_input("Table Percentage", min_value=0.0, step=0.1)

cut_dict={"Fair":0,"Good":1,"Very Good":2,"Premium":3,"Ideal":4}
color_dict={"J":0,"I":1,"H":2,"G":3,"F":4,"E":5,"D":6}
clarity_dict={"I1":0,"SI2":1,"SI1":2,"VS2":3,"VS1":4,"VVS2":5,"VVS1":6,"IF":7}
cut_encoded=cut_dict[cut]
color_encoded=color_dict[color]
clarity_encoded=clarity_dict[clarity]
input_data=np.array([[carat,cut_encoded,color_encoded,clarity_encoded,depth,table]])
if st.button("Predict Price"):
    prediction=model.predict(input_data)
    st.success(f"The predicted price of the diamond is: ${prediction[0]:.2f}")



