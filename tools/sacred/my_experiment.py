from tools.sacred.h01_hello_world import ex as ex1
from tools.sacred.hello_config import ex as ex2

r = ex1.run()
r = ex2.run()
r = ex2.run(config_updates=dict(recipient="guys"))
