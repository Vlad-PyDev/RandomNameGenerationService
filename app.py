from flask import Flask, render_template, request
import random

app = Flask(__name__)

male_names = ["Александр", "Максим", "Иван", "Дмитрий", "Николай"]
female_names = ["Анна", "Мария", "Елена", "Ольга", "Наталья"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/names', methods=['GET', 'POST'])
def names():
    names_list = []
    if request.method == 'POST':
        gender = request.form.get('gender')
        count = int(request.form.get('count', 1))
        pool = male_names if gender == 'male' else female_names
        for _ in range(count):
            names_list.append(random.choice(pool))
    return render_template('main.html', names=names_list)

if __name__ == '__main__':
    app.run(debug=True)