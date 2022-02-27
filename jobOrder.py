import csv
import random


# Job


class Jobs:
    instances = []

    def __init__(self, name, unlock, weapon):
        self.name = row[0]
        self.unlock = row[1]
        self.weapon = row[4]
        __class__.instances.append(self)

    def __repr__(self):
        return "Name: % s unlock: % s weapon: % s" % (self.name, self.unlock, self.weapon)

    def __str__(self):
        return "% s unlocks at world" " % s and uses " "% s" % (self.name, self.unlock, self.weapon)


with open('Input/Job/JobInfo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        job = Jobs(row[0], row[1], row[4])
        # print(job)
        line_count += 1

with open('Input/Job/JobInfo.csv') as csv_file:
    job_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    with open('Output/Job/JobInfo.csv', mode="w", newline="") as out_file:
        for row in job_reader:
            rowrando = random.randint(1, 3)
            randIndex = random.randrange(len(Jobs.instances))
            randJobs = Jobs.instances[randIndex]
            row[1] = rowrando
            row[4] = randJobs.weapon
            job_writer = csv.writer(out_file, delimiter=',')
            job_writer.writerow(row)
