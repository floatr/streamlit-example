import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
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

# Check if the user is authenticated
if not authenticator.is_authenticated():
    st.warning("Please log in to access the app.")
    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")

    # Check if the user is preauthorized
    if authenticator.is_preauthorized(email):
        if st.button("Login"):
            if authenticator.authenticate(email, password):
                st.success(f"Successfully logged in as {authenticator.get_username(email)}!")
            else:
                st.error("Invalid credentials. Please try again.")
    else:
        st.warning("You are not authorized to access this app. Please contact support.")
else:
    st.success(f"Welcome back, {authenticator.get_username()}!")
    # Continue with your existing app logic

    num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
    num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

    indices = np.linspace(0, 1, num_points)
    theta = 2 * np.pi * num_turns * indices
    radius = indices

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    df = pd.DataFrame({
        "x": x,
        "y": y,
        "idx": indices,
        "rand": np.random.randn(num_points),
    })

    st.altair_chart(alt.Chart(df, height=700, width=700)
                    .mark_point(filled=True)
                    .encode(
                        x=alt.X("x", axis=None),
                        y=alt.Y("y", axis=None),
                        color=alt.Color("idx", legend=None, scale=alt.Scale()),
                        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
                    ))
