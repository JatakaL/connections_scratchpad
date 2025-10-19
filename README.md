# Connections Puzzle Solver

A local Flask app that lets you solve NYT Connections puzzles with a drag-and-drop interface, without spoilers!

## Features
- ✅ Fetches puzzles directly from NYT API (no CORS issues)
- ✅ Hides categories to avoid spoilers
- ✅ Drag-and-drop word cards between groups
- ✅ Lock groups when you're confident
- ✅ Assign colors to groups as you solve
- ✅ Extra sorting areas for organizing

## Setup Instructions

### Using UV (Recommended)

1. **Install UV** (if you haven't already):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Or on macOS:
```bash
brew install uv
```

2. **Clone/Create Project Structure**:
```
connections-solver/
├── app.py
├── pyproject.toml
├── .python-version
├── .gitignore
├── templates/
│   └── index.html
```

3. **Run with UV**:
```bash
# UV will automatically create a virtual environment and install dependencies
uv run python app.py
```

That's it! Navigate to `http://localhost:5000`

### Alternative: Using pip

If you prefer pip:
```bash
pip install flask flask-cors requests
python app.py
```

## How to Use

1. **Select a date** and click "Fetch Puzzle" to load that day's puzzle
2. **Click "Start Puzzle"** to begin
3. **Drag words** from the pool into groups
4. **Assign colors** to groups as you figure out difficulty levels:
   - 🟡 Yellow = Easiest
   - 🟢 Green = Medium
   - 🔵 Blue = Hard  
   - 🟣 Purple = Trickiest
5. **Lock groups** when you're confident they're correct
6. Use the **extra groups** as temporary sorting areas

## Troubleshooting

- **UV not found?** Make sure UV is installed and in your PATH
- **Can't fetch puzzle?** Check if the date has a published puzzle (puzzles start from June 2023)
- **Port already in use?** Change the port in `app.py` from 5000 to another number

## Notes

- The app fetches puzzles directly from NYT's API
- Words are automatically shuffled to avoid spoilers
- Categories are hidden on the backend - you'll never see the answers accidentally
- All processing happens locally on your machine