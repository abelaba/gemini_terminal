#!/bin/zsh

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <text> [-c | -context]"
  echo ""
  return 1
fi

# Get the text argument
text="$*"

python3 ./gemini.py $text
