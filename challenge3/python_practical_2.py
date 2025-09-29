from human import Human

panya = Human("Panya", "Ranya", True, ['matcha'], 65, 376,
              4000.1, {'Python', 'Java', 'C#', 'React', 'Assembly', 'C', 'C++',
                                 'Rust', 'JavaScript', 'CSS', 'HTML', 'AWS', 'Lua', 'Haskell', 'LOLCODE',
                                 'reMorse', 'TrumpScript' } )

print(panya.get_name()[0])
print(panya.get_age())
good_languages = [
    'reMorse',
    'LOLCODE',
    'TrumpScript'
]
print([l for l in good_languages if l in panya.get_coding_languages()])
