from config import setup_logging
import logging
import asyncio
from rabbit.broker import broker
from handlers import handle_chunk_video # import handler to register echanges and queues
from handlers import handle_publish_video # import handler to register echanges and queues

async def main():
    setup_logging()
    logger = logging.getLogger("example_app")
    logger.info("Starting service")

    await broker.start()

    logger.info("Successfully started")

    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, asyncio.CancelledError):
        logger.info("Service stopped...")
    finally:
        await broker.stop()
        logger.info("Broker stopper")

if __name__ == "__main__":
    asyncio.run(main())
