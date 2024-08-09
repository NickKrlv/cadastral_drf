echo "Running migrations..."
python manage.py migrate
echo "Create admin..."
python manage.py csu
echo "Loading data..."
python manage.py fill_database
echo "Collect static files..."
python manage.py collectstatic --noinput
exec "$@"