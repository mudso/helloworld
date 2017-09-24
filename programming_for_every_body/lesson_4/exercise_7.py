user_score = input('Enter score:')
def computegrade(user_score):
    try:
        user_score = float(user_score)
        not 0 <= user_score <=1
        if 1 >= user_score >= 0.9 :
            retur('A')
        elif 0.9 > user_score >= 0.8:
            print('B')
        elif 0.8 > user_score >= 0.7:
            print('C')
        elif 0.7 > user_score >= 0.6:
            print('D')
        elif 0 <= user_score < 0.6:
            print('F')
        else:
            print('Bad score')


    except:
        print('Bad score')

computegrade(user_score)