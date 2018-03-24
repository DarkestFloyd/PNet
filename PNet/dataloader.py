class DataLoader(object):

    def __init__(self, path):
        
        end_tokens = ['NAME', 'ATK', 'DEF', 'COST', 'DUR', 'TYPE',
                      'PLAYER_CLS', 'RACE', 'RARITY']
        
        file_names = ['train_hs', 'dev_hs', 'test_hs']

        input = {}
        output = {}
        for file_name in file_names:
            file_path = path + '/' + file_name
            cards = []
            with open(file_path + '.in', mode='r') as infile:
                lines = infile.readlines()
                for line in lines:
                    card = {}
                    for end_token in end_tokens:
                        line = line.split(end_token + '_END')
                        card[end_token] = line[0].strip()
                        line = line[1]
                    card['DESC'] = line.strip()

                    cards.append(card)

            code = []
            with open(file_path + '.out', mode='r') as infile:
                lines = infile.readlines()
                for line in lines:
                    code.append(line.replace('§', '\n'))

            input[file_name] = cards
            output[file_name] = code

        self.train_data = Data('train', input['train_hs'], output['train_hs'])
        self.dev_data = Data('dev', input['dev_hs'], output['dev_hs'])
        self.test_data = Data('test', input['test_hs'], output['test_hs'])
                
class Data(object):
    
    def __init__(self, label, cards, code):
        
        self.label = label
        self.cards = cards
        self.code = code
