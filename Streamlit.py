import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 
from PIL import Image
import pickle

with open("best_class.pkl", "rb") as f:
    model = pickle.load(f)
with open("best_cluster.pkl", "rb") as f:
    cluster = pickle.load(f)

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

    inputs = ""


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
