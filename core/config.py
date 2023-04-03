from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
SECRET_KEY = config("SECRET_KEY", cast=str, default="f9b52f10dd24fb43a7953b8f90530a4239a861ebfccc843ff9621e0f8dc8ca33")
ALGORITHM = "HS256"