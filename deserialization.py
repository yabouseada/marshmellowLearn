from marshmallow import Schema, fields, EXCLUDE, INCLUDE


class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()
    description = fields.Str()


incoming_book_data = {"title": "Code", "author": "Bobby", "description": "a cool book"}

book_schema = BookSchema(unknown=INCLUDE)
book = book_schema.load(incoming_book_data)

print(book)
