# ProxyObject

The ProxyObject class is designed to act as a dynamic proxy to an object, representing the output of a specified retrieval function as a standalone object. It allows for seamless interaction with the underlying object by forwarding attribute accesses, modifications, and deletions.

## Example Usage

```python

import logging
from ProxyObject import ProxyObject

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class RealClass:
    def __init__(self, *args, **kwargs):
        pass

    def a(self, b):
        print(b)

class Dummy(ProxyObject):
    def __init__(self, *args, **kwargs):
        """
        A dummy object with no real implementation
        """
        super().__init__(*args, **kwargs)

    def a(self, b):
        ...

real = RealClass()

def retrieval_function(*args, **kwargs):
    print(args, kwargs)
    return real

e = Dummy(retrieval_function=retrieval_function, id=1)
e.a(1)
```
