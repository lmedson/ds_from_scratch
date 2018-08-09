def friends_of_friend_ids_bad(user):
    #"foaf" acrônimo friend of a friend
    return [foaf["id"]
            for friend in user["friends"] #para cada amigo de usuário
            for foaf in friend["friends"]] #para acada _their_friends
