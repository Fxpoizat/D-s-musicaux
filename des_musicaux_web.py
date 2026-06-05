import streamlit as st
import random

notes = [
    "", "Do (C)", "Do♯ / Ré♭ (C♯ / D♭)", "Ré (D)", "Ré♯ / Mi♭ (D♯ / E♭)",
    "Mi (E)", "Fa (F)", "Fa♯ / Sol♭ (F♯ / G♭)", "Sol (G)",
    "Sol♯ / La♭ (G♯ / A♭)", "La (A)", "La♯ / Si♭ (A♯ / B♭)", "Si (B)"
]

base_modes = [
    "Ionien", "Dorien", "Phrygien", "Lydien", "Mixolydien",
    "Éolien", "Locrien"
]

st.set_page_config(page_title="🎲 Dés Musicaux", page_icon="🎵", layout="centered")
st.title("🎲 Lanceur de Dés Musical ! 🎲")
st.markdown("**Tire une note + un mode au hasard** pour tes improvisations, compositions ou exercices")

st.markdown("### ⚙️ Options de gammes supplémentaires")

col1, col2, col3 = st.columns(3)
with col1:
    add_whole = st.checkbox("Ajouter les gammes de tons", value=False)
with col2:
    add_pent = st.checkbox("Ajouter les gammes pentatoniques", value=False)
with col3:
    add_complex = st.checkbox("Ajouter les gammes complexes", value=False)

st.caption("Les 7 modes de base sont toujours inclus.")

if st.button("🎲 LANCER LES DÉS 🎲", type="primary", use_container_width=True):
    note_num = random.randint(1, 12)
    available_modes = base_modes.copy()
    if add_whole:
        available_modes.append("Gamme de ton")
    if add_pent:
        available_modes.extend(["Pentatonique majeure", "Pentatonique mineure"])
    if add_complex:
        available_modes.extend(["Mineur harmonique", "Mineur mélodique ascendant", "Gamme de blues"])

    selected_mode = available_modes[random.randint(0, len(available_modes)-1)]

    st.success(f"**Note :** {notes[note_num]}")
    st.success(f"**Mode :** {selected_mode}")
    st.markdown(f"### 🎵 Tu joues dans : **{notes[note_num]} {selected_mode}**")

    if "history" not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append(f"{notes[note_num]} {selected_mode}")
    if len(st.session_state.history) > 10:
        st.session_state.history.pop(0)

st.markdown("---")
st.subheader("📜 Historique des derniers tirages")
if "history" in st.session_state and st.session_state.history:
    for i, tirage in enumerate(reversed(st.session_state.history)):
        st.markdown(f"**{len(st.session_state.history)-i}.** {tirage}")
else:
    st.info("Aucun tirage pour le moment…")

if st.button("🗑️ Effacer l’historique"):
    st.session_state.history = []
    st.rerun()

st.caption("Made with ❤️ pour les musiciens")
