from artiq.experiment import *

class TTL_Output(EnvExperiment):
    """ttl all channel out"""
    def build(self):
        self.setattr_device("core")
        # 注册 4 - 15 通道
        self.ttl_devices = [self.get_device(f"ttl{i}") for i in range(4, 16)]

    @kernel
    def run(self):
        self.core.reset()
        # 设置所有通道为输出模式
        for ttl in self.ttl_devices:
            ttl.output()

        for i in range(40000):
            # 0
            with parallel:
                for ttl in self.ttl_devices:
                    ttl.off()
                delay(50 * us)
            # 7
            with parallel:
                for ttl in self.ttl_devices:
                    ttl.on()
                delay(50 * us)
            # 1
            with parallel:
                for ttl in self.ttl_devices:
                    ttl.off()
                delay(50 * us)
            # 6
            with parallel:
                for ttl in self.ttl_devices[:-1]:
                    ttl.off()
                self.ttl_devices[-1].on()
                delay(50 * us)
            # 2
            with parallel:
                self.ttl_devices[0].on()
                for ttl in self.ttl_devices[1:]:
                    ttl.off()
                delay(50 * us)
            # 5
            with parallel:
                for ttl in self.ttl_devices:
                    ttl.on()
                delay(50 * us)
            # 3
            with parallel:
                self.ttl_devices[0].off()
                self.ttl_devices[1].on()
                for ttl in self.ttl_devices[2:]:
                    ttl.off()
                delay(50 * us)
            # 4
            with parallel:
                self.ttl_devices[0].on()
                self.ttl_devices[1].off()
                self.ttl_devices[2].on()
                for ttl in self.ttl_devices[3:]:
                    ttl.off()
                delay(50 * us)
    