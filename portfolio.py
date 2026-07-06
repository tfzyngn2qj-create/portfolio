import streamlit as st

st.set_page_config(
    page_title="Mac Murray |  Math Portfolio",
    page_icon="✨",
    layout="wide"
)

st.title("Mackenzie Murray")
st.subheader("Mathematics Learning Portfolio")

st.markdown("""
I design engaging and interactive math lessons that help learners build intuition through puzzles,
visual exploration, and discovery.

My goal is to help students discover mathematical ideas before memorizing formal definitions.
""")

st.divider()

st.header("Featured Lessons")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("## 🧩 Discovering Logarithms")
    st.markdown("""
An interactive lesson where learners solve exponent puzzles, encounter a missing-exponent mystery,
and naturally discover logarithms.
""")

    st.markdown("""
**Learning goals:** exponents, roots, logarithms, inverse operations, mathematical discovery.
""")

    st.link_button("Launch Lesson", "https://discovering-logarithms-macmurray.streamlit.app/")
    st.link_button("View GitHub", "https://github.com/tfzyngn2qj-create/discovering-logarithms")

with col2:
    st.markdown("## 🤖 Can You Make This Robot Dance?")
    st.markdown("""
An interactive lesson where learners teach a robot dance moves and discover that matrices
can act as instruction cards for transforming shapes.
""")

    st.markdown("""
**Learning goals:** introducation to matrix transformations, coordinate geometry, matrix multiplication, order of operations.
""")

    st.link_button("Launch Lesson", "https://discovering-matrices-macmurray.streamlit.app/")
    st.link_button("View GitHub", "https://github.com/tfzyngn2qj-create/discovering-matrices")

st.divider()

st.header("Learning Design Philosophy")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💡 Curiosity before vocabulary")
    st.markdown("Learners should experience the need for a concept before learning its formal name.")

    st.markdown("### 🎨 Visual intuition before notation")
    st.markdown("Visuals help learners understand what symbols are trying to describe.")

with col2:
    st.markdown("### 🔭 Exploration before explanation")
    st.markdown("Students remember ideas more deeply when they discover patterns themselves.")

    st.markdown("### 🚀 Small wins build confidence")
    st.markdown("Complex topics become approachable when broken into clear, achievable steps.")

with col3:
    st.markdown("## 🟨 The Positive Test Paradox")
    st.markdown("""
A visual probability lesson explaining why a positive medical test doesn't always mean you're likely to have the condition.
""")

    st.markdown("""
**Learning goals:** conditional probability, Bayes' theorem, false positives, base rates, probability intuition.
""")


    if st.button("Watch Animation", key = "probability_video"):
        st.video("positive_test_paradox.mp4", start_time=0)
    st.link_button("View GitHub", "https://github.com/tfzyngn2qj-create/probability")

st.divider()

st.header("About Me")

st.markdown("""
I have a B.S. in Computational Mathematics with a minor in Physics from Colorado State University
and am pursuing graduate study in Data Science and AI at the University of Colorado.

My background combines mathematics, teaching, data science, and visual communication. I enjoy designing curriculums and 
lessons that make abstract concepts feel concrete, playful, and discoverable.
            
In my free time I enjoy puzzles, baking, and exploring the outdoors. Ilove all things gymnastics, hiking, biking, skiing, and playing fetch with my dog, Rory.
""")

st.divider()

st.header("Links")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("GitHub", "https://github.com/tfzyngn2qj-create")

with col2:
    st.link_button("LinkedIn", "www.linkedin.com/in/macrmurray")

with col3:
    st.link_button("Resume", "https://1drv.ms/w/c/23DBFDE56B185954/IQBHIPzdIYXBQZPOBjYff20ZAcHS7kOKRXUWYLD20m2S1FU")
