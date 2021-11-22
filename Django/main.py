class Car():

  def __init__(self, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black")
    self.price = kwargs.get("price", "$20")

  def __str__(self):
    return f"Car with {self.wheels} wheels"

porche=Car(color="green", price="$40")
print(porche.color, porche.price)


mini = Car()
print(mini.color, mini.price)

# class 안에 있으면 method, class 밖에 있으면 function
# method에 첫번째 인자는 method를 호출하는 instance 자신