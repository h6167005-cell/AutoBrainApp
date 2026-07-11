#!/bin/bash
echo "========================================="
echo " 🧠 AUTO BRAIN - ARTIFACT RETRIEVAL LOOP"
echo "========================================="

# Ensure we are in the right directory
cd ~/AutoBrainApp || { echo "❌ Error: AutoBrainApp folder not found!"; exit 1; }

echo "📡 Scanning GitHub for active cloud builds..."

# Fetch the ID of the most recent GitHub Action run
RUN_ID=$(gh run list --limit 1 --json databaseId --jq '.[0].databaseId')

if [ -z "$RUN_ID" ]; then
    echo "❌ No active builds found on GitHub."
    exit 1
fi

echo "⏳ Hooked into Cloud Build ID: $RUN_ID"
echo "Watching compiler matrix. Auto Brain will wait patiently..."

# This command pauses the script and watches the cloud server until it finishes
gh run watch $RUN_ID

echo "-----------------------------------------"
echo "📥 Build complete! Pulling APK payload to local storage..."

# Create a folder for the final app and download it
mkdir -p ~/AutoBrainApp/APK_Output
gh run download $RUN_ID --name Android-APK --dir ~/AutoBrainApp/APK_Output

echo "========================================="
echo "✅ RETRIEVAL SUCCESSFUL"
echo "Your new app is waiting in: ~/AutoBrainApp/APK_Output/"
echo "========================================="
