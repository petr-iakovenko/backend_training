#### Datebase - postgres (docker)
terminal run:  
`docker run --name db_web_service-pg-15.2 -p 5002:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=db_web_service -d postgres:15.2`

Connection with help DBeaver program.  

DDL: 

```SQL
CREATE TYPE user_permission AS ENUM ('user', 'admin');
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    token_name VARCHAR(255) UNIQUE,
    username VARCHAR(255) NOT NULL,
    permission user_permission NOT NULL
);
```

```SQL
CREATE TABLE IF NOT EXISTS data_crypto_24h(
	symbol VARCHAR(20) UNIQUE,
	weightedAvgPrice REAL,
	prevClosePrice REAL,
	highPrice REAL,
	lowPrice REAL,
	date_info VARCHAR
);
```

#### Execution logic:

User send 'POST' request for data updates about "24 hour rolling price change statistics" about chose crypto-coin.
'POST' request include information in JSON about 'symbol' crypto-coin.
After posting 'POST' request server get information from API Binance for writing to Postgres(database) on server.
If on database information about crypto-coin already exists that information will update on server (in database).

User send 'GET' request for getting JSON about last information from server (from database) about crypto-coin.
'GET' request include JSON information about crypto-coin( 'symbol').
Then from database getting information about crypto-coin.
This information transforming in JSON and returned to user.
