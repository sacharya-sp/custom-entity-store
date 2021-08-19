from custom_entity_store.models import Entity
from graphene_django import DjangoObjectType
import graphene


class EntityType(DjangoObjectType):
    class Meta:
        model = Entity
        fields = "__all__"


class Query(graphene.ObjectType):
    entities = graphene.List(EntityType, entity_type=graphene.UUID())
    entity = graphene.Field(EntityType, id=graphene.UUID())

    def resolve_entities(self, info, entity_type):
        return Entity.objects.filter(type=entity_type)

    def resolve_entity(self, info, id):
        return Entity.objects.get(pk=id)


class EntityInput(graphene.InputObjectType):
    id = graphene.UUID()
    type = graphene.UUID()
    data = graphene.String()


class CreateEntity(graphene.Mutation):
    class Arguments:
        entity = EntityInput(required=True)

    entity = graphene.Field(EntityType)

    @staticmethod
    def mutate(root, info, entity=None):
        db_entity = Entity(
            id=entity.id,
            type=entity.type,
            data=entity.data,
        )
        db_entity.save()

        return CreateEntity(entity=db_entity)


class UpdateEntity(graphene.Mutation):
    class Arguments:
        entity = EntityInput(required=True)

    entity = graphene.Field(EntityType)

    @staticmethod
    def mutate(root, info, entity=None):
        db_entity = Entity.objects.get(pk=entity.id)
        if db_entity:
            db_entity.id = entity.id
            db_entity.type = entity.type
            db_entity.data = entity.data
            db_entity.save()

        return UpdateEntity(entity=db_entity)


class DeleteEntity(graphene.Mutation):
    class Arguments:
        id = graphene.UUID()

    id = graphene.Field(graphene.UUID)

    @staticmethod
    def mutate(root, info, id):
        db_entity = Entity.objects.get(pk=id)
        db_entity.delete()

        return DeleteEntity(id=id)


class Mutation(graphene.ObjectType):
    create_entity = CreateEntity.Field()
    update_entity = UpdateEntity.Field()
    delete_entity = DeleteEntity.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
