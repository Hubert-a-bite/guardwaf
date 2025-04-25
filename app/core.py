from .rules import RULES
from .heuristics import score_request
from .botdetector import is_bot
from .ml_model import predict_ml

class WAFEngine:
    def inspect(self, request: dict) -> dict:
        score = score_request(request)
        threats = [r["name"] for r in RULES if r["pattern"].search(request.get("query", ""))]
        bot = is_bot(request.get("user_agent", ""))
        ml_detected = predict_ml(request.get("query", ""))

        return {
            "malicious": bool(threats or score > 50 or ml_detected),
            "threats": threats,
            "heuristic_score": score,
            "bot": bot,
            "ml_detected": ml_detected,
            "request": request
        }
