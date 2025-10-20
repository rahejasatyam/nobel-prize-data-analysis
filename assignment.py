# https://api.nobelprize.org/v1/prize.json


import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    """Fetch Nobel Prize data from API"""
    url = "https://api.nobelprize.org/v1/prize.json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from Nobel Prize API.")
    return response.json()


def analyze_data(data):
    """Analyze Nobel Prize data"""
    prizes = data["prizes"]

    years = [prize["year"] for prize in prizes]
    categories = [prize["category"] for prize in prizes]
    laureates = [laureate for prize in prizes if "laureates" in prize for laureate in prize["laureates"]]

    total_years = len(np.unique(years))
    total_prizes = len(prizes)
    total_laureates = len(laureates)
    unique_categories = len(np.unique(categories))

    # Count prizes per year
    year_counts = pd.Series(years).value_counts().sort_index()

    stats = {
        "total_years": total_years,
        "total_prizes": total_prizes,
        "total_laureates": total_laureates,
        "unique_categories": unique_categories,
        "year_counts": year_counts,
    }
    return stats


def display_results(stats):
    print("\n--- Nobel Prize Data Analysis ---")
    print(f"Total Years Present: {stats['total_years']}")
    print(f"Total Prizes Awarded: {stats['total_prizes']}")
    print(f"Total Laureates Honored: {stats['total_laureates']}")
    print(f"Unique Categories: {stats['unique_categories']}")
    print("\nPrizes Per Year:\n")
    print(stats["year_counts"])

    # Plot data
    plt.figure(figsize=(10, 5))
    stats["year_counts"].plot(kind="bar", title="Prizes Awarded Per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Prizes")
    plt.tight_layout()
    plt.show()


def main():
    data = load_data()
    stats = analyze_data(data)
    display_results(stats)


if __name__ == "__main__":
    main()