class Student:
    
    def __init__(self, name: str, age: int, tracks: [], score: float):
        self.name = name
        self.age = age
        self.score = score
        self.tracks = [] 
               
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
            
           

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Rufaydah")
Bob.change_age(12)
Bob.add_track("Project Manager")
Bob.get_score()



