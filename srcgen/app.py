from flask import redirect

from config_app import create_app, db
from modelsdomicilio import domicilio

app = create_app()

@app.route("/")
def listar():
    data = domicilio.query.all()
    diccionario_domicilio = {}
    for d in data:
        p = {
            "id": d.id,
            "direccion": d.producto_direccion,
            "codproducto1": d.producto_codproducto1,
            "codproducto2": d.producto_codproducto2,
            "codproducto3": d.producto_codproducto3,
            "codproducto4": d.producto_codproducto4,
            "codproducto5": d.producto_codproducto5,
            "codmetpago": d.producto_codmetpago,
            "valortotal": d.producto_valortotal,
        }
        diccionario_domicilio[d.id] = p
    return diccionario_domicilio

@app.route("/agregar/<nombre>/<int:cantidad>/<int:valor>")
def agregar(nombre, cantidad, valor):
    datos = {
        "direccion": direccion,
        "codproducto1": codproducto1,
        "codproducto2": codproducto2,
        "codproducto3": codproducto3,
        "codproducto4": codproducto4,
        "codproducto5": codproducto5,
        "codmetpago": codmetpago,
        "valortotal": valortotal,
    }
    p = domicilio(datos)
    db.session.add(p)
    db.session.commit()
    return redirect("/domicilio/")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    p = domicilio.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return redirect("/domicilio/")

@app.route("/editar/<int:id>/<nombre>/<int:cantidad>/<int:valor>")
def editar(id, nombre, cantidad, valor):
    p = domicilio.query.filter_by(id=id).first()
    p.producto_direccion = direccion
    p.producto_codproducto1 = codproducto1
    p.producto_codproducto2 = codproducto2
    p.producto_codproducto3 = codproducto3
    p.producto_codproducto4 = codproducto4
    p.producto_codproducto5 = codproducto5
    p.producto_codmetpago = codmetpago
    p.producto_valortotal = valortotal
    db.session.commit()
    return redirect("/domicilio/")

@app.route("/buscar/<int:id>")
def buscar(id):
    p = domicilio.query.filter_by(id=id).first()
    datos = {
        "id": p.id,
        "direccion": p.producto_direccion,
        "codproducto1": p.producto_codproducto1,
        "codproducto2": p.producto_codproducto2,
        "codproducto3": p.producto_codproducto3,
        "codproducto4": p.producto_codproducto4,
        "codproducto5": p.producto_codproducto5,
        "codmetpago": p.producto_codmetpago,
        "valortotal": p.producto_valortotal,
    }
    return datos

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")