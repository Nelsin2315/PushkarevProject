import os

from flask import Flask

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    path_file = os.path.join(BASE_DIR, relative_path)
    with open(path_file, 'r', encoding='utf8') as file:
        read_size = file.read(size)
    return f'<b>{path_file}</b> {len(read_size)}<br>{read_size}'


if __name__ == "__main__":
    app.run(debug=True)