import streamlit as st
import os
import random

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="StudySphere",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #0b111a;
    color: #f5f7fa;
}

section[data-testid="stSidebar"] {
    background-color: #0d1520;
    border-right: 1px solid #253044;
}

section[data-testid="stSidebar"] * {
    color: #f5f7fa;
}

.brand-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 5px;
}

.brand-subtitle {
    color: #8e99aa;
    font-size: 13px;
}

.divider {
    border-top: 1px solid #2a3445;
    margin: 25px 0;
}

.workspace-title {
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 20px;
}

.user-card {
    background: #182335;
    border: 1px solid #26344a;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 20px;
}

.answer-card {
    background: #101722;
    border-radius: 14px;
    padding: 25px;
    border: 1px solid #273348;
    line-height: 1.7;
}

.feature-card {
    background: #141d2b;
    border: 1px solid #28354a;
    border-radius: 14px;
    padding: 20px;
    min-height: 130px;
}

.feature-icon {
    font-size: 25px;
}

.feature-title {
    font-size: 18px;
    font-weight: 600;
    margin-top: 8px;
}

.feature-description {
    color: #9ca7b8;
    font-size: 14px;
    margin-top: 7px;
}

div.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: 1px solid #2d3a50;
    background-color: #182335;
    color: #ffffff;
    padding: 10px;
    font-weight: 600;
}

div.stButton > button:hover {
    border-color: #536b8d;
    background-color: #202d42;
}

[data-testid="stMetric"] {
    background-color: #141d2b;
    border: 1px solid #28354a;
    padding: 15px;
    border-radius: 12px;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Study"

if "study_topic" not in st.session_state:
    st.session_state.study_topic = ""

if "study_result" not in st.session_state:
    st.session_state.study_result = ""

if "quiz_topic" not in st.session_state:
    st.session_state.quiz_topic = ""

if "quiz_generated" not in st.session_state:
    st.session_state.quiz_generated = False

if "score" not in st.session_state:
    st.session_state.score = 0


# ============================================================
# OPTIONAL GEMINI FUNCTION
# ============================================================

def ask_gemini(prompt):

    try:
        from google import genai

        api_key = None

        try:
            api_key = st.secrets.get("GEMINI_API_KEY")
        except Exception:
            api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            return None

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception:
        return None


# ============================================================
# DEMO STUDY RESPONSE
# ============================================================

def generate_demo_explanation(topic):

    return f"""
## What is {topic}?

**{topic}** is an important concept that can be understood by
breaking it into smaller ideas and studying how those ideas work
together.

### Key Points

**1. Basic Concept**

The first step is to understand the definition and purpose of
{topic}.

**2. Main Components**

{topic} can be studied by identifying its important components,
functions, and characteristics.

**3. How It Works**

Understanding the process step-by-step makes the concept easier
to remember and apply.

**4. Applications**

The concepts related to {topic} can be applied to practical
situations and real-world problems.

**5. Exam Preparation**

For examinations, focus on definitions, important functions,
examples, advantages, disadvantages, and diagrams where applicable.

### Simple Explanation

StudySphere AI converts a topic into a structured explanation so
that students can understand difficult concepts more easily and
revise them effectively.
"""


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="brand-title">🪐 StudySphere</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="brand-subtitle">AI Learning Companion</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="divider"></div>',
        unsafe_allow_html=True
    )

    if st.button("🏠  Home"):
        st.session_state.page = "Home"

    if st.button("📚  Study"):
        st.session_state.page = "Study"

    if st.button("⚡  Quiz"):
        st.session_state.page = "Quiz"

    if st.button("🔄  Revision"):
        st.session_state.page = "Revision"

    if st.button("🗓️  Planner"):
        st.session_state.page = "Planner"

    st.markdown(
        '<div class="divider"></div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🎨 App Theme")

    st.selectbox(
        "Theme",
        ["Dark"],
        label_visibility="collapsed"
    )


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.markdown(
        '<div class="workspace-title">🏠 Welcome to StudySphere</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="answer-card">

    <h2>📚 Your AI Learning Companion</h2>

    <p>
    StudySphere is a learning companion designed to help students
    understand concepts, practice through quizzes, revise important
    topics, and organize their study activities.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <div class="feature-title">Study</div>
            <div class="feature-description">
            Get structured explanations for study topics.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Quiz</div>
            <div class="feature-description">
            Test your knowledge with practice questions.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔄</div>
            <div class="feature-title">Revision</div>
            <div class="feature-description">
            Quickly review important concepts before examinations.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🗓️</div>
            <div class="feature-title">Planner</div>
            <div class="feature-description">
            Organize your study activities and schedules.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI Assistance</div>
            <div class="feature-description">
            Use AI-powered explanations when an API key is configured.
            </div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# STUDY
# ============================================================

elif st.session_state.page == "Study":

    st.markdown(
        '<div class="workspace-title">📚 Study Workspace</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="user-card">
        <strong>You</strong>
        <p style="margin-top:10px;color:#c2cad6;">
        Enter a topic below to start learning.
        </p>
    </div>
    """, unsafe_allow_html=True)

    topic = st.text_input(
        "Study Topic",
        value=st.session_state.study_topic,
        placeholder="Example: Operating System",
        label_visibility="collapsed"
    )

    st.session_state.study_topic = topic

    col1, col2 = st.columns([3, 1])

    with col1:

        operation = st.selectbox(
            "Learning Mode",
            [
                "Explain Concept",
                "Summarize Topic",
                "Exam Notes",
                "Simple Explanation"
            ]
        )

    with col2:

        difficulty = st.selectbox(
            "Level",
            ["Beginner", "Intermediate", "Advanced"]
        )

    if st.button("✨ Generate Learning Content"):

        if not topic.strip():

            st.warning("Please enter a topic first.")

        else:

            prompt = f"""
            Explain the topic "{topic}" for a {difficulty} level student.

            Learning mode: {operation}

            Give a clear, structured educational response.
            Include important points and examples where appropriate.
            """

            with st.spinner("StudySphere is preparing your learning content..."):

                ai_result = ask_gemini(prompt)

                if ai_result:
                    st.session_state.study_result = ai_result
                else:
                    st.session_state.study_result = generate_demo_explanation(topic)

    if st.session_state.study_result:

        st.markdown(
            '<div class="answer-card">',
            unsafe_allow_html=True
        )

        st.markdown(st.session_state.study_result)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# QUIZ
# ============================================================

elif st.session_state.page == "Quiz":

    st.markdown(
        '<div class="workspace-title">⚡ Quiz</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Practice what you have learned and test your understanding."
    )

    quiz_topic = st.text_input(
        "Quiz Topic",
        placeholder="Example: Computer Networks"
    )

    number_of_questions = st.slider(
        "Number of Questions",
        5,
        10,
        5
    )

    if st.button("🎯 Generate Quiz"):

        if not quiz_topic.strip():

            st.warning("Please enter a topic.")

        else:

            st.session_state.quiz_topic = quiz_topic
            st.session_state.quiz_generated = True
            st.session_state.score = 0

    if st.session_state.quiz_generated:

        st.markdown(
            f"### 📝 Quiz: {st.session_state.quiz_topic}"
        )

        questions = [
            (
                "Which approach is most useful when learning a new concept?",
                ["Memorizing without understanding",
                 "Breaking the concept into smaller parts",
                 "Ignoring examples",
                 "Avoiding practice"],
                1
            ),
            (
                "Which activity is useful for exam preparation?",
                ["Revision",
                 "Avoiding questions",
                 "Skipping important topics",
                 "Not practicing"],
                0
            ),
            (
                "What helps improve understanding of difficult topics?",
                ["Clear explanations",
                 "Ignoring the topic",
                 "Random guessing",
                 "Skipping revision"],
                0
            ),
            (
                "Which activity helps test your knowledge?",
                ["Quiz",
                 "Ignoring notes",
                 "Avoiding practice",
                 "Skipping revision"],
                0
            ),
            (
                "What is an effective study habit?",
                ["Regular revision",
                 "Studying only at the last minute",
                 "Avoiding practice",
                 "Skipping difficult concepts"],
                0
            ),
            (
                "Why are examples useful?",
                ["They connect concepts with practical situations",
                 "They make concepts impossible",
                 "They remove understanding",
                 "They prevent learning"],
                0
            ),
            (
                "What should students do after learning a concept?",
                ["Review and practice it",
                 "Forget it",
                 "Avoid it",
                 "Never revise it"],
                0
            ),
            (
                "What is an important part of learning?",
                ["Understanding",
                 "Guessing",
                 "Skipping",
                 "Ignoring"],
                0
            ),
            (
                "Which tool can help organize study activities?",
                ["Study planner",
                 "Random notes",
                 "No schedule",
                 "None"],
                0
            ),
            (
                "Which method helps identify weak areas?",
                ["Practice tests",
                 "Avoiding questions",
                 "Skipping revision",
                 "Ignoring mistakes"],
                0
            )
        ]

        selected_questions = questions[:number_of_questions]

        answers = []

        for index, (question, options, correct) in enumerate(
            selected_questions
        ):

            answer = st.radio(
                f"{index + 1}. {question}",
                options,
                key=f"quiz_{index}"
            )

            answers.append(
                options.index(answer)
            )

        if st.button("✅ Submit Quiz"):

            score = 0

            for i, (_, _, correct) in enumerate(selected_questions):

                if answers[i] == correct:
                    score += 1

            st.session_state.score = score

            st.success(
                f"Your Score: {score}/{len(selected_questions)}"
            )

            percentage = (
                score / len(selected_questions)
            ) * 100

            st.progress(int(percentage))

            if percentage >= 80:
                st.success("Excellent work! 🎉")

            elif percentage >= 50:
                st.info("Good effort! Keep revising. 📚")

            else:
                st.warning(
                    "Keep practicing and review the topic again. 💪"
                )


# ============================================================
# REVISION
# ============================================================

elif st.session_state.page == "Revision":

    st.markdown(
        '<div class="workspace-title">🔄 Revision</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Create quick revision points for an important topic."
    )

    revision_topic = st.text_input(
        "Topic",
        placeholder="Example: DBMS"
    )

    if st.button("📝 Create Revision Notes"):

        if not revision_topic.strip():

            st.warning("Please enter a topic.")

        else:

            prompt = f"""
            Create concise revision notes for {revision_topic}.

            Include:
            - Definition
            - Important concepts
            - Key points
            - Examples
            - Exam-focused points
            """

            with st.spinner("Creating revision notes..."):

                ai_result = ask_gemini(prompt)

                if ai_result:

                    revision_result = ai_result

                else:

                    revision_result = f"""
### 🔄 Quick Revision: {revision_topic}

**Definition:**  
Understand the basic meaning and purpose of {revision_topic}.

**Key Points:**
- Learn the important concepts.
- Remember the main components.
- Understand how the process works.
- Study important examples.
- Review advantages and limitations.

**Exam Tip:**  
Focus on definitions, diagrams, examples, and important keywords.
"""

            st.markdown(
                '<div class="answer-card">',
                unsafe_allow_html=True
            )

            st.markdown(revision_result)

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


# ============================================================
# PLANNER
# ============================================================

elif st.session_state.page == "Planner":

    st.markdown(
        '<div class="workspace-title">🗓️ Study Planner</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Plan your study sessions and organize your preparation."
    )

    subject = st.text_input(
        "Subject / Topic",
        placeholder="Example: Java"
    )

    study_date = st.date_input(
        "Study Date"
    )

    duration = st.slider(
        "Study Duration (hours)",
        1,
        12,
        2
    )

    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )

    if st.button("➕ Add Study Plan"):

        if not subject.strip():

            st.warning("Please enter a subject or topic.")

        else:

            st.success("Study plan added successfully! ✅")

            st.markdown(f"""
            <div class="answer-card">

            ### 📅 Study Plan

            **Subject:** {subject}

            **Date:** {study_date}

            **Duration:** {duration} hour(s)

            **Priority:** {priority}

            </div>
            """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "StudySphere • AI Learning Companion • "
    "ShadowFox AI Engineer Internship"
)
