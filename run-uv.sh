#!/bin/bash
# Simple script to run the Connections solver with uv

echo "🧩 Starting Connections Puzzle Solver with UV..."
uv run python app.py

# For Windows, create run-uv.bat:
# @echo off
# echo Starting Connections Puzzle Solver with UV...
# uv run python app.py
# pause