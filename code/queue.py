class DbWriter(object):
    @staticmethod
    def write_to_db(queue):
        raise RuntimeError("Assume this has to communicate with an external DB")

class TheQueue(object):
    def __init__(self, positive_int_only: bool):
        """
        :param positive_int_only: When set to true, the queue should only accept and store positive integers
        """
        pass

    def add(self, number: int):
        """
        Only takes int, if not int, raise custom exception
        :param number:
        """
        pass

    def isempty(self):
        pass

    def pop(self) -> int:
        """
        Return and remove oldest element, raises custom exception when queue is empty

        :return: oldest element in the queue
        """
        pass

    def dump_to_db(self, writer: DbWriter):
        writer.write_to_db(self)
