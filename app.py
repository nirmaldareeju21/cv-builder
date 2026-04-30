import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from fpdf import FPDF
from transformers import pipeline
import re

# Page setup
st.set_page_config(page_title="AI Video Assistant", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f9f6f2; } 
    .stButton>button { width: 100%; border-radius: 20px; background-color: #d97757; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 AI Video Assistant (Pro)")
st.caption("Summarize YouTube videos using transcripts + AI.")

# Summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_video_id(url):
    reg = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(reg, url)
    return match.group(1) if match else None

if url := st.chat_input("Paste YouTube link here..."):
    st.chat_message("user").markdown(url)
    msg = st.chat_message("assistant").empty()
    msg.markdown("Analyzing transcript... 🔍")

    try:
        video_id = extract_video_id(url)
        if not video_id:
            raise Exception("Invalid YouTube Link")

        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([i['text'] for i in transcript_list])

        # Summarization
        summary_chunks = summarizer(full_text, max_length=200, min_length=50, do_sample=False)
        summary = " ".join([chunk['summary_text'] for chunk in summary_chunks])

        response = f"✅ Transcript analyzed successfully!\n\n**Summary:**\n{summary}"
        msg.markdown(response)

        # PDF Export
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=summary.encode('latin-1', 'ignore').decode('latin-1'))
        pdf.output("summary.pdf")

        st.download_button("📥 Download PDF Summary", open("summary.pdf", "rb"), file_name="Summary.pdf")

    except Exception as e:
        error_msg = f"❌ Error: {str(e)}\n\n(Note: This video might not have captions enabled.)"
        msg.markdown(error_msg)
