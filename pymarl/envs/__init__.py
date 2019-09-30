from functools import partial
from .multiagentenv import MultiAgentEnv
import sys
import os

def env_fn(env, **kwargs) -> MultiAgentEnv:
    return env(**kwargs)

REGISTRY = {}
#REGISTRY["sc2"] = partial(env_fn, env=StarCraft2Env)

def register_env(nm, env_class):
    global REGISTRY
    REGISTRY[nm] = partial(env_fn, env=env_class)
