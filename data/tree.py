import csv
import json

spamReader = csv.reader(open('2014.csv', 'r')) #change year here
spamReader = list(spamReader)



def getChildren(player1, i):
    temp = {}
    # try:
    for k in range(i + 1, len(spamReader)):
        j = spamReader[k]
        if (j[1] == player1):
            if (j[0] == 'quarter'):
                j[0] = 'Quarter'
            if (j[0] == 'semi'):
                j[0] = 'Semi'
            if(j[0]=='First'):
                temp = {
                    'name': player1,
                    'round': j[0],
                    'results': j[2],
                    'player1':j[5],
                    'player2':j[6],
                    'ace1':j[11],
                    'ace2':j[12],
                    'fastServe1':j[19],
                    'fastServe2':j[20],
                    'avgFirstServe1':j[21],
                    'avgFirstServe2':j[22],
                    'avgSecServe1':j[23],
                    'avgSecServe2':j[24],
                    'children': [
                        {
                            'name': j[5],
                            'round': 'seed'
                        },
                        {
                            'name': j[6],
                            'round': 'seed'
                        }
                    ]
                }
            else:
                if (j[0] == 'quarter'):
                    j[0] = 'Quarter'
                if (j[0] == 'semi'):
                    j[0] = 'Semi'
                if not getChildren(j[5], k):
                    x={'name' : j[5],
                       'round': 'First',
                       'player1': j[5],
                       'player2': ' BYE',
                       'children':[{
                            'name': ' BYE',
                            'round': 'seed',
                            'player1': ' BYE'
                        },
                        {
                            'name': ' BYE',
                            'round': 'seed',
                            'player1': ' BYE'
                        }]}
                else:
                    x = getChildren(j[5],k)

                if not getChildren(j[6], k):
                    y={'name' : j[6],
                       'round': 'First',
                       'player1': j[6],
                       'player2': ' BYE',
                       'children':[{
                            'name': ' BYE',
                            'round': 'seed',
                            'player1': ' BYE'
                        },
                        {
                            'name': ' BYE',
                            'round': 'seed',
                            'player1': ' BYE'
                        }]}
                else:
                    y = getChildren(j[6],k)

                temp = {
                    'name': player1,
                    'round': j[0],
                    'results': j[2],
                    'player1': j[5],
                    'player2': j[6],
                    'ace1': j[11],
                    'ace2': j[12],
                    'fastServe1':j[19],
                    'fastServe2':j[20],
                    'avgFirstServe1':j[21],
                    'avgFirstServe2':j[22],
                    'avgSecServe1':j[23],
                    'avgSecServe2':j[24],
                    'children': [x, y]
                }
            break
    return temp

node={}
row = spamReader[1]
node[row[1]] = {
    'name': row[1],
    'round': row[0],
    'results': row[2],
    'player1': row[5],
    'player2': row[6],
    'ace1': row[11],
    'ace2': row[12],
    'fastServe1': row[19],
    'fastServe2': row[20],
    'avgFirstServe1': row[21],
    'avgFirstServe2': row[22],
    'avgSecServe1':  row[23],
    'avgSecServe2': row[24],
    'children': [getChildren(row[5], 1), getChildren(row[6], 1)]
}

with open('2014.json', 'w') as fp: #change year here
    json.dump(node[row[1]], fp)

# run code for each year

