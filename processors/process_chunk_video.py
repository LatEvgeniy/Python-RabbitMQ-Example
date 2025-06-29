from models.chunk_video_models import ChunkVideoRequest, ChunkVideoResponse

async def process_chunk_video(request: ChunkVideoRequest) -> ChunkVideoResponse:
    response = ChunkVideoResponse(request_id=request.request_id, status="processed")

    return response
