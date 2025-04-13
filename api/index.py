import requests
import random
from flask import Flask, jsonify, request

class GameInfo:

    def __init__(self):
        self.TitleId: str = "24EAA"
        self.SecretKey: str = "GBIPB74594RF9UDYHIAKASEJ1WG66KWWF4FAPKJK1WYZCC94S7"
        self.ApiKey: str = "OC|9807548162641339|f4cedc6635c40602c7fd43608a7c92cc"

    def get_auth_headers(self):
        return {
            "content-type": "application/json",
            "X-SecretKey": self.SecretKey
        }


settings = GameInfo()
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def titledata():
    response = requests.post(
        url=f"https://{settings.TitleId}.playfabapi.com/Server/GetTitleData",
        headers=settings.get_auth_headers())

    if response.status_code == 200:
        return jsonify(response.json().get("data").get("Data"))
    else:
        return jsonify({}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
