import random
inn_adj = ['Orange','Confused','Suspicious','Drunken','One-Legged','Cheesey','Stumbling','Sleep-Deprived Insommniac','Cooked','Prancing','Depressed','Enraged','Only In Ohio','Emo']
inn_noun = ['Horse','Beaver','Its_j3rry','Feces','I ran out of ideas :(','Eagle','Pony','Hummingbird','Drone','Baked Beans','Bean','Emu']
inn_type = ['Inn','Tavern','Pub','The','The']
adj=(random.choice(inn_adj))
noun=(random.choice(inn_noun))
type=(random.choice(inn_type))
the='The'
if type == the:
 print(type,adj,noun)
else:
 print(adj,noun,type)
