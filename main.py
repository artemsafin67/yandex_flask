from flask import Flask, url_for, request

app = Flask(__name__)

planets = ['Сатурн', 'Марс', 'Земля', 'Нептун']
planets_benefits = {
    'Марс': ['Эта планета близка к Земле', 'На ней много необходимых ресурсов',
             'На ней есть вода и атмосфера', 'На ней есть небольшое магнитное поле',
             'Наконец, она просто красива!'],

    'Сатурн': ['У неё есть 13 замечательных колец', 'Период обращения - 30 земных лет!',
               'Но сутки длятся всего 10 часов', 'Внутри Сатурна поместилось бы 764 планеты Земля',
               'Плотность Сатурна даже меньше плотности воды'],

    'Земля': ['Много удивительных живых обитателей!', 'Потрясающие пейзажи',
              'В отличие от многих планет, на ней есть вода',
              'Земля - единственная планета с таким большим спутником - Луной',
              'Дома всегда лучше!'],

    'Нептун': ['Это огромный ледяной гигант!', 'Период обращения - 165 земных лет!',
               'Есть целых 14 спутников', 'Есть тоненькие кольца',
               'На нём часто бывают крупные штормы и мощные ветры']
}
classes = ['text-warning bg-success', 'text-danger bg-warning',
           'text-warning bg-danger', 'text-warning bg-info',
           'text-warning bg-primary']

descriptions = {}
for planet in planets:
    phrases = []
    for i in range(5):
        phrases.append("<p class='{}'>{}</p>".format(classes[i], planets_benefits[planet][i]))
    descriptions[planet] = '\n'.join(phrases)


@app.route('/choice/<planet_name>')
def planet_description(planet_name):
    if planet_name not in planets:
        return 'Для такой планеты пока нет описания'

    description = descriptions[planet_name]

    return """
    <!doctype html>
    
    <html>
        <head>
            <meta charset='utf-8'>
            <meta name='viewport' content='width=devide-width, initial-scale=1, shrink-to-fit=no'>
            
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <link rel='stylesheet' href='{}'>
            
            <title>Планеты</title>
        </head>
        
        <body>
            <div class='text-center yandex-block'>
                <h2><mark>Моё предложение: {}</mark></h2>
                <br>
                {}
            </div>
        </body>
    </html>
""".format(url_for('static', filename='css/style.css'), planet_name, description)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
