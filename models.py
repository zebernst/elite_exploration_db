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
    def __init__(self, data : dict):
        self.name = data.get('BodyName')
        self.dist_from_arrival = data.get('DistanceFromArrivalLS') #in ls
        self.semimajoraxis = data.get('SemiMajorAxis')
        self.eccentricity = data.get('Eccentricity')
        self.orbit_inclination = data.get('OrbitalInclination')
        self.periapsis = data.get('Periapsis')
        self.orbit_period = data.get('OrbitalPeriod')


class Star(Body):
    def __init__(self, data : dict):
        super().__init__(data)
        self.star_class = data.get('StarType')
        self.mass = data.get('StellarMass') #in solar masses
        self.radius = data.get('Radius')
        self.magnitude = data.get('AbsoluteMagnitude')
        self.rotate_period = data.get('RotationPeriod') #in seconds
        self.temp = data.get('SurfaceTemperature')
        self.age = data.get('Age_MY') #in millions of years


class Planet(Body):

    CLASSES = {
        "metal rich body":                      1,
        "high metal content body":              2,
        "rocky body":                           3,
        "icy body":                             4,
        "rocky ice body":                       5,
        "earthlike body":                       6,
        "water world":                          7,
        "ammonia world":                        8,
        "water giant":                          9,
        "water giant with life":                10,
        "gas giant with water based life":      11,
        "gas giant with ammonia based life":    12,
        "sudarsky class i gas giant":           13,
        "sudarsky class ii gas giant":          14,
        "sudarsky class iii gas giant":         15,
        "sudarsky class iv gas giant":          16,
        "sudarsky class v gas giant":           17,
        "helium rich gas giant":                18,
        "helium gas giant":                     19 }
    TERRAFORM_STATES = {
        'Null': 0,
        'Terraformable': 1,
        'Terraforming':  2,
        'Terraformed':   3 }
    ATMOSPHERES = {}
    VOLCANISM_TYPES = {}

    def __init__(self, data : dict):
        super().__init__(data)
        self.tidal_lock = data.get('TidalLock')
        self.terraform_state = self.TERRAFORM_STATES.get(data.get('TerraformState'))
        self.planet_class = self.CLASSES.get(data.get('PlanetClass'))
        self.atmosphere = data.get('Atmosphere') # TODO
        self.atmosphere_type = data.get('AtmosphereType') # TODO
        self.atmosphere_comp = data.get('AtmosphereComposition') # TODO
        self.volcanism = data.get('Volcanism') # TODO
        self.gravity = data.get('SurfaceGravity')
        self.temp = data.get('SurfaceTemperature')
        self.pressure = data.get('SurfacePressure')
        self.landable = data.get('Landable')
        self.materials = data.get('Materials') # TODO
        self.mass = data.get('MassEM') # in earth masses
        self.radius = data.get('Radius') #
        # TODO: change get() to pop() and print remainder of dict to make sure im storing everything

class Ring(BaseModel):

    RESERVE_LEVELS = {
        "PristineResources": 0,
        "MajorResources": 1,
        "CommonResources": 2,
        "LowResources": 3,
        "DepletedResources": 4 }

    def __init__(self, data : dict, reserves):
        self.name = data.get('Name')
        self.ring_class = data.get('RingClass')
        self.mass = data.get('MassMT') #in megatons
        self.inner_radius = data.get('InnerRad')
        self.outer_radius = data.get('OuterRad')
        self.reserve_level = RESERVE_LEVELS.get(reserves)

class MaterialRecord(BaseModel):

    MATERIALS = [
        'antimony',
        'arsenic',
        'cadmium',
        'carbon',
        'chromium',
        'germanium',
        'iron',
        'manganese',
        'mercury',
        'molybdenum',
        'nickel',
        'niobium',
        'phosphorus',
        'polonium',
        'ruthenium',
        'selenium',
        'sulphur',
        'technetium',
        'tellurium',
        'tin',
        'tungsten',
        'vanadium',
        'yttrium',
        'zinc',
        'zirconium' ]
    
    def __init__(self, data : list):

        for material in data:
            # for dict in list of dicts
            setattr(self, material.get('Name'), material.get('Percent'))

        for material in self.MATERIALS:
            if not hasattr(self, material):
                setattr(self, material, None)
