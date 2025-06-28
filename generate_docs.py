from app import app
import handlers.handle_chunk_video  # Импорт подписчиков - регистрация каналов

if __name__ == "__main__":
    from faststream.asyncapi.generate import generate
    print(generate(app))
