import streamlit as st

def render_lobby(navigate):
    st.title("🏢 Lobby")

    if not st.session_state.get("is_logged_in"):
        st.header("🔐 Login")
        username = st.text_input("Enter your username")
        if st.button("Login"):
            if username:
                st.session_state.username = username
                st.session_state.user_id = username.lower().replace(" ", "_")
                st.session_state.is_logged_in = True
                st.session_state.page = "role_picker"
                st.rerun()
            else:
                st.warning("Please enter a username to log in.")
        return

    st.success(f"✅ Logged in as: {st.session_state.username}")

    if st.session_state.page == "role_picker":
        render_role_picker(navigate)
    else:
        st.write("🔁 Redirecting...")
        navigate("intro")

def render_role_picker(navigate):
    st.header("🎭 Choose Your Role")
    role = st.radio("Who are you today?", ["CEO", "Founder", "Investor"], key="role_choice")
    if st.button("Continue with Role"):
        st.session_state.role = role
        st.session_state.page = "onboarding"
        navigate("onboarding")