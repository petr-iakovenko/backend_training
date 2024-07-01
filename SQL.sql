CREATE TYPE user_permission AS ENUM ('user', 'admin');
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    token_name VARCHAR(255) UNIQUE,
    username VARCHAR(255) NOT NULL,
    permission user_permission NOT NULL
);

CREATE TABLE IF NOT EXISTS data_crypto_24h(
    id SERIAL PRIMARY KEY,
	symbol VARCHAR(20) UNIQUE,
	weightedAvgPrice REAL,
	prevClosePrice REAL,
	highPrice REAL,
	lowPrice REAL,
	date_info VARCHAR
);

DROP TABLE IF EXISTS data_crypto_24h;
TRUNCATE TABLE data_crypto_24h;

INSERT INTO data_crypto_24h (symbol, weightedAvgPrice, prevClosePrice ,highPrice, lowPrice, date_info)
VALUES ('BTCUSDT', 0.11 , 0.11, 0.11, 0.11, '2024-06-27 11:45:10 UTC+0');
