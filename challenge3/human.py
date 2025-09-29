class Human:
    def __init__(self, 
                 first_name: str = "Ranya", 
                 last_name: str = "Panya", 
                 favorite_drinks: list = ["Milk"], 
                 age: int = 0, 
                 height: int = 50, 
                 bank_balance: float = 0.0, 
                 coding_languages: set = None, 
                 is_alive: bool = True):
        
        self.name = (first_name, last_name)
        self.is_alive = is_alive
        self.favorite_drinks = favorite_drinks
        self.measurements = {
            'age': age,
            'height': height,
            'balance': bank_balance,
        }
        self.coding_languages = coding_languages

    def __str__(self) -> str:
        name = f"{self.name[0]} {self.name[1]}"
        age = self.measurements.get('age', 'N/A')
        height = self.measurements.get('height', 'N/A')
        balance = self.measurements.get('balance', 'N/A')
        drinks = ', '.join(self.favorite_drinks) if self.favorite_drinks else 'water'
        languages = ', '.join(sorted(self.coding_languages)) if self.coding_languages else 'None'
        status = "🟢 Alive" if self.is_alive else "Deceased\U0001F940"
        return (
            f"🌟 Meet {name}!\n"
            f"🎂 Age: {age} years\n"
            f"📏 Height: {height} cm\n"
            f"💰 Bank Balance: ${balance}\n"
            f"☕ Favorite Drinks: {drinks}\n"
            f"💻 Coding Languages: {languages}\n"
            f"🧬 Status: {status}"
        )

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
        return "Alive" if self.is_alive else "Deceased\U0001F940"

    def kill_human(self) -> None:
        self.is_alive = False

    def revive_human(self) -> None:
        self.is_alive = True