import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 
from PIL import Image
import pickle
import pandas as pd

with open("best_class.pkl", "rb") as f:
    model = pickle.load(f)
with open("best_cluster.pkl", "rb") as f:
    cluster = pickle.load(f)
with open ("training columns.pkl", "rb") as f:
    training_columns = pickle.load(f)
with open("Cluster maping.pkl", "rb") as f:
    cluster_maping = pickle.load(f)

def homepage():
    st.title("WELCOME TO PHONE USAGE PATTERN")
    Image1 = Image.open("D:/Guvi/Projects/Phone usage/images/generated-image.png")
    st.image(Image1, use_container_width=True)

def EDA():
    st.title("WELCOME TO EPLORATORY DATA ANALYSIS")
    Image2 = Image.open("D:/Guvi/Projects/Phone usage/images/output1.png")
    Image3 = Image.open("D:/Guvi/Projects/Phone usage/images/output2_2.png")
    Image4 = Image3.resize((900, 400))
    Image5 = Image.open("D:/Guvi/Projects/Phone usage/images/output3.png")
    st.image(Image2, use_container_width=True )
    st.image(Image4, use_container_width=True)
    st.image(Image5, use_container_width=True )

def prediction():
    st.title("WELCOME TO PREDICTION OF YOUR PHONE USAGE")
    st.subheader("Please enter the details of your choice")

    Age = st.number_input("Age (15-100)", 15, 60, 35, key="Age" )
    Gender = st.selectbox("Gender", ['Male', 'Other', 'Female'])
    Location = st.selectbox("Location",['Mumbai', 'Delhi', 'Ahmedabad', 'Pune', 'Jaipur', 'Lucknow',
       'Kolkata', 'Bangalore', 'Chennai', 'Hyderabad'])
    Phone_Brand = st.selectbox("Phone Brand", ['Vivo', 'Realme', 'Nokia', 'Samsung', 'Xiaomi', 'Oppo', 'Apple',
       'Google Pixel', 'Motorola', 'OnePlus'])
    OS = "iOS" if Phone_Brand =="Apple" else "Android"
    Screen_Tim_hrs_perday = st.slider("Screen Time (hrs/day)", 1, 12, 5, key="Screen Time")
    Data_Usage_permonth = st.slider("Data Usage (GB/month)", 1, 100, 30, key="Data Usage")
    Calls_Duration_mins_perday = st.slider("Calls Duration (mins/day)", 5, 300, 100, key="Calls Duration")
    Number_of_Apps_Installed = st.slider("Number of Apps Installed", 10, 200, 60, key = "Number of Apps Installed")
    Social_Media_Time_hrs_perday = st.slider("Social Media Time (hrs/day)", 0.5, 6.0, 2.0, key="Social Media Time")
    E_commerce_Spend_INR_permonth = st.slider("E-commerce Spend (INR/month)", 100, 10000, 4000, key = "E-commerce Spend")
    Streaming_Time_hrs_perday = st.slider("Streaming Time (hrs/day)", 0.5, 8.0, 2.0, key="Streaming Time")
    Gaming_Time_hrs_perday = st.slider("Gaming Time (hrs/day)", 0.0, 5.0, 2.0, key="Gaming Time")
    Monthly_Recharge_Cost = st.slider("Monthly Recharge Cost (INR)", 100, 2000, 300, key = "Monthly Recharge Cost (INR)")



    inputs = {
        "Age" : Age,
        "Gender" : Gender,
        "Location" : Location,
        "Phone Brand" : Phone_Brand,
        "OS": OS,
        "Screen Time (hrs/day)" : Screen_Tim_hrs_perday,
        "Data Usage (GB/month)" : Data_Usage_permonth,
        "Calls Duration (mins/day)" :Calls_Duration_mins_perday, 
        "Number of Apps Installed" : Number_of_Apps_Installed,
        "Social Media Time (hrs/day)" : Social_Media_Time_hrs_perday,
        "E-commerce Spend (INR/month)" : E_commerce_Spend_INR_permonth,
        "Streaming Time (hrs/day)" : Streaming_Time_hrs_perday,
        "Gaming Time (hrs/day)" : Gaming_Time_hrs_perday,
        "Monthly Recharge Cost (INR)" : Monthly_Recharge_Cost
    }

    cat_columns = ['Gender', 'Location', 'Phone Brand', 'OS']
    num_columns = ['Age', 'Screen Time (hrs/day)', 'Data Usage (GB/month)',
       'Calls Duration (mins/day)', 'Number of Apps Installed',
       'Social Media Time (hrs/day)', 'E-commerce Spend (INR/month)',
       'Streaming Time (hrs/day)', 'Gaming Time (hrs/day)',
       'Monthly Recharge Cost (INR)']
    
    df_input = pd.DataFrame([inputs])

    df_cat_encoded = pd.get_dummies(df_input[cat_columns])

    df_final = pd.concat([df_cat_encoded, df_input[num_columns]], axis =1)
    df_final = df_final.reindex(columns=training_columns, fill_value=0)

    if st.button("Predict The Use Group"):
        prediction = cluster.predict(df_final)[0]
        primary_use = cluster_maping.get(prediction, "Unknown")
        st.success(f"You Belong to the Goup of : {primary_use}")
    


def thanks():
    st.title("Thank you")
    st.image("C:/Users/LONE PIRATE.LAPTOP-PAANLTJP/OneDrive/Pictures/hand-lettering-thank-you-flowery-vector.jpg")
    st.subheader("By Abinash")

pages = {
    "Home": homepage,
    "EDA" : EDA,
    "Predict" : prediction,
    "End" : thanks
}

selection = st.sidebar.radio("Choose a page", list(pages.keys()))
pages[selection]()
