from flask import SQLAlchemy

db = SQLAlchemy()

class domicilio(db.Model):
    id = db.Column("domicilio_id", db.Integer, primary_key=True)
    producto_direccion = db.Column(db.String)
    producto_codproducto1 = db.Column(db.String)
    producto_codproducto2 = db.Column(db.Integer)
    producto_codproducto3 = db.Column(db.Integer)
    producto_codproducto4 = db.Column(db.Integer)
    producto_codproducto5 = db.Column(db.Integer)
    producto_codmetpago = db.Column(db.Integer)
    producto_valortotal = db.Column(db.Integer)

    def __init__(self, datos):
        self.producto_direccion = datos["direccion"]
        self.producto_codproducto1 = datos["codproducto1"]
        self.producto_codproducto2 = datos["codproducto2"]
        self.producto_codproducto3 = datos["codproducto3"]
        self.producto_codproducto4 = datos["codproducto4"]
        self.producto_codproducto5 = datos["codproducto5"]
        self.producto_codmetpago = datos["codmetpago"]
        self.producto_valortotal = datos["valortotal"]
