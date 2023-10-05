import random
inn_adj = ['Orange','Emo','Confused','Suspicious','Drunken','One-Legged','Cheesey','Stumbling','Sleep-Deprived Insommniac','Cooked','Prancing','Depressed','Enraged','Only In Ohio']
inn_noun = ['Horse','Emu','Beaver','Insurance','Jerry','Alpaca','Wombat','Feces','I ran out of ideas :(','Eagle','Pony','Hummingbird','Drone','Baked Beans','Bean']
inn_type = ['Inn','Tavern','Pub','The','The']
print ("The Medieval Inn Name Generator")
print ("Has decided your inn should be named...")
adj=(random.choice(inn_adj))
noun=(random.choice(inn_noun))
type=(random.choice(inn_type))
the='The'
if type == the:
 print(type,adj,noun)
else:
 print(adj,noun,type)
