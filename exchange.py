from faststream.rabbit import RabbitExchange, ExchangeType
from config import config  # импорт твоего конфига

service_exchange = RabbitExchange(
    name=config["service_name"],  
    type=ExchangeType.TOPIC
)
