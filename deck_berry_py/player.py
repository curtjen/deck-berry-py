import numpy as np

#  --- Player Calls v1 ---
class Player:
  def __init__(self, hand_size=5, player_class='fighter', loot=0):
    self.player_class = player_class
    # player_deck = [val for key, val in PLAYER_STARTING_DECK.items()]
    # self.player_deck = player_deck
    self.player_deck = list(PLAYER_STARTING_DECK)
    self.hand_size = hand_size
    self.discard_pile = []
    self.current_hand = []
    self.loot = loot
 
  def get_next_card(self):
    next_card = self.player_deck.pop()
    return next_card

  def draw_hand(self):
    # self.current_hand = []
    for n in range(self.hand_size):
      self.current_hand.append(self.get_next_card())

  def discard_hand(self):
    # append current_hand to discard_pile
    # set current_hard to []
    self.discard_pile = np.append(self.discard_pile, self.current_hand)
    self.current_hand = []
  
  def purchase_from_merchant(self, category, npc_name, item_key):
    merchant = get_merchant(category=category, npc_name=npc_name)
    # print(merchant



# --- Player Calls v2 ---
import repl_db as db

def get_player_class():
  # TODO: Change this to a db call
  return 'fighter'

def get_player():
  try:
    return db.get('player')
  except:
    return False

def create_player(settings):
  # TODO: Change this to be multiple calls so the individual pieces can be updated separately.
  resp = None
  try:
    resp = db.set('player', settings, 'json')
    return resp
  except:
    return resp

def get_next_card():
  pass

def draw_hand():
  pass

def discard_hand():
  pass

def purchase_from_merchant():
  pass

# TODO: Create delete_db_entry call in db utility; not here.
