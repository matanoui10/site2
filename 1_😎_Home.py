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

#-------------Set_the_background_image-------------
with st.container():
    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://i.imghippo.com/files/n0R1m1721995649.png");
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

#-------------Load_CSS-------------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Style/style.css")

#-------------ASSETS-------------

animatie = load_lottieurl("https://lottie.host/73f18945-54b2-4af0-9ba6-9c34eac4abd8/yqkf5pirZN.json")
imagine = Image.open("Images/123.jpg")
HOME = Image.open("D:\Website\Images\HOME.png")

#-------------NAVIGATION-------------

image_path = "D:\Website\Images\1280px-HD_transparent_picture.png"
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
            "color": "white",
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

#-------------HOME-------------

st.markdown("""
    <style>
    @font-face {
        font-family: 'Ja Jayagiri Sans';
        src: url('https://path-to-your-font/JaJayagiriSans.woff2') format('woff2');
    }
    .left-font {
        font-family: 'Ja Jayagiri Sans', sans-serif;
        text-align: right;
        font-size: 66.5px;
        line-height: 1.2;
    }
    .right-column-font {
        font-family: 'Ja Jayagiri Sans', sans-serif;
        font-size: 40px;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown("""
    <style>
    .custom-font {
        font-family: 'Open Sans', sans-serif;
        text-align: center;
        font-size: 24px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .left-column {
        padding-right: 120px;
    }
    .right-column {
        padding-left: -50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
if selected == "Acasa":
    with st.container():
        left_column, right_column= st.columns(2)
        with left_column:
            st.markdown(
                """
                <div class="left-column" style="position: relative; height: 100%;">
                <div class="left-font">
                    TESTE<br>GRILE
                </div>
                """,
                unsafe_allow_html=True
            )
        with right_column:
            st.markdown(
                """
                <div class="right-column" style="position: relative; height: 100%;">
                <div class="right-column-font">
                <br>
                    ALL IN ONE PLACE
                </div>
                """,
                unsafe_allow_html=True
            )
        with st.container():
            st.markdown(
                """
                <div class="custom-font">
                Bac? Admitere? Fii pregătit pentru <span style="color: #00BF63;">ORICE</span>.
                <br>
                Punem la dispoziție <span style="color: #00BF63;">1000+</span> grile, subiecte anterioare,
                <br>
                materie structurată, corectură personalizată && more
                </div>
                """,
                unsafe_allow_html=True
            )
        st.write("##")

        with st.container():
            # Adjust column width ratios to bring the buttons closer to the center
            left_column, center_column, right_column = st.columns([1, 0.2, 1])
            with left_column:
                st.markdown(
                    """
                    <div style="text-align: right; font-size: 26px"; font-family: 'Open Sans', sans-serif;">
                        <a href="#" style="background-color: #00BF63; color: black; padding: 20px 20px; text-decoration: none; border-radius: 20px;">Try it for free</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with center_column:
                st.markdown(
                    """
                    <div style="text-align: center; position: relative; top: 50%; transform: translateY(-25%); font-size: 39px;">       
                        or
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with right_column:
                st.markdown(
                    """
                    <div style="text-align: left; font-size: 26px"; font-family: 'Open Sans', sans-serif;>
                        <a href="#" style="background-color: black; color: #00BF63; padding: 20px 20px; text-decoration: none; border-radius: 20px; border: 2px solid #00BF63;">Try it for fun</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

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
