from application import app
from flask import render_template,request,flash

#Global list for look up

from application.forms import AeroForm
from application import db
from application.models import Entry

def get_entries():
    try:
        entries = Entry.query.first()
        return entries.number
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")
        return 0

def add_entry(new_entry):
    try:
        db.session.add(new_entry)
        db.session.commit()
        return new_entry.id
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")


@app.route('/')
def index_page():
    form1 = AeroForm
    entries = Entry.query.first()
    if entries is None:
        add_entry(Entry(number=0))
        entries = Entry.query.first()
        return render_template("index.html", form=form1, title="Increase Aero DB by 1 everytime button is clicked" , number = entries.number)
    else:
        return render_template("index.html", form=form1, title="Increase Aero DB by 1 everytime button is clicked" , number = entries.number)


def remove_entry(id):
    try:
        entry = Entry.query.get(id)
        db.session.delete(entry)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")
        return 0

def update_entry(id,new_number):
    try:
        entry = Entry.query.get(id)
        entry.number = new_number
        print(entry.number)
        rows_changed = Entry.query.filter_by(id=id).update(dict(number=new_number))
        db.session.commit()
        return rows_changed

    except Exception as error:
        db.session.rollback()
        flash(error,"danger")
        return 0

@app.route("/increasenum", methods=['POST'])
def predict():
    form1 = AeroForm()
    entry = get_entries()
    print(entry)
    new_entry = entry+1
    rows = update_entry(1,new_entry)
    entry = get_entries()
    return render_template("index.html", form=form1, title="Increase Aero DB by 1 everytime button is clicked" , number = entry)

        
    