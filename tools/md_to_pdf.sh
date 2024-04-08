#!/bin/bash

filename="${1%.md}"

# Convert Markdown to PDF using Pandoc
echo pandoc "$1" -o "${filename}.pdf"
pandoc "$1" -o "${filename}.pdf"

echo $0
