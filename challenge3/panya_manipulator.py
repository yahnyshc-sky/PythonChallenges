from human import Human

def panya_development(baby: Human, grown: Human) -> None:
    print (f"{baby}\n\nGrew up to become the \U0001F410\n\n{grown}")

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

panya_development(baby, panya)