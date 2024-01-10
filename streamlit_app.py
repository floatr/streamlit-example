import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import yaml
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader

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

# Initialize session state
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None
    
authenticator.login('Login', 'main')

if st.session_state['authentication_status']:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')