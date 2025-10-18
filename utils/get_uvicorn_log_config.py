def get_uvicorn_log_config():
    ansi_blue = "\x1b[0;34m"
    ansi_cyan = "\x1b[0;36m"
    ansi_reset = "\x1b[0m"
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': f"{ansi_cyan}[%(asctime)s]{ansi_reset} {ansi_blue}%(levelname)s{ansi_reset}\t%(message)s",
            },
        },
    } 