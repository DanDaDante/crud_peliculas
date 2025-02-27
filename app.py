import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

#Cargar las variables de entorno
load_dotenv()

#Crear instancia
app = Flask(__name__)

#Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desactivar el seguimiento de modificaciones de objetos

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

#Modelo de la base de datos
class Pelicula(db.Model):
    __tablename__= 'peliculas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    director = db.Column(db.String)
    estreno = db.Column(db.String)
    genero = db.Column(db.String)
    duracion = db.Column(db.Integer)

    def to_dict(self):
        return{
            'id': self.id,
            'nombre': self.nombre,
            'director': self.director,
            'estreno': self.estreno,
            'genero': self.genero,
            'duracion': self.duracion
        }

#Ruta raiz
@app.route('/')
def index():
    #Trae todas las peliculas
    peliculas = Pelicula.query.all()
    return render_template('index.html', peliculas = peliculas)




if __name__ == '__main__':
    app.run(debug=True)

#source bin/activate
#pip install -r requirements.txt
#flask run --port=5010