from db_sqlalch import insert_update_data, get_date_from_db
from get_crypto import info_binance
from flask import Flask, request


# create instance Flask
app = Flask(__name__)

# post info
@app.route('/', methods=['POST'])
def ask_info():
    data = request.json
    data_url = info_binance(data)
    insert_update_data(data_url)
    return 'Done!'


# get page
@app.route('/api/info', methods=['GET'])
def get_info():
    data = request.json
    data_ = get_date_from_db(data)
    return data_


# run app.py
if __name__ == '__main__':
    app.run(debug=True)