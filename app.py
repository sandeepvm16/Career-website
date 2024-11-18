from flask import Flask, render_template

app = Flask(__name__)

JOBS =[
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary' : 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'remote',
    'salary' : 'Rs. 12,00,000'
  },
  {
      'id': 3,
      'title': 'Frontend Engineer',
      'location': 'San Francisco, USA',
      'salary' : 'Rs. 15,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary' : 'Rs. 15,00,000'
  },
  {
      'id': 5,
      'title': 'Frontend Engineer',
      'location': 'San Francisco, USA',
      'salary' : 'Rs. 12,00,000'
  },
  {
      'id': 6,
      'title': 'Frontend Engineer',
      'location': 'Mumbai, India',
      'salary' : 'Rs. 15,00,000'
  }
]
@app.route('/')
def Atharv():
  return render_template('home.html',jobs=JOBS)

app.run(host='0.0.0.0', debug = True, port=8080)
