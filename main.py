from app import app
from logging_config import setup_logging
import logging
from app import app

def main():
    setup_logging()
    logger = logging.getLogger("myapp")
    logger.info("Запуск сервиса")

    # Импорт subscribers уже сделан в App.__init__, можно не повторять
    import handlers.handle_chunk_video
    app.broker.start()

if __name__ == "__main__":
    main()
