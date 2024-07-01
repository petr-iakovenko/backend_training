from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine("postgresql://postgres:postgres@localhost:5002/db_web_service")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

class Data_crypto_24h(Base):
    """
    Creating class table "data_crypto_24h"
    """
    __tablename__ = "data_crypto_24h"

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(20), unique=True)
    weightedavgprice = Column(Float)
    prevcloseprice = Column(Float)
    highprice = Column(Float)
    lowprice = Column(Float)
    date_info = Column(String(20))


def check_symbol(symbol):
    """
    Check unique values in DB by 'symbol'
    :param symbol: 'symbol' for looking unique value
    :return: bool
    """
    session = SessionLocal()
    existing_entry = session.query(Data_crypto_24h).filter_by(symbol=symbol).first()
    session.close()
    return existing_entry is not None


def insert_data_from_json(crypto_data):
    """
    Inserting data in BD
    :param crypto_data: json for updating data in DB
    :return: none
    """
    session = SessionLocal()
    try:
        data_objects = []
        data_obj = Data_crypto_24h(
            symbol=crypto_data['symbol'],
            weightedavgprice=crypto_data['weightedAvgPrice'],
            prevcloseprice=crypto_data['prevClosePrice'],
            highprice=crypto_data['highPrice'],
            lowprice=crypto_data['lowPrice'],
            date_info=crypto_data['date_info']
        )
        # print(data_obj)
        data_objects.append(data_obj)
        print(data_objects)
        session.add_all(data_objects)
        session.commit()
        session.close()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def update_data_from_json(symbol_crypto, crypto_data):
    """
    Updating data in DB
    :param symbol_crypto: 'symbol' for looking unique value
    :param crypto_data: json for updating data in DB
    :return: none
    """
    session = SessionLocal()
    try:
        entry = session.query(Data_crypto_24h).filter_by(symbol=symbol_crypto).first()
        entry.weightedavgprice = crypto_data['weightedAvgPrice']
        entry.prevcloseprice = crypto_data['prevClosePrice']
        entry.highprice = crypto_data['highPrice']
        entry.lowprice = crypto_data['lowPrice']
        entry.date_info = crypto_data['date_info']
        session.add(entry)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def insert_update_data(crypto_data):
    """
    Check unique data in DB for updating or inserting new data
    from API Binance
    :param crypto_data: json from API Binance
    :return: none
    """
    symbol_crypto = crypto_data['symbol']
    if check_symbol(symbol_crypto):
        update_data_from_json(symbol_crypto, crypto_data)
    else:
        insert_data_from_json(crypto_data)


def get_date_from_db(data):
    """
    Return data from DB on request JSON from user (symbol)
    :param data: json from user request
    :return: json from DB
    """
    session = SessionLocal()
    entry = session.query(Data_crypto_24h).filter_by(symbol=data['symbol']).first()
    entry_to_dict = {column.name: getattr(entry, column.name) for column in Data_crypto_24h.__table__.columns}
    entry_to_dict = json.dumps(entry_to_dict)
    session.close()
    return entry_to_dict