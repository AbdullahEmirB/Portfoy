# Import
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# İçerik sayfasını çalıştırma ve dinamik becerileri işleme
@app.route('/', methods=['GET', 'POST'])
def index():
    button_python = None
    button_discord = None
    button_html = None
    button_db = None

    if request.method == 'POST':
        if 'button_python' in request.form:
            button_python = True
        elif 'button_discord' in request.form:
            button_discord = True
        elif 'button_html' in request.form:
            button_html = True
        elif 'button_db' in request.form:
            button_db = True

    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)

@app.route('/form', methods=['POST'])
def form():
    email = request.form['email']
    text = request.form['text']

    # Verileri bir dosyaya yazma
    with open('feedback.txt', 'a') as file:
        file.write(f"Email: {email}\n")
        file.write(f"Mesaj: {text}\n")
        file.write("-" * 20 + "\n")

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
