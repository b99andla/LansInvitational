import graphene

import round.schema


class Query(round.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
