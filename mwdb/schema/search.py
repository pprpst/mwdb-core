from marshmallow import Schema, fields, validates, ValidationError


class SearchRequestSchema(Schema):
    query = fields.Str(required=True, allow_none=False)

    @validates("query")
    def validate_query(self, value):
        if not value:
            raise ValidationError("Query can't be empty")
