from app.main import app as app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=False)