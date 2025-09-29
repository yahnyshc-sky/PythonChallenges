class Human:
    def __init__(self, first_name, last_name, is_alive, belongings, age, height, weight, coding_languages):
        self.name = (first_name, last_name)
        self.is_alive = is_alive
        self.belongings = belongings
        self.measurements = {
            'age': age,
            'height': height,
            'weight': weight,
        }
        self.coding_languages = coding_languages

    def get_name(self):
        return self.name

    def get_age(self):
        return self.measurements['age']

    def get_height(self):
        return self.measurements['height']

    def get_weight(self):
        return self.measurements['weight']

    def get_coding_languages(self):
        return self.coding_languages

    def get_belongings(self):
        return self.belongings

