class ReportMixin:
    def __repr__(self, *args, **kwargs):
        return f"Создан объект {self.__class__.__name__} - {self.__dict__}"
