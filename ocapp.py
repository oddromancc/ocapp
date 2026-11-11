from flask import Flask, render_template, g, current_app, flash, request, redirect, url_for, send_file, session, send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

@app.route('/', methods=('GET', 'POST'))
def onhome():
    gg = []

    if request.method == 'POST':
            resTags = request.form.getlist('resTags')
            print(resTags)
    
            resTitle = request.form['resTitle']
            resDesc = request.form['resDesc']
            resExp = request.form['resExp']
            resTags = request.form['resTags']
            resEd = request.form['resEd']

            aRes = [('Название', resTitle), ('Описание', resDesc), ('Стаж', resExp), ('Навыки', resTags), ('Образование', resEd)]
            gg.append(aRes)
            print(aRes)
        
    return render_template('onhome.html', gg=gg)

@app.route('/jobs', methods=('GET', 'POST'))
def onjobs():
    gg = [1, 2, 3]

    return render_template('onjobs.html', gg=gg)