import streamlit as st

st.set_page_config(page_title="Lebron's Portfolio", layout="wide")

st.title("Lebron James - Portfolio")
st.image("images/lebron.jpg", width=500)

st.subheader("About LeBron James")
st.write(
    """
    LeBron James is an American professional basketball player for the Los Angeles Lakers in the NBA. 
    Known for his versatility, leadership, and dominance, he is widely regarded as the greatest basketball player of all time.
    """
)

st.subheader("Career Highlights")
st.write(
    """
    - 🏆 4× NBA Champion (2012, 2013, 2016, 2020)
    - 🏅 4× NBA Most Valuable Player (MVP)
    - 🏀 19× NBA All-Star
    - 📈 NBA's All-Time Leading Scorer
    """
)

st.subheader("Off-Court Ventures")
st.write(
    """
    - 🎬 Founded SpringHill Company, a media production firm
    - 📚 Supports educational initiatives like the "I PROMISE School"
    - 🏀 Advocate for social justice and philanthropy
    """
)

st.subheader("Nicknames")
st.write(
    """
    - The King
    - King James
    - The Chosen One
    - L-Train
    - LBJ
    - The Akron Hammer
    - Bron Bron
    - Sunshine
    - GOAT
    - LeFather
    - etc. (so many more)
    """
)

st.write("---")
st.write("Created for CS 1301 Web Development Lab 02")
