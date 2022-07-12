from users.models import Organisation, User
from customers.models import Customer
from contacts.models import Contact
from products.models import Product
from projects.models import Project
from samples.models import Sample
from tasks.models import Task
from django.core.exceptions import PermissionDenied
from django.db.models import Q


def products_filter(actual=None, chosen=None):
    query = Q()
    if actual is not None:
        query = Q(actual=actual)
    if chosen is not None:
        query.add(Q(id=chosen.id), Q.OR)
    return Product.objects.filter(query)


class AccessFilter:
    def __init__(self, request):
        self.request = request

    def organisations(self):
        organisations = [self.request.user.organisation]
        # если пользователь из Symrise, отбираются все организации
        if self.request.user.organisation.manager is None:
            organisations = Organisation.objects.all()
        return organisations

    def users(self):
        return User.objects.filter(organisation__in=self.organisations())

    def customers(self):
        return Customer.objects.filter(responsible__in=self.users())

    def customer(self, pk):
        customer = Customer.objects.get(id=pk)
        if customer not in self.customers():
            raise PermissionDenied()
        else:
            return customer

    def contacts(self, customer=None, actual=None, chosen=None):
        if customer is None:
            query = Q(customer__in=self.customers())
        else:
            query = Q(customer=customer)

        if actual is not None:
            query.add(Q(actual=actual), Q.AND)
        if chosen is not None:
            query.add(Q(id=chosen.id), Q.OR)

        return Contact.objects.filter(query)

    def contact(self, pk):
        contact = Contact.objects.get(id=pk)
        if contact.customer not in self.customers():
            raise PermissionDenied()
        else:
            return contact

    def projects(self, customer=None, archive=None, chosen=None):
        if customer is None:
            query = Q(customer__in=self.customers())
        else:
            query = Q(customer=customer)

        if archive is not None:
            query.add(Q(archive=archive), Q.AND)
        if chosen is not None:
            query.add(Q(id=chosen.id), Q.OR)
        return Project.objects.filter(query)

    def project(self, pk):
        project = Project.objects.get(id=pk)
        if project.customer not in self.customers():
            raise PermissionDenied()
        else:
            return project

    def samples(self):
        return Sample.objects.filter(customer__in=self.customers())

    def sample(self, pk):
        sample = Sample.objects.get(id=pk)
        if sample.customer not in self.customers():
            raise PermissionDenied()
        else:
            return sample

    def tasks(self):
        query = Q(customer__in=self.customers()) | Q(customer=None)
        query.add(
            Q(creator__in=self.users()) | Q(responsible__in=self.users()),
            Q.AND
        )
        return Task.objects.filter(query)

    def task(self, pk):
        task = Task.objects.get(id=pk)
        if task.creator not in self.users() or task.responsible not in self.users():
            raise PermissionDenied()
        else:
            return task

    def yes_no(self):
        return {'True': 'да',  'False': 'нет'}


def access_filter(request):
    return AccessFilter(request)
