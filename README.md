# 🐇 Python RabbitMQ Example

## 🗂 Структура папок

```
python-rabbitmq-example/
├── **handlers/**              # Обработчики сообщений (подписчики + издатели)
│   ├── `handle_{api_name}.py`
├── **processors/**            # Бизнес-логика
│   └── `process_{api_name}.py`
├── **models/**                # Pydantic модели для валидации запросов/ответов
│   └── `{api_name}_models.py`
├── **rabbit/**                # Конфигурация RabbitMQ (очереди, обмены, брокер)
│   ├── `broker.py`
│   ├── `exchanges.py`
│   └── `queues.py`
├── **tests/**                 # Юнит-тесты
│   ├── `handle_{api_name}_test.py`
│   └── `process_{api_name}_test.py`
└── `main.py`                  # Точка входа приложения
```

---

## 🔁 Как это работает

Пример взаимодействия двух микросервисов:

1. **video_publisher_service**

- `handle_publish_video.py` получает сообщение через `publish_video_request_queue`
- Обрабатывает его через `process_publish_video()`
- Публикует ответ в свою очередь ответов `publish_video_response_queue`

2. **video_processor_service**

- `handle_chunk_video.py` слушает ивенты от publish_video в его очереди ответов`publish_video_response_queue`
- Обрабатывает ивент через `process_chunk_video()`
- Отправляет ответ уже в свою очередь `chunk_video_response_queue`

**Пайплайн:**

```
video_publisher_service.publish_video_request_queue -> 
video_publisher_service.publish_video_response_queue -> 
video_processor_service.chunk_video_response_queue
```

---

## 💡 Особенности дизайна

- **Handlers** - конструкторы из queue и exchange и валидаторы запросов.
- Все настройки RabbitMQ в папке **rabbit/**.
- Бизнес-логика отделена в **processors/**.
- Для каждого handler и processor есть собственные тесты.

---

## ▶️ Запуск сервиса

Убедитесь, что RabbitMQ запущен:

```bash
docker-compose up
# или (для версии 2)
docker compose up
```

Просмотр логов приложения:

```bash
docker-compose logs -f example-app
# или (для версии 2)
docker compose logs -f example-app
```

Публикация сообщений через UI RabbitMQ:

- Откройте: `http://localhost:15672/#/queues/%2F/publish_video_request_queue`
- Используйте раздел "Publish message"
- Пример полезной нагрузки (payload):

```json
{}
```

или

```json
{"request_id": "123-321"}
```

---

## ✅ Запуск тестов

```bash
pytest
# или (если запускаете из корня проекта)
PYTHONPATH=. pytest
```
