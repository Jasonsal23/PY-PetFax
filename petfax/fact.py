from flask import ( Blueprint, render_template, request, redirect )
from . import models

bp = Blueprint('fact', __name__, url_prefix="/facts")


@bp.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        print(request.form)
        submitter = request.form['submitter']
        fact = request.form['fact']
        photo = request.form['photo']

        new_fact = models.Fact(submitter=submitter, fact=fact, photo=photo)
        models.db.session.add(new_fact)
        models.db.session.commit()

        redirect('/facts')

        results = models.Fact.query.all()
        

    return render_template('facts/index.html', facts=results)

@bp.route('/new')
def new():
    return render_template('facts/new.html')