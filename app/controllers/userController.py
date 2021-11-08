from werkzeug.utils import redirect
from app import app
from flask import render_template, request
from app.models.users import db, Mahasiswa


@app.route('/user', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        nama = request.form['nama']
        kabupaten = request.form['kabupaten']
        provinsi = request.form['provinsi']
        try:
            mhs = Mahasiswa(nama=nama, kabupaten=kabupaten, provinsi=provinsi)
            db.session.add(mhs)
            db.session.commit()
        except Exception as e:
            print("Failed to add data.")
            print(e)
    listMhs = Mahasiswa.query.all()
    print(listMhs)
    return render_template("users.html", data=enumerate(listMhs, 1))


@app.route('/userCreate', methods=['POST', 'GET'])
def userCreate():    
    return render_template("formcreate.html")


@app.route('/userUpdate/<int:id>')
def userUpdate(id):
    konten = Mahasiswa.query.filter_by(id=id).first()
    return render_template ("updateUser.html", data = konten)


@app.route('/update', methods =['POST', 'GET'])
def updateAction():
    if request.method == 'POST':
        id = request.form['id']
        nama = request.form['nama']
        kabupaten = request.form['kabupaten']
        provinsi = request.form['provinsi']
    try:
        user = Mahasiswa.query.filter_by(id=id).first()
        user.nama = nama
        user.kabupaten = kabupaten
        user.provinsi = provinsi
        db.session.commit()
    except Exception as e:
            print("Failed to update data.")
            print(e)
    return redirect('/user')

@app.route('/delete/<int:id>')
def delete(id):
    try:
        user = Mahasiswa.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

    except Exception as e:
        print("Failed to update data.")
        print(e)

    return redirect('/user')