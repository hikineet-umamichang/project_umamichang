from app import create_app
import dotenv


dotenv.load_dotenv(".env", override=True)

app = create_app()

if __name__ == "__main__":
    host = app.config["HOST"]
    port = app.config["PORT"]
    app.run(host=host, port=port)
