from models.publish_video_models import PublishVideoRequest, PublishVideoResponse

async def process_publish_video(request: PublishVideoRequest) -> PublishVideoResponse:
    response = PublishVideoResponse(request_id=request.request_id, video_url="some_url")
    
    return response
