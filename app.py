from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/puzzle/<date>')
def get_puzzle(date):
    """Fetch puzzle from NYT API and return only the shuffled words"""
    try:
        # Validate date format
        datetime.strptime(date, '%Y-%m-%d')
        
        # Fetch from NYT API
        url = f'https://www.nytimes.com/svc/connections/v2/{date}.json'
        response = requests.get(url)
        
        if response.status_code != 200:
            return jsonify({'error': f'Puzzle not found for date {date}'}), 404
        
        data = response.json()
        
        if data.get('status') == 'OK' and data.get('categories'):
            # Extract words without revealing categories
            words = []
            for category in data['categories']:
                for card in category['cards']:
                    words.append(card['content'])
            
            # Shuffle to avoid spoilers
            random.shuffle(words)
            
            return jsonify({
                'success': True,
                'date': date,
                'words': words,
                'puzzle_id': data.get('id'),
                'editor': data.get('editor')
            })
        else:
            return jsonify({'error': 'Invalid puzzle data'}), 400
            
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400
    except requests.RequestException as e:
        return jsonify({'error': f'Failed to fetch puzzle: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

def main():
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()