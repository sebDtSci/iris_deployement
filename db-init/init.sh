#!/bin/bash
# init.sh
echo "Attente de PostgreSQL pour démarrer..."
while ! pg_isready -h db -p 5432 -U alex; do
    echo "En attente... (PostgreSQL n'est pas encore prêt)"
    sleep 2
done

echo "PostgreSQL a démarré. Exécution du script init.py..."
python /docker-entrypoint-initdb.d/init.py