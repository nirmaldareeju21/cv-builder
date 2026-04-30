import streamlit as st
import whisper
import yt_dlp
import os
from fpdf import FPDF

# පිටුවේ පෙනුම Claude වගේ සකස් කිරීම
st.set_page_config(page_title="AI Video Assistant", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f9f6f2; } 
    .stButton>button { width: 100%; border-radius: 20px; background-color: #d97757; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 AI Video Assistant")
st.caption("I can summarize any YouTube video for you. Just provide the link.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if url := st.chat_input("Paste YouTube link here..."):
    st.session_state.messages.append({"role": "user", "content": url})
    with st.chat_message("user"):
        st.markdown(url)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking... 🔍")
        
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': 'audio_file.%(ext)s',
                'quiet': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                audio_filename = ydl.prepare_filename(info)
            
            model = whisper.load_model("base")
            result = model.transcribe(audio_filename, task="translate")
            summary = result["text"]

            full_response = f"Here is the summary of the video:\n\n{summary}"
            message_placeholder.markdown(full_response)
            
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            clean_text = summary.encode('latin-1', 'ignore').decode('latin-1')
            pdf.multi_cell(0, 10, txt=clean_text)
            pdf.output("summary.pdf")
            
            st.download_button("📥 Download PDF Report", open("summary.pdf", "rb"), file_name="Summary.pdf")
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            os.remove(audio_filename)

        except Exception as e:
            error_msg = f"Sorry, I encountered an error: {e}"
            message_placeholder.markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
