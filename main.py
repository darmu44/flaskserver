from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/send_data', methods=['POST'])
def send_data_ru():
    data = request.get_json()
    print(data)

    if not data or not data.get("email") or not data.get("phone"):
        response_message = (
            "Эй, а ты что, шутишь?! 😡\n"
            "Ты мне даже свой Email и Телефон не прислал? 🤨\n"
            "Ну как я тебе напишу, если ты скрываешь свои данные?! 🧐\n"
            "Без данных ты — как призрак в интернете! 👻\n"
            "Отправь мне хоть что-нибудь, пожалуйста! 🙏"
        )
    else:
        # Если данные были переданы
        email = data.get("email", "Не указан")
        phone = data.get("phone", "Не указан")
        response_message = (
            f"Ого, привет! 😎\n"
            f"Я только что получил ваши данные для связи! 📱💻\n"
            f"Электронный почтовый голубь 🕊️, я имею в виду ваш Email: {email}, "
            f"и телефонный сигнал с другой планеты 🌌, то есть ваш Телефон: {phone}!\n"
            f"Будем на связи, только не заблудитесь в лабиринте интернета! 😄"
        )

    return jsonify({"message": response_message})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)