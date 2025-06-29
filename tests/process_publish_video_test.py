import pytest
from models.publish_video_models import PublishVideoRequest, PublishVideoResponse
from processors.process_publish_video import process_publish_video

@pytest.mark.asyncio
async def test_process_publish_video():
    request = PublishVideoRequest(request_id="test_id")
    
    response = await process_publish_video(request)
    
    assert isinstance(response, PublishVideoResponse)
    
    assert response.request_id == "test_id"
    assert response.video_url == "some_url"
