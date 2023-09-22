import marshmallow as ma
from invenio_vocabularies.services.schema import i18n_strings
from oarepo_runtime.marshmallow import BaseRecordSchema
from oarepo_runtime.validation import validate_date
from oarepo_vocabularies.services.schema import HierarchySchema

import nr_metadata.common.services.records.schema_common
from nr_metadata.common.services.records.schema_datatypes import (
    CreatorsItemNRAuthoritySchema,
    NRAuthoritySchema,
)


class NRDocumentRecordSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma.fields.Nested(lambda: NRDocumentMetadataSchema())

    syntheticFields = ma.fields.Nested(lambda: NRDocumentSyntheticFieldsSchema())


class NRDocumentMetadataSchema(
    nr_metadata.common.services.records.schema_common.NRCommonMetadataSchema
):
    class Meta:
        unknown = ma.RAISE

    additionalTitles = ma.fields.List(
        ma.fields.Nested(lambda: AdditionalTitlesItemSchema())
    )

    collection = ma.fields.String()

    contributors = ma.fields.List(ma.fields.Nested(lambda: NRAuthoritySchema()))

    creators = ma.fields.List(
        ma.fields.Nested(lambda: CreatorsItemNRAuthoritySchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    thesis = ma.fields.Nested(lambda: NRThesisSchema())


class NRThesisSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    dateDefended = ma.fields.String(validate=[validate_date("%Y-%m-%d")])

    defended = ma.fields.Boolean()

    degreeGrantors = ma.fields.List(ma.fields.Nested(lambda: NRDegreeGrantorSchema()))

    studyFields = ma.fields.List(ma.fields.String())


class AdditionalTitlesItemSchema(
    nr_metadata.common.services.records.schema_common.AdditionalTitlesSchema
):
    class Meta:
        unknown = ma.RAISE


class NRDegreeGrantorSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    hierarchy = ma.fields.Nested(lambda: HierarchySchema())

    title = i18n_strings


class NRDocumentSyntheticFieldsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE
