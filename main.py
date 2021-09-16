from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)







# TODO pedir carta de recomendación a David



