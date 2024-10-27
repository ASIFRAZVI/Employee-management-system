from pathlib import os
from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
secret_key = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
debug = os.getenv("DEBUG")

allowed_host = []


# Application definition
internal_app = ["apps.base", "apps.authentication", "apps.employee_management"]

thirdparty_app = [
    "rest_framework",
    "drf_spectacular",
]

db_mode = os.getenv("DB_MODE")

dev_db_mgmt = "dev"
prod_db_mgmt = "prod"

dev_db = {
    "default": {
        "ENGINE": os.getenv("DEV_DB_ENGINE"),
        "NAME": os.getenv("DEV_DB_NAME"),
        "USER": os.getenv("DEV_DB_USER"),
        "PASSWORD": os.getenv("DEV_DB_PASSWORD"),
        "HOST": os.getenv("DEV_DB_HOST"),
        "PORT": os.getenv("DEV_DB_PORT"),
    }
}

prod_db = {
    "default": {
        "ENGINE": os.getenv("PRO_DB_ENGINE"),
        "NAME": os.getenv("PRO_DB_NAME"),
        "USER": os.getenv("PRO_DB_USER"),
        "PASSWORD": os.getenv("PRO_DB_PASSWORD"),
        "HOST": os.getenv("PRO_DB_HOST"),
        "PORT": os.getenv("PRO_DB_PORT"),
    }
}

db_error_msg = "please configure Database"

# Swagger config
rest_ramework = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

swagger_config = {
    "TITLE": "Employee management system",
    "DESCRIPTION": "kfcjvfljv",
}

JWT_SECRET = os.getenv("JWT_SECRET")
