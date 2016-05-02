class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self, p_object):
            if p_object > 0:
                super().append(p_object)
            else:
                raise NonPositiveError()
