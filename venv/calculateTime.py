from orbit import Orbit
from vehicle import Vehicle


class CalculateTime:
    def find_total_time(self, weather, orbit1Speed, orbit2Speed):
        orbitObject = Orbit()
        orbitObject.change_in_crater(weather)
        self.calculate_time_to_cover_crater(weather)
        
    def calculate_time_to_cover_crater(self):
        
