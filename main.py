import logging
from os import supports_dir_fd
from pyrogram import idle
from . import app

async def main():
    await app.start()
    await idle()
    await app.stop()

app.loop.run_until_complete(main())
