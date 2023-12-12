import streamlit as st
import pandas as pd
from PIL import Image
import random

# Load the CSV file
df = pd.read_csv('Completed-Books-with-Emotions.csv')

def recommend_books_by_emotion(emotion, num_recommendations=5):
    # Filter books based on emotion
    emotion_books = df[df['Emotions'] == emotion]

    # If there are fewer than 5 books for the given emotion, use all available books
    num_recommendations = min(num_recommendations, len(emotion_books))

    # Randomly select books
    recommended_books = emotion_books.sample(num_recommendations)

    return recommended_books

def main():
    st.title("Mood-Based Book Recommendation System")
    
    

    # Get unique emotions from the DataFrame
    emotions = df['Emotions'].unique()

    # Create a selectbox for emotion selection
    user_emotion = st.selectbox("Choose Your Reading Mood:", emotions)

    if st.button("Get Recommendations"):
        # Get recommended books
        recommended_books = recommend_books_by_emotion(user_emotion)


        # Display recommended books with title, author, and image
        st.subheader(f"Recommended Books for '{user_emotion}':")
        for index, row in recommended_books.iterrows():
            st.write(f"**Title:** {row['book_title']}")
            st.write(f"**Author:** {row['book_author']}")
            st.image(row['img_m'], caption=row['book_title'], width=300)
            
    
            
            
           

if __name__ == "__main__":
    main()