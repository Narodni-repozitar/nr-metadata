import marshmallow as ma
from oarepo_runtime.ui.marshmallow import InvenioUISchema


class NRCommonRecordUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma.fields.Nested(lambda: NRCommonMetadataUISchema())
