''' SolarOOMDPStateClass.py: Contains the SolarOOMDPState class. '''

# Local libs.
from simple_rl.mdp.oomdp.OOMDPStateClass import OOMDPState

class SolarOOMDPState(OOMDPState):
    ''' Class for Solar Panel States '''

    def __init__(self, objects):
        OOMDPState.__init__(self, objects=objects)

    def get_month(self):
        return self.objects["time"][0]["month"] * 1

    def get_day(self):
        return self.objects["time"][0]["day"] * 1

    def get_hour(self):
        return self.objects["time"][0]["hour"] * 1

    def get_minute(self):
        return self.objects["time"][0]["minute"] * 1

    def get_sun_angle_AZ(self):
        return self.objects["sun"][0]["angle_AZ"] * 1

    def get_sun_angle_ALT(self):
        return self.objects["sun"][0]["angle_ALT"] * 1

    def get_panel_angle_AZ(self):
        return self.objects["agent"][0]["angle_AZ"] * 1

    def get_panel_angle_ALT(self):
        return self.objects["agent"][0]["angle_ALT"] * 1