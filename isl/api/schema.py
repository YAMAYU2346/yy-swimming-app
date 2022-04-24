import graphene
from graphene_django import DjangoObjectType
from .models import Match, Event, Team

class MatchType(DjangoObjectType):
    class Meta:
        model = Match

class EventType(DjangoObjectType):
    class Meta:
        model = Event

class AthletesType(graphene.InputObjectType):
    lane = graphene.Int()
    name = graphene.String()
    team = graphene.String()


class CreateEventType(graphene.InputObjectType):
    match_id = graphene.Int()
    number = graphene.Int()
    distance = graphene.String()
    style = graphene.String()
    class_1 = graphene.String()
    athletes = graphene.List(AthletesType)

class TeamType(DjangoObjectType):
    class Meta:
        model = Team

class TeamArgType(graphene.InputObjectType):
    match_id = graphene.Int()
    name = graphene.String()
    short_name = graphene.String()


class Query(graphene.ObjectType):
    matches = graphene.List(MatchType)

    def resolve_matches(self, info, **kwargs):
        return Match.objects.all()

    def resolve_match(self, info, **kwargs):
        id = kwargs.get('id')
        return Match.objects.get(pk=id)


class UpsertMatch(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=False)
        name = graphene.String()
        date = graphene.Date(required=True)
        teamNum = graphene.Int(required=False)
        entryUrl = graphene.String(required=False)

    match = graphene.Field(MatchType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        if 'id' in kwargs:
            match = Match.objects.get(id=kwargs["id"])
            match.name = kwargs['name']
            match.date = kwargs['date']
            match.team_num = kwargs['teamNum']
            match.entry_url = kwargs['entryUrl']
            match.save()
        else:
            match = Match.objects.create(**kwargs)
        # Notice we return an instance of this mutation
        return UpsertMatch(match=match)

class UpsertTeams(graphene.Mutation):
    class Arguments:
        teams = graphene.List(TeamArgType)

    teams = graphene.List(TeamType)

    @classmethod
    def mutate(cls, root, info, teams):
        print(teams)
        team_list = []
        for team in teams:
            if 'id' in team:
                _team = Team.objects.get(id=team["id"])
                _team.name = team['name']
                _team.short_name = team['short_name']
                _team.save()
                team_list.append(_team)
            else:
                print(team)
                _team = Team.objects.create(**team)
                team_list.append(_team)
        # Notice we return an instance of this mutation
        return UpsertTeams(teams=team_list)


class CreateEvents(graphene.Mutation):
    class Arguments:
        events = graphene.List(CreateEventType)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, events):
        print(events)
        # if 'id' in kwargs:
        #     match = Match.objects.get(id=kwargs["id"])
        #     match.name = kwargs['name']
        #     match.date = kwargs['date']
        #     match.team_num = kwargs['teamNum']
        #     match.entry_url = kwargs['entryUrl']
        #     match.save()
        # else:
        #     match = Match.objects.create(**kwargs)
        # Notice we return an instance of this mutation
        return CreateEvents(ok=True)

class Mutation(graphene.ObjectType):
    upsert_match = UpsertMatch.Field()
    upsert_teams = UpsertTeams.Field()
    create_events = CreateEvents.Field()
