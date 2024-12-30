echo "Freezing the requirements ..."
pipenv requirements --dev > requirements.txt

echo "Starting services ..."
docker compose up -d --build
