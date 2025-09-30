from human import Human
from panya_representer import PanyaRepresenter

baby = Human()
panya = Human(
    first_name="Panya",
    last_name="Ranya",
    favorite_drinks=['matcha'],
    age=65,
    height=376,
    bank_balance=0.1,
    coding_languages={
        'Scratch', 'LOLCODE',
        'reMorse', 'TrumpScript'
    }
)

panya.kill_human()

panya_representer = PanyaRepresenter(baby, panya)
print(panya_representer)