import pytest
from unittest.mock import AsyncMock
from handlers.handle_publish_video import handle_publish_video
from models.publish_video_models import PublishVideoResponse

@pytest.mark.asyncio
async def test_handle_publish_video_success(mocker):
    logger = mocker.Mock()
    message_dict = {"request_id": "123"}

    mock_process = mocker.patch(
        'handlers.handle_publish_video.process_publish_video',
        new=AsyncMock(
            return_value=PublishVideoResponse(
                request_id=message_dict.get("request_id"), 
                video_url="some_url"
            )
        )
    )

    response = await handle_publish_video(message_dict, logger)

    mock_process.assert_awaited_once()
    assert response.request_id == message_dict.get("request_id")
    assert response.error_message is None

@pytest.mark.asyncio
async def test_handle_publish_video_negative(mocker):
    logger = mocker.Mock()
    empty_bytes = b""

    response = await handle_publish_video(empty_bytes, logger)

    assert response.request_id != None
    assert response.error_message != None
