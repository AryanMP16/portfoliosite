from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    print("Started!\n")
    return render_template('index.html')

#This is apparently how you do web page changes with flask?
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/cs')
def cs():
    return render_template('comsci.html')
@app.route('/physics')
def physics():
    return render_template('physics.html')
############################################################

@app.post('/')
def generate():
    
    return render_template('results.html', **locals())

if __name__ == '__main__':
    app.run(
        host = '127.0.0.1',
        port = 5000,
        debug = True
    )
