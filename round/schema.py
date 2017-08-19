from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from round import models as round_models


class RoundNode(DjangoObjectType):
    class Meta:
        model = round_models.Round
        interfaces = (relay.Node,)


class Query(AbstractType):
    round = relay.Node.Field(RoundNode)
    all_rounds = DjangoFilterConnectionField(RoundNode)
