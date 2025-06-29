from faststream.rabbit import RabbitBroker
from config import config
import asyncio

broker = RabbitBroker(config["rabbitmq_url"])

async def wait_for_broker_connection(timeout: int = 60, interval: int = 5):
    start_time = asyncio.get_event_loop().time()
    while True:
        try:
            await broker.connect()
            return
        except Exception as e:
            if (asyncio.get_event_loop().time() - start_time) >= timeout:
                raise TimeoutError("Could not connect to broker within timeout") from e
            await asyncio.sleep(interval)