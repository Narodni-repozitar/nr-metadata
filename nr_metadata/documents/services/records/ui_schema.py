import marshmallow as ma
from oarepo_runtime.ui import marshmallow as l10n
from oarepo_runtime.ui.marshmallow import InvenioUISchema
from oarepo_vocabularies.services.ui_schema import (
    HierarchyUISchema,
    VocabularyI18nStrUIField,
)

import nr_metadata.common.services.records.ui_schema_common
from nr_metadata.common.services.records.ui_schema_datatypes import (
    CreatorsItemNRAuthorityUIUISchema,
    NRAuthorityUIUISchema,
)


class NRDocumentRecordUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma.fields.Nested(lambda: NRDocumentMetadataUISchema())

    syntheticFields = ma.fields.Nested(lambda: NRDocumentSyntheticFieldsUISchema())


class NRDocumentMetadataUISchema(
    nr_metadata.common.services.records.ui_schema_common.NRCommonMetadataUISchema
):
    class Meta:
        unknown = ma.RAISE

    additionalTitles = ma.fields.List(
        ma.fields.Nested(lambda: AdditionalTitlesItemUISchema())
    )

    collection = ma.fields.String()

    contributors = ma.fields.List(ma.fields.Nested(lambda: NRAuthorityUIUISchema()))

    creators = ma.fields.List(
        ma.fields.Nested(lambda: CreatorsItemNRAuthorityUIUISchema()), required=True
    )

    thesis = ma.fields.Nested(lambda: NRThesisUISchema())


class NRDocumentSyntheticFieldsUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    institutions = ma.fields.Nested(lambda: InstitutionsUISchema())

    keywords_cs = ma.fields.String()

    keywords_en = ma.fields.String()

    person = ma.fields.String()


class NRThesisUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    dateDefended = l10n.LocalizedDate()

    defended = ma.fields.Boolean()

    degreeGrantors = ma.fields.List(ma.fields.Nested(lambda: NRDegreeGrantorUISchema()))

    studyFields = ma.fields.List(ma.fields.String())


class AdditionalTitlesItemUISchema(
    nr_metadata.common.services.records.ui_schema_common.AdditionalTitlesUISchema
):
    class Meta:
        unknown = ma.RAISE


class InstitutionsUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    hierarchy = ma.fields.Nested(lambda: HierarchyUISchema())

    title = VocabularyI18nStrUIField()


class NRDegreeGrantorUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    hierarchy = ma.fields.Nested(lambda: HierarchyUISchema())

    title = VocabularyI18nStrUIField()
