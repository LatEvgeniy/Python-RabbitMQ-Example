from config import setup_logging
import logging
import asyncio
from rabbit.broker import broker, wait_for_broker_connection
from handlers import handle_chunk_video # import handler to register exchanges and queues
from handlers import handle_publish_video # import handler to register exchanges and queues

async def main():
    setup_logging()
    logger = logging.getLogger("example_app")
    logger.info("Starting service")

    try:
        await wait_for_broker_connection()
    except TimeoutError:
        logger.error("Failed to connect to broker, exiting...")
        return
    
    await broker.start()

    logger.info("Successfully started")

    # kind of while True
    try: 
        await asyncio.Event().wait()
    except (KeyboardInterrupt, asyncio.CancelledError):
        logger.info("Service stopped...")
    finally:
        await broker.stop()
        logger.info("Broker stopper")

if __name__ == "__main__":
    asyncio.run(main())
