export $(xargs < .env) && pytest -s hw/code -k test_creation_ok
