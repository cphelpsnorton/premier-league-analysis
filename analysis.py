import pandas as pd 
from matplotlib import pyplot as plt 
data = pd.read_csv('epl_2023_24.csv')
print(data.head())

#team with most goals on average
most_goals_team = data.groupby('Team')['GF'].mean().sort_values(ascending=False)
print(most_goals_team) 
# Visualise it
plt.figure(figsize=(12, 6))
most_goals_team.plot(kind='bar', color='skyblue')
plt.title('Average Goals Scored per Team, 2023/24 Season')
plt.xlabel('Team')
plt.ylabel('Average Goals per Match')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('most_goals_team.png')
plt.show()

#team with the least goals conceded
least_conceded_team = data.groupby('Team')['GA'].mean().sort_values(ascending=True)
print(least_conceded_team)
#Visualise it 
plt.figure(figsize=(12, 6))
least_conceded_team.plot(kind='bar', color='salmon')
plt.title('Team with Least Goals Conceded, 2023/24 Season')
plt.xlabel('Team')
plt.ylabel('Average Goals Conceded per Match')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('least_conceded_team.png')
plt.show()

#is there a home advantage in the league?
home_away_goals = data.groupby('Venue')[['GF', 'GA']].mean()
print(home_away_goals)
#visuialise it 
plt.figure(figsize=(12, 6))
home_away_goals.plot(kind='bar', color=['lightgreen', 'firebrick'])
plt.title('Home vs Away: Goals Scored and Conceded, 2023/24 Season')
plt.xlabel('Venue')
plt.ylabel('Average Goals per Match')
plt.xticks(rotation=0)
plt.legend(['Goals Scored', 'Goals Conceded'])
plt.tight_layout()
plt.savefig('home_away_comparison.png')
plt.show()
#team most consistent in scoring goals 
consistent_team = data.groupby('Team')['GF'].std().sort_values(ascending=True)
print(consistent_team)
#visualise it
plt.figure(figsize=(12, 6))
consistent_team.plot(kind='bar', color='orange')
plt.title('Most Consistent Goal Scoring Team, 2023-24 Season')
plt.xlabel('Team')
plt.ylabel('Standard Deviation of Goals Scored')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('consistent_team.png')
plt.show()

#team that overperformed/underperformed comparted to their expected goals (xG)
performance = data.groupby('Team')[['GF', 'xG']].mean()
performance['difference'] = performance['GF'] - performance['xG']
performance_overperformed = performance.sort_values('difference', ascending=False).head()
performance_underperformed = performance.sort_values('difference', ascending=True).head()
print(performance_overperformed)
print(performance_underperformed)
#visualise it 
plt.scatter(performance.index, performance['difference'], color='purple')
plt.title('Performance vs Expected Goals (xG), 2023/24 Season')
plt.xlabel('Team')
plt.ylabel('Difference in Goals Scored vs Expected Goals')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('performance_xG.png')
plt.show()

#possession related to goals scored 
possession_goals = data.groupby('Team')[['Poss', 'GF']].mean()
possession_goals = possession_goals.sort_values('Poss', ascending=False)
print(possession_goals)
#visualise it 
plt.scatter(possession_goals['Poss'], possession_goals['GF'], color='darkgreen')
plt.title('Possession vs Goals Scored, 2023/24 Season')
plt.xlabel('Average Possession (%)')
plt.ylabel('Average Goals Scored')
plt.tight_layout()
plt.savefig('possession_goals.png')
plt.show()

#team with the best home vs away goal difference
home_away_diff = data.groupby(['Team', 'Venue'])[['GF', 'GA']].mean()
home_away_diff['goal_difference'] = home_away_diff['GF'] - home_away_diff['GA']
home_away_diff = home_away_diff.reset_index()
home_away_pivot = home_away_diff.pivot(index='Team', columns='Venue', values='goal_difference')
home_away_pivot['home_advantage_gap'] = home_away_pivot['Home'] - home_away_pivot['Away']
print(home_away_pivot.sort_values('home_advantage_gap', ascending=False))
#visualise it 
plt.figure(figsize=(12, 6))
home_away_pivot_sorted = home_away_pivot.sort_values('home_advantage_gap', ascending=False)
home_away_pivot_sorted['home_advantage_gap'].plot(kind='bar', color='indigo')
plt.title('Home Advantage Gap by Team, 2023/24 Season')
plt.xlabel('Team')
plt.ylabel('Goal Difference: Home minus Away')
plt.axhline(0, color='black', linewidth=0.8)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('home_advantage_gap.png')
plt.show()