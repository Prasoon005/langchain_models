from typing import TypedDict

class person(TypedDict):
    name:str 
    age:int


new_person:person={
    'name': 'Prasoon' ,
    'age' : 'Twenty' # u can also write 20  #it will not throw any error even if u write string in place of int  , it doesnot validate the typechecking 
                       #it only suggests 
    }

print(new_person)