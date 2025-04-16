from artiq.experiment import*
import math

class DDS_TEST(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("urukul0_ch0")
        self.setattr_device("urukul0_ch1") 
        self.setattr_device("urukul0_ch2") 
        self.setattr_device("urukul0_ch3")
        self.setattr_device("urukul1_ch0")                   
        self.setattr_device("urukul1_ch1") 
        self.setattr_device("urukul1_ch2") 
        self.setattr_device("urukul1_ch3")

    @kernel
    def run(self):
        self.core.reset()
        self.urukul0_ch0.cpld.init()
        self.urukul0_ch0.init()

        delay(100*ms)

        attr0_ch0 = 0
        self.urukul0_ch0.set_att((attr0_ch0)*dB)

        freq00 = 180
        amp0_ch0 = 0.4
        phase00 = 0.0 * math.pi

        self.urukul0_ch0.set(frequency=freq00*MHz, phase=phase00, amplitude = amp0_ch0)

        self.urukul0_ch0.sw.on()

        delay(10000*ms)

        self.urukul0_ch0.sw.off()