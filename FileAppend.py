from csv import writer
from QRreader import*

row = barcode_info

with open('Warp 7 Scouting', 'a', newline='') as f:
    append = writer(f)
    append.writerow(row)

'''row = [teamid, taxiid, autolowscoreid, autohighscoreid, autolowmissid, autohighmissid,
       teleoplowscoreid, teleophighscoreid, teleoplowmissid, teleophighmissid,
       foulid, techfoulid, lowrungid, midrungid, highrungid, traversalrungid, rankingid, commentid]'''