from antlr4 import *
import gradio as gr
from AlteryxFunctionsTranspiler.AlteryxFunctionsLexer import AlteryxFunctionsLexer
from AlteryxFunctionsTranspiler.AlteryxFunctionsParser import AlteryxFunctionsParser
from AlteryxFunctionsTranspiler.AlteryxFunctionsVisitor import AlteryxFunctionsVisitor
from AlteryxFunctionsTranspiler.AlteryxToPython import AlteryxToPythonVisitor

def transpile_alteryx_to_python(alteryx_expression):
    input_stream = InputStream(alteryx_expression)
    lexer = AlteryxFunctionsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AlteryxFunctionsParser(stream)
    tree = parser.prog()

    visitor = AlteryxToPythonVisitor()
    return visitor.visit(tree)

demo = gr.Interface(
    fn=transpile_alteryx_to_python,
    inputs=["text",],
    outputs=["text"],
)

demo.launch()
