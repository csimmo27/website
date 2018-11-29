#!/usr/bin/env python

students = ["Adkins.txt", "Bellman.txt", "Cooper.txt", "Doningly.txt", "Edwards.txt", "Finch.txt", "Green.txt", "Hopkins.txt", "Ingram.txt",
            "Jackson.txt", "Kill.txt", "Little.txt", "Murphy.txt", "Norton.txt", "Omejhad.txt", "Patterson.txt", "Quail.txt", "Rush.txt",
            "Smith.txt", "Thompson.txt", "Underhill.txt", "Vienna.txt", "Williams.txt", "Xlotel.txt", "Yankovich.txt", "Zimmerman.txt" ]
for me_file in students:
    scores = []
    total_score = 0.0
    with open(me_file, "r+") as my_file:
        data = my_file.readlines()
        for line in data:
            words = line.split()
        for item in words:
            scores.append(item)
        if scores[0] == "A":
                total_score += 1
        if scores[0] != "A":
                total_score += 0
        if scores[1] == "B":
                total_score += 1
        if scores[1] != "B":
                total_score += 0
        if scores[2] == "C":
                total_score += 1
        if scores[2] != "C":
                total_score += 0
        if scores[3] == "D":
                total_score += 1
        if scores[3] != "D":
                total_score += 0
        if scores[4] == "C":
                total_score += 1
        if scores[4] != "C":
                total_score += 0
        if scores[5] == "B":
                total_score += 1
        if scores[5] != "B":
                total_score += 0
        if scores[6] == "A":
                total_score += 1
        if scores[6] != "A":
                total_score += 0
        if scores[7] == "B":
                total_score += 1
        if scores[7] != "B":
                total_score += 0
        if scores[8] == "C":
                total_score += 1
        if scores[8] != "C":
                total_score += 0
        if scores[9] == "D":
                total_score += 1
        if scores[9] != "D":
                total_score += 0              
        percent = float(total_score)/10
        percent = float(percent)*100
        #print str(percent)+"%"
        my_file.write(str(percent)+"%")
students = ["Adkins.txt", "Bellman.txt", "Cooper.txt", "Doningly.txt", "Edwards.txt", "Finch.txt", "Green.txt", "Hopkins.txt", "Ingram.txt",
            "Jackson.txt", "Kill.txt", "Little.txt", "Murphy.txt", "Norton.txt", "Omejhad.txt", "Patterson.txt", "Quail.txt", "Rush.txt",
            "Smith.txt", "Thompson.txt", "Underhill.txt", "Vienna.txt", "Williams.txt", "Xlotel.txt", "Yankovich.txt", "Zimmerman.txt" ]
scores = []
total_score = 0.0
for me_file in students:
    with open(me_file, "r") as my_file:
        data = my_file.readlines()
        for line in data:
            words = line.split()
        for item in words:
            scores.append(item)
        if scores[0] == "A":
                total_score += 1
        if scores[0] != "A":
                total_score += 0
        if scores[1] == "B":
                total_score += 1
        if scores[1] != "B":
                total_score += 0
        if scores[2] == "C":
                total_score += 1
        if scores[2] != "C":
                total_score += 0
        if scores[3] == "D":
                total_score += 1
        if scores[3] != "D":
                total_score += 0
        if scores[4] == "C":
                total_score += 1
        if scores[4] != "C":
                total_score += 0
        if scores[5] == "B":
                total_score += 1
        if scores[5] != "B":
                total_score += 0
        if scores[6] == "A":
                total_score += 1
        if scores[6] != "A":
                total_score += 0
        if scores[7] == "B":
                total_score += 1
        if scores[7] != "B":
                total_score += 0
        if scores[8] == "C":
                total_score += 1
        if scores[8] != "C":
                total_score += 0
        if scores[9] == "D":
                total_score += 1
        if scores[9] != "D":
                total_score += 0
percent = float(total_score)/456.75
percent = float(percent)*100
print "Class Average: " + str(round(percent, 2)) + "%"