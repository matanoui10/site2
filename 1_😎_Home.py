from PIL import Image
import requests
import streamlit as st
import base64
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set the background image
with st.container():
    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://i.imghippo.com/files/tJGfA1721922579.png");
        background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
        background-position: center;  
        background-repeat: no-repeat;
    }
    </style>
    """

    st.markdown(background_image, unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Style/style.css")

# ASSETS

animatie = load_lottieurl("https://lottie.host/73f18945-54b2-4af0-9ba6-9c34eac4abd8/yqkf5pirZN.json")
imagine = Image.open("Images/123.jpg")
HOME = Image.open("D:\Website\Images\HOME.png")
# NAVIGATION

# Path to your image file
image_path = "D:\Website\Images\1280px-HD_transparent_picture.png"  # Adjust this path as needed

selected = option_menu(
    menu_title=None,
    options=["Acasa", "Despre", "Planuri", "Contact"],
    icons=["house-door-fill", "book-half", "backpack3-fill", "telephone-inbound-fill"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "rgba(0, 0, 0, 0)"},
        "icon": {"color": "#00BF63", "font-size": "25px"},
        "nav-link": {
            "font-size": "20px",
            "color": "#00BF63",
            "text-align": "middle",
            "margin": "0px",
            "--hover-color": "rgba(255, 255, 255, 0.5)",
        },
        "nav-link-selected": {"background-color": "rgba(0, 0, 0, 0)"},
    },
)
reduce_header_height_style = """
    <style>
        div.block-container {padding-top:1rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)

# HEADER
with st.container():
    left_colum, right_colum = st.columns(2)
    with left_colum:
        st.header("TESTE GRILE")
    with right_colum:
        st.subheader("ALL IN ONE PLACE")

# MAIN CONTENT
if selected == "Acasa":
    with st.container():
        st.write("---") # divider
        st.header("Teste")
        st.write("##") # spatiu
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

elif selected == "Despre":
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

elif selected == "Planuri":
    # Add your content for the "Planuri" section here
    st.write("Planuri content goes here")

elif selected == "Contact":
    with st.container():
        st.write("---")
        st.header("Daca aveti opinii")
        st.write("##")
        # Email address
        contact_form = """
        <form action="https://formsubmit.co/matanouipolojan@yahoo.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Numele" required>
            <input type="email" name="email" placeholder="Email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_colum = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_colum:
            st.empty()
