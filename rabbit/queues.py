from faststream.rabbit import RabbitQueue

chuck_video_api_name = "chunk_video"

chuck_video_request_queue = RabbitQueue(
    f"{chuck_video_api_name}_request_queue", 
    routing_key=f"{chuck_video_api_name}.request.*"
)
chuck_video_response_queue = RabbitQueue(
    f"{chuck_video_api_name}_response_queue", 
    routing_key=f"{chuck_video_api_name}.response.*"
)


publish_video_api_name = "publish_video"

publish_video_request_queue = RabbitQueue(
    f"{publish_video_api_name}_request_queue", 
    routing_key=f"{publish_video_api_name}.request.*"
)
publish_video_response_queue = RabbitQueue(
    f"{publish_video_api_name}_response_queue",
    routing_key=f"{publish_video_api_name}.response.*"
)