import json, requests, sys

handle = ''
for each in sys.argv[1:]:
    handle = handle + each + ';'

url = 'https://codeforces.com/api/user.info?handles=%s' % (handle)

page = requests.get(url)
page.raise_for_status()

userdetails = json.loads(page.text)

users = userdetails['result']
for each in users:
    print()
    print('User Handle: ' + str(each['handle']))
    if 'firstName' in each:
        print('User First name is: ' + str(each['firstName']))
    else:
        print('User First name is: Not Available')

    if 'lastName' in each:
        print('User Last name is: ' + str(each['lastName']))
    else:
        print('User Last name is: Not Available')

    if 'rating' in each:
        print('Current user Rating is: ' + str(each['rating']))
    else:
        print('Current user Rating is: Not available')

    if 'rank' in each:
        print('Current user Rank is: ' + str(each['rank']))
    else:
        print('Current user Rank is: Not available')

    if 'maxRating' in each:
        print('Maximum user rating is: ' + str(each['maxRating']))
    else:
        print('Maximum user rating is: Not Available')

    if 'maxRank' in each:
        print('Maximum user rank is: ' + str(each['maxRank']))
    else:
        print('Maximum user rank is: Not Available')

    if 'country' in each:
        print('User country is: ' + str(each['country']))
    else:
        print('User country is: Not Available')
