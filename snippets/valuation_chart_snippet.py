import pandas as pd
from utils.results import load_valuation_history

company_id = st.session_state.get("company_id", "neuronest")
history = load_valuation_history(company_id)

if history:
    df = pd.DataFrame([{
        "timestamp": h["timestamp"],
        "valuation": h["impact"]["valuation"]
    } for h in history])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    st.line_chart(df.set_index("timestamp")["valuation"])
else:
    st.info("No valuation history yet.")