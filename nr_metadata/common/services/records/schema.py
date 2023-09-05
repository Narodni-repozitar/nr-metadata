import marshmallow as ma


class NRCommonRecordSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma.fields.Nested(lambda: NRCommonMetadataSchema())
