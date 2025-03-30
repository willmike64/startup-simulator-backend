import streamlit as st

def app():

    import streamlit as st
    import random

    MAX_NEGOTIATION_ROUNDS = 10

    # -----------------------------
    # State Initialization
    # -----------------------------
    if "negotiation_round" not in st.session_state:
        st.session_state.negotiation_round = 1
    if "ai_offer" not in st.session_state:
        st.session_state.ai_offer = {"valuation": 4000000, "equity": 25}
    if "user_offer" not in st.session_state:
        st.session_state.user_offer = {"valuation": 5000000, "equity": 20}
    if "deal_agreed" not in st.session_state:
        st.session_state.deal_agreed = False

    def render_funding_ui(navigate):
        st.header("💸 AI Investor Negotiation")
    
        st.subheader(f"🔁 Round {st.session_state.negotiation_round} of {MAX_NEGOTIATION_ROUNDS}")
    
        st.write("🤖 **AI Investor's Offer:**")
        st.write(f"- Valuation: ${st.session_state.ai_offer['valuation']:,}")
        st.write(f"- Equity: {st.session_state.ai_offer['equity']}%")

        st.write("---")
        st.subheader("🧑 Your Counter Offer")

        user_val = st.number_input("Your Valuation ($)", min_value=1000000, step=100000, value=st.session_state.user_offer["valuation"])
        user_eq = st.slider("Equity You're Willing to Give (%)", min_value=1, max_value=100, value=st.session_state.user_offer["equity"])

        if st.button("💬 Counter Offer"):
            st.session_state.user_offer = {"valuation": user_val, "equity": user_eq}
            st.session_state.negotiation_round += 1

            # Basic AI negotiation logic
            ai_val = int((st.session_state.ai_offer["valuation"] + user_val) / 2)
            ai_eq = round((st.session_state.ai_offer["equity"] + user_eq) / 2)

            st.session_state.ai_offer = {
                "valuation": ai_val,
                "equity": ai_eq
            }

            if st.session_state.negotiation_round > MAX_NEGOTIATION_ROUNDS:
                st.warning("❌ Negotiation failed — you ran out of rounds.")
                st.session_state.page = "lobby"
                st.rerun()

        if st.button("✅ Accept Deal"):
            st.success("🎉 Deal Agreed!")
            st.session_state.funding_complete = True
            st.session_state.page = "single_player"
            st.session_state.negotiation_round = 1
            st.rerun()
if st.checkbox("Show Debug Info"):
        st.json(st.session_state)