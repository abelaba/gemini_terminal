#!/bin/zsh

if [ -z "$1" ]; then
  echo "Usage: $0 <text>"
  echo ""
  exit 1
fi

if [ "$1" == "--file" ]; then
  if [ -z "$2" ]; then
    echo "Usage: $0 --file <filename>"
    echo ""
    exit 1
  fi

  file="$2"

  if [ ! -f "$file" ]; then
    echo "File not found: $file"
    exit 1
  fi

  text=$(cat "$file")
else
  text="$*"
fi

echo "$text"

python3 ./gemini.py "$text"
