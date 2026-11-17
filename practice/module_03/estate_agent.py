class EstateAgent:
    def __init__(self, name, district):
        self.name = name
        self.district = district

    def __repr__(self):
        return f"EstateAgent({self.name!r}, {self.district!r})"

    def __str__(self):
        return f"{self.name}, estate agent in {self.district}"


kim = EstateAgent("Kim", "Majorna")
print("With print:", kim)
print(f"In an f-string: Call {kim}")
print("In a list:", [kim])