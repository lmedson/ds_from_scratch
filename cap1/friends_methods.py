from collections import Counter 

def friends_of_friend_ids_bad(user):
    #"foaf" acrônimo friend of a friend
    return [foaf["id"]
            for friend in user["friends"] #para cada amigo de usuário
            for foaf in friend["friends"]] #para acada _their_friends

def not_the_same(user, other_user):
    # dois usuários não são os mesmos se possuírem ids diferentes
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    return all(not_the_same(friend,other_user) for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                    for friend in user["friends"] # para cada um de meus amigos
                    for foaf in friend["friends"] # que contam *their* amigos
                    if not_the_same(user, foaf)   # que não sejam eu
                    and not_friends(user, foaf))  # e que não são meus amigos

 