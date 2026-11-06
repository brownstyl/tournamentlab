#this is the codespace that validates the teams and store them.

def validate_team_name(name, team):

    if not isinstance(name, str):
        raise ValueError (f"invalid: the input [{name}] you provided should a string instead")

    cleaned_name = name.strip()
    normalized_name = cleaned_name.casefold()

    if len(normalized_name) < 2 or len(normalized_name) >30:
        raise ValueError(f"the team name [{normalized_name}] you provided must contain between 2 and 30 characters.")
    
    for names in team:
        if normalized_name == names['name'].casefold():
            raise ValueError (f"Error {(names['name'])}: already exist please add another name that does not exist")
        
    return cleaned_name


#generate team id based on the existing team list
def generate_team_id(team):
    if not team:
        return f"TM001"
    
    numeric_id = [int(t['id'].split('TM')[1]) for t in team]
    digit = max(numeric_id) + 1

    return f"TM{digit:03d}"


#Register team when the team provides their name and then generate an ID for them. with the
def register_team(name, team, fixture):
    if fixture:
        raise ValueError ("Oops Tournament is ongoing and registration has closed Please wait for another Season!!")

    if len(team) >= 8:
        raise ValueError ("Registration is full. Maximum of 8 teams allowed.") 
    
    team_validation = validate_team_name(name, team)
    gen_id = generate_team_id(team)

    team_list = {"id": gen_id, "name": team_validation}
    team.append(team_list)

    return team_list



