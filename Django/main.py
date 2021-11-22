class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def start(self):
    print(self.doors)
    print("I started")


porche = Car()
porche.color = "Red Yellow Red"
porche.start()


# class 안에 있으면 method, class 밖에 있으면 function
# method에 첫번째 인자는 method를 호출하는 instance 자신