from app import db


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))


if __name__ == '__main__':
    from app import create_app

    my_app = create_app()
    db.drop_all(app=my_app)
    db.create_all(app=my_app)
