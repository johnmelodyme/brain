import os

from brain.core.NeuronModule import NeuronModule


class Kill_switch(NeuronModule):
    """
    Class used to exit Brain.ai process from system command
    """
    def __init__(self, **kwargs):
        super(Kill_switch, self).__init__(**kwargs)
        os._exit(1)
