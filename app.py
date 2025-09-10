from flask import Flask, request, jsonify, render_template
import ast
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_syntax', methods=['POST'])
def check_syntax():
    code = request.form.get('code', '')
    try:
        ast.parse(code)
        return jsonify({'status': 'success', 'message': 'No syntax errors found.'})
    except SyntaxError as e:
        return jsonify({
            'status': 'error',
            'message': f"{e.msg} (Line {e.lineno}, Column {e.offset})",
            'details': {
                'lineno': e.lineno,
                'offset': e.offset,
                'text': e.text
            }
        })

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file and file.filename.endswith('.py'):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        try:
            ast.parse(code)
            return jsonify({'status': 'success', 'message': 'No syntax errors found.'})
        except SyntaxError as e:
            return jsonify({
                'status': 'error',
                'message': f"{e.msg} (Line {e.lineno}, Column {e.offset})",
                'details': {
                    'lineno': e.lineno,
                    'offset': e.offset,
                    'text': e.text
                }
            })
    else:
        return jsonify({'status': 'error', 'message': 'Only .py files are allowed'})

if __name__ == '__main__':
    app.run(debug=True)
