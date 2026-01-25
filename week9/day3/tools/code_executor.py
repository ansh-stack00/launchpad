from autogen_core.tools import FunctionTool
import io
import contextlib
import traceback

def execute_code(code:str)->str:
    stdout = io.StringIO()
    local_vars = {}

    try:
        with contextlib.redirect_stdout(stdout):
            exec(code, {}, local_vars)
        output = stdout.getvalue()
        return output if output else str(local_vars)

    except Exception as e:
        return f"Error: {traceback.format_exc()}"
code_tool = FunctionTool(
    execute_code,
    "Execute Python code and return output."
)
