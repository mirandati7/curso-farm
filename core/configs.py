class Settings():
    
    #JWT_SECRET: str = '4j-N-rYqT8cWfNX5cH3-iLTnIj4Nh4RHecJzhjNWFL4'
    JWT_SECRET: str = '44bf22c4-5f99-47f6-b113-fa3ff18630c1'
    ALGORITHM: str = 'HS256'
    #60 minutos * 24 Horas  * 7 dias => 1 semana
    #ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 * 1 * 1

    CLIENT_ORIGIN: str


settings = Settings()