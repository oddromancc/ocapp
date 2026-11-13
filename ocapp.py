from flask import Flask, render_template, g, current_app, flash, request, redirect, url_for, send_file, session
import ast

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

rolecol = []
rolecolD = []
rescol = []

@app.route('/', methods=('GET', 'POST'))
def onhome():

    if request.method == 'POST':
        if 'resExp' in request.form:
            resTags = request.form.getlist('resTags')
            print(resTags)

            resTitle = request.form['resTitle']
            resDesc = request.form['resDesc']
            resExp = request.form['resExp']
            resEd = request.form['resEd']
            resComp = request.form['resComp']

            aRes = [('Название', resTitle), ('Описание', resDesc), ('Стаж', resExp), ('Навыки', resTags), ('Образование', resEd), ('Зарплата', resComp)]
            rescol.append(aRes)
            print(aRes)

        if 'resExp1' in request.form:
            resTags1 = ast.literal_eval(request.form['resTags1'])
            resEd1 = request.form['resEd1']

            for role in rolecol:
                roleTags = role[3][1]
                roleEd = role[4][1]
                if roleEd != resEd1:
                    print('llllll')
                    continue
                for s in roleTags:
                    if s not in resTags1:
                        print('Not fit for the job')
                        break
                else:
                    rolecolD.append(role)
            return redirect(url_for('onchoices'))
                    

    return render_template('onhome.html', rescol=rescol)

@app.route('/jobs', methods=('GET', 'POST'))
def onjobs():

    if request.method == 'POST':
        roleTags = request.form.getlist('roleTags')
        print(roleTags)

        roleTitle = request.form['roleTitle']
        roleDesc = request.form['roleDesc']
        roleExp = request.form['roleExp']
        roleEd = request.form['roleEd']

        aRole = [('Название', roleTitle), ('Описание', roleDesc), ('Требуемый стаж', roleExp), ('Требуемые навыки', roleTags), ('Требуемое образование', roleEd)]
        rolecol.append(aRole)
        print(aRole)

    return render_template('onjobs.html', rolecol=rolecol)

@app.route('/choices', methods=('GET', 'POST'))
def onchoices():
    print('cho', rolecolD)
    return render_template('onchoices.html')