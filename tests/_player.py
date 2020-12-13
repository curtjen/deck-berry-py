import test
import player

import repl_db

#  -------------
import requests
import os
import json
# print(os.getenv("REPLIT_DB_URL"))

db_url = os.getenv('REPLIT_DB_URL')
# data = {'key':'value'}

# --- DB CALLS ---
mock_data = {
  'foo': 'biz',
  'lorem': 'impsum',
  'answer': 5,
}

# SET DATA
requests.post(db_url, data = {'test': "Because I'm Batman!"})
r = requests.get("{0}/test".format(db_url))
print(r.content)

requests.post(db_url, data = {'test2': json.dumps(mock_data)})

# GET DATA
r2 = requests.get("{0}/test2".format(db_url))
# print(r2.text)

# This fails
# print(r2.get('foo'))

# This works
r2dict = json.loads(r2.text)
test.test(r2dict, mock_data, 'Mock data should match response')
# print(r2dict)

test.test(r2dict.get('foo'), mock_data['foo'], 'Dictionary methods should work on response')
# print(r2dict.get('foo'))

# DELETE DATA
delete_url = '{0}/{1}'.format(db_url, 'test2')
requests.delete(delete_url)
r3 = requests.get("{0}/test2".format(db_url))
test.test(r3.text, '', 'Delete call should successfully delete data')

#  -------------

#  TODO: Do new tests here using repl_db.


# test.test('a', 'a', 'this is a test')

# TODO: Create mock player in db
# TODO: Do tests
# TODO: Cleanup mock player from db
# TODO: Confirm that it has been removed
# -- May be possible to have this as part of a db utility and test this (cleanup) as part of that utility.

# test_player = player.Player()
# test.test(test_player.player_class, 'fighter', 'Player class should match default')

player_class = player.get_player_class()
test.test(player_class, 'fighter', 'Player class should match default')



# import numpy as np

# class Player:
#   def __init__(self, hand_size=5, player_class='fighter', loot=0):
#     self.player_class = player_class
#     # player_deck = [val for key, val in PLAYER_STARTING_DECK.items()]
#     # self.player_deck = player_deck
#     self.player_deck = list(PLAYER_STARTING_DECK)
#     self.hand_size = hand_size
#     self.discard_pile = []
#     self.current_hand = []
#     self.loot = loot
 
#   def get_next_card(self):
#     next_card = self.player_deck.pop()
#     return next_card

#   def draw_hand(self):
#     # self.current_hand = []
#     for n in range(self.hand_size):
#       self.current_hand.append(self.get_next_card())

#   def discard_hand(self):
#     # append current_hand to discard_pile
#     # set current_hard to []
#     self.discard_pile = np.append(self.discard_pile, self.current_hand)
#     self.current_hand = []
  
#   def purchase_from_merchant(self, category, npc_name, item_key):
#     merchant = get_merchant(category=category, npc_name=npc_name)
#     # print(merchant