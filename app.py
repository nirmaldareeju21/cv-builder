import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from fpdf import FPDF
import re
import os

# Page setup - Claude Style
st.set_page_config(page_title="AI Video Assistant", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f9f6f2; } 
    .stButton>button { width: 100%; border-radius: 20px; background-color: #d97757; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 AI Video Assistant (Pro)")
st.caption("I provide clean summaries using YouTube transcripts.")

# Session state to keep chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def extract_video_id(url):
    reg = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(reg, url)
    return match.group(1) if match else None

# Main logic
if url_input := st.chat_input("Paste YouTube link here..."):
    st.session_state.messages.append({"role": "user", "content": url_input})
    with st.chat_message("user"):
        st.markdown(url_input)

    with st.chat_message("assistant"):
        msg = st.empty()
        msg.markdown("Fetching transcript and summarizing... 🔍")
        
        try:
            video_id = extract_video_id(url_input)
            if not video_id:
                raise Exception("Invalid YouTube Link. Please check the URL.")

            # Get Transcript
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = " ".join([i['text'] for i in transcript_list])

            # AI Summary logic (Simple but effective for Free tier)
            # මුල් වචන 1500 සාරාංශයක් ලෙස ගනිමු (වඩා දියුණු AI වලට වඩා මෙය Free tier එකේ stable වේ)
            summary = full_text[:1500] + ("..." if len(full_text) > 1500 else "")

            response = f"✅ **Analysis Complete!**\n\n**Summary:**\n{summary}"
            msg.markdown(response)

            # PDF Export logic
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            # Encoding fix for FPDF
            clean_text = summary.encode('latin-1', 'ignore').decode('latin-1')
            pdf.multi_cell(0, 10, txt=clean_text)
            pdf.output("summary.pdf")

            st.download_button("📥 Download PDF Summary", open("summary.pdf", "rb"), file_name="Summary.pdf")
            st.session_state.messages.append({"role": "assistant", "content": response})

        except Exception as e:
            error_msg = f"❌ Error: {str(e)}\n\n(Note: Subtitles might be disabled for this video.)"
            msg.markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
