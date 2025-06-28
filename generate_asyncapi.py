import asyncio
from main import broker

async def save_asyncapi():
    spec = await broker.asyncapi()
    with open("asyncapi.yaml", "w") as f:
        f.write(spec)
    print("AsyncAPI спецификация сохранена в asyncapi.yaml")

if __name__ == "__main__":
    asyncio.run(save_asyncapi())
