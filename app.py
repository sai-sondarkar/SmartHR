
from fuzzywuzzy import fuzz
from flask import Flask, abort, jsonify, request



app = Flask(__name__)

@app.route('/', methods=['POST'])
def match_competency():
    data = request.get_json(force=True)
    
    candidate_competencies = data["candidate_compitencies"]
    team_leader_competencies = data["leader_competencies"]
    profile_competencies = data["profile_competencies"]
    tl_mul = data["tl_multiplier"]
    profile_mul = data["pl_multiplier"]
    
    candidate_competencies_strng = ""
    team_leader_competencies_strng = "" 
    profile_competencies_strng = ""


    for item in candidate_competencies:
        candidate_competencies_strng = candidate_competencies_strng + item + " ";
    
    for item in team_leader_competencies:
        team_leader_competencies_strng = team_leader_competencies_strng + item + " ";
    
    for item in profile_competencies:
        profile_competencies_strng = profile_competencies_strng + item + " ";    


    tl_candidate_score = fuzz.ratio(team_leader_competencies_strng,candidate_competencies_strng)
    pl_candidate_score = fuzz.ratio(profile_competencies_strng,candidate_competencies_strng)

    final_score = (tl_candidate_score * tl_mul) + (pl_candidate_score *profile_mul);
    

    output = {'score': int(final_score),'tl_s':tl_candidate_score,'pl_s':pl_candidate_score}
    print(output)
    return jsonify(results=output)

if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0')

    
