users=["rahul","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followes=["rohit","kohli","rahul"]


rahuls_follow_suggestion=set(users).difference(set(rahul_followers))

print(rahuls_follow_suggestion)


mutual_followers=set(rahul_followers).intersection(set(sanju_followes))

print(mutual_followers)