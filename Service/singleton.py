class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        #проверяем, существует ли уже экземпляр класса
        if cls not in cls._instances:
            #если экземпляра нет, создаем его и сохраняем в словаре
            cls._instances[cls] = super().__call__(*args, **kwargs)
        #возвращаем существующий экземпляр
        return cls._instances[cls]