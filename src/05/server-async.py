import asyncio
import time

async def tidur(n):
    time.sleep(5)

async def handle_echo(reader, writer):
    print(f"serving {writer.get_extra_info('peername')}")
    await tidur(5)
    writer.write(b'Hello')
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8080)

    async with server:
        await server.serve_forever()

asyncio.run(main())
