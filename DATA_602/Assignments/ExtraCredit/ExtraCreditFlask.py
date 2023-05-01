from flask import Flask, render_template, request

    # ------ Place code below here \/ \/ \/ ------

app = Flask(__name__)

@app.route('/')
def run_app():
    return render_template('index.html')

@app.route('/calc', methods=['POST'])
def my_form_post():
    if request.method == 'POST':
        number = request.form['number']
        multiply_number = float(number) * 5
        return '%s number multiplied by 5 is: %s * 5 = %f' % (number, number, multiply_number) 

if __name__ == '__main__':
   app.run(debug = True)

    # ------ Place code above here /\ /\ /\ ------
