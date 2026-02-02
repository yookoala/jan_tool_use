import logging

class SuppressCancelledErrorFilter(logging.Filter):
    """Filter to suppress CancelledError logs during graceful shutdown"""
    def filter(self, record):
        # Suppress logs containing CancelledError
        if record.exc_info:
            exc_type = record.exc_info[0]
            if exc_type and 'CancelledError' in exc_type.__name__:
                return False
        # Also check the message itself
        if 'CancelledError' in str(record.getMessage()):
            return False
        return True

