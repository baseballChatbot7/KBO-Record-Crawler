import os
import pandas as pd
import Player.Player_Hitter
import Player.Player_Pitcher
import Player.Player_Defense
import Player.Player_Runner

if not os.path.isfile('./Data/Player_Hitter.csv'):
    print('선수 기록 타자 데이터를 수집하고 있습니다.')
    PH = Player.Player_Hitter.Player_Hitter()
else:
    PH = pd.read_csv('./Data/Player_Hitter.csv', encoding='EUC-KR')

if not os.path.isfile('./Data/Player_Pitcher.csv'):
    print('선수 기록 투수 데이터를 수집하고 있습니다.')
    PP = Player.Player_Pitcher.Player_Pitcher()
else:
    PP = pd.read_csv('./Data/Player_Pitcher.csv', encoding='EUC-KR')

if not os.path.isfile('./Data/Player_Defense.csv'):
    print('선수 기록 수비 데이터를 수집하고 있습니다.')
    PD = Player.Player_Defense.Player_Defense()
else:
    PD = pd.read_csv('./Data/Player_Defense.csv', encoding='EUC-KR')

if not os.path.isfile('./Data/Player_Runner.csv'):
    print('선수 기록 주자 데이터를 수집하고 있습니다.')
    PR = Player.Player_Runner.Player_Runner()
else:
    PR = pd.read_csv('./Data/Player_Runner.csv', encoding='EUC-KR')