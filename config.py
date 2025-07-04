import os

import logging.config

config = {
    "rabbitmq_url": os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/"),
}

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "example_app": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "faststream": {
        "handlers": ["console"],
        "level": "DEBUG",
        "propagate": False,
    },
    "aio_pika": {
        "handlers": ["console"],
        "level": "DEBUG",
        "propagate": False,
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
