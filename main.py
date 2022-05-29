class Student:

    # [assignment] Skeleton class. Add your code here

    def __init__(self, name: str, age: int, tracks: [], score: float):

        self.name = name
        self.age = age
        self.score = score
        self.tracks = tracks
        
        

    def change_name(self, name: str):
        self.name = name
        print(self.name)

    def change_age(self, age: int):
        self.age = age
        print(self.age)

    def add_track(self, track:str):
        self.tracks.append(track)
        print(self.tracks)

    def get_score(self):
        print(self.score)


# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Bob = Student(name=input("enter your name: "), age=input("enter your age: "), tracks=[], 
              score=input("enter your score: "))
print("Here are the details you just entered: ", "name:", Bob.name,";"  " age:", Bob.age,";"  " tracks: ", Bob.tracks,";"  " score: ", Bob.score )


answer = input("Do you want to add a track to your profile now? (yes or no)")

while True:
    if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
        Bob.add_track(track = input("Add a new track here: "))
        print("Do you want to change your name?")
        answer = input("(yes or no):")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            Bob.change_name(name = input("Input your new name here: "))
            
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            pass
        print("Do you want to change your age?")
        answer = input("(yes or no):")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            Bob.change_age(age = input("Input your new age here: "))
            
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            pass
        print("Do you want to check your score?:")
        answer = input("(yes or no):")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            Bob.get_score()
            pass
            
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            pass
               
        
            
    elif any(answer.lower() == f for f in ['no', 'n', '0']):
        print("Do you want to change your name?")
        answer = input("(yes or no):")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            Bob.change_name(name = input("Input your new name here: "))
            
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            pass
        print("Do you want to change your age?")
        answer = input("(yes or no):")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            Bob.change_age(age = input("Input your new age here: "))
            
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            pass
        print("Do you want to check your score?:")
        answer = input("(yes or no):")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            Bob.get_score()
            
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            pass       
    else:
        print('Please enter yes or no')
        answer = input("Do you want to add a track to your profile now? (yes or no)")
        continue

    print("Here are the details you just edited: ", "name:", Bob.name,";"  " age:", Bob.age,";"  " tracks: ", Bob.tracks,";"  " score: ", Bob.score ) 


# Expected methods
Bob.change_name("Peter")

Bob.change_age(34)

Bob.add_track("UI/UX")

Bob.get_score()
