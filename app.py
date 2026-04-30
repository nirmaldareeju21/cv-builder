import streamlit as st
import whisper
import yt_dlp
import os
import re
from fpdf import FPDF

st.set_page_config(page_title="AI Video Summarizer", page_icon="📝")
st.title("📝 YouTube AI Video Summarizer")
st.write("වීඩියෝවේ ලින්ක් එක ලබා දී සාරාංශය PDF එකක් ලෙස ලබාගන්න.")

def clean_url(url):
    # ලින්ක් එකේ අගට එන අනවශ්‍ය දේවල් අයින් කිරීම
    clean = url.split('&')[0].split('?si=')[0]
    return clean

url_input = st.text_input("YouTube Link එක මෙතනට ලබා දෙන්න:")

if url_input:
    url = clean_url(url_input)
    if st.button("Summarize Now"):
        try:
            with st.status("AI එක වැඩ කරමින් පවතී...", expanded=True):
                st.write("📥 වීඩියෝව පරීක්ෂා කරමින්...")
                
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': 'audio_file.%(ext)s',
                    'quiet': False,
                    'no_warnings': False,
                    'nocheckcertificate': True,
                    # YouTube Block මගහැරීමට මෙය ඉතා වැදගත්
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    audio_filename = ydl.prepare_filename(info)
                
                st.write("🧠 AI මගින් සාරාංශය සකසමින්...")
                model = whisper.load_model("base")
                result = model.transcribe(audio_filename, task="translate")
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
                
            if os.path.exists(audio_filename):
                os.remove(audio_filename)

        except Exception as e:
            st.error(f"Error: {e}")
            st.info("සමහර වීඩියෝ YouTube මගින් බ්ලොක් කර ඇත. වෙනත් වීඩියෝ ලින්ක් එකක් උත්සාහ කරන්න.")
