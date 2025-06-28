import os

config = {
    "rabbitmq_url": os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/"),
    "service_name": "video_processor", 
}
