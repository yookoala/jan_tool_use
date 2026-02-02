import asyncio
import logging
from datetime import datetime
import json
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import dotenv
from mcp.server.fastmcp import Context, FastMCP
import uvicorn

from lib.tts import text_to_speech
from utils import get_logger, get_uvicorn_log_config, SuppressCancelledErrorFilter

# Create a named MCP server
mcp = FastMCP("Dummy MCP Server")

@mcp.tool()
async def where_am_i(ctx: Context) -> str:
    """Get the user's current location

    This function do not need any input. It will resolve the user's location
    and reply the city name or location name.

    Example output:
    - "Hong Kong"
    - "Tokyo"
    """
    logger.info("where_am_i()")
    return "Tokyo"

@mcp.tool()
async def what_is_the_timezone(ctx: Context, location: str) -> str:
    """Get the user's timezone in ISO8601 format

    Example use:
    - what_is_the_timezone("Hong Kong")
    """
    logger.info(f"what_is_the_timezone({location})" )

    # This works for our purpose. In real world, you may want to use a more
    # comprehensive location to timezone resolver.
    timezones = {
        "Hong Kong": "Asia/Hong_Kong",
        "Tokyo": "Asia/Tokyo",
        "New York": "America/New_York",
        "London": "Europe/London",
        "UTC": "UTC",
    }
    result = timezones.get(location, "UTC")
    logger.debug(f"what_is_the_timezone: result={result}")
    return result

@mcp.tool()
async def now(ctx: Context, timezone: str = "UTC") -> str:
    """Get the current date, time of a given tz database timezone name, in ISO8601 format

    For example:
    - what_is_the_timezone("Asia/Tokyo")
    - what_is_the_timezone("UTC")
    """
    logger.info(f"now({json.dumps(timezone)})")
    if timezone == "":
        timezone = "UTC"
    try:
        tz = ZoneInfo(timezone)
    except ZoneInfoNotFoundError:
        return "Invalid timezone"
    result = datetime.now(tz).isoformat()
    logger.debug(f"now: result={result}")
    return result

@mcp.tool()
async def speak(ctx: Context, message: str, model: int) -> str:
    """Ouput the message text as speech audio
    to user via Deepgram TTS API.

    User can choose the voice: 1 for female, 2 for male

    Example use:
    - speak("Hello, world!", 1)
    """
    logger.info(f"speak({json.dumps(message)},{model})")
    api_key = dotenv.get_key(".env", "DEEPGRAM_API_KEY")
    text_to_speech(message, api_key, model)
    return message


async def main():
    config = uvicorn.Config(
        app=mcp.sse_app(),
        host='0.0.0.0',
        port=8080,
        log_level='info',
        log_config=get_uvicorn_log_config(),
        timeout_graceful_shutdown=10,
    )
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    dotenv.load_dotenv()
    log_level_str = dotenv.get_key(".env", "LOG_LEVEL") or "INFO"
    logger = get_logger("Dummy MCP Server", level=log_level_str)

    # Suppress CancelledError logs during graceful shutdown
    cancel_filter = SuppressCancelledErrorFilter()
    logging.getLogger("uvicorn.error").addFilter(cancel_filter)
    logging.getLogger("uvicorn").addFilter(cancel_filter)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass  # Graceful shutdown, suppress traceback
    except asyncio.exceptions.CancelledError:
        pass  # Graceful shutdown, suppress traceback
