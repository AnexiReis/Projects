def calculate_average_performance(stats):
    # Calculate average performance based on matches, goals, and assists
    return sum(stats) / len(stats)

def assign_role(performance):
    # Assign roles based on performance
    if performance >= 15:
        return 'Star Player'
    elif performance >= 12:
        return 'Regular Player'
    elif performance >= 9:
        return 'Support Player'
    else:
        return 'Bench Warmer'
