from logging_config import setup_logging
import logging
import asyncio
from rabbit import broker
from handlers import handle_chunk_video # import handler to register echanges nad queues

async def main():
    setup_logging()
    logger = logging.getLogger("myapp")
    logger.info("Запуск сервиса")

    await broker.start()

    logger.info("Запуск успешен")

    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, asyncio.CancelledError):
        logger.info("Остановка сервиса...")
    finally:
        await broker.stop()
        logger.info("Сервис остановлен")

if __name__ == "__main__":
    asyncio.run(main())
