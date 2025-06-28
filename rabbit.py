from faststream.rabbit import RabbitExchange, ExchangeType, RabbitBroker
from config import config

service_exchange = RabbitExchange(
    name=config["service_name"],
    type=ExchangeType.TOPIC
)

broker = RabbitBroker(config["rabbitmq_url"])
