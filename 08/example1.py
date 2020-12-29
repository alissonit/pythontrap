#FUNÇÕES (FUNCTION)

#EXEMPLO SEM O USO DE FUNÇÃO :(
rappers_choice = ["L7NNON", "KB", "Trip Lee", "Travis Scott", ["Lecrae", "Projota", "Tupac"], "Don Omar"]

rappers_country = {"BR":["Hungria", "Kamau", "Projota", "Mano Brown", "Luo", "L7NNON"],
    "US":["Tupac", "Drake", "Eminem", "KB", "Kanye West", "Lecrae", "Travis Scott", "Trip Lee"]}

for rp in rappers_choice:
    if isinstance(rp, list):
        for rp_one in rp:
            if rp_one in rappers_country["BR"]:
                print(f"Rapper BR: {rp_one}")
            elif rp_one in rappers_country["US"]:
                print(f"Rapper US: {rp_one}")
            else:
                print(f"Rapper not found in lists: {rp_one}")
    else:
        if rp in rappers_country["BR"]:
            print(f"Rapper BR: {rp}")
        elif rp in rappers_country["US"]:
            print(f"Rapper US: {rp}")
        else:
            print(f"Rapper not found in lists: {rp}")