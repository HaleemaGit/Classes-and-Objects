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


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")

Bob.change_age(34)

Bob.add_track("UI/UX")

Bob.get_score()
