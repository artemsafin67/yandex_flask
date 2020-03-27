from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return """
    <!doctype html>
    
    <html>
        <head>
            <meta charset='utf-8'>
            <meta name='viewport' content='width=devide-width, initial-scale=1, shrink-to-fit=no'>
            
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <link rel='stylesheet' href='{}'>
            
            <title>Результаты</title>
        </head>
        
        <body>
            <h1>Результаты отбора</h1>
            <h2>Претендента на участие {}</h2>
            
            <p class='bg-success'>Поздравляем! Ваш рейтинг после {} этапа отбора</p>
            <p>составляет {}</p>
            <p class='bg-warning'>Желаем удачи!</p>
        </body>
    </html>
    """.format(url_for('static', filename='css/style.css'), nickname, str(level), str(rating))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
