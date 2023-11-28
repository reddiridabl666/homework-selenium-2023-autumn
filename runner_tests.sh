export $(xargs < .env) && pytest -s hw/code -k test_account_type_radio
