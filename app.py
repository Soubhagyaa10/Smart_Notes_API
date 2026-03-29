notes = []

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API is working"

@app.route('/notes', methods=['POST'])

def add_note():
    data = request.get_json()
    
    if not data or 'title' not in data or 'content' not in data:
        return {"error": "Please provide title and content"}, 400

    title = data['title']
    content = data['content']

    words = content.split()

    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "word_count": len(words)
    }
   
    notes.append(note)

    return jsonify({
    "message": "Note added",
    "note": note
})

if __name__ == '__main__':
    app.run(debug=True)
