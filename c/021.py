try:
    age = 88
    if not(age >=0 and age <= 100):
        raise Exception('Invalid Age')
    print('Valid Age')
except Exception as e:
    print('Err.:', e)