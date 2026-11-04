#thi is the codespace that create the teams and store them.

def validate_team_name(name, team):

    cleaned_name = name.strip().title()
    
    if cleaned_name in team:
        return f"Error {[name]}: already exist please add another name that does not exist"

    return cleaned_name


def generate_team_id(team):
    if not team:
        return f"TM001"