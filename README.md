# Premier League 2023/24 Season Analysis

## Overview
An analysis of the 2023/24 Premier League season using Python, pandas and Matplotlib. It explores team performance, home advantage, finishing efficiency and consistency across the full 38 game season. 

## Data Source 
Data sourced from Kaggle: [English Premier League Matches 2023/2024 Season](https://www.kaggle.com/datasets/mertbayraktar/english-premier-league-matches-20232024-season)

## Key Findings

### Goals scored and conceded 
Manchester City led the league on average goals scored (2.53 per game), consistent with their title winning campaign. Sheffield United struggled the most going forward, averaging just 0.92 goals per game, ultimately reflecting their eventual relegtion. 

### Home Advantage 
The data confirms a clear, league-wide home advantage. It showed that teams scored more and conceded fewer goals at home on average compared to when playing away. The average goals at home was a 1.75 goal average across the league, above the trailing 1.5 average goals scored away from home. Highlighting the well known phrase 'home advantage'.

### Home advantage by team 
The size of the home advantage varied significantly by team. Newcastle United benefited most, with a home vs away goal difference gap of +1.63.  Interestingly, Burnley were an exception to the trend, performing worse at home than away (-0.58). The league's strongest teams Manchester City and Arsenal - showed relatively small home/away gaps, suggesting elite teams perform consistently regardless of venue, while mid-table teams rely more heavily on home advantage to boost results.

### Overperforming and underperforming Expected Goals (xG)
Comparing actual goals scored to expected goals (xG) reveals which teams converted their chances more efficiently than underlying data predicted and which teams underperformed despite creating good quality chances. The data shows that the teams at the top end of the league, Manchester City in particular, outperformed their expected goals(xG) by 0.41 goals per game (2.53 actual vs 2.12 expected). This is equivalent to roughly 15 additional goals across the season - suggesting genuinely elite finishing quality, consistent with their title-winning campaign in this particular season. On the other end of the spectrum, Sheffield United underperformed compared to their expected goals with a -0.94 goals per game (0.92 actual vs 1.015 expected). This aligns with the trend of their season, not creating a lot of chances as well as not being clinical enough with the little chances that they created. Matched with their poor defensive record, this was another huge contributing factor to their relegation at the end of the campaign. 

### Consistency in scoring 

Standard deviation of goals scored per match was used to identify which teams scored most consistently versus which teams swung between big wins and low-scoring games. The top seven teams in the data that showed the ability to score goals on a consistent basis, transfers to the exact same seven clubs that finished in the top seven places in the campaign, with Manchester City, Arsenal and Liverpool identically transferring their ability to score consistently, to their overall position at the end of the season. If we look at the other end of the table, out the bottom three teams in the data (Everton, Nottingham Forest and Sheffield United), only Sheffield United ended up getting relegated. This shows that goal scoring on a consistent basis isn't the be all and end all to staying in the top flight however, if your defensive consistency is equally as bad as your ability to score, ultimately the result is going to be the same as Sheffield United's season, ending up in the league below. However, at the top half of the table, scoring consistently matched with good defensive consistency, is a key ingredient to having a successful season, as proven by the data. 

### Possession vs goals scored
Comparing average possession to average goals scored per team explored whether greater ball possession translated directly into more goals. On the whole, the trend shows that the higher possession percentage that a team has, correlates into a higher goal output. For example Manchester City held the highest ball retention in the league as well as the highest goal output - a key feature in why they were champions in this specific season. However, Brighton and Hove Albion averaged a 59.8% possession rate compared to Arsenal's 58.1%. Despite the slight difference in a higher ball possession, they only averaged 1.44 goals per game, inferior to Arsenal's 2.39 per game output. This shows that despite being more in control of games, they lacked overall efficiency when forced to convert possession into goals. 

### Tools Used
- Python
- pandas
- Matplotlib
- NumPy (statistics)

## Personal Note
Having played professionally in the Championship and League One, this analysis reflects patterns often discussed within the game — particularly around home advantage. Having played at away grounds that have been hostile, with home fans in full voice supporting their team, is a real mental disadvantage that I believe is illustrated through the data. However, there are anomalies, as seen with Burnley. Sometimes when the team isn't reaching the capabilities that fans believe they can, the support can quickly turn to tumult within the ground. In turn, this can negatively impact a player's psyche, with some preferring to play away from home rather than feel the immense pressure of the home fans. 

## How to Run
1. Clone this repository
2. Install required packages: `pip3 install pandas matplotlib numpy`
3. Run `analysis.py`

## Visualisations
All charts generated by this project are saved as `.png` files within the repository, 
including goals scored/conceded comparisons, home vs away analysis, xG performance, 
possession vs goals, and scoring consistency.

