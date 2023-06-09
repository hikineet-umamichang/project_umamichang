from app import create_app
import dotenv


dotenv.load_dotenv(".env", override=True)

app = create_app()

if __name__ == "__main__":
    app.run()
