import logging.config

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
        "myapp": {
            "handlers": ["console"],
            "level": "DEBUG",
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
