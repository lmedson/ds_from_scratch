from __future__ import division
from friends_methods import friends_of_friend_ids_bad as foaf_m
from friends_methods import *
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
print(friends_of_friend_ids(users[3]))
