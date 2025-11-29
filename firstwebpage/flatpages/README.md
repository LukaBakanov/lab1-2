flatpages приложение

Last Updated: 2025-11-30

## Главная страница
- [CANONICAL] Представление `home` в `flatpages/views.py` рендерит `/` через шаблон `templates/static_handler.html` и подключённую статику.
- [CANONICAL] Представление `hello` в `flatpages/views.py` отвечает за `/hello/` и возвращает текст `Привет, Мир!`.
- Проверка: `py -3.12 manage.py runserver` из корня проекта, затем открыть http://127.0.0.1:8000/ и http://127.0.0.1:8000/hello/ — главная страница с таблицей/списками и стилизацией, hello даёт чистый текст.

## Шаблоны и статика
- Шаблоны лежат в `flatpages/templates/` (`index.html` — эталон без стилей, `static_handler.html` — рабочий с подключением CSS).
- Статика в `flatpages/static/`: `index.css` (фон, границы таблицы, шрифты, 30px логотип) и `placeholder.svg`.
- Настройки поиска шаблонов/статики: см. [REF: ../README.md#настройки-шаблонов-и-статики].
