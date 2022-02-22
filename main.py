from src.api_controller import is_palindromeambigram_v1, get_palindromeambigram_v1
from flask import Flask

app = Flask(__name__)

app.register_blueprint(is_palindromeambigram_v1, url_prefix='/api/v1')
app.register_blueprint(get_palindromeambigram_v1, url_prefix='/api/v1')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
