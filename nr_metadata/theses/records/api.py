from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.systemfields import ConstantField, RelationsField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from invenio_vocabularies.records.api import Vocabulary
from oarepo_runtime.relations import InternalRelation, PIDRelation, RelationsField

from nr_metadata.theses.records.dumper import ThesesDumper
from nr_metadata.theses.records.models import ThesesMetadata


class ThesesRecord(Record):
    model_cls = ThesesMetadata

    schema = ConstantField("$schema", "http://localhost/schemas/theses-1.0.0.json")

    index = IndexField("theses-theses-1.0.0")

    pid = PIDField(
        create=True, provider=RecordIdProviderV2, context_cls=PIDFieldContext
    )

    dumper_extensions = []
    dumper = ThesesDumper(extensions=dumper_extensions)

    relations = RelationsField(
        degreeGrantor=PIDRelation(
            "metadata.degreeGrantor",
            keys=["id", "title", "hierarchy", "id", "title", "hierarchy"],
            pid_field=Vocabulary.pid.with_type_ctx("degreeGrantor"),
        ),
        affiliations_item=PIDRelation(
            "metadata.creators.affiliations",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("creator_affiliations"),
        ),
        role=PIDRelation(
            "metadata.contributors.role",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("role"),
        ),
        affiliations_item_1=PIDRelation(
            "metadata.contributors.affiliations",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor_affiliations"),
        ),
        resourceType=PIDRelation(
            "metadata.resourceType",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("resourceType"),
        ),
        subjectCategories_item=PIDRelation(
            "metadata.subjectCategories",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("subjectCategories"),
        ),
        languages_item=PIDRelation(
            "metadata.languages",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("languages"),
        ),
        rights_item=PIDRelation(
            "metadata.rights",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("accessRights"),
        ),
        accessRights=PIDRelation(
            "metadata.accessRights",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("accessRights"),
        ),
        affiliations_item_2=PIDRelation(
            "metadata.relatedItems.itemCreators.affiliations",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("item-creator-affiliations"),
        ),
        role_1=PIDRelation(
            "metadata.relatedItems.itemContributors.role",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("role"),
        ),
        affiliations_item_3=PIDRelation(
            "metadata.relatedItems.itemContributors.affiliations",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("item-creator-affiliations"),
        ),
        itemRelationType=PIDRelation(
            "metadata.relatedItems.itemRelationType",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("itemRelationType"),
        ),
        itemResourceType=PIDRelation(
            "metadata.relatedItems.itemResourceType",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("resourceType"),
        ),
        funder=PIDRelation(
            "metadata.fundingReferences.funder",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("funders"),
        ),
        country=PIDRelation(
            "metadata.events.eventLocation.country",
            keys=["id", "title", "id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("country"),
        ),
    )