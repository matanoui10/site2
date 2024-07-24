import os
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.jason()

#CSS

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Style/style.css")
#ASSETS

animatie = "https://lottie.host/73f18945-54b2-4af0-9ba6-9c34eac4abd8/yqkf5pirZN.json"
imagine = Image.open("Images/123.jpg")

#NAVIGATION
selected = option_menu(
        menu_title="Main Meniu",
        options=["Home", "Politehnica", "Contcat"],
        default_index=0,
        orientation="horizontal",
)

#HEADER

with st.container():
    st.subheader("Hi, I am Stefan :wave:")
    st.title("Teste admitere")
    st.write("Acest site a fost creat pentru a ajuta elevii de clasa a 12 a")
    st.write("[Instagram>](https://www.instagram.com/stefanpolojan_09)")#Link la instagramul meu

with st.container():
    st.write("---")#divider
    st.header("Teste")
    st.write("##")#spatiu
    left_colum, right_colum = st.columns(2)
    with left_colum:
        st.header("Politehnica")
        st.write("Mate")
        st.write("Info")
        st.write("Fizica")
        st.header("FMI")
        st.write("Mate")
        st.write("Info")
        st.write("Fizica")
    with right_colum:
        st_lottie(animatie, height=350, key="Test")

with st.container():
    st.write("---")
    st.header("Fondatorii")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(imagine)
    with text_column:
        st.header("Nicole")
        st.write("Unul dintre cei care au creat siteul")
with st.container():
    st.write("---")
    st.header("Daca aveti opinii")
    st.write("##")
    #Email adress
    contact_form = """
    <form action="https://formsubmit.co/matanouipolojan@yahoo.com" method="POST">
         <imput type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Numele" required>
         <input type="email" name="email" placeholder="Email" required>
         <textarea name="message" placeholder="Your message here" requierd></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_colum = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_colum:
        st.empty()