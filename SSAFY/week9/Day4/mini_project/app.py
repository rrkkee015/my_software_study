from flask import Flask, render_template, request, redirect
import sqlite3
import datetime

app=Flask(__name__)

@app.route('/articles')
def articles_list():
    db=sqlite3.connect('blog.db')
    c=db.cursor()
    sql="SELECT * FROM articles"
    c.execute(sql)
    articles=c.fetchall()
    return render_template('articles_list.html', articles=articles)
    
@app.route('/articles/new')
def new():
    return render_template('new.html')
    
@app.route('/articles/create')
def articles_create():
    dt=datetime.datetime.now()
    now=dt.strftime("%Y년%m월%d일%H시%M분")
    
    title=request.args.get('title')
    content=request.args.get('content')
    author=request.args.get('author')
    
    db=sqlite3.connect('blog.db')
    c=db.cursor()
    sql="INSERT INTO articles (title, content, created_at, author) VALUES ('{}', '{}', '{}', '{}')".format(title,content,now,author)
    c.execute(sql)
    db.commit()
    
    d=db.cursor()
    sql2="SELECT MAX(id) FROM articles"
    d.execute(sql2)
    article=d.fetchone()
    return redirect('/articles/{}'.format(article[0]))
    
@app.route('/articles/<int:article_id>')
def detail(article_id):
    db=sqlite3.connect('blog.db')
    c=db.cursor()
    sql="SELECT * FROM articles WHERE ID = {}".format(article_id)
    c.execute(sql)
    article=c.fetchone()
    return render_template('detail.html',article=article)

@app.route('/articles/<int:article_id>/edit')
def edit(article_id):
    db=sqlite3.connect('blog.db')
    c=db.cursor()
    sql="SELECT * FROM articles WHERE ID = {}".format(article_id)
    c.execute(sql)
    article=c.fetchone()
    return render_template('edit.html',article=article)

@app.route('/articles/<int:article_id>/update')
def update(article_id):
    dt=datetime.datetime.now()
    now=dt.strftime("%Y년%m월%d일%H시%M분")

    title=request.args.get('title')
    content=request.args.get('content')
    author=request.args.get('author')
    
    db=sqlite3.connect('blog.db')
    c=db.cursor()
    sql="UPDATE articles SET title = '{}', content = '{}', created_at='{}', author ='{}' WHERE ID = {}".format(title, content, now, author, article_id)
    c.execute(sql)
    db.commit()
    
    return redirect('articles/{}'.format(article_id))
    
@app.route('/articles/<int:article_id>/delete')
def delete(article_id):
    db=sqlite3.connect('blog.db')
    c=db.cursor()
    sql='DELETE FROM articles WHERE ID = {}'.format(article_id)
    c.execute(sql)
    db.commit()
    return redirect('/articles')