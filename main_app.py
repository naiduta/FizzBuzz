import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/FizzBuzz',methods=['POST'])
def FizzBuzz():
    try:
        input = [float(x) for x in request.form.values()]
        i = np.int64(input)
        if i % 15 == 0:
            return render_template('index.html', output= "FizzBuzz")
        elif i % 3 == 0:
            return render_template('index.html', output= "Fizz")
        elif i % 5 == 0:
            return render_template('index.html', output= "Buzz")
        else:
            return render_template('index.html', output= i)
    except ValueError:
        return render_template('index.html', output="Oops!  Please Enter a positive Integer.  Try again...")
        #print("Oops!  Please Enter a positive Integer.  Try again...")

if __name__ == "__main__":
    app.run(debug=True)