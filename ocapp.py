from flask import Flask, render_template, current_app, flash, request, redirect, url_for
import ast
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

conn = sqlite3.connect('ocapp.db', check_same_thread=False)
sqlc = conn.cursor()
with open('schema.sql', 'r') as file:
    schema = file.read()
sqlc.executescript(schema)
conn.commit()

sqlc.execute('SELECT * FROM rescol')
prong = sqlc.fetchall()
for p in prong:
    print(p)

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
            print(resComp)

            aRes = [('Название', resTitle), ('Описание', resDesc), ('Стаж', resExp), ('Навыки', resTags), ('Образование', resEd), ('Минимальная желаемая зарплата', resComp)]
            rescol.append(aRes)
            print(aRes)
            sqlc.execute('INSERT INTO rescol (title) VALUES (?)', (resTitle,))
            conn.commit()

        if 'resExp1' in request.form:
            resTags1 = ast.literal_eval(request.form['resTags1'])
            resEd1 = request.form['resEd1']
            resComp1 = int(request.form['resComp1'])

            for role in rolecol:
                roleTags = role[3][1]
                roleEd = role[4][1]
                roleComp = role[5][1]
                if roleComp < resComp1 or roleEd != resEd1:
                    continue
                for s in roleTags:
                    if s not in resTags1:
                        break
                else:
                    rolecolD.append(role)
            return redirect(url_for('onchoices'))
                    
    return render_template('onhome.html', rescol=rescol)

@app.route('/jobs', methods=('GET', 'POST'))
def onjobs():

    if request.method == 'POST':
        roleTags = request.form.getlist('roleTags')

        roleTitle = request.form['roleTitle']
        roleDesc = request.form['roleDesc']
        roleExp = request.form['roleExp']
        roleEd = request.form['roleEd']
        roleComp = request.form['roleComp']

        aRole = [('Название', roleTitle), ('Описание', roleDesc), ('Требуемый стаж', roleExp), ('Требуемые навыки', roleTags), ('Требуемое образование', roleEd), ('Минимальная зарплата', roleComp)]
        rolecol.append(aRole)
        print(aRole)

    return render_template('onjobs.html', rolecol=rolecol)

@app.route('/choices', methods=('GET', 'POST'))
def onchoices():
    print('cho', rolecolD)
    return render_template('onchoices.html')