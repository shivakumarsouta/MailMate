import streamlit as st
from agents.email_agent import generate_email_response
from utils.email_sender import send_email

st.set_page_config(page_title="Auto Email Responder", layout="wide")
st.title("MailMate - Think Less, Send Smart")

email_text = st.text_area("Paste the email content you have recieved:", height=300)
recipient_email = st.text_input("Recipient Email address")
tone = st.selectbox("Select response tone", ["Professional", "Friendly", "Apologetic", "Persuasive"])

if st.button("Generate & Send Email"):
    if not recipient_email:
        st.warning("Please enter the recipient Email address.")

    else:
        with st.spinner("Generating & Sending Email..."):
            response = generate_email_response(email_text, tone)
            send_status = send_email(recipient_email, response)
            st.subheader("✉️ Response")
            st.markdown(response, unsafe_allow_html=True)
            if send_status:
                st.success(f"Email sent successfully to {recipient_email}.")
            else:
                st.error("Failed to send Email.")