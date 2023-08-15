from dotenv import dotenv_values


class Settings:
    PATH = "/home/kirillhact/work-directory/Anixart-copy/.env"
    CONFIG = dotenv_values(PATH)
    DB_HOST: int = CONFIG["DB_HOST"]
    DB_PORT: str = CONFIG["DB_PORT"]
    DB_USER: str = CONFIG["DB_USER"]
    DB_NAME: str = CONFIG["DB_NAME"]
    DB_PASS: str = CONFIG["DB_PASS"]

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
settings = Settings()
