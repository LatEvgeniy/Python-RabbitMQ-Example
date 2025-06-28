async def process_chunk_video(data: dict):
    processed = {"result": data.get("value", 0) * 2}
    return processed
