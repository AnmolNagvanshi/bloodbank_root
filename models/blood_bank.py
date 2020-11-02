from datetime import datetime
from app import db


class BloodBank(db.Model):
    __tablename__ = "blood_banks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)

    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    registered_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    mobile_no = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(400), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    pin_code = db.Column(db.String(6), nullable=False)

    latitude = db.Column(db.String(20), nullable=True)
    longitude = db.Column(db.String(20), nullable=True)

    # bags = db.relationship('BloodBag', backref='blood_bank', lazy='dynamic')

    def __repr__(self):
        return f"{self.name} in {self.city}, {self.state}"








# class BloodGroup(db.Model):
#     __tablename__ = "blood_groups"
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     group = db.Column(db.String(2))
#     is_positive = db.Column(db.Boolean)
#
#     def __repr__(self):
#         if self.is_positive:
#             return f"{self.group}+"
#         return f"{self.group}-"


# class TotalBlood(db.Model):
#     __tablename__ = "total_blood"
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     blood_bank_id = db.Column(db.Integer, db.ForeignKey('blood_bank.id'))
#     blood_group_id = db.Column(db.Integer, db.ForeignKey('blood_group.id'))
#     total_ml = db.Column(db.Integer)
#
#     def __repr__(self):
#         return f"{self.blood_bank_id} has {self.total_ml} ml of {self.blood_group_id}"
#