import unittest
from antlr4 import InputStream, CommonTokenStream
from AlteryxFunctionsTranspiler.AlteryxFunctionsLexer import AlteryxFunctionsLexer
from AlteryxFunctionsTranspiler.AlteryxFunctionsParser import AlteryxFunctionsParser
from AlteryxFunctionsTranspiler.AlteryxToPython import AlteryxToPythonVisitor


class TestConversions(unittest.TestCase):
    def setUp(self):
        """Setup shared transpiler for use in tests."""
        self.transpiler = AlteryxToPythonVisitor()

    def parse_and_transpile(self, input_text):
        """Helper function to parse and transpile input."""
        input_stream = InputStream(input_text)
        lexer = AlteryxFunctionsLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = AlteryxFunctionsParser(token_stream)
        tree = parser.prog()
        return self.transpiler.visit(tree)

    def test_toboolean(self):
        """Test TOBOOLEAN function."""
        # True cases
        self.assertEqual(self.parse_and_transpile('TOBOOLEAN("1")'), "bool(\"1\")")
        self.assertEqual(self.parse_and_transpile('TOBOOLEAN("true")'), "bool(\"true\")")
        self.assertEqual(self.parse_and_transpile('TOBOOLEAN("True")'), "bool(\"True\")")

        # False cases
        self.assertEqual(self.parse_and_transpile('TOBOOLEAN("0")'), "bool(\"0\")")
        self.assertEqual(self.parse_and_transpile('TOBOOLEAN("false")'), "bool(\"false\")")

    def test_tonumber(self):
        """Test TONUMBER function."""
        self.assertEqual(self.parse_and_transpile('TONUMBER("123")'), "float(\"123\")")
        self.assertEqual(self.parse_and_transpile('TONUMBER("123.45")'), "float(\"123.45\")")

    def test_tostring(self):
        """Test TOSTRING function."""
        self.assertEqual(self.parse_and_transpile('TOSTRING(123)'), "str(123)")
        self.assertEqual(self.parse_and_transpile('TOSTRING(123.45)'), "str(123.45)")


