для запуска контейнера используем команды:
docker-compose build
docker-compose up -d

для остановки:
docker-compose down

автоматически создаются миграции, суперпользователь, загружаются тестовые кадастовые номера

тестирование проводить по пути:
http://localhost:8000/api/swagger/

админка:
http://localhost:8000/admin/
