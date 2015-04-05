var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var router = express.Router();
var spawn = require('child_process').spawn;

var app = express();

require('dotenv').load();

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

//app.use(favicon(__dirname + '/public/favicon.ico'));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', router);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: {}
    });
});

var server = app.listen(8080, function() {
  console.log('Express started on port ' + 8080);
});
var io = require('socket.io')(server);

router.get('/', function(req, res) {
    res.render('index', { title: 'Twitter Sentiment Analysis' });
});

router.get('/sentiment', function(req, res) {
    var proc = spawn('python', ['-u', 'twitter-analysis.py'], { env: process.env });

    proc.stdout.setEncoding('utf8');

    proc.stdout.on('data', function (data) {
        var str = data.toString()
        var lines = str.split(/(\r?\n)/g);
        io.emit('data', {d : lines.join("")});
        console.log(lines.join(""));
    });

    proc.on('close', function (code) {
        console.log('process exit code ' + code);
    });

    res.render('sentiment', {
        title: 'Twitter Sentiment Analysis',
        hashtag: req.query.hashtag
    });
});

module.exports = app;
