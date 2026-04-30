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
            with st.status("AI එක වැඩ කරමින් පවතී... (මෙයට විනාඩි කිහිපයක් ගත විය හැක)", expanded=True):
                # 1. Download Audio with better settings to avoid 403
                st.write("📥 වීඩියෝව පරීක්ෂා කරමින්...")
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': 'audio_file.%(ext)s',
                    'quiet': True,
                    'no_warnings': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    audio_filename = ydl.prepare_filename(info)
                
                # 2. Transcription and Translation
                st.write("🧠 AI මගින් ලියවිල්ල සකසමින්...")
                model = whisper.load_model("base")
                result = model.transcribe(audio_filename, task="translate")
                summary_text = result["text"]

            st.subheader("Summary:")
            st.success(summary_text)

            # 3. PDF Generation
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=summary_text.encode('latin-1', 'ignore').decode('latin-1'))
            pdf.output("summary.pdf")

            with open("summary.pdf", "rb") as f:
                st.download_button("📥 Download Summary PDF", f, file_name="AI_Summary.pdf")
                
            # Cleanup
            if os.path.exists(audio_filename):
                os.remove(audio_filename)

        except Exception as e:
            st.error(f"Error: YouTube system blocked the request. Try another link or wait. ({e})")
