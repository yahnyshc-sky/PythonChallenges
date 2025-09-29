from human import Human

def circleoflife(human: Human) -> None:
    print(human.human_status())
    print(human.kill_human())
    print(human.human_status())

panya = Human("Panya", "Ranya", ['matcha'], 65, 376,
                4000.1, {'Python', 'Java', 'C#', 'React', 'Assembly', 'C', 'C++',
                'Rust', 'JavaScript', 'CSS', 'HTML', 'AWS', 'Lua', 'Haskell', 'LOLCODE',
                'reMorse', 'TrumpScript' } )

# print(panya.get_name()[0])
# print(panya.get_age())
# good_languages = [
#     'reMorse',
#     'LOLCODE',
#     'TrumpScript'
# ]
# print([l for l in good_languages if l in panya.get_coding_languages()])


first_name, last_name = panya.get_name()
print(first_name.split("a") [0] + "ie", last_name)
circleoflife(panya)