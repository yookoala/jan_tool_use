import asyncio
import signal
from datetime import datetime
import json
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import dotenv
from mcp.server.fastmcp import Context, FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount, Host
import uvicorn

from lib.tts import text_to_speech
from utils import get_logger, get_uvicorn_log_config

# Create a named server
logger = get_logger("Dummy MCP Server")
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
    return "Asia/Tokyo"

@mcp.tool()
async def now(ctx: Context, timezone: str = "UTC") -> str:
    """Get the current date, time of a given tz database timezone name, in ISO8601 formati

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
    return datetime.now(tz).isoformat()

@mcp.tool()
async def speak(ctx: Context, message: str) -> str:
    """Ouput the message text as speech audio
    to user via Deepgram TTS API.

    Example use:
    - speak("Hello, world!")
    """
    logger.info(f"speak({json.dumps(message)})")
    api_key = dotenv.get_key(".env", "DEEPGRAM_API_KEY")
    text_to_speech(message, api_key)
    return message


async def main():
    dotenv.load_dotenv()
    config = uvicorn.Config(
        app=mcp.sse_app(),
        host='0.0.0.0',
        port=8080,
        log_level='info',
        log_config=get_uvicorn_log_config(),
        timeout_graceful_shutdown=10,
    )
    server = uvicorn.Server(config)

    def handle_exit(*args):
        logger.info("Received shutdown signal. Shutting down gracefully...")
        # Triggering shutdown on the server instance
        asyncio.create_task(server.shutdown())

    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    try:
        await server.serve()
    except Exception as e:
        logger.error(f"Server exception: {e}")

if __name__ == "__main__":
    asyncio.run(main())
