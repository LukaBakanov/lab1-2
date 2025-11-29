firstwebpage Django проект

Last Updated: 2025-11-30

- [CANONICAL] Среда выполнения: Python 3.12 (установлен через winget), Django 4.2.16.
- Основные команды:
  - `py -3.12 -m django --version` — проверить доступность Django для Python 3.12.
  - `py -3.12 manage.py migrate` — применить миграции (уже выполнялось один раз).
  - `py -3.12 manage.py runserver` — запустить dev-сервер.
- Маршруты dev-страницы: `/` рендерит `flatpages/templates/static_handler.html`; `/hello/` отдаёт текст «Привет, Мир!».
- Настройки шаблонов и статики:
  - `TEMPLATES.DIRS = [BASE_DIR / 'flatpages']`, подключён `django.template.context_processors.static`.
  - `STATIC_URL = '/static/'`, `STATICFILES_DIRS = [BASE_DIR / 'flatpages' / 'static']`.
  - В `firstwebpage/urls.py` при `DEBUG` добавлены `staticfiles_urlpatterns()` для отдачи статики.
- Скрипты: находятся в `C:\Users\lukab\AppData\Local\Programs\Python\Python312\Scripts`; добавьте путь в PATH, если хотите вызывать `django-admin`/`pip` без `py -3.12 -m`.
- MEMORY BANK: [REF: flatpages/README.md#главная-страница] для деталей о представлениях, шаблонах и статике.
