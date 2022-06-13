def troca(string, string_achar, string_trocar):
    
    string_return = ''
    
    if string_achar in string:
        
        sep_string = string.split(string_achar)
        
        for letter in sep_string:
            
            string_return += letter + string_trocar
        
        string = string_return[:-1]
    
    return string


nome = 'gorda'

nome = troca(nome, 'a', 'o')

print(nome)
nome.replace
        


