import csv

header = ['axi', 'Auto Low Goal Scored', 'Auto High Goal Scored', 'Auto Low Goal Miss', 'Auto High Goal Miss',
          'Teleop Low Goal Score', 'Teleop High Goal Score', 'Teleop Low Goal Miss', 'Teleop High Goal Miss',
          'Foul', 'Tech Foul', 'Defensive', 'Low Rung Success', 'Mid Rung Success', 'High Rung Success', 'Traversal Rung Success',
          'Ranking Points', 'Comments']
Team', 'T
with open('qrcode.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
