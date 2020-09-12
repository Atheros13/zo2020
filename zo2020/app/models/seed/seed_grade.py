from app.models.generic.person import Gender

for gender in ['Female', 'Male', 'Non-binary']:
    if not Gender.objects.filter(gender=gender):
        g = Gender(gender=gender)
        g.save()
