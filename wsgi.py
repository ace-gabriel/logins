from application.main import app
import os

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(port=5400, debug=True)
