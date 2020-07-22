# Lesson 8 enumerate and zip

workDays = [19, 21, 22, 21, 20, 22]

print(workDays)
print(workDays[2])

enumeratedDays = list(enumerate(workDays))
print(enumeratedDays)

for pos, value in enumeratedDays:
    print('Position:', pos, 'value:', value)

months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthDays = list(zip(months, workDays))
print(monthDays)

for m, d in monthDays:
    print('Month:', m, 'Days:', d)

for pos, (m, d) in enumerate(zip(months, workDays)):
    print('Position:', pos, "moth:", m, 'days:', d)

# LAB

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

ptLead = list(zip(projects, leaders))
for p, l in ptLead:
    print('The leader of', p, 'is', l)

projectsLeadersDates = list(zip(projects, leaders, dates))
for p, l, d in projectsLeadersDates:
    print("The leader of", p, 'started', d, 'is', l)

projectsLeadersDates = zip(projects, leaders, dates)
for pos, (p, l, d) in enumerate(projectsLeadersDates):
    print(pos + 1, "- The leader of", p, 'started', d, 'is', l)
