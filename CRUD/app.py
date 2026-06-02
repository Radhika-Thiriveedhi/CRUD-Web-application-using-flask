from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data = []

@app.route('/')
def index():
    return render_template('index.html', records=data, edit_index=None)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']

    if name and age:
        data.append({
            'name': name,
            'age': age
        })

    return redirect(url_for('index'))


@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(data):
        data.pop(index)

    return redirect(url_for('index'))


@app.route('/edit/<int:index>')
def edit(index):
    return render_template(
        'index.html',
        records=data,
        edit_index=index
    )


@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    if 0 <= index < len(data):
        data[index]['name'] = request.form['name']
        data[index]['age'] = request.form['age']

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)