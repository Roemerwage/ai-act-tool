"""
ai_act_tool.py — single‑file Flask wizard (works without external files)

Run:
    python ai_act_tool.py

Flow:
 1.  Prohibited check  (Art 5)            → STOP if yes
 2.  Domain (Annex III high‑risk?)        → sets high_risk flag
 3.  Feature triggers (chatbot / biometric / deepfake) → Title IV

Result page groups obligations by quality attribute.
"""
from flask import Flask, request, redirect, render_template
from jinja2 import DictLoader

app = Flask(__name__)

# ────────────────────────────────────────────────────────────────────
# Templates (kept as strings, loaded via DictLoader)
# ────────────────────────────────────────────────────────────────────
BASE = """
<!doctype html><html lang=en>
<head>
  <meta charset="utf-8"><meta name=viewport content="width=device-width,initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <title>AI Act Assistant</title>
</head>
<body class="container py-4">
<h1 class="mb-4">AI Act Compliance Assistant</h1>
{% block body %}{% endblock %}
</body></html>
"""

PAGE1 = """
{% extends "base.html" %}{% block body %}
<form method="post">
  <p class="fw-semibold">Does your concept include <em>any</em> of these prohibited practices (Art 5)?</p>
  <ul>
    <li>Subliminal manipulation that distorts behaviour and causes harm</li>
    <li>Exploitation of minors / disabled vulnerabilities</li>
    <li>Social scoring of natural persons</li>
    <li>Real‑time public remote biometric identification for law‑enforcement</li>
  </ul>
  <div class="mt-3">
    <button name="prohibited" value="yes" class="btn btn-danger">Yes – it does</button>
    <button name="prohibited" value="no"  class="btn btn-primary">No – none of those</button>
  </div>
</form>
{% endblock %}
"""

PAGE2 = """
{% extends "base.html" %}{% block body %}
<form method="post">
  <p class="fw-semibold">Main domain / purpose of your AI system?</p>
  {% for code,label in domains %}
    <div class="form-check">
      <input class="form-check-input" type="radio" name="domain" id="d-{{code}}" value="{{code}}" required>
      <label class="form-check-label" for="d-{{code}}">{{label}}</label>
    </div>
  {% endfor %}
  <button class="btn btn-primary mt-3" type="submit">Next</button>
</form>
{% endblock %}
"""

PAGE3 = """
{% extends "base.html" %}{% block body %}
<form method="post">
  <p class="fw-semibold">Check any that apply:</p>
  <div class="form-check mb-2">
    <input class="form-check-input" type="checkbox" name="chatbot" id="chatbot">
    <label class="form-check-label" for="chatbot">Users will interact directly (chatbot / voice assistant)</label>
  </div>
  <div class="form-check mb-2">
    <input class="form-check-input" type="checkbox" name="biometric" id="biometric">
    <label class="form-check-label" for="biometric">Biometric identification / emotion recognition</label>
  </div>
  <div class="form-check mb-2">
    <input class="form-check-input" type="checkbox" name="deepfake" id="deepfake">
    <label class="form-check-label" for="deepfake">Generates realistic synthetic media (deepfakes)</label>
  </div>
  <button class="btn btn-primary mt-3">Show checklist</button>
</form>
{% endblock %}
"""

RESULTS = """
{% extends "base.html" %}{% block body %}
{% if stop %}
  <div class="alert alert-danger">
    <strong>Prohibited (Art 5)</strong><br>
    The described practice is banned under the AI Act — redesign or abandon the concept.
  </div>
{% else %}
  {% for attr,items in grouped.items() %}
    <h2 class="h5 mt-4">{{attr}}</h2>
    <ul class="list-unstyled">
      {% for r in items %}
        <li class="mb-3">
          <span class="text-muted">{{r.article}}</span><br>{{r.recommendation}}
        </li>
      {% endfor %}
    </ul>
  {% endfor %}
{% endif %}
<a href="/" class="btn btn-link mt-4">Start over</a>
{% endblock %}
"""

# Register templates
app.jinja_loader = DictLoader({
    "base.html": BASE,
    "page1.html": PAGE1,
    "page2.html": PAGE2,
    "page3.html": PAGE3,
    "results.html": RESULTS,
})

# ────────────────────────────────────────────────────────────────────
# Decision‑tree data + rules
# ────────────────────────────────────────────────────────────────────
HIGH_RISK_DOMAINS = {
    "recruitment":  "Recruitment / CV screening  (Annex III)",
    "education":    "Education / student assessment  (Annex III)",
    "healthcare":   "Healthcare diagnosis / medical device  (Annex III)",
    "law":          "Law‑enforcement investigation support  (Annex III)",
}

OTHER_DOMAINS = {
    "chatbot":      "General chatbot or virtual assistant",
    "genai":        "Generative AI for images/text (non‑high‑risk)",
    "other":        "Other / none of the above",
}

# Helper to decide high‑risk
def is_high_risk(domain): return domain in HIGH_RISK_DOMAINS

# Obligations  -----------------------------------------------------------------
RULES_PROHIBITED = [{
    "article":"Art 5 – Prohibited",
    "attribute":"N/A",
    "trigger":lambda ans: ans.get("prohibited")=="yes",
    "recommendation":"Banned practice — must not be developed or deployed."
}]

RULES_HIGH_RISK = [
    {"article":"Art 9 – Risk management","attribute":"Robustness",
     "trigger":lambda a: a.get("high_risk"), 
     "recommendation":"Maintain a continuous risk‑management file with hazard log, mitigations, and periodic review."},
    {"article":"Art 10 – Data governance","attribute":"Robustness",
     "trigger":lambda a: a.get("high_risk"),
     "recommendation":"Version datasets, test for bias, record provenance; document cleaning and labeling procedures."},
    {"article":"Art 11 – Technical docs","attribute":"Accountability",
     "trigger":lambda a: a.get("high_risk"),
     "recommendation":"Create a technical file (Annex IV): purpose, architecture, training process, performance metrics."},
    {"article":"Art 12 – Record‑keeping","attribute":"Accountability",
     "trigger":lambda a: a.get("high_risk"),
     "recommendation":"Implement tamper‑evident logging of inputs, outputs, model versions and operator actions."},
    {"article":"Art 13 – Transparency","attribute":"Transparency",
     "trigger":lambda a: a.get("high_risk"),
     "recommendation":"Provide user‑facing explanations of outputs and disclose AI capabilities & limitations."},
    {"article":"Art 14 – Human oversight","attribute":"Accountability",
     "trigger":lambda a: a.get("high_risk"),
     "recommendation":"Design human‑override / fail‑safe; ensure operators can halt or reverse AI decisions."},
    {"article":"Art 15 – Accuracy & cybersecurity","attribute":"Robustness",
     "trigger":lambda a: a.get("high_risk"),
     "recommendation":"Set performance thresholds; add adversarial‑input detection and regular penetration testing."},
]

RULES_TRANSPARENCY = [
    {"article":"Art 50(1) – AI interaction","attribute":"Transparency",
     "trigger":lambda a: a.get("chatbot"),
     "recommendation":"Show a notice that users are interacting with an AI system at each session start."},
    {"article":"Art 50(2) – Deepfake disclosure","attribute":"Transparency",
     "trigger":lambda a: a.get("deepfake"),
     "recommendation":"Watermark or label synthetic media so viewers know it is AI‑generated."},
    {"article":"Art 50(3) – Biometric consent","attribute":"Transparency",
     "trigger":lambda a: a.get("biometric"),
     "recommendation":"Provide prior notice and obtain explicit consent before biometric analysis or emotion detection."},
]

ALL_RULES = RULES_PROHIBITED + RULES_HIGH_RISK + RULES_TRANSPARENCY

# ────────────────────────────────────────────────────────────────────
# Routes
# ────────────────────────────────────────────────────────────────────
@app.route("/", methods=["GET", "POST"])
def page1():
    if request.method=="POST":
        prohibited=request.form["prohibited"]
        return redirect(f"/step2?prohibited={prohibited}")
    return render_template("page1.html")

@app.route("/step2", methods=["GET", "POST"])
def page2():
    if request.args.get("prohibited")=="yes":
        # skip rest → results with stop flag
        return redirect("/results?stop=1")
    if request.method=="POST":
        domain=request.form["domain"]
        qs=f"domain={domain}&high_risk={int(is_high_risk(domain))}"
        return redirect(f"/step3?{qs}")
    domains=list(HIGH_RISK_DOMAINS.items())+list(OTHER_DOMAINS.items())
    return render_template("page2.html", domains=domains)

@app.route("/step3", methods=["GET", "POST"])
def page3():
    if request.method=="POST":
        flags = {
            "chatbot":   int("chatbot" in request.form),
            "biometric": int("biometric" in request.form),
            "deepfake":  int("deepfake" in request.form),
        }
        query="&".join([f"{k}={v}" for k,v in flags.items()])
        return redirect(f"/results?{request.query_string.decode()}&{query}")
    return render_template("page3.html")

@app.route("/results")
def results():
    if request.args.get("stop"):
        return render_template("results.html", stop=True)
    # assemble answer dict
    ans = {
        "high_risk": bool(int(request.args.get("high_risk",0))),
        "chatbot":   bool(int(request.args.get("chatbot",0))),
        "biometric": bool(int(request.args.get("biometric",0))),
        "deepfake":  bool(int(request.args.get("deepfake",0))),
    }
    # evaluate rules
    applicable=[r for r in ALL_RULES if r["trigger"](ans)]
    grouped={}
    for r in applicable:
        attr=r["attribute"]
        grouped.setdefault(attr,[]).append(r)
    return render_template("results.html", grouped=grouped, stop=False)

# ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("* Starting Flask — http://127.0.0.1:5000/")
    app.run()
