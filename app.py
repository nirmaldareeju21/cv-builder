import streamlit as st
import whisper
import os
from fpdf import FPDF

st.set_page_config(page_title="AI Audio Summarizer", page_icon="📝")
st.title("📝 AI Audio Summarizer to PDF")
st.write("ඔබේ Audio (.mp3) ගොනුව ලබා දී එහි සාරාංශය PDF එකක් ලෙස ලබාගන්න.")

# Audio file upload කිරීමට ඉඩ දීම
uploaded_file = st.file_uploader("ඔබේ Audio ගොනුව (MP3) තෝරන්න:", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    if st.button("Summarize Now"):
        try:
            with st.status("AI එක වැඩ කරමින් පවතී...", expanded=True):
                # ගොනුව තාවකාලිකව save කිරීම
                with open("temp_audio.mp3", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Whisper AI මගින් සාරාංශය කිරීම
                st.write("🧠 AI මගින් සාරාංශය සකසමින්...")
                model = whisper.load_model("base")
                result = model.transcribe("temp_audio.mp3", task="translate")
                summary_text = result["text"]

            st.subheader("Summary:")
            st.success(summary_text)

            # PDF එකක් සෑදීම
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            clean_text = summary_text.encode('latin-1', 'ignore').decode('latin-1')
            pdf.multi_cell(0, 10, txt=clean_text)
            pdf.output("summary.pdf")

            with open("summary.pdf", "rb") as f:
                st.download_button("📥 Download PDF", f, file_name="AI_Summary.pdf")
                
            os.remove("temp_audio.mp3") # ඉඩ ඉතිරි කර ගැනීමට මකා දැමීම

        except Exception as e:
            st.error(f"Error: {e}")
