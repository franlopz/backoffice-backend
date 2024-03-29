from peewee import *
from .Base import BaseModel

class State(BaseModel):
    id = IntegerField()
    name = CharField(max_length=255)

    class Meta:
        db_table = 'states'