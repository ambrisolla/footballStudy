"""
    Autor: André Müzel Brisolla
    Objetivo: Gerar um output para carregar um 
    "bar race" para carregar no site: https://app.flourish.studio
"""

import os,json,pycountry,sys

class Football:
    def __init__(self):

        try:
            # Get file name after parameter --dataset 
            for i,p in enumerate(sys.argv):
                if p == '--dataset':
                    dataset_file = sys.argv[i+1]
            
            # Check if file exists
            if dataset_file == "":
                print("Erro: Dataset not found!")
                sys.exit(1)
            elif not os.path.exists(dataset_file):
                print("Erro: File not found: {}".format(dataset_file))
                sys.exit(1)

            # Generate a dict with "dataset.csv" data
            dataset = open(dataset_file,"r")

            # Config dict keys
            first_line = dataset.readline()
            keys = first_line.replace("\n","").split(",")

            # Add dataset data to all_games dict
            list_games = []
            for idx,line in enumerate(dataset.readlines()):
                line = line.replace("\n","")
                if idx > 0:
                    field_list = {}
                    line_splited = line.split(",")
                    for idx2,key in enumerate(keys):
                        field_list[key] = line_splited[idx2]
                    list_games.append(field_list)
            self.games_with_no_winner = list_games
            
            # Set dates/countries/winners
            list_dates = []
            list_countries = []
            games_with_winner = []
            for g in self.games_with_no_winner:
                # Set dates
                date = g['date'].split("-")
                date = "{}-{}".format(date[0],date[1])
                if date not in list_dates:
                    list_dates.append(date)

                # Set countries
                if g['home_team'] not in list_countries:
                    list_countries.append(g['home_team'])
                if g['away_team'] not in list_countries:
                    list_countries.append(g['away_team'])

                # Set winner
                home_wins = g['home_score'] > g['away_score']
                away_wins = g['home_score'] < g['away_score']
                no_winner = g['home_score'] == g['away_score']
                if home_wins:
                    winner = g['home_team']
                elif away_wins:
                    winner = g['away_team']
                elif no_winner:
                    winner = False
                
                # Add a winner
                g['winner'] = winner

                # Add to a new dict
                games_with_winner.append(g)

            self.games = games_with_winner
            self.dates = list_dates
            self.countries = sorted(list_countries)
        except Exception as e:
            return {
                "Erro" : str(e)
            }            

    # Set flag
    def setCountryFlag(self,country):
        try:
            codes = pycountry.countries.search_fuzzy(country)[0]
            code2 = codes.alpha_2
            url = "https://www.countryflags.io/{}/flat/64.png".format(code2)
            return url
        except:
            return ""
    
    # Set columns indexes
    def mountHeader(self):
        dates = self.dates
        for idx,date in enumerate(dates):
            if idx == 0:
                print("Teams,Image",end=",")
            else:
                print(date,end=",")

    # Set data 
    def mountBarRaceTable(self):
        # Mount column index
        self.mountHeader()
        # Get all games 
        games = self.games
        # Get victory by country/date
        for country in self.countries:
            # get country flag url image
            flag = self.setCountryFlag(country)
            print("\n{},{}".format(country,flag),end=",")
            total_wins = 0
            for date in self.dates:
                wins = len([x for x in games if x['winner'] == country and date in x['date']])
                total_wins = total_wins+wins
                print(total_wins,end=",")
    
# Create output    
if '--dataset' not in sys.argv:
    print("Informe o dataset: \n\t\t--dataset example.csv")
else:
    Football().mountBarRaceTable()
