from main import broker
from config import config
from processors.process_chunk_video import process_chuck_video

exchange = config["service_name"]
queue_cfg = next(q for q in config["queues"] if q["name"] == "delete_video")

@broker.subscriber(
    exchange=exchange,
    queue=queue_cfg["name"],
    routing_key=queue_cfg["routing_key"]
)
async def handler_queue2(data: dict):
    await process_chuck_video(data)
