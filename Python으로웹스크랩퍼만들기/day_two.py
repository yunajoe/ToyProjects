# 4가지의 함수만들깅 

# 해당되는 요일이 있으면 true, 없으면 false 
def is_on_list(day_list=None, day=""):  # days, 요일
    if day_list is None: 
        day_list = []
        if day in day_list:
            return True
        return False 
    if day in day_list:
        return True
    return False    

# days 리스트에서  인덱스 값을 반환해주는 함수
def get_x(day_list, day_index:int):  # days, days인덱스
    return day_list[3]
    

# list에 요일을 append 해 준다 
def add_x(day_list, day:str):   # days, 요일 
    day_list.append(day)
    return day_list

# list에 요일을 remove 해 준다
# list_name.remove(value)
def remove_x(day_list, day:str):  # days, 요일
    day_list.remove(day) 
    return day_list

# is_on_list 함수
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print("Is Wed on 'days' list?", is_on_list(days, "Wed"))
print("Is xxx on 'days' list?", is_on_list(days, "xxx"))

# get_x 함수 
print("The fourth item in 'days' is:", get_x(days, 3))  

# add_x 함수
add_x(days, "Sat")
print(days)  

# remove 함수 
remove_x(days, "Mon")
print(days)
