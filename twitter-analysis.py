from bottle import request, route, run, template, view

@route('/')
def index():
    return template('index')

@route('/sentiment')
@view('analysis')
def analysis():
    data = {}
    data['hashtag'] = request.query.hashtag
    return data

run(host='localhost', port=8080)
