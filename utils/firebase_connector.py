import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st

# Initialize Firebase only once
if "firebase_initialized" not in st.session_state:
    firebase_config = st.secrets["firebase"]
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)
    st.session_state["firebase_initialized"] = True

# Connect to Firestore
db = firestore.client()

def save_user_game():
    """Save minimal game state to Firebase (example stub)"""
    doc_ref = db.collection("games").document(ss("company_id", "test"))
    doc_ref.set({
        "company_id": ss("company_id", "unknown"),
        "role": ss("role", "unknown"),
        "mode": ss("mode", "single"),
        "funding_complete": ss("funding_complete", False),
        "page": ss("page", "intro")
    })

def log_session_data(data):
    """Log full session snapshot including results_df"""
    log_ref = db.collection("logs").document()
    log_ref.set(data)

# Safe getter helper for reuse
def ss(key, default=None):
    return st.session_state[key] if key in st.session_state else default
