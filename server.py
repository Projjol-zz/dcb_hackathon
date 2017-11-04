import json
import traceback
import os
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['POST'])
def find_service():
    req = request.get_data()
    print req

    return {"status": 200}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port, debug=True)
    # app.run(host='0.0.0.0', debug=True)
