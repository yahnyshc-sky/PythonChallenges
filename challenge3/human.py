class Human:
    def __init__(self, first_name, last_name, belongings, age, height, weight, coding_languages, is_alive = True): #Default parameter is_alive = True
        self.name = (first_name, last_name)
        self.is_alive = is_alive
        self.belongings = belongings
        self.measurements = {
            'age': age,
            'height': height,
            'weight': weight,
        }
        self.coding_languages = coding_languages

    # Getters

    def get_name(self) -> tuple:
        return self.name

    def get_age(self) -> int:
        return self.measurements['age']

    def get_height(self) -> int:
        return self.measurements['height']

    def get_weight(self) -> float:
        return self.measurements['weight']

    def get_coding_languages(self) -> set:
        return self.coding_languages

    def get_belongings(self) -> list:
        return self.belongings
    
    def is_human_alive(self) -> bool:
        return self.is_alive
    
    # Setters 
    
    def set_name(self, first_name: str, last_name: str) -> None:
        self.name = (first_name, last_name)
    
    def set_age(self, age: int) -> None:
        self.measurements['age'] = age
    
    def set_height(self, height: int) -> None:
        self.measurements['height'] = height
    
    def set_weight(self, weight: float) -> None:
        self.measurements['weight'] = weight
    
    def set_coding_languages(self, coding_languages: set) -> None:
        self.coding_languages = coding_languages
    
    def set_belongings(self, belongings: list) -> None:
        self.belongings = belongings

    def human_status(self) -> str:
        return "Alive" if self.is_alive else "Deceased"

    def kill_human(self) -> None:
        self.is_alive = False
        return f"{self.name[0]} {self.name[1]} aka. the \U0001F410 has been killed."