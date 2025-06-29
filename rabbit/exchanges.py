from faststream.rabbit import RabbitExchange, ExchangeType
from config import config

video_processor_service_exchange = RabbitExchange(
    name="video_processor_service",
    type=ExchangeType.TOPIC
)

video_publisher_service_exchange = RabbitExchange(
    name="video_publisher_service",
    type=ExchangeType.TOPIC
)