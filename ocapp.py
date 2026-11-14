from flask import Flask, render_template, current_app, flash, request, redirect, url_for
import ast
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

conn = sqlite3.connect('ocapp.db', check_same_thread=False)
sor = conn.cursor()
with open('schema.sql', 'r') as file:
    schema = file.read()
sor.executescript(schema)
conn.commit()

sor.execute('SELECT * FROM rescol')
prong = sor.fetchall()

rescol = []
rolecol = []
rolecolD = []

@app.route('/', methods=('GET', 'POST'))
def onhome():

    global rescol
    rescol = []
    sor.execute('SELECT * FROM rescol')
    prong = sor.fetchall()

    for p in prong:
        aRes = ['placeholder', ['Название', 1], ['Описание', 1], ['Стаж', 1], ['Навыки', 1], ['Образование', 1], ['Минимальная желаемая зарплата', 1]]
        ind = 0
        forapp = []
        for t in p:
            if ind == 0:
                ind += 1
                continue
            li = [aRes[ind][0], t]
            forapp.append(li)
            ind += 1
        rescol.append(forapp)

    if request.method == 'POST':
        if 'resExp' in request.form:
            resTags = request.form.getlist('resTags')
            resTitle = request.form['resTitle']
            resDesc = request.form['resDesc']
            resExp = request.form['resExp']
            resEd = request.form['resEd']
            resComp = request.form['resComp']

            sor.execute('INSERT INTO rescol (title, desc, exp, tags, ed, comp) VALUES (?, ?, ?, ?, ?, ?)', (resTitle, resDesc, resExp, str(resTags), resEd, resComp))
            conn.commit()
            return redirect(url_for('onhome'))

        if 'resExp1' in request.form:
            resTags1 = ast.literal_eval(request.form['resTags1'])
            resEd1 = request.form['resEd1']
            resComp1 = int(request.form['resComp1'])

            for role in rolecol:
                roleTags = role[3][1]
                roleEd = role[4][1]
                roleComp = int(role[5][1])
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

    global rolecol
    rolecol = []
    sor.execute('SELECT * FROM rolecol')
    prong = sor.fetchall()

    for p in prong:
        aRole = ['placeholder', ['Название', 1], ['Описание', 1], ['Требуемый стаж', 1], ['Требуемые навыки', 1], ['Требуемое образование', 1], ['Предлагаемая зарплата', 1]]
        ind = 0
        forapp = []
        for t in p:
            if ind == 0:
                ind += 1
                continue
            li = [aRole[ind][0], t]
            forapp.append(li)
            ind += 1
        rolecol.append(forapp)

    if request.method == 'POST':
        roleTags = request.form.getlist('roleTags')
        roleTitle = request.form['roleTitle']
        roleDesc = request.form['roleDesc']
        roleExp = request.form['roleExp']
        roleEd = request.form['roleEd']
        roleComp = request.form['roleComp']

        sor.execute('INSERT INTO rolecol (title, desc, exp, tags, ed, comp) VALUES (?, ?, ?, ?, ?, ?)', (roleTitle, roleDesc, roleExp, str(roleTags), roleEd, roleComp))
        conn.commit()
        return redirect(url_for('onjobs'))

    return render_template('onjobs.html', rolecol=rolecol)

@app.route('/choices', methods=('GET', 'POST'))
def onchoices():
    print('cho', rolecolD)
    return render_template('onchoices.html')