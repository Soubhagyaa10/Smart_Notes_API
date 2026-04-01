notes = []

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "API is working"

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "Please provide title and content"}), 400

    title = data['title']
    content = data['content']

    words = content.split()

    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "word_count": len(words),
        "created_at": created_at
    }
   
    notes.append(note)

    return jsonify({
        "message": "Note added",
        "note": note
})

@app.route('/notes', methods=['GET'])
def get_notes():
    if len(notes) == 0:
        return jsonify({
            "message": "No notes found",
            "notes": []
})
    else:
        return jsonify({
    "notes": notes
})

@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            return jsonify({"message": "Note deleted"})

    return jsonify({"error": "Note not found"}), 404

@app.route('/notes/stats', methods=['GET'])
def get_stats():
    total_notes = len(notes)
    total_words = sum(note['word_count'] for note in notes)
    average_words = total_words / total_notes if total_notes > 0 else 0

    return jsonify({
        "total_notes": total_notes,
        "total_words": total_words,
        "average_words": average_words
    })

if __name__ == '__main__':
    app.run(debug=True)
