import asyncio


async def handler(reader, writer):
    meta = await reader.readline()
    writer.write()
    await writer.drain()
    writer.close()


async def main():
    server = await asyncio.start_server(handler, host='0.0.0.0', port=8000)
    await server.serve_forever()
