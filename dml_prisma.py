from prisma import Prisma

async def push_data_db(data_binance) -> None:
    try:
        db = Prisma(auto_register=True) # автоматическая регистрация моделей из schema.prisma
        await db.connect()

        # Проверяем, что запись существует по символу
        existing_data = await db.data_crypto_24h.find_first(
            where={
                "symbol": data_binance["symbol"]
            }
        )

        if existing_data:
            # Обновляем существующую запись
            updated_data = await db.data_crypto_24h.update_many(
                where={
                    "symbol": data_binance["symbol"]
                },
                data={
                    "weightedavgprice": float(data_binance["weightedAvgPrice"]),
                    "prevcloseprice": float(data_binance["prevClosePrice"]),
                    "highprice": float(data_binance["highPrice"]),
                    "lowprice": float(data_binance["lowPrice"]),
                    "date_info": data_binance["date_info"]
                }
            )
            print("Updating was successful")
        else:
            # Создаем новую запись, если запись не существует
            insert_data = await db.data_crypto_24h.create_many(
                data={
                    "symbol": data_binance["symbol"],
                    "weightedavgprice": float(data_binance["weightedAvgPrice"]),
                    "prevcloseprice": float(data_binance["prevClosePrice"]),
                    "highprice": float(data_binance["highPrice"]),
                    "lowprice": float(data_binance["lowPrice"]),
                    "date_info": data_binance["date_info"]
                }
            )
            print("Inserting was successful")

        await db.disconnect()

    except Exception as e:
        print(f"An error occurred: {e}")


async def get_data_db(name_symbol) -> dict:
    db = Prisma(auto_register=True)  # автоматическая регистрация моделей из schema.prisma
    await db.connect()

    row = await db.data_crypto_24h.find_first(
        where={
            "symbol": name_symbol
        }
    )
    row_dict = row.dict()  # Преобразование в словарь
    await db.disconnect()
    return row_dict




# # выполнено!
# async def get_data_db(name_symbol) -> None:
#     db = Prisma(auto_register=True)  # автоматическая регистрация моделей из schema.prisma
#     await db.connect()
#
#     all_data = await db.data_crypto_24h.find_many()
#
#     list = []
#     for data in all_data:
#         a = [f"{data.symbol}",
#              f"Weighted_Avg_Price: {data.weightedavgprice}",
#              f"Prev_Close_Price: {data.prevcloseprice}",
#              f"High_Price: {data.highprice}",
#              f"Low_Price: {data.lowprice}",
#              f"date_update: {data.date_info}"]
#         list.append(a)
#
#     for i in list:
#         if name_symbol in i:
#             print(i)
#
#     await db.disconnect()


# выполнено!

# if __name__ == "__main__":
#     get_data_db("ETHUSDT")
