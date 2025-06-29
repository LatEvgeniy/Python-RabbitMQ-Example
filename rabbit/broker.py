from faststream.rabbit import RabbitBroker
from config import config

broker = RabbitBroker(config["rabbitmq_url"])

