# logging_config.py
import logging
import logging.config

def setup_logging():
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'mode': 'w',
                'formatter': 'standard',
            },
        },
        'loggers': {
            'kilosort': {  # module-level logger
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    }
    logging.config.dictConfig(logging_config)
