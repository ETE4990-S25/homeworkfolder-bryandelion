import pandas as pd

# Load the dataset (Ensure you download and place the JSON file in the correct path)
FILE_PATH = 'romantic_movies.json'  # Update this with the actual dataset path

def load_dataset(file_path):
    """Loads the dataset from a JSON file and verifies content."""
    try:
        df = pd.read_json(file_path)
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')  # Convert date
        print("Dataset loaded successfully!\n")
        print(df.head())  # Display first few rows to verify content
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def recommend_romantic_movie(df, sub_genre=None, min_rating=0, start_year=1900, end_year=2025):
    """
    Recommends romantic movies based on user preferences.
    
    Parameters:
        df (DataFrame): The movie dataset.
        sub_genre (str): Specific sub-genre to filter (e.g., 'Comedy', 'Drama').
        min_rating (float): Minimum average rating.
        start_year (int): Earliest release year.
        end_year (int): Latest release year.

    Returns:
        DataFrame: Filtered DataFrame with recommended movies.
    """
    if df is None:
        print("No dataset loaded. Exiting.")
        return None

    # Filter for romantic movies
    romantic_movies = df[df['genres'].str.contains('Romance', case=False, na=False)]

    # Apply additional filters
    if sub_genre:
        romantic_movies = romantic_movies[romantic_movies['genres'].str.contains(sub_genre, case=False, na=False)]
    romantic_movies = romantic_movies[
        (romantic_movies['vote_average'] >= min_rating) &
        (romantic_movies['release_date'].dt.year >= start_year) &
        (romantic_movies['release_date'].dt.year <= end_year)
    ]

    return romantic_movies

# Load the dataset
movies_df = load_dataset(FILE_PATH)

# User Preferences (Modify as needed)
sub_genre = 'Comedy'  # Looking for Romantic Comedy movies
min_rating = 7.0      # Minimum rating out of 10
start_year = 2000     # Movies from year 2000 onwards
end_year = 2025       # Up to the year 2025

# Get recommendations
recommendations = recommend_romantic_movie(movies_df, sub_genre, min_rating, start_year, end_year)

# Display recommendations
if recommendations is not None and not recommendations.empty:
    print("\nRecommended Romantic Movies:")
    print(recommendations[['title', 'release_date', 'vote_average', 'genres']])
else:
    print("\nNo movies found matching your preferences.")
