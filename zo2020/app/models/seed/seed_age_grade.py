from calendar import monthrange

from app.custom.classes import CustomYearlessDate
from app.models.generic.grade.age_grade import AgeGrade

values = [(True, None, None, '')]

for under in [True, False]:
    for age in range(1,121):
        for month in range(1,13):
            for day in range(1,32):                
                if day <= monthrange(2012, month)[1]: # 2012 was a leap year

                    date = CustomYearlessDate(day, month)

                    values.append((False, under, age, date))

for values in age_grades:

    open = values[0]
    under = values[1]
    age = values[2]
    date = values[3]

    if not AgeGrade.objects.filter(open=open, under=under, age=age, date=date):
        ag = AgeGrade(open=open, under=under, age=age, date=date)
        ag.save()
