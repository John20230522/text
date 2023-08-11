class Cars:
    # 建構式
    def __init__(self, color, seat):
        self.color = color  # 物件屬性
        self.seat = seat
        self.weight = 140
        
mazda = Cars("blue", 4)
mazda.color = "yellow"
mazda.seat = 8
mazda.weight = 200

toyota = Cars("red", 6)
print("mazda color: ", mazda.color)
print("mazda seat: ", mazda.seat)
print("mazda weight: ", mazda.weight)
print("toyota color: ", toyota.color)
print("toyota seat: ", toyota.seat)
print("toyota weight: ", toyota.weight)

#%%
class Cars:
    doors = 4 # 類別屬性  共用
    # 建構式
    def __init__(self, color, seat):
        self.color = color
        self.seat = seat
        self.weight = 140
     
mazda = Cars("blue", 4)
toyota = Cars("red", 6)

print("mazda original door: ", mazda.doors)
print("toyota original door: ", toyota.doors)

Cars.doors = 6
print("mazda new door: ", mazda.doors)
print("toyota new door: ", toyota.doors)

#%%  
class Cars:
    def __init__(self):
        self.color = "blue"
        
    def drive(self):
        print(f"{self} is {self.color}.")
        self.message()
    
    def message(self):
        print("Message method is called.")
        
mazda = Cars()
mazda.drive

#%%
class Cars:
    def __init__(self):
        self.color = "blue"
        
    def drive(self):  
        print(f"{self} is {self.color}.")

Cars.drive()  # 沒建立 obj error
#%%
class Cars:
    door = 4
    
    def drive(self):
        self.__class__.door = 5  # 修改類別屬性
    
print("Cars original door:", Cars.door)
    
mazda = Cars()
mazda.drive()

print("Cars new door:", Cars.door)

#%%
class Cars:
    door = 4
    
    @classmethod
    def open_door(cls):
        print(f"{cls} has {cls.door} doors")
        
mazda = Cars()     # 建立 obj
mazda.open_door()  # obj 呼叫

Cars.open_door()   # class 呼叫
#%%
class Cars:
    # 建構式
    def __init__(self, color, seat):
        self.color = color  # 物件屬性
        self.seat = seat
    
    @classmethod 
    def van(cls):
        return cls(6, "black")
    
    @classmethod 
    def sport_cars(cls):
        return cls(4, "yellow")

# 不需建立 obj 即可呼叫 因有 @
van = Cars.van()
sport_car = Cars.sport_cars()
#%%  static 沒 self cls 等參數
class Cars:
    @staticmethod   # 可用類別呼叫方法 可以不需建立 obj
    def speed_rate(distance, minute):
        return distance / minute

van = Cars()
van_rate = van.speed_rate(10000, 20)
print("van rate: ", van_rate)

sport_car_rate = Cars.speed_rate(20000, 20)
print("sport car rate: ", sport_car_rate)

#%%
def myDeco(x):
    def run():
        print("裝飾器的程式碼")
        x(3)   # 裝飾的普通函式
    return run

# 使用裝飾器
@myDeco
def test(n):
    print("普通函式的程式碼", n)

test()
#%%  1+2+..+50 = 1275
def calculate(callback):
    def run():
        result = 0
        for n in range(51):
            result += n
        callback(result)  
    return run   # 回傳執行下面的函式並傳入參數繼續後續執行

@calculate
def showChinese(n):
    print("計算結果為:", n)
@calculate    
def showEnglish(n):
    print("Result is:", n)
    
showChinese()  # 不須先帶參數 
showEnglish()
    
