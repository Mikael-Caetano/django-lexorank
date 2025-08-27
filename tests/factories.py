import factory

from django_lexorank.models import ScheduledRebalancing

from .models import Board, Status, Task, Team, User


class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    name = factory.Sequence(lambda n: f"team_{n}")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: f"user_{n}")
    team = factory.SubFactory(TeamFactory)


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    name = factory.Sequence(lambda n: f"board_{n}")


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status

    board = factory.SubFactory(BoardFactory)
    name = factory.Sequence(lambda n: f"status_{n}")


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    board = factory.SubFactory(BoardFactory)
    status = factory.SubFactory(StatusFactory)
    assigned_to = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: f"task_{n}")


class ScheduledRebalancingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ScheduledRebalancing
