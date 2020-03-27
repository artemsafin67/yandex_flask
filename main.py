from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        return """
    <!doctype html>

    <html lang='en'>

        <head>

            <meta charset='utf-8'>
            <meta name='viewport' content='width=devide-width, initial-scale=1, shrink-to-fit=no'>

            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

            <link rel='stylesheet' href='{}'>
            <title>Отбор астронавтов</title>

        </head>

        <body>
            <h1 class='text-center text-info'>Анкета претендента</h1>
            <h2 class='text-center text-muted'>на участие в миссии</h2>

            <form class='login_form' method='post' role='form' enctype="multipart/form-data">

                <div class='form-group'>
                    <input type='text' class='form-control' id='surname' name='surname' placeholder='Введите фамилию'>
                </div>

                <div class='form-group'>
                    <input type='text' class='form-control' id='name' name='name' placeholder='Введите имя'>
                </div>

                <br>

                <div class='from-group'>
                    <input type='email' class='form-control' id='email' name='email' placeholder='Введите email'>
                </div>

                <div class='form-group'>

                    <label for='educationSelect'>Какое у вас образование?</label>
                    <select class='form-control' id='educationSelect' name='educationSelect'>
                        <option>Начальное</option>
                        <option>Среднее</option>
                        <option>Высшее</option>
                    </select>

                </div>

                <div class='form-group'>

                    <label for='form-check'>Какие у вас были професии?</label>

                    <div class='form-check'>
                        <input type='checkbox' class='form-check-input' id='engineer' name='job'>
                        <label for='engineer' class='form-check-label'>Инженер</label>
                    </div>

                    <div class='form-check'>
                        <input type='checkbox' class='form-check-input' id='teacher' name='teacher'>
                        <label for='teacher' class='form-check-label'>Учитель</label>
                    </div>

                    <div class='form-check'>
                        <input type='checkbox' class='form-check-input' id='doctor' name='doctor'>
                        <label class='form-check-label' for='doctor'>Врач</label>
                    </div>

                </div>

                <div class="form-group">

                    <label for="form-check">Укажите пол</label>

                    <div class="form-check">
                        <input class="form-check-input" type="radio" id="male" value="male" name='sex' checked>
                        <label class="form-check-label" for="male">Мужской</label>
                    </div>

                    <div class="form-check">
                      <input class="form-check-input" type="radio" id="female" value="female" name='sex'>
                      <label class="form-check-label" for="female">Женский</label>
                    </div>

                </div>

                <div class='form-group'>
                    <label for='motivation'>Почему вы хотите принять участие в миссии</label>
                    <textarea class='form-control' id='motivation' name='motivation' rows=3></textarea>
                </div>

                <div class='form-group'>
                    <label for='photo'>Приложите фотографию</label>
                    <input class='form-control-file' type='file' id='file' name='file'>
                </div>

                <div class='form-group form-check'>
                    <input class='form-check-input' type='checkbox' id='accept' name='accept'>
                    <label class='form-check-label' for='accept'>Готовы остаться на Марсе?</label>
                </div>

                <div class='text-center'><button type='submit' class='in_the_middle btn btn-info'>Отправить</button></div>

            </form>

        </body>

    </html>
    """.format(url_for('static', filename='css/style.css'))

    elif request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('educationSelect'))

        for job in ['engineer', 'doctor', 'teacher']:
            print('{}: {}'.format(job, 'Yes' if request.form.get(job) else 'No'))

        print(request.form.get('sex'))
        print(request.form.get('motivation'))

        f = request.files.get('file')
        print(f.read())

        print(request.form.get('accept'))

        return '<h1>Данные отправлены</h1>'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
