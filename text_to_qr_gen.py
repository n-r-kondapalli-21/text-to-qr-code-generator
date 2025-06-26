import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Inject animated background and UI styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap');

html, body, .stApp {
    margin: 0;
    padding: 0;
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #a1c4fd, #c2e9fb);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

h1 {
    font-size: 2.5rem;
    color: white;
    text-align: center;
    margin-top: 50px;
    margin-bottom: 30px;
}

.stTextInput > div > input {
    border-radius: 12px;
    padding: 10px;
    border: 1px solid #ccc;
    font-size: 16px;
}

button[kind="primary"] {
    background-color: #ff6f61;
    border-radius: 12px;
    font-size: 16px;
    padding: 10px 20px;
    color: white;
    margin-top: 20px;
    transition: background-color 0.3s ease;
}

button[kind="primary"]:hover {
    background-color: #e85c50;
}

img {
    border-radius: 12px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1>QR Code Generator</h1>', unsafe_allow_html=True)

# User input
user_text = st.text_input("Enter text to generate QR code:")

# Generate and display QR code
if user_text:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(user_text)
    qr.make(fit=True)

    q_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    q_img = q_img.resize((300, 300), Image.Resampling.LANCZOS)

    buf = BytesIO()
    q_img.save(buf, format="PNG")
    buf.seek(0)

    st.image(buf, caption="Your QR Code", use_container_width=False)
    st.download_button(
        label="Download QR Code",
        data=buf,
        file_name="qrcode.png",
        mime="image/png"
    )
