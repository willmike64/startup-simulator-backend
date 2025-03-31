# 🚀 Startup Simulation Alpha v1.4

This version includes:
- ✅ Full simulation game flow (Rounds 1–12+)
- ✅ Streamlit UI with onboarding, company selection, decisions
- ✅ AI consultants, morale tracking, supply chain logic
- ✅ Launch scripts and secrets configuration

## 🔧 Setup

```bash
python3 scripts/setup_env.py
./scripts/launch_sim.sh
```

## 🔐 Configure secrets

```bash
streamlit run secrets_setup.py
```

Add your OpenAI + Discord API keys to `.streamlit/secrets.toml`.