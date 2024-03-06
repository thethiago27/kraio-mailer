import unittest

from src.utils.template.templateParser import template_parser


class TestTemplateParser(unittest.TestCase):
    def test_template_parser(self):
        template = "<h1>Hello Mrs. {{name}}</h1>"
        args = {"name": "Doe"}
        result = template_parser(template, args)
        self.assertEqual(result, "<h1>Hello Mrs. Doe</h1>")

    def test_template_parser_no_args(self):
        template = "<h1>Hello Mrs. {{name}}</h1>"
        args = {}
        result = template_parser(template, args)
        self.assertEqual(result, "<h1>Hello Mrs. {{name}}</h1>")

    def test_template_parser_with_multiple_args(self):
        template = "<h1>Hello Mrs. {{name}} {{last_name}}</h1>"
        args = {"name": "Doe", "last_name": "John"}
        result = template_parser(template, args)
        self.assertEqual(result, "<h1>Hello Mrs. Doe John</h1>")

    def test_template_parser_no_template(self):
        template = ""
        args = {"name": "Doe"}
        result = template_parser(template, args)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()