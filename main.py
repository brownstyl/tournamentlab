from tournament import create_team

team = [{"id":"TM", "name":"Arsenal"}]
try:

    testing = create_team.validate_team_name(True, team)
    print(testing)
    gen_id = create_team.generate_team_id(team)
    print(gen_id)
except ValueError as e:
    print("Error:", e)
    