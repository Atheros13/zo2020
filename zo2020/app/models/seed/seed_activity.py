from app.models.tournament.activity.activity import Activity, ActivityType

sport = ActivityType(type='Sport')
sport.save()

sport_list = {
    
    'Athletics':['Track', 'Field'],
    'Swimming': [],
    
    }

for s in sport_list:

    a = Activity(type=sport, activity=s)
    a.save()

    for sp in sport_list[s]:

        a = Activity(type=sport, activity=s, sub_activity=sp)
        a.save()


