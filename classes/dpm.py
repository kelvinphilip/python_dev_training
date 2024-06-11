from enum import Enum

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

class LinkDPM:
    """
    LinkDPM class to apply DPM settings and check link state
    """
    dpmlevels = 0   # Class variable to keep track of DPM levels

    def __init__(self, speed:LinkSpeed, width:LinkWidth, lclkfreq:LCLKFrequency) -> None:
        self.debug = False
        self.speed = speed.name
        self.width = width.name
        self.lclkfreq = lclkfreq.value
        LinkDPM.dpmlevels += 1
    
    def __str__(self) -> str:
        return f'DPM Settings :: Speed={self.speed} :: Width={self.width} :: LCLK Frequency={self.lclkfreq}'

    def apply_dpm(self):
        print(f'Applying DPM settings :: Speed={self.speed} :: Width={self.width}')
        self.set_link_speed(self.speed)
        self.set_link_width(self.width)
        print(f'Switch LCLK Frequency: {self.lclkfreq}')
    
    def check_link_state(self):
        print('Checking link state...')
        currentspeed = self.get_link_speed()
        speedstatus = self.speed == currentspeed
        if not speedstatus:
            print(f'Link is DOWN :: Speed Mismatch :: Expected {self.speed} but got {currentspeed}')
        currentwidth = self.get_link_width()
        widthstatus = self.width == currentwidth
        if not widthstatus:
            print(f'Link is DOWN :: Width Mismatch :: Expected {self.width} but got {currentwidth}')

    def set_link_speed(self, speed):
        print(f'Setting Link Speed to {speed}')
    
    def set_link_width(self, width):
        print(f'Setting Link Width to {width}')

    def get_link_speed(self):
        currentlinkspeed = 'GEN2'
        return currentlinkspeed
    
    def get_link_width(self):
        currentlinkwidth = 'x4'
        return currentlinkwidth
        
# Define the LinkDPM instances
DPM0 = LinkDPM(speed=LinkSpeed.GEN1, width=LinkWidth.x1, lclkfreq=LCLKFrequency.FREQ100MHZ)
print(DPM0)
print(f'Total DPM levels: {LinkDPM.dpmlevels}')

DPM1 = LinkDPM(speed=LinkSpeed.GEN2, width=LinkWidth.x4, lclkfreq=LCLKFrequency.FREQ200MHZ)
print(DPM1)
print(f'Total DPM levels: {LinkDPM.dpmlevels}')

DPM2 = LinkDPM(speed=LinkSpeed.GEN5, width=LinkWidth.x16, lclkfreq=LCLKFrequency.FREQ300MHZ)
print(DPM2)
print(f'Total DPM levels: {LinkDPM.dpmlevels}')

# Apply DPM settings and check link state
DPM0.apply_dpm()
DPM0.check_link_state()
DPM2.apply_dpm()

