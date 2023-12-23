import logging


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class ProxyObject:

    def __init__(self, retrieval_function: callable, **kwargs):
        """
        Represents the output of a function retrieval_function(**kwargs) as a standalone object.
        In other words, this class poses as a dynamic proxy to an object.

        Logging is used in this module.

        :param retrieval_function: the function will be called on every get and set off an attribute
        :param kwargs: will be passed to the retrieval_function
        """
        self.object_retrieval_function: callable = retrieval_function
        self.retrieval_kwargs: dict = kwargs
        logger.debug(
            f"ProxyObject {id(self)} initialized with retrieval function {retrieval_function} and kwargs {kwargs}")

    def __getattribute__(self, item):
        try:
            if item != "object_retrieval_function" and item != "retrieval_kwargs" and item != "extended_logging":
                po = self.object_retrieval_function(**self.retrieval_kwargs)
                if po is None:
                    logger.warning(
                        f"ProxyObject {id(self)} retrieved object is None when trying to get attribute '{item}'")
                    return None
                return getattr(po, item)
            return super().__getattribute__(item)
        except Exception as e:
            logger.error(f"ProxyObject {id(self)} encountered an error when getting attribute '{item}': {e}")
            raise e

    def __setattr__(self, name, value):
        try:
            if name != "object_retrieval_function" and name != "retrieval_kwargs" and name != "extended_logging":
                setattr(self.object_retrieval_function(**self.retrieval_kwargs), name, value)
            else:
                super().__setattr__(name, value)
        except Exception as e:
            logger.error(f"ProxyObject {id(self)} encountered an error when setting attribute '{name}': {e}")
            raise e

    def __del__(self):
        try:
            logger.debug(f"ProxyObject {id(self)} destroyed")
        except Exception as e:
            logger.error(f"ProxyObject {id(self)} encountered an error when destroying: {e}")
            raise e
