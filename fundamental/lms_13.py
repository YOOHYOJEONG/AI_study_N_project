# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:27:06 2021

@author: user
"""

myvar = 3
myvar = 'cat'

myword = 'cat'
myword.upper()

var = 4

print(id(var), id(4))

mylist = [1,2,3]
var = mylist


mylist.append(4)
print(mylist)
print(var)

# print(id(mylist), id(var))


#얕은 복사 : copy.copy() -> 원복 객체의 주소 복사
#깊은 복사 : copy.deepcopy()  -> 원본 객체의 값 복사

#%%

class Car : 
    pass

class Car() :
    pass

#id(Car)는 여러번 호출해도 같은 값
print(id(Car))
print(id(Car))

#id(car())는 Car()가 호출될 때 마다 다른 값
print(id(Car()))
print(id(Car()))

#두 객체의 type
print(type(Car))
print(type(Car()))


#인스턴스화
mycar = Car()
mycar2 = Car()
print(id(mycar))
print(id(mycar2))

#클래스 표기법
#카멜케이스 : 각 단어 앞 글자를 대문자로 쓸 것
#함수명 표기법
#스네이크케이스 : 단어는 소문자, 각 단어 연결은 언더바 사용
#함수명은 동사로 명명

#%%

# Car 클래스입니다.
class Car:
    '''
    속성은 클래스의 상태를 나타냅니다.
    색상: 빨강
    종류: 스포츠 카
    '''
    color = 'red'
    category = 'sports car'
		
    '''
    동작은 메서드로 나타냅니다.
    '''
    def drive(self):
    
    #주행 메서드
    
        print("I'm driving")
				
    def accel(self, speed_up, current_speed=10):
    
    # 가속 메서드
    # :param speed_up: 현재속도
    # :param current_speed: 가속
    # :type speed_up: string
    # :type current_speed: string
    
        self.speed_up = speed_up
        self.current_speed = current_speed + speed_up
        print("speed up", self.speed_up, "driving at", self.current_speed)

mycar = Car()
print(mycar.color)

#mycar.dirve() 코드는 인터프리터 내부에서는 Car.drive(mycar)로 동작함.
mycar.drive()

mycar.accel(5)

#%%

#self 인자를 사용하지 않으면 에러가 발생
class Test:
    def run1(self):
        print("run1")

    def run2():
        print("run2")

t = Test()

t.run1()

#%%

#인스턴스의 속성으로 사용하고 싶은 변수는 self.을 써줌.
#self 인자를 통해 선언된 객체의 값이란 의미

class Test2:
    def run1(self, a):
        self.a = float(a) * 10
        print(self.a)

    def run2(self, b):
        b = float(b) + 10   #self.을 사용해야 함
        print(self.b)
        
t = Test2()

t.run1(1)

#%%

#Car 클래스를 만들 때부터 색깔과 카테고리를 지정해 주고 싶다면
#__init__ 을 사용

#__init__ 메소드안에 인자를 전달함으로써 인스턴스 객체의 속성을 초기화할 수 있음.
#__init__ 메소드안에 정의된 속성(변수) color와 category는 클래스를 인스턴스화할 때 값을 설정할 수 있음.
#이걸 인스턴스 객체의 초기화(initializing instance)라고 함.
#__init__함수는 생성자(constructor)
#__init__ 역시 def 키워드로 정의함. 클래스 안의 메소드이므로 self 문법이 가장 중요

class Car:
    color = 'red'
    category = 'sports car'

    def drive(self):
        print("I'm driving")

    def accel(self, speed_up, current_speed=10):
        self.speed_up = speed_up
        self.current_speed = current_speed + self.speed_up
        print("speed up", self.speed_up, "driving at", self.current_speed)

class Car2:
    def __init__(self, color, category):
        self.color = color
        self.category = category

    def drive(self):
        print("I'm driving")

    def accel(self, speed_up, current_speed=10):
        self.speed_up = speed_up
        self.current_speed = current_speed + self.speed_up
        print("speed up", self.speed_up, "driving at", self.current_speed)

#인스턴스 객체 선언
car1 = Car()
car2 = Car2('yellow', 'sedan')

print(car1.color)

print(car2.color )

print(car1.category)

print(car2.category)


#%%
#키워드 인자를 지정할 수도 있음.

class Car2:
    def __init__(self, color='red', category='sprots car'):
        self.color = color
        self.category = category
        
print(car2.color )
print(car2.category)

#%%
#클래스 내 변수 선언

#보통 변수와 동일하게 변수명을 쓰고 값을 할당
# __init__ 메소드 안에 self.와 함께 설정

class Car:
    Manufacture = "India"

    def __init__(self, color, category='sedan'):
        self.color = color
        self.category = category
        
#Manufacture 같은 변수를 클래스 변수
#self.color와 같은 변수를 인스턴스 변수

car1 = Car('red','sports car')
car2 = Car('white')
print(car1.Manufacture, car1.color, car1.category)
print(car2.Manufacture, car2.color, car2.category)

#클래스에 바로 선언된 속성을 클래스 변수라고 함.
#클래스에 의해 생성된 모든 객체에서 같은 값을 조회할 때 가능 (????)

#Manufacture는 클래스 변수
#Manufacture 속성은 car1과 car2가 공유

#__init__() 안에서 self를 사용해 선언된 변수는 인스턴스 변수
#color와 category는 인스턴스 변수
#color와 category 속성은 car1과 car2가 공유하지 않음

#%%
#클래스 상속

class Car:
    Manufacture = "India"

    def __init__(self, color='red', category='sedan'):
        self.color = color
        self.category = category

    def drive(self):
        print("I'm driving")

    def accel(self, speed_up, current_speed=10):
        self.speed_up = speed_up
        self.current_speed = current_speed + self.speed_up
        print("speed up", self.speed_up, "driving at", self.current_speed)

class NewCar(Car):
    pass

car = NewCar()
car.drive()
car.accel(10)


class NewCar(Car):
    maker = 'Porsche'

car = NewCar()
print(car.maker)


#상속받은 클래스 : 자식 클래스, 서브 클래스(sub class), 파생된 클래스(derived class)
#기존 클래스 : 부모 클래스, 슈퍼 클래스(super class), 베이스 클래스(base class)

#%%

#메소드 추가
class NewCar(Car):
    def fly(self):
        print("I'm flying!! This is the new car!!")
#%%
        
#메소드 오버라이드(재정의)
class NewCar(Car):
    def fly(self):
        print("I'm flying!! This is the new car!!")

    def drive(self):
        print("I'm driving and can fly")

#fly() : 메소드 추가
#drive() : 메소드 재정의

#%%
#부모 메서드 호출 : super()
class NewCar(Car):
    def __init__(self, color, category, maker):
        super().__init__(color, category)
        self.maker = maker

    def fly(self):
        print("I'm flying!! This is the new car!!")

    def accel(self, speed_up, level=1, current_speed=10):
        self.boost[level] = {1 : 0, 2 : 30, 3 : 50}
        self.speed_up = speed_up + self.boost[level]
        self.current_speed = current_speed + self.speed_up
        print("speed up", self.speed_up, "driving at", self.current_speed)


class Car:
    Manufacture = "India"

    def __init__(self, color='red', category='sedan'):
        self.color = color 
        self.category = '2020Y '+ category


class NewCar(Car):
    def __init__(self, color, category, maker):
        super().__init__(color, category)
        self.maker = maker

newcar = NewCar('red','sports car', 'Kia')
print(newcar.category)


#%%

#주사위 만들기

class FunnyDice:
    def __init__(self, n=6):
        self.n = int(n)
        self.numbers = list(range(1, n+1))
        self.index = randrange(0, self.n)
        self.val = self.numbers[self.index]

    def throw(self):
        self.index = randrange(0, self.n)
        self.val = self.numbers[self.index]
    
    def getval(self):
        return self.val        

    def setval(self, val:int):
        if val <= self.n:
            self.val = val
        else:
            msg = "주사위에 없는 숫자입니다. 주사위는 1 ~ {0}까지 있습니다. ".format(self.n)
            raise ValueError(msg)    

from random import randrange

def get_inputs():
    n = int(input("주사위 면의 개수를 입력하세요: "))
    return n

def main() :
    n = get_inputs()
    mydice = FunnyDice(n)
    mydice.throw()
    print("lucky number : {}".format(mydice.getval()))
    
  
if __name__ == '__main__' :
    main()