import asyncio
import time
from datetime import datetime

lock = asyncio.Lock()
clients = []

async def handle_echo(reader, writer):
    async with lock:
        clients.append(writer)
    addr = writer.get_extra_info('peername')
    while True:
        data = await reader.read(1024)
        if "quit" in data.decode():
            break
        # broadcast data ke seluruh writer yang connected
        async with lock:
            for w in clients:
                if w is not writer:
                    w.write(f"{datetime.now()} - {addr}: {data.decode()}".encode())
                    await w.drain()
    async with lock:
        clients.remove(writer)
    writer.close()
    print("client closed")

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8080)

    async with server:
        await server.serve_forever()

asyncio.run(main())
