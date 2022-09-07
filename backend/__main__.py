from backend import create_app

app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1")
    # For accept anywhere requests use: "0.0.0.0"
