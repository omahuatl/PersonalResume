from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)

# TODO Cambiar el Favicon
# TODO Agregar a la topbar ligas a mi educación e skills
# TODO agregar las cartas de recomendación a "clients are saying
# TODO cambiar el apartado What can I do
# TODO pensar si quiero conservar el Portafolio
# TODO Quitar el objeto de configuración de colores.


