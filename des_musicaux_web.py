import streamlit as st
import random

# ================== DONNÉES MUSICALES ==================
notes = [
    "", "Do (C)", "Do♯ / Ré♭ (C♯ / D♭)", "Ré (D)", "Ré♯ / Mi♭ (D♯ / E♭)",
    "Mi (E)", "Fa (F)", "Fa♯ / Sol♭ (F♯ / G♭)", "Sol (G)",
    "Sol♯ / La♭ (G♯ / A♭)", "La (A)", "La♯ / Si♭ (A♯ / B♭)", "Si (B)"
]

modes = [
    "", "Ionien", "Dorien", "Phrygien", "Lydien", "Mixolydien",
    "Éolien", "Locrien", "Mineur harmonique", "Mineur mélodique ascendant", "Gamme de ton"
]

# ================== CONFIGURATION DE L'APP ==================
st.set_page_config(page_title="🎲 Dés Musicaux", page_icon="🎵", layout="centered")

st.title("🎲 Lanceur de Dés Musical ! 🎲")
st.markdown("**Tire une note + un mode au hasard** pour tes improvisations, compositions ou exercices")

# Bouton principal bien visible
if st.button("🎲 **LANCER LES DÉS** 🎲", type="primary", use_container_width=True, key="roll"):
    note_num = random.randint(1, 12)
    mode_num = random.randint(1, 10)
    
    # Affichage stylé
    st.success(f"**Note :** {notes[note_num]}")
    st.success(f"**Mode :** {modes[mode_num]}")
    st.markdown(f"### 🎵 Tu joues dans : **{notes[note_num]} {modes[mode_num]}**")
    
    # Sauvegarde dans l'historique
    if "history" not in st.session_state:
        st.session_state.history = []
    
    st.session_state.history.append(f"{notes[note_num]} {modes[mode_num]}")
    
    # On garde seulement les 10 derniers tirages
    if len(st.session_state.history) > 10:
        st.session_state.history.pop(0)

# ================== HISTORIQUE ==================
st.markdown("---")
st.subheader("📜 Historique des derniers tirages")

if "history" in st.session_state and st.session_state.history:
    for i, tirage in enumerate(reversed(st.session_state.history)):
        st.markdown(f"**{len(st.session_state.history)-i}.** {tirage}")
else:
    st.info("Aucun tirage pour le moment… Appuie sur le gros bouton !")

# Bouton pour effacer l'historique
if st.button("🗑️ Effacer l’historique"):
    st.session_state.history = []
    st.rerun()

# ================== INFOS & PARTAGE ==================
st.markdown("---")
st.caption("Made with ❤️ pour les musiciens • Version web Streamlit")
st.caption("Tu peux partager ce lien à tes amis une fois déployé !")
