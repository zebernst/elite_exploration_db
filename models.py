from peewee import *

db = SqliteDatabase('exploration.db')


class StarSystem(Model):
    name = CharField()
    star_class = CharField()
    pos_x = FloatField()
    pos_y = FloatField()
    pos_z = FloatField()

    class Meta:
        database = db


    def __init__(self, name, star_class=None, coords=None):
        # self.sector = # logic for extracting sector name
        self.name = name
        if star_class:
            self.star_class = star_class
        if coords:
            self.pos_x = coords[0]
            self.pos_y = coords[1]
            self.pos_z = coords[2]

    def __repr__(self):
        # fix with sector and name and coords (?)
        return "StarSystem({})".format(self.name)

    @property
    def pos(self):
        return [self.pos_x, self.pos_y, self.pos_z]


class Body:
    pass

class Star(Body):
    pass

class Planet(Body):
    pass

class Ring:
    pass
