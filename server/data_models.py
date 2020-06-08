from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password, method='sha256')

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            return None

        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def to_dict(self):
        return dict(id=self.id, email=self.email)

class Journal(db.Model):

    __tablename__ = 'journal'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    #id = db.Column(db.Text, default = str(uuid.uuid4()), primary_key = True)
    note = db.Column(db.Text)
    color = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
      return dict(id=self.id,
                  note=self.note,
                  color=self.color,
                  created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S')
                  )