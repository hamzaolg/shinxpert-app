import streamlit as st
from PIL import Image
import base64
import io
import pandas as pd

st.set_page_config(page_title="ShinXpert", layout="centered")

# -------------------
# Authentification simple
# -------------------
def login():
    st.title("🔐 Login to ShinXpert")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "coach" and password == "shin123":
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

# -------------------
# Données des joueurs
# -------------------
players_data = [{'number': 1, 'time': '80 min', 'injury': '9%', 'speed': '32 km/h', 'heart': '87 bpm'}, {'number': 2, 'time': '53 min', 'injury': '8%', 'speed': '30 km/h', 'heart': '83 bpm'}, {'number': 3, 'time': '67 min', 'injury': '7%', 'speed': '21 km/h', 'heart': '83 bpm'}, {'number': 4, 'time': '57 min', 'injury': '10%', 'speed': '20 km/h', 'heart': '74 bpm'}, {'number': 5, 'time': '32 min', 'injury': '3%', 'speed': '26 km/h', 'heart': '69 bpm'}, {'number': 6, 'time': '79 min', 'injury': '5%', 'speed': '26 km/h', 'heart': '73 bpm'}, {'number': 7, 'time': '58 min', 'injury': '1%', 'speed': '24 km/h', 'heart': '68 bpm'}, {'number': 8, 'time': '81 min', 'injury': '9%', 'speed': '27 km/h', 'heart': '72 bpm'}, {'number': 9, 'time': '37 min', 'injury': '1%', 'speed': '26 km/h', 'heart': '78 bpm'}, {'number': 10, 'time': '78 min', 'injury': '5%', 'speed': '21 km/h', 'heart': '89 bpm'}, {'number': 11, 'time': '43 min', 'injury': '2%', 'speed': '20 km/h', 'heart': '66 bpm'}]
bpm_data = [72, 74, 75, 78, 80, 77, 76, 74, 73, 72]

# Sidebar + recherche joueur
st.sidebar.title("ShinXpert Dashboard")
search_input = st.sidebar.text_input("Search player number", "")
player = players_data[0]

if search_input:
    try:
        num = int(search_input)
        match = [p for p in players_data if p["number"] == num]
        if match:
            player = match[0]
        else:
            st.warning("Player not found.")
    except:
        st.warning("Enter a valid number")

st.markdown(f"### Player #{player['number']}")

# CSS & affichage stats
st.markdown("""
<style>
.card {
  background-color: #ffffff;
  border-radius: 15px;
  padding: 25px;
  color: #000;
  box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  font-size: 18px;
  text-align: center;
}
.card span {
  font-weight: bold;
  color: #222;
}
</style>
""", unsafe_allow_html=True)

html_block = f"""
<div class="card">
🕒 <span>{player['time']}</span> Time played  &nbsp;|&nbsp;
⚕️ <span>{player['injury']}</span> Injury risk  &nbsp;|&nbsp;
⚡ <span>{player['speed']}</span> Speed<br>
💓 <span>{player['heart']}</span> Heart rate
</div>
"""
st.markdown(html_block, unsafe_allow_html=True)

# BPM Chart
st.subheader("📈 Heart Rate Evolution")
bpm_df = pd.DataFrame(bpm_data, columns=["BPM"])
bpm_df.index.name = "Minute"
st.line_chart(bpm_df)

# Heatmap
st.subheader("📊 Player Heatmap")
heatmap_base64 = """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"""
image_data = base64.b64decode(heatmap_base64)
image = Image.open(io.BytesIO(image_data))
st.image(image, use_container_width=True)

# Export CSV
st.subheader("📁 Export Player Stats")
if st.button("Export to CSV"):
    df = pd.DataFrame([player])
    df.to_csv(f"player_{player['number']}_stats.csv", index=False)
    st.success(f"CSV exported for Player #{player['number']}.")

# Export PDF (simple)
import pdfkit
from tempfile import NamedTemporaryFile

if st.button("Export to PDF"):
    html = f"""
    <h2>Player #{player['number']} Stats</h2>
    <ul>
        <li>🕒 Time played: {player['time']}</li>
        <li>⚕️ Injury risk: {player['injury']}</li>
        <li>⚡ Speed: {player['speed']}</li>
        <li>💓 Heart rate: {player['heart']}</li>
    </ul>
    """

    try:
        with NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            pdfkit.from_string(html, f.name)
            with open(f.name, "rb") as pdf_file:
                st.download_button(
                    label="📄 Download PDF",
                    data=pdf_file,
                    file_name=f"player_{player['number']}_stats.pdf",
                    mime="application/pdf"
                )
    except Exception as e:
        st.error("PDF export failed. Please make sure pdfkit and wkhtmltopdf are properly installed.")

st.markdown("---")
st.caption("ShinXpert • Performance intelligence 💙")