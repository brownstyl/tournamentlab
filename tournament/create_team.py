#this is the codespace that validates the teams and store them.

def validate_team_name(name, team):

    cleaned_name = name.strip().title()
    
    if cleaned_name in team:
        return f"Error {[name]}: already exist please add another name that does not exist"

    return cleaned_name

#generate team id based on the existing team list
def generate_team_id(team):
    if not team:
        return f"TM001"
    
    numeric_id = [int(t['id'].split('TM')[1]) for t in team]
    digit = max(numeric_id) + 1

    return f"TM{digit:03d}"

    