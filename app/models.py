
from app import db


class LifeGoalList(db.Model):
    """This is the table model"""

    __tablename__ = 'LifeGoalList'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
            db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())


    def __init__(self, name):
        """ init """
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return LifeGoalList.query.all()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<LifeGoalList: {}>".format(self.name)



