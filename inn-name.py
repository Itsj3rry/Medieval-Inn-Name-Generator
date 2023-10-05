import random
inn_adj = ['Orange','Confused','Suspicious','Emo','Drunken','One-Legged','Cheesey','Stumbling','Sleep-Deprived Insommniac','Cooked','Prancing','Depressed','Enraged','Only In Ohio']
inn_noun = ['Horse','Beaver','Its_j3rry','Feces','Capybara','Emu''I ran out of ideas :(','Eagle','Pony','Hummingbird','Drone','Baked Beans','Bean']
inn_type = ['Inn','Tavern','Pub','The']
adj=(random.choice(inn_adj))
noun=(random.choice(inn_noun))
type=(random.choice(inn_type))
if type='the' print(type)
print(adj,noun,type)
