from artiq.experiment import *

class TTL_input(EnvExperiment):
    """
    302 CT PMT Read
    """
    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl2")
        self.setattr_device("ttl13")

    @kernel
    def run(self):
        self.core.reset()
        self.ttl2.input()
        self.ttl13.output()

        # delay(1*us)
        self.core.break_realtime()

        # # self.ttl1.sample_input()
        # # input = self.ttl1.sample_get()
        # # delay(100*us)

        # t_end = self.ttl2.gate_rising(10*ms)
        # t_edge =self.ttl2.timestamp_mu(t_end)
        
        # if t_edge > 0:
        #     at_mu(t_edge)
        #     delay(5*us)
        #     self.ttl13.pulse(5*ms)
        delay(10*ms)
        with parallel:
            cnt = self.ttl2.gate_rising(100*ms)
            num = self.ttl2.count(cnt)
        
        # count = self.ttl2.count(t_end)
        # delay(1000*ms)
        # for i in range(1000):
        #     self.ttl13.on()
        #     delay(5*ms)
        #     self.ttl13.off()
        #     delay(5*ms)
        # print(num)
        # print(t_edge)
        delay(10*ms)
        print(num)
        # print(h)