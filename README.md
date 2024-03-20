Команда для инициализации алембика.
Вместо "migrations" может быть любое слово. Это название папки
`alembic init migrations`

Далее alembic.ini вынесли на рутовый уровень и поменяли только один параметр
`script_location = app/migrations`
это сделано для того, чтобы алембик знал, где его папка migrations

Далее переходим к настройке алембика и моделей.

---

Добавляем несколько параметров и импортов в app/migrations/env.py файл алембика

Эти строки необязательно должны быть в таком порядке и друг за другом. 
Это просто фрагменты кода, который необходимо будет вставить или изменить.

```python
import sys
from os.path import abspath, dirname
# Это нужно для того, чтобы env.py от миграций понимал,
# что существует папка app, из которой мы что-то пытаемся импортнуть
sys.path.insert(0, dirname(dirname(abspath(__file__))))

# Сначала загрузится класс Base,
# потом загрузится класс Hotels, который унаследован от Base
# и теперь класс Base знает, что у нас есть такая-то модель Hotels
from app.database import Base, DB_URL
from app.hotels.models import Hotels

# Устанавливаем параметр, который используется в alembic.ini файле
# дополнительный параметр рекомендуют юзать для асинхронных драйверов (у нас asyncpg)
config.set_main_option("sqlalchemy.url", f"{DB_URL}?async_fallback=True")

# Сначала импортнули из нашего файла database класс Base,
# и потом здесь его применили
target_metadata = Base.metadata
```

---

Далее, для запуска миграции используем команду из рута
`alembic revision --autogenerate -m "Initial migration"`

После выполнения команды мы увидим сообщение о том, что было изменено в этой миграции.
Для примера, у нас добавилась таблица Hotels.
И далее сообщение о том, что под это изменение (ревизию) был создан файл миграции.

Файл лежит в app/migrations/versions/......py
Внутри этого файла указаны функции upgrade/downgrade, которые запустят какие-то функции в ОРМ

---

Накатим миграцию

В файле миграции метод называется upgrade, значит так и пишем команду
`alembic upgrade айди_миграции_из_файла`
типа
`alembic upgrade 36c8c0374b73`

Помимо айди миграции мы можем использовать слово `head`, тогда прогонятся все миграции до самой последней

---

Чтобы откатиться мы можем использовать следующую команду

`alembic downgrade -1` чтобы откатиться на 1 миграцию назад

---

Для настроек создали файл app/config.py, в котором создали класс Settings, и с помощью pydantic валидируем значения env переменных