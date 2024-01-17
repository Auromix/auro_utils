# Import the profiler
from auro_utils.profilers.profiler import auro_profiler


# Use the profiler as a decorator
@auro_profiler
# Your code here
def your_function_code():
    # Simulate your time-consuming operations
    import time
    time.sleep(2)


# Your Class
class YourClass:
    def __init__(self):
        pass

    @staticmethod
    @auro_profiler
    def your_static_method():
        # Simulate your time-consuming operations
        import time
        time.sleep(1)

    @auro_profiler
    def your_method(self):
        # Simulate your time-consuming operations
        import time
        time.sleep(0.5)


# Example1
your_function_code()
# Example2
your_class = YourClass()
your_class.your_static_method()
# Example3
your_class.your_method()
