from peewee import *

db = SqliteDatabase('exploration.db')

class BaseModel(Model):
    class Meta:
        database = db

class StarSystem(BaseModel):
    name = CharField()
    star_class = CharField()
    pos_x = FloatField()
    pos_y = FloatField()
    pos_z = FloatField()

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


class Body(BaseModel):
    def __init__(self):
        self.name = #
        self.dist_from_arrival = #in ls
        self.semimajoraxis = #
        self.eccentricity = #
        self.orbit_inclination = #
        self.periapsis = #
        self.orbit_period = #


class Star(Body):
    def __init__(self):
        super().__init__()
        self.star_class = #
        self.mass = #in solar masses
        self.radius = #
        self.magnitude = #
        self.rotate_period = #
        self.temp = #
        self.age = #in millions of years


class Planet(Body):
    def __init__(self):
        super().__init__()
        self.tidal_lock = #
        self.terraform_state = #
        self.planet_class = #
        self.atmosphere = #
        self.atmosphere_type = #
        self.atmosphere_comp = #
        self.volcanism = #
        self.gravity = #
        self.temp = #
        self.pressure = #
        self.landable = #
        self.materials = #

class Ring(BaseModel):
    def __init__(self):
        self.name = #
        self.ring_class = #
        self.mass = #in megatons
        self.inner_radius = #
        self.outer_radius = #
        self.reserve_level = #technically a planet attribute but whatever
