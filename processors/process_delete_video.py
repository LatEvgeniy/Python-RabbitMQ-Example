async def process_delete_video(data: dict):
    processed = {"result": data.get("value", 0) * 2}
    return processed
