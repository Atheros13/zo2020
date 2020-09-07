from app.models.hub import HubType

for type in ['Club', 'School', 'Other']:
    if not HubType.objects.filter(type=type):
        ht = HubType(type=type)
        ht.save()