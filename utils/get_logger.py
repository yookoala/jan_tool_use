import logging

def get_logger(name: str, level: str = "INFO") -> logging.Logger:
    log_level = getattr(logging, level.upper(), logging.INFO)
    ansi_blue = "\x1b[0;34m"
    ansi_cyan = "\x1b[0;36m"
    ansi_reset = "\x1b[0m"
    log_handler = logging.StreamHandler()
    log_handler.formatter = logging.Formatter(
        f"{ansi_cyan}[%(asctime)s]{ansi_reset} {ansi_blue}%(levelname)s{ansi_reset}\t%(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S',
    )

    # Check if the logger already exists
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    if not logger.hasHandlers():
        logger.addHandler(log_handler)
    return logger
