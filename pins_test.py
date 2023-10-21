import gpiod
import sys
import time


LED_CHIP = 'gpiochip0'


LED_LINE_OFFSET = 27


chip = gpiod.chip(LED_CHIP)
port = chip.get_line(LED_LINE_OFFSET)

config = gpiod.line_request()
config.consumer = "Blink"
config.request_type = gpiod.line_request.DIRECTION_OUTPUT

port.request(config)


for _ in range(100):
    port.set_value(0)
    time.sleep(2)
    port.set_value(1)
    time.sleep(2)

def test():    
    for p in range(27):
        port = chip.get_line(p+1)
        config = gpiod.line_request()
        config.consumer = "Test"
        config.request_type = gpiod.line_request.DIRECTION_OUTPUT
        try:
            port.request(config)
            # port.set_value(1)
            print(p+1, port.get_value())
        except (OSError, PermissionError):
            print(f'Port {p+1} busy!')
    
    
"""
['ACTIVE_HIGH', 'ACTIVE_LOW', 'BIAS_AS_IS', 'BIAS_DISABLE', 'BIAS_PULL_DOWN', 
'BIAS_PULL_UP', 'DIRECTION_INPUT', 'DIRECTION_OUTPUT', '__bool__', '__class__', 
'__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'_m_chip', '_m_line', '_throw_if_null', '_throw_if_null_and_get_m_line', 'active_state', 
'bias', 'consumer', 'direction', 'event_get_fd', 'event_read', 'event_wait', 'get_chip', 
'get_value', 'is_open_drain', 'is_open_source', 'is_requested', 'is_used', 'name', 
'offset', 'release', 'request', 'reset', 'set_config', 'set_direction_input', 
'set_direction_output', 'set_flags', 'set_value', 'update']
"""
