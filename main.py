from utils import get_candidate, get_candidates_by_skill, get_candidates_by_name, load_candidates_from_json
from utils import path
if __name__ == '__main__':
    from flask import Flask, render_template

    app = Flask(__name__)


    @app.route("/")
    def page_candidates():
        candidates = load_candidates_from_json(path)
        return render_template('list.html', candidates=candidates)


    @app.route("/candidate/<int:candidate_id>")
    def page_single(candidate_id):
        candidate = get_candidate(candidate_id)
        return render_template('single.html', candidate=candidate)


    @app.route("/search/<candidate_name>")
    def page_searched_candidate(candidate_name):
        candidate = get_candidates_by_name(candidate_name)
        return render_template('search.html', candidate=candidate)

    @app.route("/skill/<skill_name>")
    def page_searched_by_skill_candidate(skill_name):
        candidates = get_candidates_by_skill(skill_name)
        return render_template('skill.html', candidates=candidates, skill_name=skill_name, count=len(candidates))


    app.run(debug=True)
