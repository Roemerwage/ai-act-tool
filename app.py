from flask import Flask, render_template, request, session, redirect, url_for
from knowledge import architecture_rules 

app = Flask(__name__)
app.secret_key = 'secret_key_here'

@app.route('/')
def landing():
    session.clear()
    return render_template('landing.html')

@app.route('/page1', methods=['GET', 'POST'])
def page1():
    if request.method == 'POST':
        prohibited_values = request.form.getlist('prohibited')
        if prohibited_values:
            return render_template('results.html', grouped={"Prohibited": [{
                "article": "Article 5",
                "quote": "Prohibited practice selected.",
                "advice": "This AI system may not be developed or deployed under the EU AI Act."
            }]})
        session['page1'] = request.form
        return redirect(url_for('page2'))
    return render_template('page1.html')

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        session['page2'] = request.form
        return redirect(url_for('page3'))
    return render_template('page2.html')

@app.route('/page3', methods=['GET', 'POST'])
def page3():
    if request.method == 'POST':
        session['page3'] = request.form
        return redirect(url_for('results'))
    return render_template('page3.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        session['page3'] = request.form

    answers = {**session.get('page1', {}), **session.get('page2', {}), **session.get('page3', {})}
    grouped = {}

    is_exempt = 'article112_exemption' in answers

    high_risk_domains = {
        'employment', 'education', 'access', 'law', 'migration', 'justice',
        'biometric', 'infrastructure', 'medical', 'credit', 'toys', 'safety'
    }
    selected_domain = answers.get('category') or answers.get('domain')
    is_high_risk = selected_domain in high_risk_domains and not is_exempt
    is_gpai = selected_domain == 'general'

    features = answers.get('feature', [])
    if not isinstance(features, list):
        features = [features]
    triggers_transparency = any(f in [
        'chatbot', 'emotion', 'synthetic_image', 'synthetic_audio', 'synthetic_video'
    ] for f in features)
    # foundation_model on page 3 upgrades to GPAI obligations if no high-risk domain selected
    has_foundation_model = 'foundation_model' in features
    if has_foundation_model and not is_high_risk:
        is_gpai = True

    # GPAI providers (Arts. 51–55) have obligations beyond disclosure:
    # technical documentation → Auditability, cybersecurity → Security, incident response → Modifiability
    gpai_qas = {'Security', 'Auditability', 'Transparency', 'Modifiability'}

    for qa, entries in architecture_rules.items():
        if is_high_risk:
            grouped[qa] = entries
        elif is_gpai and qa in gpai_qas:
            grouped[qa] = entries
        elif triggers_transparency and qa == 'Transparency':
            # Art. 13 applies to high-risk systems only; Art. 50 applies to all transparency-triggering systems
            grouped[qa] = [e for e in entries if 'Article 50' in e['article']]

    # Derive classification label for the results template
    if is_high_risk:
        classification = 'high_risk'
    elif is_gpai:
        classification = 'gpai'
    elif triggers_transparency:
        classification = 'transparency_only'
    else:
        classification = 'none'

    return render_template('results.html', grouped=grouped, classification=classification)

if __name__ == '__main__':
    app.run(debug=True)
