export $(xargs < .env) && pytest -s hw/code -k test_long_audience_name
