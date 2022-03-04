from ch6_profile_matcher import build_profile, match

print("Create 1st profile")
profile1 = build_profile()

print("Create 2nd profile")
profile2 = build_profile()

match_quality = match(profile1, profile2)

print(f"Match Quality: {match_quality}")