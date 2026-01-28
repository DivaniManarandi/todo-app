from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Store todos with unique IDs
todos = []
next_id = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    global next_id
    data = request.get_json()
    
    todo = {
        'id': next_id,
        'task': data.get('task', ''),
        'status': data.get('status', 'total')  # total, active, or completed
    }
    
    todos.append(todo)
    next_id += 1
    
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>/status', methods=['PUT'])
def change_status(todo_id):
    data = request.get_json()
    new_status = data.get('status')
    
    if new_status not in ['total', 'active', 'completed']:
        return jsonify({'error': 'Invalid status'}), 400
    
    for todo in todos:
        if todo['id'] == todo_id:
            todo['status'] = new_status
            return jsonify(todo)
    
    return jsonify({'error': 'Todo not found'}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            deleted = todos.pop(i)
            return jsonify(deleted)
    
    return jsonify({'error': 'Todo not found'}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)