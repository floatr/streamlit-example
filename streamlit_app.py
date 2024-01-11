import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import yaml
from pathlib import Path
import base64
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader

# Initial page config
st.set_page_config(
     page_title='Calidid con Precicíon - NuecesIA',
     layout="wide",
     initial_sidebar_state="expanded",
)

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


# st.sidebar.image('logo_vitakai.png', use_column_width=True)

st.sidebar.image('walnut_icon.png', width=50)



    #hashed_passwords = stauth.Hasher(['testing']).generate()
    #print(hashed_passwords)

    # Load authentication configurations from config.yaml
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

    # Create an authentication object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
    )

authentication_status = authenticator.login('Bienvenidos a la temporada 2024!','sidebar')

if st.session_state['authentication_status']:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    # container = st.container(border=True)
    # container.image('nuecesia_logo.png', width=150)
    with st.container():
        col1, col2, col3 = st.columns(3)
    with col2:
        st.image('nuecesia_logo.png', width=150)
    with st.container():
        st.markdown("""
        <style>
            .centered-header {
            text-align: center;
            }
        </style>
        <h1 class="centered-header">Precisión en calidad</h1>
        """, unsafe_allow_html=True)
