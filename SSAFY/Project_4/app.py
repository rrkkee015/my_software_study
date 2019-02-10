from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__="movies"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #id키
    title = db.Column(db.String, nullable=False) #영화명
    title_en = db.Column(db.String, nullable=False) #영화명(영문)
    audience = db.Column(db.Integer, nullable=False) #누적 관객수
    open_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #개봉일
    genre = db.Column(db.String, nullable=False) #장르
    watch_grade = db.Column(db.String, nullable=False) #관람등급
    score = db.Column(db.Float, nullable=False) #평점
    poster_url = db.Column(db.String, nullable=False) #포스터 이미지 URL
    description = db.Column(db.String, nullable=False) #영화소개

db.create_all()
    
@app.route('/movies')
def movies():
    movies = Movie.query.all()
    return render_template('movies.html', movies=movies)
    
@app.route('/movies/new')
def new():
    return render_template('new.html')
    
@app.route('/movies/create')
def create():
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    
    open_date = request.args.get('open_date')
    year=int(open_date[:4])
    month=int(open_date[5:7])
    date=int(open_date[8:10])
    dt = datetime(year, month, date)
    
    genre = request.args.get('genre')
    watch_grade = request.args.get('watch_grade')
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    movie = Movie(title=title, title_en=title_en, audience=audience, open_date=dt, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    db.session.add(movie)
    db.session.commit()
    
    idx = Movie.query.order_by(Movie.id.desc()).first().id
    return redirect('/movies/{}'.format(idx))
    
@app.route('/movies/<int:movie_id>')
def detail(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template('detail.html', movie=movie)
    
@app.route('/movies/<int:movie_id>/edit')
def edit(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template('edit.html', movie=movie)

@app.route('/movies/<int:movie_id>/update')
def update(movie_id):
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    
    open_date = request.args.get('open_date')
    year=int(open_date[:4])
    month=int(open_date[5:7])
    date=int(open_date[8:10])
    dt = datetime(year, month, date)
    
    genre = request.args.get('genre')
    watch_grade = request.args.get('watch_grade')
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    movie = Movie.query.get(movie_id)
    movie.title=title
    movie.title_en=title_en
    movie.audience=audience
    movie.open_date=dt
    movie.genre=genre
    movie.watch_grade=watch_grade
    movie.score=score
    movie.poster_url=poster_url
    movie.description=description
    db.session.commit()
    return redirect('/movies/{}'.format(movie_id))
    
@app.route('/movies/<int:movie_id>/delete')
def delete(movie_id):
    movie=Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect('/movies')