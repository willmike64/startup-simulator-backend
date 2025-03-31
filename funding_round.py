from utils.session import init_session_state
init_session_state()

from utils.session import init_session_state
init_session_state()

import streamlit as st

if "negotiation_round" not in st.session_state:
    st.session_state.negotiation_round = 1
if "ai_offer" not in st.session_state:
    st.session_state.ai_offer = {"valuation": 1000000, "equity": 10}
if "user_offer" not in st.session_state:
    st.session_state.user_offer = {}
if "deal_agreed" not in st.session_state:
    st.session_state.deal_agreed = False

    MAX_NEGOTIATION_ROUNDS = 10

    # -----------------------------
    # State Initialization
    # -----------------------------
if "negotiation_round" not in st.session_state:
    st.session_state.negotiation_round = 1
if "ai_offer" not in st.session_state:
    st.session_state.ai_offer = {"valuation": 1000000, "equity": 10}
if "user_offer" not in st.session_state:
    st.session_state.user_offer = {}
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


if st.button("💬 Counter Offer"):
    pass
st.session_state.negotiation_round += 1

            # Basic AI negotiation logic
st.session_state.counter_offer = {
                "valuation": ai_val,
                "equity": ai_eq
            }

            if st.session_state.negotiation_round > MAX_NEGOTIATION_ROUNDS:
                st.warning("❌ Negotiation failed — you ran out of rounds.")
                st.rerun()
        if st.button("✅ Accept Deal"):
            st.success("🎉 Deal Agreed!")
            st.rerun()
with st.expander("🛠 Debug Session State 1", expanded=False):
    st.json(st.session_state)
        st.json(st.session_state)
