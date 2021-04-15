# KBO-Record-Crawler

# Source
- [KBO 기록실](https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx)

# Usage
1. [ChromeDriver](https://chromedriver.chromium.org/downloads) Download
2. Player_Total.py을 실행하여 선수 기록을 수집
3. Team_Total.py을 실행하여 팀 기록을 수집
4. /Data 폴더에 수집된 데이터를 사용

# Code
```
$> tree -d
.
├── /Data
│     ├── Player_Defense.csv
│     ├── Player_Hitter.csv
│     ├── Player_Pitcher.csv
│     ├── Player_Runner.csv
│     ├── Team_Defense.csv
│     ├── Team_Hitter.csv
│     ├── Team_Pitcher.csv
│     ├── Team_Runner.csv
│     └── Team_Total.csv
├── /Player
│     ├── Player_Defense.py
│     ├── Player_Hitter.py
│     ├── Player_Pitcher.py
│     └── Player_Runner.py
├── /Team
│     ├── Team_Defense.py
│     ├── Team_Hitter.py
│     ├── Team_Pitcher.py
│     └── Team_Runner.py
├── Player_Total.py
├── Team_Total.py
└── chromedriver
```