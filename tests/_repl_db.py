import test
import repl_db as db
import json

# --- DB CALLS ---
mock_data = {
  'test_string': 'This is a test string.',
  'test_integer': 123,
  'test_decimal': 12.345,
  'test_json': {
    'foo': 'biz',
    'lorem': 'impsum',
    'answer': 5,
  }
}

# SET DATA
# requests.post(db_url, data = {'test': "Because I'm Batman!"})
def basic_key_value_db_calls():
  # resp = db.set('bruce', 'Batman!')
  # test.test(resp.status_code, 200, 'String type should write to the database')
  # --- Strings ---
  resp = db.set('test_string', mock_data['test_string'])
  test.test(resp.status_code, 200, 'Strings should write to the database')
  
  resp = db.get('test_string')
  test.test(resp, mock_data['test_string'], 'String data should be retrievable from the database')

  # --- Numbers
  resp = db.set('test_integer', mock_data['test_integer'])
  test.test(resp.status_code, 200, 'Integers should write to the database')

  resp = db.get('test_integer')
  test.test(resp, mock_data['test_integer'], 'Integers should be retrievable from the database')

  # --- Decimals ---
  resp = db.set('test_decimal', mock_data['test_decimal'])
  test.test(resp.status_code, 200, 'Decimals should write to the database')

  resp = db.get('test_decimal')
  test.test(resp, mock_data['test_decimal'], 'Decimals should be retrievable from the database')

  # # r = requests.get("{0}/test".format(db_url))
  # resp = db.get('bruce')
  # test.test(resp, 'Batman!', 'String type data should be retrievable from the database')
  # # print(r.content)

def json_data_in_db():
  # # requests.post(db_url, data = {'test2': json.dumps(mock_data)})
  # resp = db.set('dict_test', mock_data, 'json')
  # test.test(resp.status_code, 200, '"json" type data should write to the database')
  resp = db.set('test_json', mock_data['test_json'], 'json')
  test.test(resp.status_code, 200, 'JSON data should write to the database')

  resp = db.get('test_json')
  test.test(resp.get('lorem'), mock_data['test_json']['lorem'], 'JSON data should be retrievable from the database')
  
  # resp = db.get('dict_test')
  # test.test(resp.get('lorem'), mock_data['lorem'], '"json" type data should be retrievable from the database')

def list_the_things():
  resp = db.list('test')
  test.test(len(resp), 5, 'List call should have the correct length (prefix key + keys from mock data)')
  # print(resp)
  # for key in resp:
  #   print('{0}'.format(key))

def clean_up():
  # test_keys = ['bruce', 'dict_test', 'fake_key']
  test_keys = mock_data.keys()

  for key in test_keys:
    resp = db.delete(key)
    test.test(resp.status_code, 204, 'Successfully removed test data')
    # db.delete(key)
    # resp = db.get(key)
    # test.test(resp, '', 'Successfully removed test data')


# # GET DATA
# r2 = requests.get("{0}/test2".format(db_url))
# # print(r2.text)

# # This fails
# # print(r2.get('foo'))

# # This works
# r2dict = json.loads(r2.text)
# test.test(r2dict, mock_data, 'Mock data should match response')
# # print(r2dict)

# test.test(r2dict.get('foo'), mock_data['foo'], 'Dictionary methods should work on response')
# # print(r2dict.get('foo'))

# # DELETE DATA
# delete_url = '{0}/{1}'.format(db_url, 'test2')
# requests.delete(delete_url)
# r3 = requests.get("{0}/test2".format(db_url))
# test.test(r3.text, '', 'Delete call should successfully delete data')
test.run_all_tests([
  basic_key_value_db_calls,
  json_data_in_db,
  list_the_things,
  clean_up,
])