from django.db.models import Q


class ChoiceFilter:
    def __init__(self, initial, request):
        self.list = initial
        self.request = request
        self.filter_choice = {}

    def choice(self, field, default=''):
        choice = self.request.GET.get(field, default)
        try:
            choice = int(choice)
        except:
            pass

        if choice != '':
            try:
                self.list = self.list.filter(query_options(field, choice))
            except:
                pass

        self.filter_choice[field] = choice


def choice_filter(initial, request):
    return ChoiceFilter(initial, request)


def query_options(field, choice):
    # customers
    if field == 'priority':
        return Q(priority=choice)
    if field == 'organisation_customer':
        return Q(responsible__organisation=choice)
    elif field == 'user_customer':
        return Q(responsible=choice)
    # contact
    elif field == 'actual':
        return Q(actual=choice)
    elif field == 'emailing':
        return Q(emailing=choice)
    # projects
    elif field == 'archive':
        return Q(archive=choice)
    # samples
    if field == 'organisation':
        return Q(customer__responsible__organisation=choice)
    elif field == 'user':
        return Q(customer__responsible=choice)
    elif field == 'important':
        return Q(important=choice)
    elif field == 'status':
        return Q(status=choice)
    elif field == 'status_date_from':
        return Q(status_date__gte=choice)
    elif field == 'status_date_till':
        return Q(status_date__lte=choice)
    # tasks
    elif field == 'done':
        return Q(done=choice)
    elif field == 'remind_from':
        return Q(reminder__gte=choice)
    elif field == 'remind_till':
        return Q(reminder__lte=choice)
    # products
    elif field == 'sanctioned':
        return Q(sanctioned=choice)
