tweet = input("Enter your tweet: ")
if len(tweet) <140:
    print(f"That {len(tweet)} char tweet will work.")
else:
    print(f"Your {len(tweet)} char tweet is {len(tweet) -140} too long.")