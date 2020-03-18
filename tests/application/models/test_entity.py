from pytest import fixture
from instark.application.models import Entity


@fixture
def entity() -> Entity:
    return Entity()


def test_entity_creation(entity: Entity) -> None:
    assert isinstance(entity, Entity)


def test_entity_default_attributes(entity: Entity) -> None:
    assert entity.id == ""
    assert entity.created_at == 0
    assert entity.updated_at == 0
    assert entity.created_by == ''
    assert entity.updated_by == ''


def test_entity_attributes_from_dict() -> None:

    entity_dict = {
        "id": "ABC123",
        "created_at": 1520265903,
        "updated_at": 1520265903,
        "created_by": "07506ce5-edd7-4e1d-af9c-4e87bbc8e034",
        "updated_by": "07506ce5-edd7-4e1d-af9c-4e87bbc8e034"
    }

    entity = Entity(**entity_dict)

    assert entity.id == entity_dict['id']
    assert entity.created_by == entity_dict['created_by']
    assert entity.updated_by == entity_dict['updated_by']
    assert entity.created_at == entity_dict['created_at']
    assert entity.updated_at == entity_dict['updated_at']