import json
import toml
import os

# Ask for the raw Firebase JSON
raw_input = input("Paste your full Firebase service account JSON here:\n\n")

try:
    firebase_data = json.loads(raw_input)

    # Escape newlines in private_key
    firebase_data["private_key"] = firebase_data["private_key"].replace("\n", "\\n")

    # Wrap in [firebase] block
    firebase_toml = {"firebase": firebase_data}

    # Load or create secrets.toml
    secrets_file = ".streamlit/secrets.toml"
    os.makedirs(".streamlit", exist_ok=True)

    if os.path.exists(secrets_file):
        with open(secrets_file, "r") as f:
            existing = toml.load(f)
    else:
        existing = {}

    # Merge and overwrite firebase section
    existing["firebase"] = firebase_data

    # Write updated secrets.toml
    with open(secrets_file, "w") as f:
        toml.dump(existing, f)

    print("\n✅ Successfully wrote Firebase config to .streamlit/secrets.toml")

except Exception as e:
    print(f"\n❌ Failed to process Firebase JSON: {e}")