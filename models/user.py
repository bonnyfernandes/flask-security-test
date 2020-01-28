from mongoengine import Document, StringField, ListField, ReferenceField
from flask_security import RoleMixin, UserMixin


class Role(Document, RoleMixin):
    name = StringField(unique=True, required=True)


class User(Document, UserMixin):
    publicId = StringField(required=True, unique=True)
    name = StringField(required=True, unique=True)
    roles = ListField(ReferenceField(Role))
