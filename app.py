from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/incidencia", methods=["POST"])
def crear_incidencia():
    aula = request.form.get("aula")
    usuario = request.form.get("usuario")
    descripcion = request.form.get("descripcion")

    print("Aula:" + aula)
    print("Usuario:" + usuario)
    print("Descripcion:" + descripcion)
    

    conexion = mysql.connector.connect(
        host="localhost",
        user="incidencias",
        password="incidencias",
        database="incidencias")

    cursor = conexion.cursor()

    sql = """
    insert into registro
    (aual, usuario, descripcion, extado)
    values (%s,%s,%s,%s)
    """

    valores = (
        aula,
        usuario,
        descripcion,
        "Abierta"
    )

    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

    return "<h1>Incidencia recibida</h1> <ul><li>Aula: " + aula + "</li></ul>"

if __name__ == "__main__":
    app.run(debug=True)

