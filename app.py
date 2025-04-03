from flask import Flask, send_file, request

app = Flask(__name__)

# Обрабатываем GET-запрос и возвращаем страницу "Контакты"
@app.route("/", methods=["GET"])
def contacts():
    return send_file("templates/contacts.html", mimetype="text/html")

# Дополнительно: обработка POST-запроса
@app.route("/", methods=["POST"])
def handle_post():
    data = request.form  # Получаем данные из формы
    print("Полученные данные:", data)  # Выводим в консоль
    return "Данные получены!", 200  # Отправляем ответ клиенту

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, send_file, request

app = Flask(__name__)

# Обрабатываем GET-запрос и возвращаем страницу "Контакты"
@app.route("/", methods=["GET"])
def contacts():
    return send_file("templates/contacts.html", mimetype="text/html")

# Дополнительно: обработка POST-запроса
@app.route("/", methods=["POST"])
def handle_post():
    data = request.form  # Получаем данные из формы
    print("Полученные данные:", data)  # Выводим в консоль
    return "Данные получены!", 200  # Отправляем ответ клиенту

if __name__ == "__main__":
    app.run(debug=True)
