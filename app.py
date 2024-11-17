from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def Atharv():
  return render_template('home.html')

app.run(host='0.0.0.0', debug = True, port=8080)
