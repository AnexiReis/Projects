# process_data.py

import csv
from utils import calculate_average_performance, assign_role

def process_team_data():
    players = []
    performances = []  # List to store individual player performances for min/max calculation
    
    # Read players data
    with open('players.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            name, matches_played, goals, assists = row
            performance = calculate_average_performance([int(matches_played), int(goals), int(assists)])
            performance = round(performance, 3)  # Round performance to 3 decimal places
            role = assign_role(performance)
            players.append([name, performance, role])
            performances.append(performance)  # Store performance for later analysis
    
    # Sort players by performance in descending order
    players_sorted = sorted(players, key=lambda x: x[1], reverse=True)
    
    # Find the player with the highest and lowest performance
    highest_performance_player = players_sorted[0]  # First player after sorting is the highest
    lowest_performance_player = players_sorted[-1]  # Last player after sorting is the lowest

    # Print highest and lowest performing players
    print(f"Player of the Year: {highest_performance_player[0]} with a performance of {highest_performance_player[1]} (Highlighted in Light Green)")
    print(f"Lowest Performance: {lowest_performance_player[0]} with a performance of {lowest_performance_player[1]}")
    
    # Add a special label for the player of the year (highlight in light green in CSV)
    highest_performance_player.append("Player of the Year")  # Adding a label to the best player
    
    # Save the results to team_results.csv
    with open('team_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Performance', 'Role', 'Special Note'])  # Added Special Note column
        for player in players_sorted:
            # For Player of the Year, highlight in light green (we'll just use text here)
            if player == highest_performance_player:
                writer.writerow([player[0], player[1], player[2], player[3]])  # Add "Player of the Year" label
            else:
                writer.writerow([player[0], player[1], player[2], ""])  # No special note for others
    
    print('Results saved to team_results.csv')