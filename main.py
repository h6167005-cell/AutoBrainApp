cat << 'EOF' > ~/AutoBrainApp/injector.sh
#!/bin/bash
echo "========================================="
echo " 🧠 AUTO BRAIN - DIRECT INJECTION ACTIVE"
echo "========================================="
cd ~/AutoBrainApp || exit

echo "📋 PASTE your Gemini Python code below."
echo "🟢 When finished, press CTRL + D to auto-save and launch!"
echo "-----------------------------------------"

# This reads your paste directly into the file without opening an editor
cat > main.py

echo ""
echo "-----------------------------------------"
echo "✅ Code locked in! Packaging for the cloud..."
git add main.py buildozer.spec
git commit -m "Auto Brain: Direct Blueprint Update" || echo "No changes."

echo "🚀 Pushing to GitHub Matrix..."
git push

echo "-----------------------------------------"
echo "👁️ Waking up the Observer..."
bash autobrain_fetch.sh
EOF

chmod +x ~/AutoBrainApp/injector.sh
