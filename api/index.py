from flask import Flask

app = Flask(__name__)

TitleId = "7AF94"

@app.route("/", methods=["POST", "GET"])
def title_data():
    response = requests.post(
        url=f"https://{settings.TitleId}.playfabapi.com/Server/GetTitleData",
        headers=settings.get_auth_headers()
    )
    return jsonify(response.json().get("data").get("Data"))

@app.route('/about')
def about():
    return 'About'
