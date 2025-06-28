from models.chunk_video_mobels import ChunkVideoRequest, ChunkVideoResponse

async def process_chunk_video(data: ChunkVideoRequest) -> ChunkVideoResponse:
    processed = {"request_id": data.request_id, "status": "processed"}
    return processed
