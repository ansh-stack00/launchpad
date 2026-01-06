def refine_answer(llm, query, context, previous_answer):
    
    refinement_prompt = f"""
The previous answer may contain information NOT present in the context.

Context:
{context}

User Question:
{query}

Previous Answer:
{previous_answer}

Instructions:
- Answer ONLY using the given context
- If information is missing, say "Sorry, this information is not available in the document"
- Be concise and factual
"""

    response = llm.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": refinement_prompt}]
    )

    return response.choices[0].message.content
