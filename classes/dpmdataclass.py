from dataclasses import dataclass, field
from enum import Enum
from typing import List

class LinkSpeed(Enum):
    GEN1 = 1
    GEN2 = 2
    GEN3 = 3
    GEN4 = 4
    GEN5 = 5

class LinkWidth(Enum):
    x1 = 1
    x2 = 2
    x4 = 4
    x8 = 8
    x16 = 16

class LCLKFrequency(Enum):
    FREQ100MHZ = '100MHz'
    FREQ200MHZ = '200MHz'
    FREQ300MHZ = '300MHz'

# Define the DPMLevel class as a dataclass
@dataclass
class LinkDPM:
    speed: LinkSpeed
    width: LinkWidth
    lclkfreq: LCLKFrequency
    speedhistory: List[LinkSpeed] = field(default_factory=list, repr=False)
    debug: bool = field(default=False, repr=False)

    def __post_init__(self):
        self.speedhistory.append(LinkSpeed.GEN1)

    def apply_dpm(self):
        print(f'Applying DPM settings :: Speed={self.speed.name} :: Width={self.width.name}')
        self.set_link_speed(self.speed)
        self.set_link_width(self.width)
        print(f'Switch LCLK Frequency: {self.lclkfreq.value}')
    
    def check_link_state(self):
        print('Checking link state...')
        currentspeed = self.get_link_speed()
        speedstatus = self.speed.name == currentspeed
        if not speedstatus:
            print(f'Link is DOWN :: Speed Mismatch :: Expected {self.speed.name} but got {currentspeed}')
        currentwidth = self.get_link_width()
        widthstatus = self.width.name == currentwidth
        if not widthstatus:
            print(f'Link is DOWN :: Width Mismatch :: Expected {self.width.name} but got {currentwidth}')

    def get_speed_history(self):
        print(self.speedhistory)

    def set_link_speed(self, speed: LinkSpeed):
        self.speedhistory.append(speed)
        print(f'Setting Link Speed to {speed.name}')
    
    def set_link_width(self, width:LinkWidth):
        print(f'Setting Link Width to {width.name}')

    def get_link_speed(self):
        currentlinkspeed = 'GEN2'
        return currentlinkspeed
    
    def get_link_width(self):
        currentlinkwidth = 'x4'
        return currentlinkwidth
    
# Define the LinkDPM instances
DPM0 = LinkDPM(speed=LinkSpeed.GEN1, width=LinkWidth.x1, lclkfreq=LCLKFrequency.FREQ100MHZ)
print(DPM0)

DPM1 = LinkDPM(speed=LinkSpeed.GEN2, width=LinkWidth.x4, lclkfreq=LCLKFrequency.FREQ200MHZ)
print(DPM1)

DPM2 = LinkDPM(speed=LinkSpeed.GEN5, width=LinkWidth.x16, lclkfreq=LCLKFrequency.FREQ300MHZ)
print(DPM2)

# Apply DPM settings and check link state
DPM0.apply_dpm()
DPM0.check_link_state()
DPM2.apply_dpm()
DPM2.get_speed_history()