export $(xargs < .env_vk_id) && pytest -s hw/code -k test_dummy
