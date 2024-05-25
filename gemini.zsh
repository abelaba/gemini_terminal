#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <text>"
  echo ""
  exit 1
fi

text="$*"

python3 ./gemini.py "$text"
