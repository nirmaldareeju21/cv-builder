import streamlit as st

# පෙනුම සකස් කිරීම
st.set_page_config(page_title="Walawwa Adventure", page_icon="🏰")

st.markdown("""
    <style>
    .stApp { background-color: #1a1a1a; color: #e0e0e0; } /* කළු පසුබිම - Horror/Mystery look */
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #4a0404; color: white; border: 1px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏰 වලව්වේ අභිරහස (Mystery of Walawwa)")

# Game State කළමනාකරණය
if 'scene' not in st.session_state:
    st.session_state.scene = 'start'

def change_scene(next_scene):
    st.session_state.scene = next_scene

# කතාවේ දර්ශන (Scenes)
if st.session_state.scene == 'start':
    st.image("https://img.freepik.com/free-photo/creepy-old-house-night_23-2151000676.jpg", caption="පාලු වලව්ව")
    st.write("වර්ෂාව අධික රාත්‍රියකි. ඔබේ වාහනය කැඩී අතරමං වී සිටින ඔබ, ඈතින් පෙනෙන පැරණි වලව්වක් දෙසට පියමනින්නෙහිය...")
    if st.button("වලව්වේ ප්‍රධාන දොරටුව තට්ටු කරන්න"):
        change_scene('door')
    if st.button("වත්ත වටේ ගොස් ජනේලයකින් බලන්න"):
        change_scene('window')

elif st.session_state.scene == 'door':
    st.write("ඔබ දොරට තට්ටු කළ සැණින් එය කෙඳිරිගාමින් විවෘත විය. ඇතුළත කිසිවෙකු නැත, නමුත් ලාම්පුවක් දැල්වෙමින් පවතී...")
    if st.button("ඇතුළට ගොස් 'කවුද ඉන්නේ?' කියා අසන්න"):
        change_scene('hall')
    if st.button("බිය වී ආපසු හැරී දිව යන්න"):
        change_scene('run')

elif st.session_state.scene == 'window':
    st.write("ඔබ ජනේලයෙන් බලන විට, කළු පැහැති සෙවනැල්ලක් වේගයෙන් කාමරය හරහා යනවා දුටුවේය!")
    if st.button("ධෛර්යය ගෙන ඇතුළට යාමට උත්සාහ කරන්න"):
        change_scene('door')
    if st.button("වහාම එතැනින් ඉවත් වන්න"):
        change_scene('run')

elif st.session_state.scene == 'hall':
    st.write("ඔබ සාලය මැද සිටගෙන සිටියදී, ඉහළ මාලයෙන් ගැහැනු ළමයෙකුගේ හැඬුම් හඬක් ඇසෙයි...")
    st.success("මතු සම්බන්ධයි... (To be continued)")
    if st.button("නැවත මුල සිට පටන් ගන්න"):
        change_scene('start')

elif st.session_state.scene == 'run':
    st.error("ඔබ බිය වී දිව යන විට මඩක පටලැවී බිම වැටුණි. වලව්වේ දොර ඉබේම වැසී ගියේය. ඔබ අතරමං විය!")
    if st.button("නැවත උත්සාහ කරන්න"):
        change_scene('start')
