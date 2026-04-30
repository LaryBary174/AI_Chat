# Чат с ИИ
Приложение с подключенным ИИ от гигачат,поддержка WebSocket, ответы в реальном времени.

## Установка
Используется менеджер пакетов uv, проверьте, что он установлен
1. Клонируйте репозиторий
2. Установите зависимости:
   ```bash
   uv sync
   ```

3. В корне проекта создайте файл .env
   ```ini
   AI_API_KEY=your_api_key_here
   ```
   Получить API ключ можно по [инструкции](https://developers.sber.ru/docs/ru/gigachat/quickstart/ind-create-project)

4. Запустите приложение:
   ```bash
   uv run uvicorn app:app --reload
   ```
   