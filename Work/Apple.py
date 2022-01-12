class Apple():
    def __init__(self,name,diametr,high,weigh,color):
        #Иниалиазиция атрибутов: наименование, диаметр фрукта, его высота, вес и цвет
        self.name = name
        self.diametr = diametr
        self.high = high
        self.weigh = weigh
        self.color = color

    def cut(self):
        #Нарезать
        print("Яблоко", self.name + " нарезали")

    def drop(self):
        #Выбросить
        print("Яблоко", self.name + " выбросили")
        
    def slicing(self):
        #Тонко нарезать
        print("Яблоко", self.name + " тонко нарезали")

    def squeezeout(self):
        #Выжать
        print("Из яблока", self.name + " выжали сок")
        
    def cook(self):
        #Приготовить(варить)
        print("Яблоко", self.name + " приготовили")

    def dryout(self):
        #Высушить
        print("Яблоко", self.name  +  " высушили")
        
    def sugared(self):
        #Засахарить
        print("Яблоко", self.name + " засахарили")
        
class Smallapple(Apple):
    def sqr(self):
        #Рассчёт калорийности продукта: вес продукта* каллрийность продукта 100г (52) и деленое на 100
        return((self.weigh * 52)/100)
apple = Apple("Карамелька",100,300,300,"Красный")
apple_2 = Smallapple("Карамелька",100,300,300,"Красный")

print("Наименование:",apple.name)
print("Диаметр:",apple.diametr,"мм.")
print("Высота:",apple.high,"мм.")
print("Вес:",apple.weigh,"г.")
print("Цвет:",apple.color)
print("Калорийность яблока:",apple_2.sqr(),"ккал.")
apple.squeezeout()
#Пример полиморфизма:
a=2+2
b= "2"+ "2"
print(a)
print(b)
