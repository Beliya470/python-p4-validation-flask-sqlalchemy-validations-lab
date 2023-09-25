from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String(length=10))  # Add length constraint

    @validates('phone_number')
    def validate_phone_number(self, key, value):
        # Add phone number validation
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be exactly 10 digits.")
        return value

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)

    @validates('title')
    def validate_title(self, key, value):
        # Add custom title validation
        keywords = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(keyword in value for keyword in keywords):
            raise ValueError("Title must contain one of: 'Won't Believe', 'Secret', 'Top [number]', 'Guess'")
        return value

    # Add constraints for content and summary lengths
    content = db.Column(db.String(length=250), nullable=False)
    summary = db.Column(db.String(length=250))

    @validates('category')
    def validate_category(self, key, value):
        # Add category validation
        if value not in ["Fiction", "Non-Fiction"]:
            raise ValueError("Category must be either 'Fiction' or 'Non-Fiction'")
        return value

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, summary={self.summary})'
