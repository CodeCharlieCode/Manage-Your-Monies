from db.run_sql import run_sql
from models.profile import Profile

def save(profile):
    sql = "INSERT INTO profiles ( balance, total_budget ) VALUES(%s, %s) RETURNING id"
    values = [profile.balance, profile.total_budget]
    results = run_sql(sql, values)
    profile.id = results[0]['id']
    return profile

def select(id):
    profile = None
    sql = "SELECT * FROM profiles WHERE id =%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        profile = Profile(result['balance'], result['total_budget'])
    return profile

def select_all():
    profiles = []

    sql = "SELECT * FROM profiles"
    results = run_sql(sql)

    for result in results:
        profile = Profile(result['balance'], result['total_budget'], result['id'])
        profiles.append(profile)
    return profiles