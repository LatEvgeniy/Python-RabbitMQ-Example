from faststream.rabbit import RabbitBroker

class App:
    title = "My FastStream RabbitMQ Service"
    version = "1.0.0"
    description = "Описание моего сервиса на FastStream и RabbitMQ"
    terms_of_service = None
    contact = None
    license = None
    identifier = "amqp://guest:guest@localhost:5672/myservice"
    asyncapi_tags = []
    external_docs = None


    def __init__(self):
        self.broker = RabbitBroker()

app = App()
