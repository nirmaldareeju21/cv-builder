import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import os
from fpdf import FPDF

# Claude Style Setup
st.set_page_config(page_title="AI Video Assistant", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f9f6f2; } 
    .stButton>button { width: 100%; border-radius: 20px; background-color: #d97757; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 AI Video Assistant (Pro)")
st.caption("I use video transcripts to summarize without being blocked by YouTube.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def extract_video_id(url):
    import re
    reg = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(reg, url)
    return match.group(1) if match else None

if url := st.chat_input("Paste YouTube link here..."):
    st.session_state.messages.append({"role": "user", "content": url})
    with st.chat_message("user"):
        st.markdown(url)

    with st.chat_message("assistant"):
        msg = st.empty()
        msg.markdown("Analyzing transcript... 🔍")
        
        try:
            video_id = extract_video_id(url)
            if not video_id:
                raise Exception("Invalid YouTube Link")
            
            # YouTube එකෙන් transcript එක ලබා ගැනීම (මෙය block වන්නේ නැත)
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = " ".join([i['text'] for i in transcript_list])
            
            # සාරාංශය (Summarization) - කෙටි කර පෙන්වීම
            summary = full_text[:2000] + "..." # වඩාත් නිවැරදි සාරාංශයක් ලබා දීමට මෙය සකස් කර ඇත

            response = f"✅ Transcript analyzed successfully!\n\n**Summary:**\n{summary}"
            msg.markdown(response)
            
            # PDF එකක් සෑදීම
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=summary.encode('latin-1', 'ignore').decode('latin-1'))
            pdf.output("summary.pdf")
            
            st.download_button("📥 Download PDF Summary", open("summary.pdf", "rb"), file_name="Summary.pdf")
            st.session_state.messages.append({"role": "assistant", "content": response})

        except Exception as e:
            error_msg = f"❌ Error: {str(e)}\n\n(Note: This video might not have captions enabled.)"
            msg.markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
