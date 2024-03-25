import random
from tabulate import tabulate

india = ['Jaiswal', 'Rohit', 'Virat', 'Sky', 'Rinku', 'Pant', 'Pandya', 'Jadeja', 'Kuldeep', 'Shami', 'Bumrah']
australia = ['Head', 'Warner', 'Marsh', 'Maxwell', 'Inglis', 'David', 'Stoinis', 'Cummins', 'Starc', 'Zampa', 'Hazlewood']

ind_player_stats = {
    'Jaiswal': 'Bat',
    'Rohit': 'Bat',
    'Virat': 'Bat', 
    'Sky': 'Bat', 
    'Rinku': 'Bat', 
    'Pant': 'Bat', 
    'Pandya': 'All', 
    'Jadeja': 'All', 
    'Kuldeep': 'Bowl', 
    'Shami': 'Bowl', 
    'Bumrah': 'Bowl'
}

aus_player_stats = {
    'Head': 'Bat',
    'Warner': 'Bat',
    'Marsh': 'Bat', 
    'Maxwell': 'Bat', 
    'Inglis': 'Bat', 
    'David': 'Bat', 
    'Stoinis': 'All', 
    'Cummins': 'All', 
    'Starc': 'Bowl', 
    'Zampa': 'Bowl', 
    'Hazlewood': 'Bowl'
}

player_type = {
    'Bat': {
        'six': list(range(0,10)),
        'four': list(range(10,25)),
        'single': list(range(25,70)),
        'double': list(range(70,80)),
        'dot': list(range(80,95)),
        'out': list(range(95,101)),
        'wicket': 0
    },
    'All': {
        'six': list(range(0,15)),
        'four': list(range(15,30)),
        'single': list(range(30,70)),
        'double': list(range(70,80)),
        'dot': list(range(80,95)),
        'out': list(range(95,101)),
        'wicket': 0.03
    },
    'Bowl': {
        'six': list(range(0,5)),
        'four': list(range(5,15)),
        'single': list(range(15,55)),
        'double': list(range(55,60)),
        'dot': list(range(60,90)),
        'out': list(range(90,101)),
        'wicket': 0.05
    }
}

class Score:
    def __init__(self,runs=0,wickets=0):
        self.runs = runs
        self.wickets = wickets

    def calculate_score(self,ball_runs,batsmen):
        self.runs += ball_runs
        self.wickets = 11 - len(batsmen)

    def __str__(self):
        return f'{self.runs}-{self.wickets}'

class Bowler:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.wicket_chance = player_type[type]['wicket']
        self.runs = 0
        self.balls = 0
        self.wickets = 0

    def add_score(self,runs):
        self.runs += runs
        self.balls += 1
    
    def add_wickets(self):
        self.wickets += 1

    def calculate_econrate(self):
        pass

class Batsman:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.six = player_type[type]['six']
        self.four = player_type[type]['four']
        self.single = player_type[type]['single']
        self.double = player_type[type]['double']
        self.dot = player_type[type]['dot']
        self.out = player_type[type]['out']
        self.wicket = player_type[type]['wicket']
        self.runs = 0
        self.balls = 0
        self.fours = 0
        self.sixes = 0

    def add_score(self,runs):
        self.runs += runs
        self.balls += 1
    
    def add_fours(self):
        self.fours += 1

    def add_sixes(self):
        self.sixes += 1
    
    def calculate_strikerate(self):
        pass

def ind_bolwers_list(ind_player_stats):
    india_bowlers = []
    for player in ind_player_stats:
        if ind_player_stats[player] == 'Bowl' or ind_player_stats[player] == 'All':
            bowler = Bowler(player,ind_player_stats[player]) 
            india_bowlers.append(bowler)
    return india_bowlers

def aus_bolwers_list(aus_player_stats):
    aus_bowlers = []
    for player in aus_player_stats:
        if aus_player_stats[player] == 'Bowl' or aus_player_stats[player] == 'All':
            bowler = Bowler(player,aus_player_stats[player])
            aus_bowlers.append(bowler)
    return aus_bowlers

def ind_batsmen_list(ind_player_stats):
    ind_batsmen = []
    for player in ind_player_stats:
        batsman = Batsman(player,ind_player_stats[player])
        ind_batsmen.append(batsman)
    return ind_batsmen

def aus_batsmen_list(aus_player_stats):
    aus_batsmen = []
    for player in aus_player_stats:
        batsman = Batsman(player,aus_player_stats[player])
        aus_batsmen.append(batsman)
    return aus_batsmen

def over(batsmen,bowler,score,target):
    
    for ball in range(1,7):
        ball_runs = 0
        if(len(batsmen) == 1):
            print('\nALL OUT')
            break
        
        print(f'\tBall {ball}: ', end='')
        current_batsman = batsmen[0]

        bowler_chance = random.random()

        if bowler_chance <= bowler.wicket_chance:
            print(f'OUT. {bowler.name} dismissed {batsmen[0].name}')
            dismissed_batsmen.append(batsmen.pop(0))
            current_batsman.add_score(0)
            bowler.add_score(0)
            bowler.add_wickets()
            score.calculate_score(ball_runs,batsmen)
        else:
            batsman_chance = round(random.random()*100)
            if batsman_chance in current_batsman.six:
                print(f'{current_batsman.name} scored 6 runs.')
                ball_runs += 6
                current_batsman.add_score(6)
                current_batsman.add_sixes()
                bowler.add_score(6)
                score.calculate_score(ball_runs,batsmen)
            elif batsman_chance in current_batsman.four:
                print(f'{current_batsman.name} scored 4 runs.')
                ball_runs += 4
                current_batsman.add_score(4)
                current_batsman.add_fours()
                bowler.add_score(4)
                score.calculate_score(ball_runs,batsmen)
            elif batsman_chance in current_batsman.single:
                print(f'{current_batsman.name} scored 1 run.')
                ball_runs += 1
                current_batsman.add_score(1)
                bowler.add_score(1)
                score.calculate_score(ball_runs,batsmen)
            elif batsman_chance in current_batsman.double:
                print(f'{current_batsman.name} scored 2 runs.')
                ball_runs += 2
                current_batsman.add_score(2)
                bowler.add_score(2)
                score.calculate_score(ball_runs,batsmen)
            elif batsman_chance in current_batsman.dot:
                print(f'{current_batsman.name} scored 0 runs.')
                current_batsman.add_score(0)
                bowler.add_score(0)
                score.calculate_score(ball_runs,batsmen)
            elif batsman_chance in current_batsman.out:
                print(f'OUT. {bowler.name} dismissed {batsmen[0].name}')
                current_batsman.add_score(0)
                bowler.add_score(0)
                bowler.add_wickets()
                dismissed_batsmen.append(batsmen.pop(0))
                score.calculate_score(ball_runs,batsmen)
                
        if(score.runs >= target):
            dismissed_batsmen.append(batsmen.pop(0))
            break
   
    return score

def innings(batsmen,bowlers,target):

    score = Score()
    all_out = False
    over_number = 0
    num = 1

    while(not all_out and num < 5):
        for bowler in bowlers:
            over_number += 1
            print(f"\nOver - {over_number}. {bowler.name} bowling his over number {num}.")                
            score = over(batsmen,bowler,score,target)   
            if(score.runs >= target):
                break        
            if(len(batsmen) == 1):
                all_out = True
                break             
            print(f'\nAfter {over_number} overs, Score: {score}')            

        if(len(batsmen) == 1):
            all_out = True
            break
        if(score.runs >= target):
                break
        num +=1

    return score

def ind_bat_first(ind_batsmen,ind_bolwers,aus_batsmen,aus_bolwers):

    scores = []

    ind_score = innings(ind_batsmen,aus_bolwers,721)

    aus_score = innings(aus_batsmen,ind_bolwers,ind_score.runs+1)

    scores.append(ind_score)  
    scores.append(aus_score)    

    return scores

def aus_bat_first(ind_batsmen,ind_bolwers,aus_batsmen,aus_bolwers):

    scores = []

    aus_score = innings(aus_batsmen,ind_bolwers,721)
    print(f'\n\nAustralia score: {aus_score}')    

    ind_score = innings(ind_batsmen,aus_bolwers,aus_score.runs+1)
    print(f'\n\nIndia score: {ind_score}')
    
    scores.append(ind_score)  
    scores.append(aus_score)   

    return scores

def calculate_overs(balls):
    spare_balls = balls%6
    overs = (balls - spare_balls)/6
    return (f'{int(overs)}.{spare_balls}')

def strike_rate(runs,balls):
    return round((runs/balls)*100,2)

def econ_rate(runs,balls):
    return round((runs/balls)*6,2)

def scoresheet(dismissed_batsmen,scores,ind_bolwers,aus_bolwers):

    ind_batsmen = []
    aus_batsmen = []

    for batsman in dismissed_batsmen:
        if batsman.name in india:
            ind_batsmen.append(batsman)
        else:
            aus_batsmen.append(batsman)

    ind_batsman_figures = []
    aus_batsman_figures = []
    ind_bowler_figures = []
    aus_bowler_figures = []
    ind_total_balls = 0
    aus_total_balls = 0

    for batsman in ind_batsmen:
        single_batsman_figures = [batsman.name,batsman.runs,batsman.balls,batsman.fours,batsman.sixes,strike_rate(batsman.runs,batsman.balls)]
        ind_batsman_figures.append(single_batsman_figures)
    
    for batsman in aus_batsmen:
        single_batsman_figures = [batsman.name,batsman.runs,batsman.balls,batsman.fours,batsman.sixes,strike_rate(batsman.runs,batsman.balls)]
        aus_batsman_figures.append(single_batsman_figures)

    for bowler in ind_bolwers:
        single_bowler_figures = [bowler.name,calculate_overs(bowler.balls),bowler.runs,bowler.wickets,econ_rate(bowler.runs,bowler.balls)]
        ind_bowler_figures.append(single_bowler_figures)
        ind_total_balls += bowler.balls

    for bowler in aus_bolwers:
        single_bowler_figures = [bowler.name,calculate_overs(bowler.balls),bowler.runs,bowler.wickets,econ_rate(bowler.runs,bowler.balls)]
        aus_bowler_figures.append(single_bowler_figures)
        aus_total_balls += bowler.balls

    print('\n\nSCORESHEET:\n')

    if dismissed_batsmen[0].name == 'Head':
        print(f'\nAUSTRALIA: {scores[1]} in {calculate_overs(ind_total_balls)} overs')
        print(tabulate(aus_batsman_figures,headers=['Batsman','Runs','Balls','Fours','Sixes','Strike Rate'],tablefmt='grid'))   
        print(tabulate(ind_bowler_figures,headers=['Bowler','Overs','Runs','Wickets','Econ. Rate'],tablefmt='grid'))

        print(f'\nINDIA: {scores[0]} in {calculate_overs(aus_total_balls)} overs')
        print(tabulate(ind_batsman_figures,headers=['Batsman','Runs','Balls','Fours','Sixes','Strike Rate'],tablefmt='grid'))   
        print(tabulate(aus_bowler_figures,headers=['Bowler','Overs','Runs','Wickets','Econ. Rate'],tablefmt='grid'))     
    else:
        print(f'\nINDIA: {scores[0]} in {calculate_overs(aus_total_balls)} overs')
        print(tabulate(ind_batsman_figures,headers=['Batsman','Runs','Balls','Fours','Sixes','Strike Rate'],tablefmt='grid'))
        print(tabulate(aus_bowler_figures,headers=['Bowler','Overs','Runs','Wickets','Econ. Rate'],tablefmt='grid'))     

        print(f'\nAUSTRALIA: {scores[1]} in {calculate_overs(ind_total_balls)} overs')
        print(tabulate(aus_batsman_figures,headers=['Batsman','Runs','Balls','Fours','Sixes','Strike Rate'],tablefmt='grid'))  
        print(tabulate(ind_bowler_figures,headers=['Bowler','Overs','Runs','Wickets','Econ. Rate'],tablefmt='grid'))     


# MATCH STARTS

ind_batsmen = ind_batsmen_list(ind_player_stats)
aus_batsmen = aus_batsmen_list(aus_player_stats)
ind_bolwers = ind_bolwers_list(ind_player_stats)
aus_bolwers = aus_bolwers_list(aus_player_stats)

print('Welcome to India vs Australia. \n\nTOSS time: ', end='')
toss = random.randint(1,2)

dismissed_batsmen = []

if toss == 1:
    choice = random.randint(1,2)
    if choice == 1:
        print('India wins the toss and elect to Bat first')
        scores = ind_bat_first(ind_batsmen,ind_bolwers,aus_batsmen,aus_bolwers)
        ind_bat_first = True
    else:
        print('India wins the toss and elect to Bowl first')
        scores = aus_bat_first(ind_batsmen,ind_bolwers,aus_batsmen,aus_bolwers)
        ind_bat_first = False
else:
    choice = random.randint(1,2)
    if choice == 1:
        print('Australia wins the toss and elect to Bat first')
        scores = aus_bat_first(ind_batsmen,ind_bolwers,aus_batsmen,aus_bolwers)
        ind_bat_first = False
    else:
        print('Australia wins the toss and elect to Bowl first')
        scores = ind_bat_first(ind_batsmen,ind_bolwers,aus_batsmen,aus_bolwers)
        ind_bat_first = True

scoresheet(dismissed_batsmen,scores,ind_bolwers,aus_bolwers)

if scores[0].runs > scores[1].runs:
    print(f'\n\nIndia WINS', end='')
    if ind_bat_first:
        print(f' by {scores[0].runs - scores[1].runs} runs.')
    else:
        print(f' by {10 - scores[0].wickets} wickets')
elif scores[0].runs < scores[1].runs:
    print(f'\n\nAustralia WINS', end='')
    if ind_bat_first:
        print(f' by {10 - scores[1].wickets} wickets')
    else:
        print(f' by {scores[1].runs - scores[0].runs} runs.')

else:
    print("\n\nIt's a DRAW")



