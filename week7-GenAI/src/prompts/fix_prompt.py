def build_fix_prompt(question, issues):
    return f"""
The previous SQL has the following issues:

{chr(10).join(issues)}

Fix ONLY these issues.
Do NOT change unrelated logic.
Return ONLY the corrected SQL inside ```sql``` blocks.

Question:
{question}
"""
