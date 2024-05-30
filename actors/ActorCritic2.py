import torch
import torch.nn as nn
from modules.VanillaCNN2 import VanillaCNNQFunction2
from actors.BaseActor2 import MyActorModule2
from modules.VanillaCNN2 import VanillaCNN2

class VanillaCNNActorCritic2(nn.Module):
    """
    Actor-critic module for the SAC algorithm.
    """
    def __init__(self, observation_space, action_space):
        super().__init__()

        # Policy network (actor):
        self.actor = MyActorModule2(observation_space, action_space)
        # Value networks (critics):
        self.q = VanillaCNNQFunction2(observation_space, action_space)
