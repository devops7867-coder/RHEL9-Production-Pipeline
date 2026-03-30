#!/bin/bash
echo "🔍 Checking VM1 (Jenkins) status..."
curl -Is http://192.168.56.105:8080 | head -n 1

echo "🔍 Checking VM2 (App Server) status..."
curl -Is http://192.168.56.106 | head -n 1
