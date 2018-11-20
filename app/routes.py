from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello ,World'

@app.route('/address')
def minus():
    return '<h1> Block 20 Flat 5 FESTAC Extension Lagos<h1>'

