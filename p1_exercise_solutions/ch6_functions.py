from ch6_profile_matcher import build_profile , match

print('Create 1st profile')
p1 = build_profile()

print('Create 2nd profile')
p2 = build_profile()

match_quality = match(p1, p2)
print("\nMatch Quality:", match_quality)