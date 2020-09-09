from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import UserMixin, current_user, logout_user
from flask import redirect
from app import db, admin

#thuvien
class Loaisach(db.Model):
    __tablename__ = "loaisach"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenloai = Column(String(50), nullable=False)
    sach = relationship('Sach', backref = "loaisach", lazy = True)

    def __str__(self):
        return self.tenloai

class Sach(db.Model):
    __tablename__ = "sach"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tensach = Column(String(70), nullable=False)
    gia = Column(Float, default=0)
    soluong = Column(Integer, default=0)
    img = Column(String(255), nullable=True)
    loaisach_id = Column(Integer, ForeignKey(Loaisach.id), nullable=False)

    def __str__(self):
        return self.tensach

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    #Khachhang_id = Column(Integer, ForeignKey(Khachhang.id), nullable=False)

    def __str__(self):
        return self.name

class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated

admin.add_view(AuthenticatedView(Loaisach, db.session))
admin.add_view(AuthenticatedView(Sach, db.session))
admin.add_view(LogoutView(name="Logout"))

if __name__ == "__main__":
    db.create_all()