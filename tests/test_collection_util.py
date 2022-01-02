import src.adash as _


class TestAllkeys:
    def test_01(self):
        d = {"name": {"first": "John", "last": "Smith"}, "age": 36}
        res = _.allkeys(d)
        assert res == ["name.first", "name.last", "age"]

    def test_02(self):
        # https://json.org/example.html
        d = {
            "glossary": {
                "title": "example glossary",
                "GlossDiv": {
                    "title": "S",
                    "GlossList": {
                        "GlossEntry": {
                            "ID": "SGML",
                            "SortAs": "SGML",
                            "GlossTerm": "Standard Generalized Markup Language",
                            "Acronym": "SGML",
                            "Abbrev": "ISO 8879:1986",
                            "GlossDef": {
                                "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                "GlossSeeAlso": ["GML", "XML"],
                            },
                            "GlossSee": "markup",
                        }
                    },
                },
            }
        }
        assert _.allkeys(d) == [
            "glossary.title",
            "glossary.GlossDiv.title",
            "glossary.GlossDiv.GlossList.GlossEntry.ID",
            "glossary.GlossDiv.GlossList.GlossEntry.SortAs",
            "glossary.GlossDiv.GlossList.GlossEntry.GlossTerm",
            "glossary.GlossDiv.GlossList.GlossEntry.Acronym",
            "glossary.GlossDiv.GlossList.GlossEntry.Abbrev",
            "glossary.GlossDiv.GlossList.GlossEntry.GlossDef.para",
            "glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso",
            "glossary.GlossDiv.GlossList.GlossEntry.GlossSee",
        ]

    def test_03(self):
        assert _.allkeys({"a": 1, "b": 1}) == ["a", "b"]
