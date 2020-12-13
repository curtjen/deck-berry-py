# ===== Make worky with apps libs =====
import sys
# -- Paths specific to Repl.it ---
sys.path.insert(1, '/home/runner/deck-berry-py/deck_berry_py')

# ===== Test Library =====
def test(rec, expect, msg):
  result = None
  if (rec == expect):
    result = 'PASS: ' + msg
  else:
    # response = 'FAIL: ' + msg + '\n|__ Got: ' + str(result) + '\n|__ Expected: ' + str(expect)
    result = 'FAIL: {}\n|__ Expected: {}\n|__ Received: {}'.format(msg, str(expect), str(rec))
  print(result)

def test_loop_basic(test_cases):
  for t in test_cases:
    msg, expect, rec = t
    test(rec, expect, msg)

def test_loop_more(test_cases):
  for t in test_cases:
    msg, data = t
    test(data['rec'], data['expect'], msg)

def run_all_tests(tests_list):
  for t in tests_list:
    print('\n### ' + t.__name__.replace('_', ' '))
    t()
