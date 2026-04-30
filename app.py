import streamlit as st
import whisper
import yt_dlp
import os
from fpdf import FPDF

st.set_page_config(page_title="AI Video Summarizer", page_icon="📝")
st.title("📝 YouTube AI Video Summarizer")
st.write("වීඩියෝවේ සාරාංශය ගෙන PDF එකක් ලෙස ලබාගන්න.")

url = st.text_input("YouTube Link එක මෙතනට ලබා දෙන්න:")

if url:
    if st.button("Summarize Now"):
        try:
            with st.status("AI එක වැඩ කරමින් පවතී...", expanded=True):
                # Audio එක බාගැනීම
                ydl_opts = {'format': 'bestaudio/best', 'outtmpl': 'audio_file'}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                # Whisper AI මගින් ලියවිල්ලක් කිරීම සහ පරිවර්තනය
                model = whisper.load_model("base")
                result = model.transcribe("audio_file.webm", task="translate")
                summary_text = result["text"]

            st.subheader("Summary:")
            st.success(summary_text)

            # PDF එකක් සෑදීම
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=summary_text.encode('latin-1', 'ignore').decode('latin-1'))
            pdf.output("summary.pdf")

            with open("summary.pdf", "rb") as f:
                st.download_button("📥 Download PDF", f, file_name="AI_Summary.pdf")
        except Exception as e:
            st.error(f"Error: {e}")