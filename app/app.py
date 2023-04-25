from flask import Flask, render_template, request, redirect, flash
import articulosController

app = Flask(__name__)


@app.route('/')
def index():
    # datos = Articles()
    datos = articulosController.listar()
    return render_template('index.html', data=datos)


@app.route('/agregarArticulo')
def agregar():
    return render_template('agregar.html')


@app.route('/guardarArticulo', methods=["POST"])
def guardar_articulo():
    id = request.form['id']
    title = request.form['title']
    body = request.form['body']
    author = request.form['author']
    create_date = request.form['date']
    articulosController.insertar(id, title, body, author, create_date)
    return redirect('/')


@app.route('/eliminarArticulo',  methods=["POST"])
def eliminiar_articulo():
    articulosController.eliminarArticulo(request.form['id'])
    return redirect('/')


@app.route("/editarArticulo/<int:id>")
def editar_articulo(id):
    # Obtener el juego por ID
    datos = articulosController.ListarArticulo(id)
    return render_template("editarArticulo.html", data=datos)


@app.route("/actualizarArticulo", methods=["POST"])
def actualizar_articulo():
    id = request.form['id']
    title = request.form['title']
    body = request.form['body']
    author = request.form['author']
    articulosController.actualizarArticulo(
        id, title, body, author)
    return redirect("/")


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

