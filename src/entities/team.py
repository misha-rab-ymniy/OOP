class Team:
    id: int
    name: str
    image_ig: str
    cc: str

    def __init__(self, id: int, name: str, logo: str, cc: str):
        self.id = id
        self.name = name
        self.image_ig = logo
        self.cc = cc

    def __repr__(self):
        return f'Team(id: {self.id}, name: {self.name}, logo: {self.image_ig})'

    def __str__(self):
        return f'Team(id: {self.id}, name: {self.name}, logo: {self.image_ig})'

    def get_id(self):
        return self.id
