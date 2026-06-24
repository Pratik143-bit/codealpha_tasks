import pandas as pd

print("AI Music Recommendation System")

data = pd.read_csv("songs.csv")

mood = input("Enter Your Mood (Happy/Sad/Relaxed/Energetic): ").strip()

recommendations = data[data["Mood"].str.lower() == mood.lower()]

if not recommendations.empty:
    print("\nRecommended Songs:\n")
    for i, song in enumerate(recommendations["Song"], start=1):
        print(f"{i}. {song}")
else:
    print("No songs found for this mood.")
