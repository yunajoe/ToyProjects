
''' 
print(type(dict))  # <class 'type'>
print(dict)   # <class 'dict'>         
my_english_dict = {}
print(type(my_english_dict))    # <class 'dict'> 

'''  

import os 
os.system('clear')

# 딕션너리에 값을 넣는 함수 
def add_to_dict(dic, word="", desc=""):  
    # word:str, desc:str 이면은 안된당.. 왜죵
    if type(dic) == dict:  # dic이 dictionary 타입이면은! 
        if word == "" or desc == "": # word 나 desc 가 한개라도 없으면은!
            print("You need to send a word and a definition")
        else:  #word, desc 둘다 있을때 
            if word not in dic:
                dic[word] = desc
                print(f"{word} has been added")
            else:
                print(f"{word} is  already on the dictionary. Won't add.")             
    else:
        print(f"You need to send a dictionary. You sent: {type(dic)}")     
 
        
my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


# 딕셔너리에서값을 꺼내오는 함수 

def get_from_dict(dic, word=""):
    if type(dic) == dict:
        if word != "":
            if word not in dic:
                print(f"{word} was not found in this dic")                
            else:
                print(f"{word} 의 의미는 {dic[word]}")
        else:
            print("You need to send a word to search for.")
    else:
        print(f"You need to send a dictionary. You sent: {type(dic)}")
            
print("---------------- get_from_dictionary 함수 ------------------")

print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")


print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)


print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")



def update_word(dic, word="",desc=""):
    if type(dic) == dict:
        if word == "" or desc == "":   
            print(f"You need to send a word and a definition to update")             
        else:
            if word in dic:
                dic[word] = desc
                print(f"{word} has beetn updated to: {dic[word]}")
            else:
                print(f"{word} is not on the dict. Can't update non-existing word.")
    else:
        print(f"You need to send a dictionary. You sent {type(dic)}")
        
             
print("---------------- update_from_dictionary 함수 ------------------")
       
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")


print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")


print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("---------------- delete_from_dictionary 함수 ------------------")

def delete_from_dict(dic, word):
    if type(dic) == dict:
        if word not in dic:
            print(f"{word}  is not in this dict. Won't delete.")             
        else:
            del dic[word]
            print(f"{word} has been deleted.")         
    else:
        print("You need to specify a word to delete.")
        
        
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")


print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")