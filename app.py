import streamlit as st
from agents.email_agent import generate_email_response
from utils.email_sender import send_email

st.set_page_config(page_title="Auto Email Responder", layout="wide")
st.title("MailMate - Think Less, Send Smart")

# Inputs
email_text = st.text_area("📩 Paste the email you received:", height=300)
recipient_email = st.text_input("✉️ Recipient Email address")
tone = st.selectbox("🎨 Select response tone", ["Professional", "Friendly", "Apologetic", "Persuasive"])

# Session state to persist draft
if "draft_reply" not in st.session_state:
    st.session_state.draft_reply = ""

# Step 1: Generate only
if st.button("💡 Generate Reply"):
    if not recipient_email:
        st.warning("Please enter the recipient Email address.")
    else:
        with st.spinner("Generating reply..."):
            st.session_state.draft_reply = generate_email_response(email_text, tone)

# Step 2: Show editable preview
if st.session_state.draft_reply:
    st.subheader("✍️ Preview & Edit Generated Email")

    # Ensure editable_reply is initialized only once
    if "editable_reply" not in st.session_state:
        st.session_state.editable_reply = st.session_state.draft_reply

    # Editable TextArea (linked to session_state)
    edited_reply = st.text_area(
        "You can edit the generated email before sending:",
        key="editable_reply", 
        height=300
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("✅ Send Email"):
            with st.spinner("Sending email..."):
                success = send_email(recipient_email, st.session_state.editable_reply)
                if success:
                    st.success(f"Email sent to {recipient_email} successfully!")
                    st.session_state.draft_reply = ""
                    del st.session_state.editable_reply
                else:
                    st.error("Failed to send email.")

    with col2:
        if st.button("❌ Cancel Draft"):
            st.session_state.draft_reply = ""
            del st.session_state.editable_reply 