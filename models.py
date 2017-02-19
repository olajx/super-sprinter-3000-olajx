from flaskr.connectdatabase import ConnectDatabase
from peewee import *


class Story(Model):
    story_title = CharField()
    user_story = CharField()
    criteria = CharField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()


    class Meta:
        database = ConnectDatabase.db


