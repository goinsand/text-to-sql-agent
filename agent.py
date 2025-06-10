# ===============================
# agent.py
# ===============================
def agent(question):
    # Placeholder logic for now
    sql = f"SELECT * FROM sales WHERE question = '{question}'"  # dummy logic
    confidence = 0.4  # default low confidence
    data = [
        {"region": "North", "sales": 120},
        {"region": "South", "sales": 90}
    ]
    graph = {
        "type": "bar",
        "x": [d['region'] for d in data],
        "y": [d['sales'] for d in data]
    }
    return {
        "question": question,
        "sql": sql,
        "confidence": confidence,
        "data": data,
        "graph": graph
    }
