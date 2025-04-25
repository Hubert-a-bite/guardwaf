def score_request(req: dict) -> int:
    query = req.get("query", "")
    score = 0
    if "'" in query or "--" in query:
        score += 30
    if "<script" in query:
        score += 40
    if "../" in query:
        score += 20
    if ";" in query:
        score += 10
    return score
