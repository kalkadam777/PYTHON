class Car:
    def __init__(self, model, engine, color) -> None:
        self.model = model
        self.engine = float(engine)
        self.color = color
    
    def __str__(self) -> str:
        return "{} {} {}".format(self.model, self.engine, self.color)