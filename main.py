from flask import Flask, request, redirect

main = Flask(__name__)  # Создание главного файла


@main.route("/", methods=["GET"])
def index():
    name = request.args.get('name')
    message = request.args.get('message')
    if not name or not message:
        return redirect("/?name=Rekruto&message=Давай дружить!")
    return f'Hello {name}! {message}!'

# Запуск
if __name__ == "__main__":
    main.run(debug=False)
