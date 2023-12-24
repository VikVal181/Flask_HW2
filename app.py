from pathlib import PurePath, Path


from flask import Flask, render_template, request, redirect, make_response

app = Flask('__name__')

@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Семинар 2'
    }
    return render_template('base.html', **context)


@app.route('/task/', methods=['GET', 'POST'])
def task_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect('/hi'))
        response.set_cookie('user_name', name)
        response.set_cookie('user_email', email)
        return response
    return render_template('login.html', title='Введите данные')

@app.route('/hi/')
def hi():
    context = {
        'title': 'Приветствие',
        'name': request.cookies.get('user_name')
    }
    return render_template('hi.html', **context)

@app.route('/logout/')
def logout():
    response = redirect('/task')
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response

if __name__ == '__main__':
    app.run(debug=True)