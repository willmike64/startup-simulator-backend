#!/bin/bash

BASE_PORT=8501
MAX_ATTEMPTS=20
ATTEMPT=0

echo "🧠 Smart Streamlit Launcher v76.4"
echo "🔍 Scanning ports from $BASE_PORT to $((BASE_PORT + MAX_ATTEMPTS - 1))"
echo "🧼 Killing any zombie Streamlit servers..."

for (( p=BASE_PORT; p<BASE_PORT+MAX_ATTEMPTS; p++ )); do
  PID=$(lsof -ti tcp:$p)
  if [ ! -z "$PID" ]; then
    echo "⚠️ Killing PID $PID on port $p"
    kill -9 $PID 2>/dev/null
  fi
done

echo "✅ Cleanup complete."

while [ $ATTEMPT -lt $MAX_ATTEMPTS ]; do
  PORT=$((BASE_PORT + ATTEMPT))
  if ! lsof -i :$PORT >/dev/null 2>&1; then
    echo "🚀 Launching on port $PORT..."
    streamlit run streamlit_creator_dashboard.py --server.port $PORT --server.headless true
    exit 0
  fi
  ATTEMPT=$((ATTEMPT + 1))
done

echo "❌ All ports $BASE_PORT to $((BASE_PORT + MAX_ATTEMPTS - 1)) are in use."
exit 1