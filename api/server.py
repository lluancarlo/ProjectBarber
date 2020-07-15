import logging

from app import create_app

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app = create_app()

if __name__ == "__main__":
    app.run()