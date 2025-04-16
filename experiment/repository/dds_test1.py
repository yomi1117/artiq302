from artiq.experiment import*
import math

class DDS_TEST(EnvExperiment):
    """ DDS yym
    """
    def build(self):
        self.setattr_device("core")
        self.setattr_device("urukul0_ch0")
        self.setattr_device("urukul0_ch1")
        self.setattr_device("urukul0_ch2")
        self.setattr_device("urukul0_ch3")
        self.setattr_device("urukul1_ch0")
        self.setattr_device("urukul1_ch1")
        self.setattr_device("urukul1_ch2")

        self.setattr_argument("delays", NumberValue(10, precision=0, step=1))
    
    @kernel
    def device_init(self):
        self.core.reset()
        self.urukul0_ch3.cpld.init()
        self.urukul0_ch1.cpld.init()
        self.urukul0_ch2.cpld.init()
        self.urukul0_ch0.cpld.init()
        self.urukul1_ch1.cpld.init()
        self.urukul1_ch2.cpld.init()
        self.urukul1_ch0.cpld.init()

        self.urukul0_ch3.init()
        self.urukul0_ch0.init()
        self.urukul0_ch1.init()
        self.urukul0_ch2.init()
        self.urukul1_ch0.init()
        self.urukul1_ch1.init()
        self.urukul1_ch2.init()

    @kernel
    def run(self):
        self.device_init()

        delay(100*ms)

        attr0_ch0 = 0
        attr0_ch1 = 0
        attr0_ch2 = 0
        attr0_ch3 = 0
        attr1_ch0 = 0
        attr1_ch1 = 0
        attr1_ch2 = 0

        self.urukul0_ch0.set_att((attr0_ch0)*dB)
        self.urukul0_ch1.set_att((attr0_ch1)*dB)
        self.urukul0_ch2.set_att((attr0_ch2)*dB)
        self.urukul0_ch3.set_att((attr0_ch3)*dB)
        self.urukul1_ch0.set_att((attr1_ch0)*dB)
        self.urukul1_ch1.set_att((attr1_ch1)*dB)
        self.urukul1_ch2.set_att((attr1_ch2)*dB)

        freq00 = 180
        freq01 = 185
        freq02 = 188
        freq03 = 184

        amp0_ch0 = 0.4
        amp0_ch1 = 0.4
        amp0_ch2 = 0.4
        amp0_ch3 = 0.4

        phase00 = 0.0 * math.pi
        phase01 = 0.0 * math.pi
        phase02 = 0.0 * math.pi
        phase03 = 0.0 * math.pi

        freq10 = 190
        freq11 = 200
        freq12 = 205

        amp1_ch0 = 0.4
        amp1_ch1 = 0.4
        amp1_ch2 = 0.4

        phase10 = 0.0 * math.pi
        phase11 = 0.0 * math.pi
        phase12 = 0.0 * math.pi

        self.urukul0_ch0.set(frequency=freq00*MHz, phase=phase00, amplitude = amp0_ch0)
        self.urukul0_ch1.set(frequency=freq01*MHz, phase=phase01, amplitude = amp0_ch1)
        self.urukul0_ch2.set(frequency=freq02*MHz, phase=phase02, amplitude = amp0_ch2)
        self.urukul0_ch3.set(frequency=freq03*MHz, phase=phase03, amplitude = amp0_ch3)
        self.urukul1_ch0.set(frequency=freq10*MHz, phase=phase10, amplitude = amp1_ch0)
        self.urukul1_ch1.set(frequency=freq11*MHz, phase=phase11, amplitude = amp1_ch1)
        self.urukul1_ch2.set(frequency=freq12*MHz, phase=phase12, amplitude = amp1_ch2)

        with parallel:
            self.urukul0_ch0.sw.on()
            self.urukul0_ch1.sw.on()
            self.urukul0_ch2.sw.on()
            self.urukul0_ch3.sw.on()
            self.urukul1_ch0.sw.on()
            self.urukul1_ch1.sw.on()
            self.urukul1_ch2.sw.on()

        delay(self.delays*s)

        with parallel:
            self.urukul0_ch0.sw.off()
            self.urukul0_ch1.sw.off()
            self.urukul0_ch2.sw.off()
            self.urukul0_ch3.sw.off()
            self.urukul1_ch0.sw.off()
            self.urukul1_ch1.sw.off()
            self.urukul1_ch2.sw.off()    