from bottle import Bottle, request, route, run, template, view

app=Bottle()
app.config.load_config('config.conf')


@app.route('/')
def index():
    return template('index')

@app.route('/sentiment')
@view('analysis')
def analysis():
    data = {}
    data['hashtag'] = request.query.hashtag
    return data

run(host='localhost', port=8080)
