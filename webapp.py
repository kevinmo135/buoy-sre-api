from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# Set base directory for sqllite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define columns class
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=False)
    content = db.Column(db.String(250), unique=False)
    like = db.Column(db.Integer)
    def __init__(self, title, content, like):
        self.title = title
        self.content = content
        self.like = like

# Initiate schemas
class CommentsSchema(ma.Schema):
    class Meta:
        fields = ('title', 'content', 'like')
comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)


# Endpoints

# Post endpoint
@app.route('/comment', methods=["POST"])
def add_comment():
    title = request.json['title']
    content = request.json['content']
    like = "0"
    new_comment = Comments(title, content, like)
    db.session.add(new_comment)
    db.session.commit()
    comment = Comments.query
    return comment_schema.jsonify(comment)

# Return all comments
@app.route("/comments", methods=["GET"])
def get_comments():
    all_comments = Comments.query.all()
    result = comments_schema.dump(all_comments)
    return jsonify(result)

# Return single comment
@app.route("/comment/<id>", methods=["GET"])
def get_comment(id):
    comment = Comments.query.get(id)
    return comment_schema.jsonify(comment)

# Update Comment 
@app.route("/comment/<id>", methods=["PUT"])
def comment_update(id):
    comment = Comments.query.get(id)
    title = request.json['title']
    content = request.json['content']
    comment.title = title
    comment.content = content
    db.session.commit()
    return comment_schema.jsonify(comment)

# Like
@app.route("/like/<id>", methods=["PUT"])
def comment_like(id):
    comment = Comments.query.get(id)
    comment.like += 1
    db.session.commit()
    return comment_schema.jsonify(comment)

# Unlike
@app.route("/unlike/<id>", methods=["PUT"])
def comment_unlike(id):
    comment = Comments.query.get(id)
    if comment.like != 0:
        comment.like -= 1
        db.session.commit()
    return comment_schema.jsonify(comment)

# Delete full comment
@app.route("/comment/<id>", methods=["DELETE"])
def comment_delete(id):
    comment = Comments.query.get(id)
    db.session.delete(comment)
    db.session.commit()
    return comment_schema.jsonify(comment)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
