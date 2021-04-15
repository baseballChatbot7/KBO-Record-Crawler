import os
import pandas as pd
import Team.Team_Hitter
import Team.Team_Pitcher
import Team.Team_Defense
import Team.Team_Runner

if not os.path.isfile('./Data/Team_Hitter.csv'):
    print('팀 기록 타자 데이터를 수집하고 있습니다.')
    TH = Team.Team_Hitter.Team_Hitter()
else:
    TH = pd.read_csv('./Data/Team_Hitter.csv', encoding='EUC-KR')

if not os.path.isfile('./Data/Team_Pitcher.csv'):
    print('팀 기록 투수 데이터를 수집하고 있습니다.')
    TP = Team.Team_Pitcher.Team_Pitcher()
else:
    TP = pd.read_csv('./Data/Team_Pitcher.csv', encoding='EUC-KR')

if not os.path.isfile('./Data/Team_Defense.csv'):
    print('팀 기록 수비 데이터를 수집하고 있습니다.')
    TD = Team.Team_Defense.Team_Defense()
else:
    TD = pd.read_csv('./Data/Team_Defense.csv', encoding='EUC-KR')

if not os.path.isfile('./Data/Team_Runner.csv'):
    print('팀 기록 주자 데이터를 수집하고 있습니다.')
    TR = Team.Team_Runner.Team_Runner()
else:
    TR = pd.read_csv('./Data/Team_Runner.csv', encoding='EUC-KR')

TH.columns = ['연도','팀명'] + [i+'_Hitter' for i in TH.columns if i not in ['연도','팀명']]
TP.columns = ['연도','팀명'] + [i+'_Pitcher' for i in TP.columns if i not in ['연도','팀명']]
TD.columns = ['연도','팀명'] + [i+'_Defense' for i in TD.columns if i not in ['연도','팀명']]
TR.columns = ['연도','팀명'] + [i+'_Runner' for i in TR.columns if i not in ['연도','팀명']]

df_INNER_JOIN_1 = pd.merge(TH, TP, left_on=['연도','팀명'], right_on=['연도','팀명'], how='inner')
df_INNER_JOIN_2 = pd.merge(TD, TR, left_on=['연도','팀명'], right_on=['연도','팀명'], how='inner')

df_INNER_JOIN = pd.merge(df_INNER_JOIN_1, df_INNER_JOIN_2, left_on=['연도','팀명'], right_on=['연도','팀명'], how='inner')

df_INNER_JOIN.to_csv('./Data/Team_Total.csv', index=False, encoding='EUC-KR')