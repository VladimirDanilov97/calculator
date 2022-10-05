from flask import Flask, request, render_template
import math
from calculation import *


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def circle():
   context = {'units': LENGTH_UNITS}
   if request.method == 'POST':
      data = request.form
      r = float(data['radius']) * float(data['unit']) 
      circle = Circle(r)
      square =  circle.calculate_square()
      context['square'] =  square
   return render_template('index.html', **context)

if __name__ == '__main__':
   app.run(debug=True)
