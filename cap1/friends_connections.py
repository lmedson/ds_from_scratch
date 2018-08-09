from __future__ import division
from friends_methods import friends_of_friend_ids_bad as foaf_m
from friends_methods import *
from collections import defaultdict, Counter
#cria uma rede de users
users = [
  {"id":0, "name":"Hero"},
  {"id":1,"name":"Dunn"},
  {"id":2,"name":"Sue"},
  {"id":3,"name":"Chi"},
  {"id":4,"name":"Thor"},
  {"id":5,"name":"Clive"},
  {"id":6,"name":"Hicks"},
  {"id":7,"name":"Devin"},
  {"id":8,"name":"Kate"},
  {"id":9,"name":"Klein"},
]

#cria uma rede e conexões
friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
               (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

#adiciona uma lista de amigos para cada usuario
for user in users:
  user["friends"] = []
#povoamento da lista com os dados das amizades
for i,j in friendships:
  #isso funciona porque users[i] é o usuário cuja id é i
  users[i]["friends"].append(users[j])#add i como amigo de j
  users[j]["friends"].append(users[i])#add j como amigo de i

def number_of_friends(user):
  #quantos amigos o usuário tem?
  return len(user["friends"]) #tamanho da lista friend_ids

total_connections = sum(number_of_friends(user) for user in users)

# print(total_connections)

num_users = len(users) #tamanho da lista de usuários
avg_connections = total_connections / num_users
#print(avg_connections) # número médio de conexões

#cria uma lista da quantidade de amigos por id
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users ] 
#sorted(num_friends_by_id, key=lambda (user_id, num_friends): num_friends, reverse=True)

#print(friends_of_friend_ids(users[3]))

interests = [
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), 
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"), 
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"), 
    (4, "machine learning"), (4, "regression"), (4, "decision trees"), 
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), 
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"), 
    (6, "probability"), (6, "mathematics"), (6, "theory"), 
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), 
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"), 
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"), 
    (9, "Java"), (9, "MapReduce"), (9, "Big Data"), (10, "statistics"), 
    (10, "R"), (10, "statsmodels")
]

def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]
            
users_by_interest = defaultdict(list)

for user_id, interest in interests:
    users_by_interest[interest].append(user_id)

interests_by_user = defaultdict(list)

for user_id, interest in interests:
    interests_by_user[user_id].append(interest)

def most_common_interests_with(user_id):
    return Counter(interested_user_id
        for interest in interests_by_user["user_id"]   
        for interested_user_id in users_by_interest[interest]
        if interested_user_id != user_id)
