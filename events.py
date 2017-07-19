import dateutil.parser
import models

class JournalEvent:
    def __init__(self, event):
        self.timestamp = dateutil.parser.parse(event.get('timestamp'))


####
# child classes
####

class EventFSDJump(JournalEvent):
    def __init__(self, event):
        super().__init__(event)
        self.jump_dist = event.get('JumpDist')
        self.star_system = models.StarSystem(event.get('StarSystem'), event.get('StarPos')) # LINK TO EVENTSTARTJUMP
        self.fuel_used = event.get('FuelUsed')  
        self.fuel_level = event.get('FuelLevel')
        self.boost_used = event.get('BoostUsed')

    def __repr__(self):
        return 'EventFSDJump(dist={}, to={})'.format(self.jump_dist, self.star_system)


class EventStartJump(JournalEvent):
    def __init__(self, event):
        super().__init__(event)
        self.jump_type = event.get("JumpType")
        self.star_class = event.get("StarClass")
        self.star_system = models.StarSystem(event.get('StarSystem'), self.star_class) # LINK TO EVENTFSDJUMP

class EventScan(JournalEvent):
    def __init__(self, event):
        pass
