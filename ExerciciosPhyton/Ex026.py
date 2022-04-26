frase = str(input('Digite um frase: ')).strip().lower()
print(f'A letra "A" aperece {frase.count("a",0,)} vezes na frase.' )
print(f'A primeira letra "A" aparece na posição {frase.find("a") + 1}.')
print(f'A ultima letra "A" aparece na posição {frase.rfind("a") + 1}.')