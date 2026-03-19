import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="SMCM Course Planning Guide", layout="wide")

# Custom CSS for SMCM colors
st.markdown("""
<style>
    /* SMCM Color Palette */
    :root {
        --smcm-navy: #00205c;
        --smcm-gold: #f3c10e;
    }

    /* Header box styling */
    .header-box {
        background-color: var(--smcm-navy);
        color: white;
        padding: 30px;
        border-radius: 8px;
        margin-bottom: 30px;
        border-bottom: 6px solid var(--smcm-gold);
    }

    .header-box h1 {
        color: white !important;
        margin: 0;
        padding: 0;
        border: none;
    }

    .header-box h3 {
        color: white !important;
        margin: 5px 0;
        font-weight: 400;
    }

    .header-box p {
        color: rgba(255, 255, 255, 0.8);
        margin: 5px 0 0 0;
        font-style: italic;
    }

    /* Subheaders */
    h2 {
        margin-top: 20px;
    }

    /* Section headers with navy color */
    h3 {
        color: var(--smcm-navy) !important;
    }

    /* Selectbox labels - bold by default */
    .stSelectbox label {
        color: var(--smcm-navy) !important;
        font-weight: 700;
    }

    /* Selectbox border in navy */
    .stSelectbox > div > div {
        border-color: var(--smcm-navy) !important;
    }

    /* Horizontal rules with gold */
    hr {
        border-top: 2px solid var(--smcm-gold);
        margin: 20px 0;
    }

    /* Expander header with gold accent */
    .streamlit-expanderHeader {
        background-color: #f8f9fa;
        border-left: 4px solid var(--smcm-gold);
    }

    /* Checkboxes in neutral black/white to match expander header indicators */
    [data-testid="stCheckbox"] input[type="checkbox"] {
        accent-color: #333333;
    }

    /* Links in navy, gold on hover */
    a {
        color: var(--smcm-navy) !important;
    }

    a:hover {
        color: var(--smcm-gold) !important;
    }

    /* Info boxes with gold border */
    .stAlert {
        border-left: 4px solid var(--smcm-gold);
    }

    /* Markdown strong/bold in navy */
    strong {
        color: var(--smcm-navy);
    }

    /* Footer styling */
    .footer-box {
        background-color: var(--smcm-navy);
        color: white;
        padding: 25px;
        border-radius: 8px;
        margin-top: 40px;
        border-top: 6px solid var(--smcm-gold);
        text-align: center;
    }

    .footer-box p {
        margin: 3px 0;
        color: white !important;
    }

    .footer-box strong {
        color: white !important;
    }

    .footer-box .title {
        font-size: 0.85em;
        color: rgba(255, 255, 255, 0.8) !important;
    }

    .footer-box .email {
        color: var(--smcm-gold) !important;
        font-weight: 500;
    }

    /* Print styles */
    @media print {
        /* Hide Streamlit chrome */
        header[data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stSidebar"],
        [data-testid="stBottom"],
        .stDeployButton { display: none !important; }

        /* Hide selection controls and interactive widgets */
        [data-testid="stSelectbox"],
        [data-testid="stAlert"],
        [data-testid="stToggle"],
        [data-testid="stCheckbox"],
        .no-print { display: none !important; }

        /* Force color backgrounds to print */
        * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }

        /* Tighten spacing */
        .block-container { padding: 1rem !important; }

        /* Avoid page breaks inside course items */
        [data-testid="stHorizontalBlock"] { page-break-inside: avoid; }

        /* Page margins */
        @page { margin: 1.5cm; }
    }

    /* Course color-coding */
    .course-major-only {
        color: #1B7837;
    }

    .course-lead-only {
        color: #364B9A;
    }

    .course-multiple {
        color: #762A83;
    }

    .course-major2-only {
        color: #B05D0E;
    }

    .course-both-majors {
        color: #C0392B;
    }
</style>
""", unsafe_allow_html=True)

# Header with SMCM colors
st.markdown("""
<div class="header-box">
    <h1>Course Planning Self-Service Kiosk</h1>
    <h3>St. Mary's College of Maryland</h3>
    <p>Integrated LEAD Curriculum + Major Requirements</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state for course completion tracking
if 'completed_courses' not in st.session_state:
    st.session_state.completed_courses = {}

# ==============================================================================
# LEAD PATH DATA STRUCTURE
# ==============================================================================
# This structure contains all LEAD paths (Exploration and Inquiries)
# ==============================================================================

lead_paths = {
    "LEAD Exploration": {
        "description": "Take one course in each of 6 breadth areas (24 credits total). Foundational Study courses require a minimum D grade. Maintain 2.0 overall GPA.",
        "inquiry_electives": {
            "Arts": [
                "ART 204 - Introduction to Drawing (4 credits)",
                "ART 205 - Introduction to Visual Thinking (4 credits)",
                "ART 206 - Introduction to Painting (4 credits)",
                "ART 207 - Illustration (4 credits)",
                "ART 211 - Portrait Photography: Identity and Social Justice (4 credits)",
                "ART 212 - Introduction to Photography (4 credits)",
                "ART 213 - Book Arts: Text, Image, and Design (4 credits)",
                "ART 214 - Introduction to Digital Media Art (4 credits)",
                "ART 223 - Introduction to Printmaking 1: Traditional and Contemporary Techniques (4 credits)",
                "ART 224 - Introduction to Printmaking 2: The Matrix and the Painterly Print (4 credits)",
                "ART 233 - Topics in Art (4 credits)",
                "ART 239 - Painting and Drawing from Life (4 credits)",
                "ART 240 - Landscape Drawing and Painting (4 credits)",
                "ART 247 - Introduction to Animation: 2D Methods (4 credits)",
                "ART 248 - Introduction to Animation: Stop Motion (4 credits)",
                "ART 269 - Community Arts (4 credits)",
                "ENGL 270 - Creative Writing (4 credits)",
                "MUSA 180 - Choir Ensemble (3 credits, 4 semesters)",
                "MUSA 182 - Chamber Singers (3 credits, 4 semesters)",
                "MUSA 186 - Jazz Ensemble (3 credits, 4 semesters)",
                "MUSA 187 - Chamber Ensembles (1 credit, 4 semesters)",
                "MUSA 189 - Orchestra (3 credits, 4 semesters)",
                "MUSA 280-288 - Private Instruction (1 credit each, 4 semesters)",
                "MUSC 203 - Music Theory I (3 credits)",
                "PERF 110 - Critical Creativity in the Performing Arts (4 credits)",
                "TDPS 130 - Idea into Performance (4 credits)",
                "TDPS 170 - Stagecraft (4 credits)",
                "TDPS 171 - Elements of Design (4 credits)",
                "TDPS 221 - Film and Media Production Modes (4 credits)",
                "TDPS 228 - Media Production I (4 credits)",
                "TDPS 230 - Acting I (4 credits)",
                "TDPS 250 - Movement I (4 credits)",
                "TDPS 255 - Modern Dance I (4 credits)",
                "TDPS 258 - Dance in History (4 credits)",
                "TDPS 260 - Topics in Dance/Movement (4 credits)",
                "TDPS 275 - Costumes and Clothes in History (4 credits)",
                "TDPS 280 - Topics in Production (4 credits)"
            ],
            "Cultural Literacy": [
                "AADS 214 - Africa and the African Diaspora (4 credits)",
                "ANTH 230 - Cultural Anthropology (4 credits)",
                "ANTH 250 - Language and Culture (4 credits)",
                "ARTH 255 - Topics in Global Art History (4 credits)",
                "ASIA 200 - Introduction to Asian Studies (4 credits)",
                "ENGL 235 - Topics in Literature and Culture (4 credits)",
                "HIST 221 - Islamic Civilizations (4 credits)",
                "HIST 253 - Latin American Civilizations (4 credits)",
                "HIST 268 - Russian Civilization (4 credits)",
                "HIST 280 - Africa and the African Diaspora (4 credits)",
                "ILCC 102/201/202 - Chinese (if not used for Language Requirement)",
                "ILCF 102/201/202/206 - French (if not used for Language Requirement)",
                "ILCS 102/201/202/260 - Spanish (if not used for Language Requirement)",
                "ILCT 106 - Introduction to World Literature (4 credits)",
                "ILCX 205 - The Latinx Experience in the United States (4 credits)",
                "ILAS 210 - Latin American Cultural Studies (4 credits)",
                "LNG 102/201/202/206/260 - Language courses (if not used for Language Requirement)",
                "MUSC 216 - Introduction to the World's Music (4 credits)",
                "POSC 252 - Comparative Politics (4 credits)",
                "POSC 269 - International Politics (4 credits)",
                "PSYC 263 - Multicultural Psychology (4 credits)",
                "TDPS 210 - Japanese Performance Traditions (4 credits)",
                "TDPS 251 - Introduction to Traditional African Dance (4 credits)"
            ],
            "Humanities": [
                "ARTH 225 - Survey 1 (4 credits)",
                "ARTH 226 - Survey 2 (4 credits)",
                "ARTH 250 - Topics in Western Art History (4 credits)",
                "ENGL 106 - Introduction to Literature (4 credits)",
                "ENGL 130 - Literary Topics (4 credits)",
                "ENGL 204 - Reading and Writing in the Major (4 credits)",
                "ENGL 284 - Literature in History I: Before 1800 (4 credits)",
                "ENGL 285 - Literature in History II: After 1800 (4 credits)",
                "HIST 104 - Historical Foundations of the Modern World to 1450 (4 credits)",
                "HIST 105 - Western Civilization (4 credits)",
                "HIST 108 - History of the Modern World (4 credits)",
                "HIST 200 - United States History, 1776-1980 (4 credits)",
                "HIST 205 - History of Britain, 1066-1945 (4 credits)",
                "HIST 206 - East Asian Civilizations (4 credits)",
                "HIST 219 - Atlantic World Survey (4 credits)",
                "HIST 264 - Introduction to Museum Studies (4 credits)",
                "HIST 272 - Ancient Mediterranean (4 credits)",
                "HIST 276 - Twentieth-Century World (4 credits)",
                "MUSC 205 - The Story of Music (4 credits)",
                "MUSC 217 - The Jazz Makers (4 credits)",
                "MUSC 221 - Topics in Music History (4 credits)",
                "MUST 200 - Introduction to Museum Studies (4 credits)",
                "PHIL 101 - Introduction to Philosophy (4 credits)",
                "PHIL 120 - Introduction to Ethics (4 credits)",
                "TDPS 106 - Introduction to Dramatic Literature (4 credits)",
                "TDPS 220 - Introduction to Film and Media Studies (4 credits)",
                "TDPS 225 - Topics in Film and Media (4 credits)",
                "TDPS 332 - Theater in History (4 credits)",
                "WGSX 220 - Women, Gender, and Sexuality Studies (4 credits)"
            ],
            "Mathematics": [
                "COSC 120 - Introduction to Computer Science I (4 credits)",
                "ECON 253 - Economic Statistics (4 credits)",
                "MATH 131 - Survey of Mathematics (4 credits)",
                "MATH 151 - Calculus I (4 credits)",
                "MATH 152 - Calculus II (4 credits)",
                "MATH 200 - Discrete Mathematics (4 credits)",
                "MATH 221 - Introduction to Statistics (4 credits)",
                "MATH 255 - Vector Calculus (4 credits)",
                "MATH 256 - Linear Algebra (4 credits)",
                "MATH 281 - Foundations of Mathematics (4 credits)",
                "PHIL 215 - Systems of Logic (4 credits)",
                "POSC 200 - Scope and Methods of Political Science (4 credits)"
            ],
            "Natural Sciences with Lab": [
                "ASTR 154 - Solar System Astronomy with Laboratory (4 credits)",
                "ASTR 155 - Stellar Astronomy and Cosmology with Laboratory (4 credits)",
                "BIOL 101 - Contemporary Bioscience with Laboratory (4 credits)",
                "BIOL 105 - Principles of Biology I (4 credits)",
                "BIOL 105L - Principles of Biology Lab I (1 credit)",
                "CHEM 101 - Contemporary Chemistry with Laboratory (4 credits)",
                "CHEM 106 - General Chemistry II (4 credits)",
                "ENST 250 - Environmental Science (4 credits)",
                "ENST 265 - Earth Systems (4 credits)",
                "PHYS 104 - Basic Physics with Laboratory (4 credits)",
                "PHYS 121 - College Physics I (4 credits)",
                "PHYS 141 - General Physics I (4 credits)",
                "PHYS 142 - General Physics II (4 credits)",
                "PHYS 151 - Fundamentals of Physics I (4 credits)",
                "PHYS 152 - Fundamentals of Physics II (4 credits)",
                "PHYS 251 - Fundamentals of Physics III (4 credits)"
            ],
            "Social and Behavioral Sciences": [
                "ANTH 101 - Introduction to Anthropology (4 credits)",
                "ECON 102 - Principles of Microeconomics (4 credits)",
                "ECON 103 - Principles of Macroeconomics (4 credits)",
                "POSC 100 - Introduction to Politics (4 credits)",
                "PSYC 101 - Introduction to Psychology (4 credits)",
                "SOCI 101 - Introduction to Sociology (4 credits)"
            ]
        },
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "Exploration Course: Arts (4 credits) - choose one from the course list",
                "Exploration Course: Cultural Literacy (4 credits) - choose one from the course list",
                "Exploration Course: Humanities (4 credits) - choose one from the course list",
                "ENST 250 - Environmental Science (counts toward LEAD science breadth; or choose another course from the full list) (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship (transfers/dual-enrollment: LEAD 311 optional)",
                "Exploration Course: Mathematics (4 credits) - choose one from the course list",
                "Exploration Course: Social and Behavioral Sciences (4 credits) - choose one from the course list"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Climate Inquiry": {
        "description": "Understanding climate change through scientific, social, cultural, and political perspectives (17-21 credits)",
        "inquiry_electives": {
            "Natural Sciences": [
                "BIOL 101 - Contemporary Bioscience with Laboratory (4 credits)",
                "CHEM 106 - General Chemistry II (4 credits)",
                "ENST 250 - Environmental Science (4 credits)",
                "ENST 265 - Earth Systems (4 credits)",
                "MRNE 110 - Introduction to Marine Science (4 credits)"
            ],
            "Mathematics": [
                "COSC 120 - Introduction to Computer Science I (4 credits)",
                "MATH 131 - Survey of Mathematics (4 credits)"
            ],
            "Humanities and Cultural Literacy": [
                "PHIL 321 - Environmental Ethics (4 credits)",
                "HIST 396 - Topics in Comparative, Thematic, or Global History (4 credits)"
            ],
            "Arts and Humanities": [
                "ENGL 201 - Topics in Writing (4 credits)",
                "ART 240 - Landscape Drawing and Painting (4 credits)",
                "ART 269 - Community Arts (4 credits)"
            ]
        },
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "ENST 100 - Environment and Society (Anchor Course, 4 credits)",
                "ENST 250 - Environmental Science (counts toward LEAD science breadth; or choose BIOL 101, CHEM 106, ENST 265, or MRNE 110) (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship (transfers/dual-enrollment: LEAD 311 optional)",
                "Mathematics: Computer Science or Survey Mathematics (4 credits)",
                "Humanities/Cultural Literacy: Environmental Ethics or Comparative History (4 credits)",
                "Arts/Humanities: Writing, Landscape Art, or Community Arts (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Justice Inquiry": {
        "description": "Examination of racial, gender, economic, and environmental injustices and their intersections (17-21 credits)",
        "inquiry_electives": {
            "Humanities, Cultural Literacy": [
                "ARTH 250 - Topics in Western Art History (4 credits)",
                "ARTH 255 - Topics in Global Art History (4 credits)",
                "PHIL 120 - Introduction to Ethics (4 credits)",
                "PHIL 321 - Environmental Ethics (4 credits)",
                "PHIL 323 - Bioethics (4 credits)"
            ],
            "Mathematics": [
                "COSC 120 - Introduction to Computer Science I (4 credits)",
                "MATH 131 - Survey of Mathematics (4 credits)"
            ],
            "Social and Behavioral Sciences, Cultural Literacy": [
                "ENST 285 - Topics in Environmental Policy & Social Sciences (4 credits)",
                "POSC 100 - Introduction to Politics (4 credits)",
                "SOCI 101 - Introduction to Sociology (4 credits)"
            ],
            "Arts": [
                "ART 269 - Community Arts (4 credits)",
                "TDPS 390 - Theater Seminar: Production Contexts (2-4 credits)"
            ],
            "Natural Sciences with Lab": [
                "ASTR 154 - Solar System Astronomy with Laboratory (4 credits)",
                "ASTR 155 - Stellar Astronomy and Cosmology with Laboratory (4 credits)",
                "BIOL 101 - Contemporary Bioscience with Laboratory (4 credits)",
                "BIOL 105 - Principles of Biology I (4 credits)",
                "BIOL 105L - Principles of Biology Lab I (1 credit)",
                "CHEM 101 - Contemporary Chemistry with Laboratory (4 credits)",
                "CHEM 106 - General Chemistry II (4 credits)",
                "ENST 265 - Earth Systems (4 credits)",
                "PHYS 104 - Basic Physics with Laboratory (4 credits)",
                "PHYS 121 - College Physics I (4 credits)",
                "PHYS 141 - General Physics I (4 credits)",
                "PHYS 142 - General Physics II (4 credits)",
                "PHYS 151 - Fundamentals of Physics I (4 credits)",
                "PHYS 152 - Fundamentals of Physics II (4 credits)",
                "PHYS 251 - Fundamentals of Physics III (4 credits)"
            ]
        },
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "Humanities/Cultural Literacy: Ethics, Environmental Ethics, or Bioethics (4 credits)",
                "Mathematics: Computer Science or Survey Mathematics (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship (transfers/dual-enrollment: LEAD 311 optional)",
                "Social/Behavioral Sciences: Environmental Policy, Politics, or Sociology (4 credits)",
                "Arts: Community Arts or Theater Production (2-4 credits)",
                "Natural Sciences with Lab: Astronomy, Biology, Chemistry, Environmental Science, or Physics (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Public and Environmental Health Inquiry": {
        "description": "Exploring relationships between health policy, behavior, climate change, and health disparities (17-21 credits)",
        "inquiry_electives": {
            "Natural Sciences": [
                "BIOL 101 - Contemporary Bioscience with Laboratory (4 credits)",
                "BIOL 105 - Principles of Biology I (4 credits)",
                "BIOL 105L - Principles of Biology Lab I (1 credit)",
                "CHEM 101 - Contemporary Chemistry with Laboratory (4 credits)",
                "CHEM 106 - General Chemistry II (4 credits)",
                "ENST 250 - Environmental Science (4 credits)"
            ],
            "Humanism and Ethics": [
                "PHIL 120 - Introduction to Ethics (4 credits)",
                "PHIL 321 - Environmental Ethics (4 credits)",
                "PHIL 323 - Bioethics (4 credits)"
            ],
            "Social and Behavioral Sciences": [
                "ANTH 101 - Introduction to Anthropology (4 credits)",
                "ECON 102 - Principles of Microeconomics (4 credits)",
                "POSC 100 - Introduction to Politics (4 credits)",
                "PSYC 101 - Introduction to Psychology (4 credits)",
                "SOCI 101 - Introduction to Sociology (4 credits)"
            ],
            "Communication and Art": [
                "ART 204 - Introduction to Drawing (4 credits)",
                "ART 205 - Introduction to Visual Thinking (4 credits)",
                "ART 206 - Introduction to Painting (4 credits)",
                "ART 207 - Illustration (4 credits)",
                "ART 211 - Portrait Photography: Identity and Social Justice (4 credits)",
                "ART 212 - Introduction to Photography (4 credits)",
                "ART 213 - Book Arts: Text, Image, and Design (4 credits)",
                "ART 214 - Introduction to Digital Media Art (4 credits)",
                "ART 217 - Introduction to Digital Photography (4 credits)",
                "ART 223 - Introduction to Printmaking 1: Traditional and Contemporary Techniques (4 credits)",
                "ART 224 - Introduction to Printmaking 2: The Matrix and the Painterly Print (4 credits)",
                "ART 233 - Topics in Art (4 credits)",
                "ART 239 - Painting and Drawing from Life (4 credits)",
                "ART 240 - Landscape Drawing and Painting (4 credits)",
                "ART 247 - Introduction to Animation: 2D Methods (4 credits)",
                "ART 269 - Community Arts (4 credits)",
                "ENGL 201 - Topics in Writing (4 credits)"
            ]
        },
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "IDIS 122 - Gateway Course (4 credits)",
                "ENST 250 - Environmental Science (counts toward LEAD science breadth; or choose BIOL 101, BIOL 105+105L, CHEM 101, or CHEM 106) (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship (transfers/dual-enrollment: LEAD 311 optional)",
                "Humanism/Ethics: Ethics or Bioethics (4 credits)",
                "Social/Behavioral Sciences: Anthropology, Economics, Politics, Psychology, or Sociology (4 credits)",
                "Communication/Art: Visual Arts or Writing (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Gender and Power Inquiry": {
        "description": "Interdisciplinary examination of gender and sexuality's intersection with race, class, nationality, and ability (17-21 credits)",
        "inquiry_electives": {
            "Mathematics, Cultural Literacy": [
                "MATH 132 - Calling BS (4 credits)"
            ],
            "Social and Behavioral Sciences, Cultural Literacy": [
                "WGSX 220 - Women, Gender, and Sexuality Studies (4 credits)",
                "WGSX 350 - Advanced Topics in Women, Gender, and Sexuality Studies (4 credits)"
            ],
            "Arts": [
                "ART 205 - Introduction to Visual Thinking (4 credits)",
                "ART 212 - Introduction to Photography (4 credits)",
                "ART 214 - Introduction to Digital Media Art (4 credits)",
                "ART 269 - Community Arts (4 credits)",
                "TDPS 332 - Theater in History (4 credits)"
            ],
            "Natural Sciences with Lab": [
                "ASTR 154 - Solar System Astronomy with Laboratory (4 credits)",
                "ASTR 155 - Stellar Astronomy and Cosmology with Laboratory (4 credits)",
                "BIOL 101 - Contemporary Bioscience with Laboratory (4 credits)",
                "BIOL 105 - Principles of Biology I (4 credits)",
                "BIOL 105L - Principles of Biology Lab I (1 credit)",
                "CHEM 101 - Contemporary Chemistry with Laboratory (4 credits)",
                "CHEM 106 - General Chemistry II (4 credits)",
                "ENST 265 - Earth Systems (4 credits)",
                "PHYS 104 - Basic Physics with Laboratory (4 credits)",
                "PHYS 121 - College Physics I (4 credits)",
                "PHYS 141 - General Physics I (4 credits)",
                "PHYS 142 - General Physics II (4 credits)",
                "PHYS 151 - Fundamentals of Physics I (4 credits)",
                "PHYS 152 - Fundamentals of Physics II (4 credits)",
                "PHYS 251 - Fundamentals of Physics III (4 credits)"
            ]
        },
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "MATH 132 - Calling BS (Mathematics/Cultural Literacy, 4 credits)",
                "Social/Behavioral Sciences: Women, Gender, and Sexuality Studies (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship (transfers/dual-enrollment: LEAD 311 optional)",
                "Arts: Photography, Digital Media, Community Arts, or Theater (4 credits)",
                "Natural Sciences with Lab: Astronomy, Biology, Chemistry, Environmental Science, or Physics (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Global Studies Inquiry": {
        "description": "Understanding international politics, cultures, and systems (17-21 credits)",
        "inquiry_electives": {
            "Mathematics": [
                "ECON 253 - Economic Statistics (4 credits)",
                "MATH 131 - Survey of Mathematics (4 credits)",
                "MATH 151 - Calculus I (4 credits)",
                "MATH 152 - Calculus II (4 credits)",
                "SOCI 201 - Social Statistics (4 credits)"
            ],
            "Global and Non-Western Perspectives": [
                "AADS 214 - Africa and the African Diaspora (4 credits)",
                "ASIA 200 - Introduction to Asian Studies (4 credits)",
                "HIST 104 - Historical Foundations of the Modern World to 1450 (4 credits)",
                "HIST 108 - History of the Modern World (4 credits)",
                "HIST 109 - History of Religion (4 credits)",
                "PHIL 101 - Introduction to Philosophy (4 credits)"
            ],
            "Cultural Expression": [
                "ENGL 285 - Literature in History II: After 1800 (4 credits)",
                "MUSC 216 - Introduction to the World's Music (4 credits)",
                "TDPS 221 - Film and Media Production Modes (4 credits)"
            ],
            "Natural Sciences with Lab": [
                "ASTR 154 - Solar System Astronomy with Laboratory (4 credits)",
                "ASTR 155 - Stellar Astronomy and Cosmology with Laboratory (4 credits)",
                "ENST 250 - Environmental Science (4 credits)",
                "ENST 265 - Earth Systems (4 credits)",
                "MRNE 220 - Physical Oceanography (4 credits)"
            ]
        },
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "POSC 100 - Gateway Course (4 credits)",
                "Mathematics: Economics, Statistics, or Calculus (4 credits)",
                "ENST 250 - Environmental Science (counts toward LEAD science breadth; or choose ASTR 154/155, ENST 265, or MRNE 220) (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship (transfers/dual-enrollment: LEAD 311 optional)",
                "Global/Non-Western Perspectives: African Diaspora, Asian Studies, History, or Philosophy (4 credits)",
                "Cultural Expression: Literature, World Music, or Film/Media (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Asia in the World Inquiry": {
        "description": "Contextualizing Asia's role within global frameworks (17-21 credits)",
        "inquiry_electives": {
            "Next Level Contexts": [
                "ECON 372 - Economics of Developing Countries (4 credits)",
                "HIST 206 - East Asian Civilizations (4 credits)",
                "HIST 221 - Islamic Civilizations (4 credits)",
                "PHIL 351 - East Asian Philosophies: Confucianism, Daoism, & Zen (4 credits)",
                "PHIL 352 - South Asian Philosophies: Hinduism, Buddhism, & Islam (4 credits)",
                "POSC 252 - Comparative Politics (4 credits)",
                "POSC 269 - International Politics (4 credits)",
                "POSC 333 - Asian Politics (4 credits)"
            ],
            "Creative/Interpretive Methodologies": [
                "ART 205 - Introduction to Visual Thinking (4 credits)",
                "ART 211 - Portrait Photography: Identity and Social Justice (4 credits)",
                "ART 212 - Introduction to Photography (4 credits)",
                "ART 214 - Introduction to Digital Media Art (4 credits)",
                "ART 239 - Painting and Drawing from Life (4 credits)",
                "ART 269 - Community Arts (4 credits)",
                "ENGL 270 - Creative Writing (4 credits)",
                "TDPS 130 - Idea into Performance (4 credits)",
                "TDPS 220 - Introduction to Film and Media Studies (4 credits)",
                "TDPS 221 - Film and Media Production Modes (4 credits)",
                "TDPS 228 - Media Production I (4 credits)"
            ],
            "Computational Methodologies": [
                "COSC 120 - Introduction to Computer Science I (4 credits)",
                "ECON 253 - Economic Statistics (4 credits)",
                "MATH 221 - Introduction to Statistics (4 credits)",
                "SOCI 201 - Social Statistics (4 credits)"
            ],
            "Natural Science with Lab": [
                "ENST 250 - Environmental Science (4 credits)",
                "ENST 250L - Introduction to Environmental Science Lab (0 credits)",
                "ENST 265 - Earth Systems (4 credits)",
                "MRNE 110 - Introduction to Marine Science (4 credits)"
            ]
        },
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "ASIA 200 - Gateway Course (4 credits)",
                "Next Level Contexts: Economics, History, Philosophy, or Political Science (4 credits)",
                "ENST 250 - Environmental Science (counts toward LEAD science breadth; or choose ENST 265 or MRNE 110) (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship (transfers/dual-enrollment: LEAD 311 optional)",
                "Creative/Interpretive: Visual Arts, Writing, Film/Media, or Performance (4 credits)",
                "Computational: Computer Science, Statistics, or Economics (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Latinx Americas Inquiry": {
        "description": "Hemispheric perspective on history, politics, and cultures of the Americas with emphasis on Latinx contributions (17-21 credits)",
        "inquiry_electives": {
            "Cultural Studies": [
                "ILCX 205 - The Latinx Experience in the United States (4 credits)",
                "ILAS 210 - Latin American Cultural Studies (4 credits)"
            ],
            "The Ideas, Histories, Behaviors, and Institutions of Societies": [
                "AADS 214 - Africa and the African Diaspora (4 credits)",
                "ANTH 230 - Cultural Anthropology (4 credits)",
                "ANTH 250 - Language and Culture (4 credits)",
                "HIST 253 - Latin American Civilizations (4 credits)",
                "POSC 376 - Mexican Politics (4 credits)",
                "POSC 382 - Latin American Politics (4 credits)",
                "POSC 385 - Topics in Political Science or Public Policy (4 credits)"
            ],
            "Creative, Embodied, and Immersive Processes": [
                "ART 205 - Introduction to Visual Thinking (4 credits)",
                "ART 211 - Portrait Photography: Identity and Social Justice (4 credits)",
                "ART 212 - Introduction to Photography (4 credits)",
                "ART 214 - Introduction to Digital Media Art (4 credits)",
                "ART 233 - Topics in Art (4 credits)",
                "ART 239 - Painting and Drawing from Life (4 credits)",
                "ART 269 - Community Arts (4 credits)",
                "MUSA courses - Voice or Instrumental in Latin American Traditions (1 credit × 4 semesters)"
            ],
            "Problem Solving from a Mathematical Perspective": [
                "COSC 120 - Introduction to Computer Science I (4 credits)",
                "ECON 253 - Economic Statistics (4 credits)",
                "POSC 200 - Scope and Methods of Political Science (4 credits)"
            ],
            "Natural Science with Lab": [
                "ENST 250 - Environmental Science (4 credits)",
                "ENST 250L - Introduction to Environmental Science Lab (0 credits)",
                "ENST 265 - Earth Systems (4 credits)"
            ]
        },
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "Cultural Studies: Latinx Experience and Latin American Cultural Studies (4 credits each)",
                "Societies/Institutions: Anthropology, History, or Political Science (4 credits)",
                "ENST 250 - Environmental Science (counts toward LEAD science breadth; or choose ENST 265) (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship (transfers/dual-enrollment: LEAD 311 optional)",
                "Creative/Embodied Processes: Visual Arts or Music (4 credits)",
                "Mathematical Perspective: Computer Science, Economics, or Political Science Methods (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Idea of the West Inquiry": {
        "description": "Interrogating how 'the West' became geographically and culturally centered on Western Europe and the USA (17-21 credits)",
        "inquiry_electives": {
            "Social and Behavioral Sciences, Cultural Literacy": [
                "ANTH 101 - Introduction to Anthropology (4 credits)"
            ],
            "Humanities": [
                "ENGL 284 - Literature in History I: Before 1800 (4 credits)",
                "ENGL 285 - Literature in History II: After 1800 (4 credits)",
                "HIST 104 - Historical Foundations of the Modern World to 1450 (4 credits)",
                "HIST 105 - Western Civilization (4 credits)",
                "HIST 108 - History of the Modern World (4 credits)",
                "HIST 219 - Atlantic World Survey (4 credits)",
                "HIST 253 - Latin American Civilizations (4 credits)",
                "HIST 272 - Ancient Mediterranean (4 credits)"
            ],
            "Arts and Humanities": [
                "MUST 200 - Introduction to Museum Studies (4 credits)"
            ],
            "Natural Sciences with Lab / Mathematics": [
                "ASTR 154 - Solar System Astronomy with Laboratory (4 credits)",
                "ASTR 155 - Stellar Astronomy and Cosmology with Laboratory (4 credits)"
            ]
        },
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "ANTH 101 - Introduction to Anthropology (4 credits)",
                "Humanities: Literature in History or World History (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship (transfers/dual-enrollment: LEAD 311 optional)",
                "Arts/Humanities: Museum Studies (4 credits)",
                "Natural Sciences with Lab/Mathematics: Astronomy (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    }
}

# ==============================================================================
# MAJOR DATA STRUCTURE
# ==============================================================================
# This structure allows easy addition of new majors
# Each major can have tracks (like ENST) or be track-less (like Biology)
# Note: LEAD requirements are now pulled from lead_paths instead
# ==============================================================================

# Majors available as a second major (expand this list to add more over time)
DOUBLE_MAJOR_OPTIONS = ["Biology", "Environmental Studies", "Marine Science", "Psychology"]

major_data = {
    "Environmental Studies": {
        "has_tracks": True,
        "tracks": ["Environmental Science", "Environmental Policy and Social Science", "Environmental Arts and Humanities"],
        "track_electives": {
            "Environmental Science": [
                "BIOL 271 - Ecology and Evolution (4 credits)",
                "BIOL 380 - Topics in Biology (2-4 credits)",
                "BIOL 316 - Tropical Biology (4 credits)",
                "BIOL 383 - Biological Oceanography (4 credits)",
                "BIOL 463 - Ecology of Coastal Systems (4 credits)",
                "BIOL 435 - Plant Physiology (4 credits)",
                "CHEM 301 - Marine Chemistry (2 credits)",
                "CHEM 302 - Geochemistry (2 credits)",
                "CHEM 305 - Quantitative Analysis (4 credits)",
                "CHEM 306 - Instrumental Analysis (4 credits)",
                "ENST 265 - Earth Systems (4 credits)",
                "ENST 295 - Topics in Environmental Science (4 credits)",
                "ENST 222 - Environmental Data Analysis and Visualization (4 credits)",
                "MRNE 222 - Environmental Data Analysis and Visualization (4 credits)",
                "ENST 382 - GIS Applications (4 credits)",
                "ENST 392 - Field Research Methods (4 credits)",
                "MRNE 392 - Field Research Methods (4 credits)",
                "ENST 393 - Coastal Ecosystem Management (4 credits)",
                "MRNE 393 - Coastal Ecosystem Management (4 credits)",
                "ENST 394 - Earth and Space Science for Educators (4 credits)",
                "ENST 365 - Marine Environmental Toxicology (4 credits)",
                "MRNE 365 - Marine Environmental Toxicology (4 credits)",
                "ENST 395 - Advanced Topics in Environmental Science (4 credits)",
                "MRNE 110 - Introduction to Marine Science (4 credits)",
                "MRNE 220 - Physical Oceanography (4 credits)"
            ],
            "Environmental Policy and Social Science": [
                "ANTH 243 - Biological Anthropology (4 credits)",
                "ANTH 302 - Food and Culture (4 credits)",
                "ANTH 337 - Atlantic World Archaeology (4 credits)",
                "ANTH 341 - Economic and Ecological Anthropology (4 credits)",
                "ANTH 352 - Topics in Anthropology (4 credits)",
                "ECON 350 - Environmental Economics (4 credits)",
                "ECON 354 - Natural Resource Economics (4 credits)",
                "ECON 372 - Economics of Developing Countries (4 credits)",
                "ENST 285 - Topics in Environmental Policy & Social Sciences (4 credits)",
                "ENST 283 - Race and Place (4 credits)",
                "ENST 383 - Race, Gender, and Environmental Justice (4 credits)",
                "ENST 385 - Advanced Topics in Environmental Policy & Social Sciences (4 credits)",
                "HIST 394 - Topics in Asian and African History (4 credits)",
                "MRNE 480 - Topics in Marine Science (4 credits)",
                "MUST 390 - Topics in Museum Studies",
                "POSC 311 - Public Policy (4 credits)",
                "POSC 385 - Topics in Political Science or Public Policy (4 credits)",
                "POSC 408 - Studies in Public Policy (4 credits)",
                "PPOL 408 - Studies in Public Policy (4 credits)",
                "PSYC 396 - Collaborative Research in Psychology (4 credits)",
                "SOCI 315 - Environmental Sociology (4 credits)",
                "SOCI 355 - Demography (4 credits)"
            ],
            "Environmental Arts and Humanities": [
                "ART 233 - Topics in Art (4 credits)",
                "ART 239 - Painting and Drawing from Life (4 credits)",
                "ART 240 - Landscape Drawing and Painting (4 credits)",
                "ART 333 - Advanced Topics in Art (4 credits)",
                "ART 390 - The Artist Naturalist (4 credits)",
                "ILAS 210 - Latin American Cultural Studies (4 credits)",
                "ILCS 365 - Creating for Social Change (4 credits)",
                "ILCS 372 - Multicultural Characteristics of Early Modern Spain (4 credits)",
                "ENGL 106 - Introduction to Literature (4 credits)",
                "ENGL 130 - Literary Topics (4 credits)",
                "ENGL 201 - Topics in Writing (4 credits)",
                "ENGL 365 - Studies in American Literature (4 credits)",
                "ENGL 390 - Topics in Literature (4 credits)",
                "ENGL 391 - The Word in the World (4 credits)",
                "ENGL 395 - Advanced Topics in Writing (4 credits)",
                "ENGL 430 - Special Topics in Literature (4 credits)",
                "ENST 275 - Topics in Environmental Humanities (4 credits)",
                "ENST 375 - Advanced Topics in Environmental Humanities (4 credits)",
                "PHIL 321 - Environmental Ethics (4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas (Arts, Cultural Literacy, Humanities, Math, Natural Sciences w/lab, Social/Behavioral Sciences)"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "ENST 100 - Environment and Society (4 credits)",
                    "BIOL 105 - Principles of Biology I (4 credits, satisfies ENST Biology with Lab requirement; BIOL 101 also accepted)",
                    "BIOL 105L - Principles of Biology Lab I (1 credit)",
                    "ENST 250 - Environmental Science (4 credits)",
                    "CHEM 101 - Contemporary Chemistry with Lab (4 credits, satisfies ENST Chemistry with Lab requirement; CHEM 103 also accepted)"
                ],
                "Sophomore": [
                    "Toolkit Course: Choose from ENST 182 (GIS), ANTH 201, BIOL 311 (Biostatistics), CHEM 305, POSC 200, ECON 253, MATH 221, or SOCI 201 (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Environmental Science": {
                "First Year": [],
                "Sophomore": [
                    "BIOL 271 - Ecology and Evolution (4 credits)",
                    "ENST 222 - Environmental Data Analysis and Visualization (4 credits)"
                ],
                "Junior": [
                    "BIOL 383 - Biological Oceanography OR MRNE 220 - Physical Oceanography (4 credits)",
                    "CHEM 302 - Geochemistry OR ENST 265 - Earth Systems (4 credits)",
                    "Environmental Science Track Depth Electives: 8+ credits at 300-400 level",
                    "Application Requirement: ENST 390 (Sustainability Practicum), ENST 391 (Field Study), 4 credits Independent Study/Research/Internship, or Study Abroad (4 credits)"
                ],
                "Senior": [
                    "Environmental Science Track Depth Electives: 4+ credits to complete 16 credit depth requirement"
                ]
            },
            "Environmental Policy and Social Science": {
                "First Year": [],
                "Sophomore": [
                    "ECON 350 - Environmental Economics OR ECON 354 - Natural Resource Economics (4 credits)",
                    "POSC 311 - Public Policy OR ANTH 341 - Economic & Ecological Anthropology (4 credits)"
                ],
                "Junior": [
                    "ENST 383 - Race, Gender, and Environmental Justice OR ENST 283 - Race and Place (4 credits)",
                    "SOCI 315 - Environmental Sociology OR ANTH 302 - Food and Culture (4 credits)",
                    "Environmental Policy and Social Science Track Depth Electives: 8+ credits at 300-400 level",
                    "Application Requirement: ENST 390 (Sustainability Practicum), ENST 391 (Field Study), 4 credits Independent Study/Research/Internship, or Study Abroad (4 credits)"
                ],
                "Senior": [
                    "Environmental Policy and Social Science Track Depth Electives: 4+ credits to complete 16 credit depth requirement"
                ]
            },
            "Environmental Arts and Humanities": {
                "First Year": [],
                "Sophomore": [
                    "ENGL 391 - The Word in the World OR ENGL 365 - Studies in American Literature (4 credits)",
                    "PHIL 321 - Environmental Ethics OR ENST 275 - Topics in Environmental Humanities (4 credits)"
                ],
                "Junior": [
                    "ART 390 - The Artist Naturalist OR ART 240 - Landscape Drawing and Painting (4 credits)",
                    "ENST 375 - Advanced Topics in Environmental Humanities OR ENGL 390 - Topics in Literature (4 credits)",
                    "Environmental Arts and Humanities Track Depth Electives: 8+ credits at 300-400 level",
                    "Application Requirement: ENST 390 (Sustainability Practicum), ENST 391 (Field Study), 4 credits Independent Study/Research/Internship, or Study Abroad (4 credits)"
                ],
                "Senior": [
                    "Environmental Arts and Humanities Track Depth Electives: 4+ credits to complete 16 credit depth requirement"
                ]
            },
            "Breadth": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Breadth Requirement: 4 credits from a 2nd ENST track (not your depth track)"
                ],
                "Senior": [
                    "Breadth Requirement: 4 credits from a 3rd ENST track (complete 8 credit breadth total)"
                ]
            },
            "Seminar": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "ENST 490 - Environmental Studies Junior Seminar (take before capstone)"
                ],
                "Senior": []
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Capstone: ENST 493 + ENST 494 St. Mary's Project (8 credits total) - satisfies both ENST major and LEAD Capstone",
                    "Alternative: ENST 495 Environmental Studies Capstone (4 credits) + 4 credits upper-level ENST course",
                    "Alternative: 8 credits SMP in another program + ENST coursework as needed"
                ]
            }
        }
    },

    "Biology": {
        "has_tracks": False,
        "elective_courses": {
            "Upper-Level Biology Electives": [
                "BIOL 303 - Invertebrate Zoology (4 credits)",
                "BIOL 311 - Biostatistics (4 credits)",
                "BIOL 316 - Tropical Biology (4 credits)",
                "BIOL 339 - Ecology of Marine Plants (4 credits)",
                "BIOL 342 - Plankton Ecology (4 credits)",
                "BIOL 344 - Marine Microbiology (4 credits)",
                "BIOL 365 - Animal Behavior (4 credits)",
                "BIOL 380 - Topics in Biology (2-4 credits)",
                "BIOL 383 - Biological Oceanography (4 credits)",
                "BIOL 384 - Ichthyology (4 credits)",
                "BIOL 430 - Cellular and Molecular Neurobiology (4 credits)",
                "BIOL 435 - Plant Physiology (4 credits)",
                "BIOL 450 - Sensory Biology (4 credits)",
                "BIOL 463 - Ecology of Coastal Systems (4 credits)",
                "BIOL 465 - Comparative Animal Physiology (4 credits)",
                "BIOL 471 - Molecular Biology (4 credits)",
                "BIOL 480 - Advanced Topics in Biology (4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Physical Science Foundation": {
                "First Year": [
                    "CHEM 103 - General Chemistry I (4 credits)",
                    "CHEM 106 - General Chemistry II (4 credits)"
                ],
                "Sophomore": [
                    "CHEM 311 - Organic Chemistry I (4 credits)",
                    "Recommended for grad/pre-professional: CHEM 312 - Organic Chemistry II (4 credits)",
                    "Recommended for grad/pre-professional: MATH 151/152 - Calculus I & II (8 credits)"
                ],
                "Junior": [
                    "Recommended for grad/pre-professional: PHYS 121/122 or PHYS 141/142 (8 credits)"
                ],
                "Senior": []
            },
            "Biology Core": {
                "First Year": [
                    "BIOL 105 - Principles of Biology I (4 credits)",
                    "BIOL 105L - Lab (1 credit)",
                    "BIOL 106 - Principles of Biology II (4 credits)",
                    "BIOL 106L - Lab (1 credit)"
                ],
                "Sophomore": [
                    "BIOL 270 - Genetics (4 credits)",
                    "BIOL 270L - Lab (1 credit)",
                    "BIOL 271 - Ecology and Evolution (4 credits)",
                    "BIOL 271L - Lab (1 credit)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Upper-Level Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Upper-Level Biology Electives: 16+ credits (minimum 8 credits with lab)"
                ],
                "Senior": [
                    "Upper-Level Biology Electives: Continue as needed to meet 16 credit requirement"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "BIOL 493/494 - St. Mary's Project (4-8 credits)"
                ]
            }
        }
    },

    "Marine Science": {
        "has_tracks": False,
        "elective_courses": {
            "Marine Science Electives": [
                "PHEC 232 - Advanced Open-Water Scuba (2 credits)",
                "BIOL 384 - Ichthyology (4 credits)",
                "BIOL 303 - Invertebrate Zoology (4 credits)",
                "BIOL 463 - Ecology of Coastal Systems (4 credits)",
                "ENST 392 / MRNE 392 - Field Research Methods (4 credits)",
                "ENST 393 / MRNE 393 - Coastal Ecosystem Management (4 credits)",
                "MRNE 181 - Lower-Level Marine Science Transfer Course (1-4 credits)",
                "ENST 222 / MRNE 222 - Environmental Data Analysis and Visualization (4 credits)",
                "ENST 320 - Quantitative Methods (4 credits)",
                "MRNE 307 - Student Assistantship (1 credit)",
                "BIOL 339 / MRNE 339 - Ecology of Marine Plants (4 credits)",
                "BIOL 342 / MRNE 342 - Plankton Ecology (4 credits)",
                "BIOL 344 / MRNE 344 - Marine Microbiology (4 credits)",
                "ENST 365 / MRNE 365 - Marine Environmental Toxicology (4 credits)",
                "MRNE 480 - Topics in Marine Science (4 credits)",
                "MRNE 481 - Upper-Level Marine Science Topics with Laboratory (4 credits)",
                "MRNE 482 - Upper-Level Marine Science Transfer Course (1-4 credits)",
                "ANTH 351 - Underwater Archaeology (4 credits)",
                "CHEM 301 - Marine Chemistry (2 credits)",
                "CHEM 302 - Geochemistry (2 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Physical Science Foundation": {
                "First Year": [
                    "CHEM 103 - General Chemistry I (4 credits)",
                    "CHEM 106 - General Chemistry II (4 credits)"
                ],
                "Sophomore": [
                    "PHYS 121/122, PHYS 141/142, or PHYS 151/152 - Physics sequence (8 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Biology Core": {
                "First Year": [
                    "BIOL 105 - Principles of Biology I (4 credits)",
                    "BIOL 105L - Lab (1 credit)",
                    "BIOL 106 - Principles of Biology II (4 credits)",
                    "BIOL 106L - Lab (1 credit)"
                ],
                "Sophomore": [],
                "Junior": [],
                "Senior": []
            },
            "Mathematics": {
                "First Year": [
                    "Strongly recommended: MATH 151 - Calculus I (4 credits)",
                    "Strongly recommended: MATH 152 - Calculus II (4 credits)"
                ],
                "Sophomore": [
                    "MATH 221 - Introduction to Statistics OR BIOL 311 - Biostatistics (4 credits, required)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Marine Science Core": {
                "First Year": [
                    "MRNE 110 - Introduction to Marine Science (4 credits)"
                ],
                "Sophomore": [
                    "BIOL 383 - Biological Oceanography (4 credits)"
                ],
                "Junior": [
                    "MRNE 220 - Physical Oceanography (4 credits)"
                ],
                "Senior": []
            },
            "Marine Science Electives": {
                "First Year": [],
                "Sophomore": [
                    "Marine Science Electives: Begin taking electives"
                ],
                "Junior": [
                    "Marine Science Electives: 16 credits total required (minimum 12 credits at 300+ level)"
                ],
                "Senior": [
                    "Marine Science Electives: Continue as needed"
                ]
            },
            "Professional Experience": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Professional Experience: 4 credits (internship, directed research, independent study, or specialized seminars)"
                ],
                "Senior": []
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "MRNE 490 - Marine Science Capstone (4 credits) OR MRNE 494 - SMP Part 2, OR 8-credit SMP sequence in related department"
                ]
            }
        }
    },

    "Psychology": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "PSYC 101 - Introduction to Psychology (4 credits)"
                ],
                "Sophomore": [
                    "PSYC 204 - Psychological Research, Analysis, and Writing I (4 credits)",
                    "PSYC 206 - Psychological Research, Analysis, and Writing II (4 credits)"
                ],
                "Junior": [
                    "PSYC 310 - Scientific Writing and Professional Development (4 credits)"
                ],
                "Senior": []
            },
            "Breadth Requirements": {
                "First Year": [
                    "Choose 1 course from each of the 5 areas (5 courses total): Biological & Sensory Processes, Culture & Community, Development & Learning, Health & Counseling, Social & Cognitive Processes — begin 200-level courses"
                ],
                "Sophomore": [
                    "Continue breadth courses — at least 2 of the 5 must be 200-level"
                ],
                "Junior": [
                    "Complete remaining breadth courses — at least 2 of the 5 must be 300-level laboratory (5 cr) or lab seminar (4 cr)"
                ],
                "Senior": []
            },
            "Upper-Level Elective": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "One 300- or 400-level PSYC course not used elsewhere (4-5 credits)"
                ],
                "Senior": []
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "PSYC 493/494 - St. Mary's Project (8 credits)"
                ]
            }
        }
    },

    "Political Science": {
        "has_tracks": True,
        "tracks": ["General Track", "American Politics", "Comparative Politics", "International Politics", "Political Theory"],
        "track_electives": {
            "General Track": [
                "Any upper-level (300-400) Political Science courses across all subfields"
            ],
            "American Politics": [
                "POSC 301 - The American Presidency (4 credits)",
                "POSC 302 - Congress and the Legislative Process (4 credits)",
                "POSC 303 - Constitutional Law (4 credits)",
                "POSC 304 - Civil Rights and Liberties (4 credits)",
                "POSC 305 - State and Local Government (4 credits)",
                "POSC 385 - Topics in American Politics (4 credits)",
                "Other approved 300-400 level American Politics courses"
            ],
            "Comparative Politics": [
                "POSC 351 - Politics of Developing Nations (4 credits)",
                "POSC 352 - European Politics (4 credits)",
                "POSC 353 - East Asian Politics (4 credits)",
                "POSC 354 - Latin American Politics (4 credits)",
                "POSC 385 - Topics in Comparative Politics (4 credits)",
                "Other approved 300-400 level Comparative Politics courses"
            ],
            "International Politics": [
                "POSC 361 - International Political Economy (4 credits)",
                "POSC 362 - International Security (4 credits)",
                "POSC 363 - International Organizations (4 credits)",
                "POSC 364 - Foreign Policy Analysis (4 credits)",
                "POSC 385 - Topics in International Politics (4 credits)",
                "Other approved 300-400 level International Politics courses"
            ],
            "Political Theory": [
                "POSC 371 - Ancient Political Thought (4 credits)",
                "POSC 372 - Modern Political Thought (4 credits)",
                "POSC 373 - Contemporary Political Theory (4 credits)",
                "POSC 374 - American Political Thought (4 credits)",
                "POSC 385 - Topics in Political Theory (4 credits)",
                "Other approved 300-400 level Political Theory courses"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Core Breadth Requirements": {
                "First Year": [
                    "POSC 100 - Introduction to Politics (4 credits)",
                    "POSC 200 - Scope and Methods of Political Science (4 credits)",
                    "One 200-level survey: POSC 201, 252, 262, or 269 (begin one in First Year, 4 credits)"
                ],
                "Sophomore": [
                    "POSC 201 - American Politics (4 credits)",
                    "POSC 252 - Comparative Politics (4 credits)",
                    "POSC 262 - Democratic Political Thought (4 credits)",
                    "POSC 269 - International Politics (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Depth & Concentration": {
                "First Year": [],
                "Sophomore": [
                    "Concentration depth: Begin 4 upper-level credits in chosen concentration"
                ],
                "Junior": [
                    "Concentration depth: 8 upper-level credits in chosen concentration"
                ],
                "Senior": []
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "All students: One 400-level POSC seminar (4 credits)",
                    "Option One: One additional 400-level seminar (4 credits) + one 300-level POSC course (4 credits) = 12 credits total",
                    "Option Two: POSC 493/494 - St. Mary's Project (8 credits) = 12 credits total"
                ]
            }
        }
    },

    "English": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Core Requirements - Historical Literature": {
                "First Year": [
                    "One of ENGL 284 or 285 — begin one in First Year (4 credits)"
                ],
                "Sophomore": [
                    "ENGL 284 - Literature in History I: Before 1800 (4 credits)",
                    "ENGL 285 - Literature in History II: After 1800 (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Core Requirements - Writing & Methodology": {
                "First Year": [
                    "ENGL 204 - Reading and Writing in the Major (4 credits)"
                ],
                "Sophomore": [],
                "Junior": [
                    "ENGL 304 - Methods of Literary Study (4 credits)"
                ],
                "Senior": []
            },
            "Electives": {
                "First Year": [
                    "One 100/200-level English elective (4 credits)"
                ],
                "Sophomore": [
                    "Two 100/200-level English electives (8 credits)"
                ],
                "Junior": [
                    "Two 300/400-level English electives (8 credits, minimum 12 upper-level total)"
                ],
                "Senior": [
                    "Complete remaining electives as needed to reach 44 credit minimum"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Option One: ENGL 493/494 - St. Mary's Project (8 credits)",
                    "Option Two: Two 400-level English seminars (8 credits)"
                ]
            }
        }
    },

    "Computer Science": {
        "has_tracks": False,
        "elective_courses": {
            "Computer Science Electives": [
                "COSC 301 - Software Engineering (4 credits)",
                "COSC 335 - Operating Systems (4 credits)",
                "COSC 336 - Computer Networks (4 credits)",
                "COSC 338 - Computer Graphics (4 credits)",
                "COSC 360 - Data Science for Computer Scientists (4 credits)",
                "COSC 370 - Artificial Intelligence (4 credits)",
                "COSC 420 - Distributed and Parallel Computing (4 credits)",
                "COSC 435 - Acceleration (4 credits)",
                "COSC 438 - Game Design and Development (4 credits)",
                "COSC 440 - Theory of Computation (4 credits)",
                "COSC 445 - Design and Analysis of Algorithms (4 credits)",
                "COSC 450 - Database Management Systems (4 credits)",
                "COSC 455 - Graph Theory (4 credits)",
                "COSC 460 - Advanced Data Science and Visualization (4 credits)",
                "COSC 480 - Topics in Computer Science (4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "COSC 120 - Introduction to Computer Science I (4 credits)",
                    "COSC 130 - Introduction to Computer Science II (4 credits)",
                    "MATH 151 - Calculus I (4 credits)",
                    "MATH 152 - Calculus II (4 credits)",
                    "MATH 200 - Discrete Mathematics (4 credits)"
                ],
                "Sophomore": [
                    "COSC 201 - Algorithms and Data Structures (4 credits)",
                    "COSC 230 - Computer Architecture (4 credits)",
                    "COSC 251 - Programming Languages (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Three Computer Science electives from: COSC 301, 335, 336, 338, 360, 370, 420, 435, 438, 440, 445, 450, 455, 460, 480 (12 credits)"
                ],
                "Senior": [
                    "Two additional Computer Science electives (8 credits)"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "COSC 402 - Software Startup Simulator Part 1 (4 credits) — if taking COSC capstone route"
                ],
                "Senior": [
                    "Option One: St. Mary's Project (8 credits)",
                    "Option Two: COSC 401 - Software Startup Simulator Part 2 (4 credits, completes COSC 402 sequence)"
                ]
            }
        }
    },

    "Chemistry": {
        "has_tracks": True,
        "tracks": ["ACS-Certified", "Non-ACS-Certified"],
        "elective_courses": {
            "ACS-Certified Track Electives": [
                "CHEM 306 - Instrumental Analysis (4 credits)",
                "CHEM 425 - Biochemistry II (4 credits)",
                "CHEM 480 - Topics in Chemistry (2-4 credits)",
                "PHYS 462 - Quantum Mechanics (4 credits)"
            ],
            "Non-ACS Track Electives": [
                "MTSC 301 - Introduction to Materials Science (4 credits)",
                "CHEM 306 - Instrumental Analysis (4 credits)",
                "CHEM 325 - Introduction to Chemical Literature (1 credit)",
                "CHEM 420 - Biochemistry I (4 credits)",
                "CHEM 480 - Topics in Chemistry (2-4 credits)",
                "CHEM 397 - Directed Research in Chemistry (1-4 credits)",
                "CHEM 399 - Independent Study in Chemistry (1-4 credits)",
                "CHEM 497 - Directed Research in Chemistry (1-4 credits)",
                "CHEM 499 - Independent Study in Chemistry (1-4 credits)",
                "PHYS 462 - Quantum Mechanics (4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Mathematics & Physics Foundation": {
                "First Year": [
                    "MATH 151 - Calculus I (4 credits)",
                    "MATH 152 - Calculus II (4 credits)"
                ],
                "Sophomore": [
                    "Physics Sequence: PHYS 141/142 OR PHYS 151/152 (8 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Chemistry Core": {
                "First Year": [
                    "CHEM 103 - General Chemistry I (4 credits)",
                    "CHEM 106 - General Chemistry II (4 credits)"
                ],
                "Sophomore": [
                    "CHEM 311 - Organic Chemistry I (4 credits)",
                    "CHEM 312 - Organic Chemistry II (4 credits)"
                ],
                "Junior": [
                    "CHEM 305 - Quantitative Analysis (4 credits)",
                    "CHEM 405 - Inorganic Chemistry (4 credits)",
                    "CHEM 451 - Physical Chemistry I (4 credits)",
                    "CHEM 452 - Physical Chemistry II (4 credits)"
                ],
                "Senior": []
            },
            "ACS-Certified Track": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "CHEM 325 - Introduction to Chemical Literature (1 credit)",
                    "CHEM 420 - Biochemistry I (4 credits)",
                    "One elective from: CHEM 306, CHEM 425, CHEM 480, or PHYS 462 (4 credits)"
                ]
            },
            "Non-ACS-Certified Track": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Chemistry electives (4+ credits from: MTSC 301, CHEM 306, CHEM 325, CHEM 420, CHEM 480, CHEM 397, CHEM 399, CHEM 497, CHEM 499, or PHYS 462)"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "CHEM 493/494 - St. Mary's Project in Chemistry or related discipline (8 credits)"
                ]
            }
        }
    },

    "History": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "One intro course from: HIST 104, 105, 108, or 109 (4 credits)",
                    "One 200-level history course (4 credits)"
                ],
                "Sophomore": [
                    "HIST 224 - Introduction to Historical Methods and Skills (4 credits)",
                    "Begin area distribution (minimum 8 credits at 200-level total)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Area Distribution": {
                "First Year": [],
                "Sophomore": [
                    "Americas area course (4 credits)"
                ],
                "Junior": [
                    "Europe area course (4 credits)",
                    "Asia & Africa area course (4 credits)",
                    "Comparative/Thematic/Global area course (4 credits)"
                ],
                "Senior": []
            },
            "Upper-Level Requirements": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "HIST 395 - Theories and Uses of History (4 credits)",
                    "One pre-modern content course at 300-400 level (4 credits)",
                    "Additional 300-400 level history courses (12+ credits)"
                ],
                "Senior": [
                    "Continue 300-400 level courses to reach 32 credits at upper level (total 48 credits)"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Option A: HIST 493 + HIST 494 - St. Mary's Project in History (8 credits) + one 400-level course (4 credits)",
                    "Option B: HIST 495 - History Capstone Seminar (4 credits) + two 400-level courses (8 credits)"
                ]
            }
        }
    },

    "Economics": {
        "has_tracks": False,
        "elective_courses": {
            "Field-Specific Economics": [
                "ECON 310 - Topics in Economics (4 credits)",
                "ECON 318 - International Trade (4 credits)",
                "ECON 325 - Urban Economics (4 credits)",
                "ECON 330 - Money and Banking (4 credits)",
                "ECON 335 - Labor Economics (4 credits)",
                "ECON 340 - Public Finance (4 credits)",
                "ECON 342 - Financial Economics (4 credits)",
                "ECON 350 - Environmental Economics (4 credits)",
                "ECON 351 - Industrial Organization (4 credits)",
                "ECON 354 - Natural Resource Economics (4 credits)",
                "ECON 355 - Health Economics (4 credits)",
                "ECON 356 - Economic Development (4 credits)",
                "ECON 357 - International Finance (4 credits)",
                "ECON 360 - International Political Economy (4 credits)",
                "ECON 372 - Economics of Developing Countries (4 credits)",
                "ECON 380 - Econometrics (4 credits)",
                "ECON 390 - Independent Study in Economics (1-4 credits)",
                "ECON 397/497 - Directed Research (1-4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Theory Core": {
                "First Year": [
                    "ECON 102 - Principles of Microeconomics (4 credits)",
                    "ECON 103 - Principles of Macroeconomics (4 credits)"
                ],
                "Sophomore": [
                    "ECON 251 - Intermediate Macroeconomics (4 credits)",
                    "ECON 252 - Intermediate Microeconomics (4 credits)",
                    "ECON 253 - Economic Statistics (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Field-Specific Analysis": {
                "First Year": [],
                "Sophomore": [
                    "One upper-level economics course (ECON 300-380) (4 credits)"
                ],
                "Junior": [
                    "Four 300-level economics courses (16 credits)"
                ],
                "Senior": [
                    "Two to three 300-400 level economics courses (8-12 credits) to complete 24 total credits of field-specific work"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Senior Experience - Choose one: ECON 405 - History of Economic Thought, ECON 412 - U.S. Economic History, ECON 459 - Senior Seminar, or ECON 493/494 - St. Mary's Project (4-8 credits)"
                ]
            }
        }
    },

    "Mathematics": {
        "has_tracks": False,
        "elective_courses": {
            "Senior-Level Mathematics": [
                "MATH 422 - Abstract Algebra II (4 credits)",
                "MATH 452 - Analysis II (4 credits)",
                "MATH 411 - Partial Differential Equations (4 credits)",
                "COSC 440 - Theory of Computation (4 credits)",
                "COSC 455 - Graph Theory (4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "MATH 151 - Calculus I (4 credits)",
                    "MATH 152 - Calculus II (4 credits)"
                ],
                "Sophomore": [
                    "MATH 255 - Vector Calculus (4 credits)",
                    "MATH 256 - Linear Algebra (4 credits)",
                    "MATH 281 - Foundations of Mathematics (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Core Mathematics": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "MATH 321 - Abstract Algebra I (4 credits)",
                    "MATH 312 - Differential Equations (4 credits)"
                ],
                "Senior": [
                    "MATH 351 - Analysis I (4 credits)"
                ]
            },
            "Senior-Level Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "MATH 422 - Abstract Algebra II OR MATH 452 - Analysis II (required choice, 4 credits)"
                ],
                "Senior": [
                    "One additional senior-level elective: Choose from MATH 411, COSC 440, COSC 455, or other approved course (4 credits)"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Option One: St. Mary's Project in Mathematics (8 credits)",
                    "Option Two: MATH 490 - Senior Topics Seminar in Mathematics (4 credits)",
                    "Option Three: MATH 495 - Senior Project in Mathematics (4 credits)"
                ]
            }
        }
    },

    "Anthropology": {
        "has_tracks": True,
        "tracks": ["General Anthropology", "Archaeology Concentration"],
        "elective_courses": {
            "General Anthropology Electives": [
                "ANTH 301 - Evolution of Culture (4 credits)",
                "ANTH 302 - Food and Culture (4 credits)",
                "ANTH 311 - Introduction to African Archaeology (4 credits)",
                "ANTH 323 - Archaeology and Heritage of the Chesapeake (4 credits)",
                "ANTH 334 - Underwater Archaeology (4 credits)",
                "ANTH 337 - Atlantic World Archaeology (4 credits)",
                "ANTH 339 - History of Archaeological Thought (4 credits)",
                "ANTH 341 - Economic and Ecological Anthropology (4 credits)",
                "ANTH 351 - Medical Anthropology (4 credits)",
                "ANTH 352 - Topics in Anthropology (4 credits)",
                "ANTH 357 - Material Culture (4 credits)",
                "ANTH 377 - Archaeological Field Study (6 credits)",
                "ANTH 410 - Historical Archaeology Field School (4 credits)",
                "ANTH 454 - Archaeological Survey (4 credits)",
                "Other 300-400 level ANTH courses (variable credits)"
            ],
            "Archaeology Concentration Electives": [
                "ANTH 311 - Introduction to African Archaeology (4 credits)",
                "ANTH 323 - Archaeology and Heritage of the Chesapeake (4 credits)",
                "ANTH 334 - Underwater Archaeology (4 credits)",
                "ANTH 337 - Atlantic World Archaeology (4 credits)",
                "ANTH 339 - History of Archaeological Thought (4 credits)",
                "ANTH 351 - Medical Anthropology (4 credits)",
                "ANTH 352 - Topics in Anthropology (4 credits)",
                "ANTH 357 - Material Culture (4 credits)",
                "ANTH 454 - Archaeological Survey (4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Core Foundation": {
                "First Year": [
                    "ANTH 101 - Introduction to Anthropology (4 credits)",
                    "One subfield course from: ANTH 230 (Cultural), ANTH 243 (Biological), ANTH 250 (Language/Culture), ANTH 281 (Archaeology), or ILCT 300 (Linguistics) (4 credits)"
                ],
                "Sophomore": [
                    "ANTH 201 - Anthropology Toolkit OR ANTH 202 - Archaeology Practicum (4 credits)",
                    "One subfield course from: ANTH 230 (Cultural), ANTH 243 (Biological), ANTH 250 (Language/Culture), ANTH 281 (Archaeology), or ILCT 300 (Linguistics) (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Theory and Methods": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "ANTH 349 - Anthropological Theory (4 credits)",
                    "ANTH 385 - Anthropological Research Methods (4 credits)"
                ],
                "Senior": []
            },
            "Electives": {
                "First Year": [],
                "Sophomore": [
                    "Two 300-400 level anthropology electives (8 credits)"
                ],
                "Junior": [
                    "One 300-400 level anthropology elective (4 credits)"
                ],
                "Senior": []
            },
            "Archaeology Concentration": {
                "First Year": [],
                "Sophomore": [
                    "Archaeology concentration: Must take ANTH 202 and ANTH 281"
                ],
                "Junior": [
                    "Archaeology concentration: Field school requirement - ANTH 377 (6 credits), ANTH 410 (4 credits), or ANTH 454 (4 credits)",
                    "Archaeology concentration: One additional subfield course (4 credits)",
                    "Archaeology concentration: Two 300-level archaeology electives (8 credits)",
                    "Archaeology concentration: One 300-level cultural anthropology elective (4 credits)"
                ],
                "Senior": []
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Option One: ANTH 490 - Senior Tutorial (4 credits) + one 300/400-level course (4 credits)",
                    "Option Two: ANTH 493/494 - St. Mary's Project (8 credits)",
                    "Option Three: ANTH 497 - Directed Research (4+ credits) + one 300/400-level course"
                ]
            }
        }
    },

    "Philosophy": {
        "has_tracks": False,
        "elective_courses": {
            "Upper-Level Philosophy": [
                "PHIL 310 - Ancient Philosophy (4 credits)",
                "PHIL 311 - Medieval Philosophy (4 credits)",
                "PHIL 315 - Early Modern Philosophy (4 credits)",
                "PHIL 320 - Philosophy of Science (4 credits)",
                "PHIL 321 - Environmental Ethics (4 credits)",
                "PHIL 325 - Feminism and Philosophy (4 credits)",
                "PHIL 330 - Philosophy of Mind (4 credits)",
                "PHIL 331 - Philosophy of Language (4 credits)",
                "PHIL 333 - Ethical Theories (4 credits)",
                "PHIL 335 - Existentialism (4 credits)",
                "PHIL 340 - Logic (4 credits)",
                "PHIL 345 - Epistemology (4 credits)",
                "PHIL 350 - Metaphysics (4 credits)",
                "PHIL 351 - East Asian Philosophies (4 credits)",
                "PHIL 352 - South Asian Philosophies (4 credits)",
                "PHIL 360 - Political Philosophy (4 credits)",
                "PHIL 370 - Philosophy of Religion (4 credits)",
                "PHIL 380 - Topics in Philosophy (4 credits)",
                "PHIL 381 - Happiness and Meaning (4 credits)",
                "PHIL 382 - Meditation and the Mind (4 credits)",
                "PHIL 390 - Independent Study in Philosophy (1-4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "PHIL 101 - Introduction to Philosophy OR PHIL 120 - Introduction to Ethics (4 credits)",
                    "One upper-level philosophy elective (300+ level, 4 credits)"
                ],
                "Sophomore": [],
                "Junior": [],
                "Senior": []
            },
            "History of Philosophy": {
                "First Year": [],
                "Sophomore": [
                    "PHIL 300 - Cranks and Sages: Greek and Roman Philosophy (4 credits)",
                    "Non-Western philosophy: PHIL 351, 352, or approved PHIL 380 (4 credits)"
                ],
                "Junior": [
                    "PHIL 302 - Mind and Knowledge: Descartes to Kant (4 credits)"
                ],
                "Senior": []
            },
            "Distribution Requirements": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Topics course: PHIL 380, 381, or 382 (4 credits)",
                    "Value theory: PHIL 321, 325, or 333 (4 credits)",
                    "Upper-level philosophy elective (4 credits)",
                    "PHIL 492 - SMP Proseminar (1 credit)"
                ],
                "Senior": [
                    "Two upper-level philosophy electives (8 credits)"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "PHIL 493 - St. Mary's Project in Philosophy (1-8 credits)",
                    "PHIL 494 - St. Mary's Project in Philosophy (1-8 credits)"
                ]
            }
        }
    },

    "Physics": {
        "has_tracks": True,
        "tracks": ["Physics (Standard)", "Applied Physics"],
        "elective_courses": {
            "Physics Electives": [
                "PHYS 342 - Mechanics (4 credits)",
                "PHYS 382 - Optics (4 credits)",
                "PHYS 391 - Astrophysics (4 credits)",
                "PHYS 392 - Cosmology (4 credits)",
                "PHYS 473 - Statistical Mechanics (4 credits)",
                "PHYS 490 - Senior Seminar in Physics (4 credits)",
                "CHEM 451 - Physical Chemistry I (4 credits)",
                "COSC 301 - Software Engineering (4 credits)",
                "MATH 312 - Differential Equations (4 credits)",
                "MATH 411 - Partial Differential Equations (4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Mathematics Foundation": {
                "First Year": [
                    "MATH 151 - Calculus I (4 credits)",
                    "MATH 152 - Calculus II (4 credits)"
                ],
                "Sophomore": [
                    "MATH 255 - Vector Calculus (4 credits)",
                    "MATH 256 - Linear Algebra (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Physics Core": {
                "First Year": [
                    "Physics Sequence: PHYS 151/152 - Fundamentals OR PHYS 141/142 - General Physics (8 credits)"
                ],
                "Sophomore": [
                    "PHYS 251 - Fundamentals of Physics III (4 credits)",
                    "PHYS 351 - Electricity and Magnetism (4 credits)"
                ],
                "Junior": [
                    "PHYS 312 - Advanced Physics Laboratory (4 credits)",
                    "PHYS 462 - Quantum Mechanics (4 credits)",
                    "CHEM 106 - General Chemistry II OR COSC 120 - Intro to Computer Science I (4 credits)"
                ],
                "Senior": [
                    "PHYS 311 - Electronics (4 credits)"
                ]
            },
            "Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Physics electives (4+ credits from: PHYS 342, 382, 391, 392, 473, 490, CHEM 451, COSC 301, MATH 312, 411)"
                ],
                "Senior": [
                    "Continue physics electives as needed"
                ]
            },
            "Applied Physics Track": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "PHYS 475 - Topics in Applied Physics I (4 credits, two different topics over two semesters)",
                    "Research experience: St. Mary's Project in physics OR PHYS 397/497 Directed Research (4 credits) + seminar presentation OR approved external research (160+ hours) + seminar presentation"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Standard Physics: St. Mary's Project required (capstone research)"
                ]
            }
        }
    },

    "Sociology": {
        "has_tracks": False,
        "elective_courses": {
            "Sociology Electives": [
                "SOCI 304 - Organizations and Work (4 credits)",
                "SOCI 310 - Sociology of Religion (4 credits)",
                "SOCI 312 - Social Psychology (4 credits)",
                "SOCI 315 - Environmental Sociology (4 credits)",
                "SOCI 320 - Social Movements (4 credits)",
                "SOCI 325 - Deviance and Social Control (4 credits)",
                "SOCI 330 - Social Inequality (4 credits)",
                "SOCI 335 - Sociology of Education (4 credits)",
                "SOCI 340 - Race and Ethnicity (4 credits)",
                "SOCI 345 - Sex and Gender (4 credits)",
                "SOCI 347 - Work and Family (4 credits)",
                "SOCI 350 - Medical Sociology (4 credits)",
                "SOCI 355 - Demography (4 credits)",
                "SOCI 360 - Urban Sociology (4 credits)",
                "SOCI 365 - Criminology (4 credits)",
                "SOCI 370 - Political Sociology (4 credits)",
                "SOCI 380 - Topics in Sociology (4 credits)",
                "SOCI 385 - Sociology Seminar (4 credits)",
                "SOCI 397/497 - Directed Research (1-4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Core Foundation": {
                "First Year": [
                    "SOCI 101 - Introduction to Sociology (4 credits)",
                    "One additional sociology course (4 credits)"
                ],
                "Sophomore": [
                    "SOCI 201 - Social Statistics (4 credits)",
                    "Two additional sociology courses (8 credits)"
                ],
                "Junior": [
                    "SOCI 350 - Sociological Theory (4 credits)",
                    "SOCI 385 - Research Methods (4 credits)"
                ],
                "Senior": []
            },
            "Elective Coursework": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Two additional sociology electives (8 credits)"
                ],
                "Senior": [
                    "Complete remaining sociology electives to reach 20 total credits of SOCI courses"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Option One: SOCI 493/494 - St. Mary's Project (8 credits)",
                    "Option Two: SOCI 490 - Senior Seminar (4 credits) + one 300-400 level sociology course (4 credits)"
                ]
            }
        }
    },

    "Public Policy": {
        "has_tracks": True,
        "tracks": ["American Public Policy", "International Public Policy"],
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "POSC 100 - Introduction to Politics (4 credits)",
                    "ECON 102 - Principles of Microeconomics (4 credits)",
                    "ECON 103 - Principles of Macroeconomics (4 credits)"
                ],
                "Sophomore": [],
                "Junior": [],
                "Senior": []
            },
            "Core Requirements": {
                "First Year": [],
                "Sophomore": [
                    "POSC 311 - Public Policy (4 credits)",
                    "POSC 315 - Policy Evaluation (4 credits)",
                    "Quantitative methods: ECON 253 OR POSC 200 (4 credits)",
                    "Intermediate economics: ECON 251 OR ECON 252 (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "American Public Policy Track": {
                "First Year": [],
                "Sophomore": [
                    "POSC 201 - American Politics (4 credits)",
                    "One from: POSC 367, 330, 312, or SOCI 330 (4 credits)"
                ],
                "Junior": [
                    "Track electives (4 credits)"
                ],
                "Senior": []
            },
            "International Public Policy Track": {
                "First Year": [],
                "Sophomore": [
                    "POSC 252 - Comparative Politics OR POSC 269 - International Politics (4 credits)",
                    "ECON 318 - International Finance OR ECON 356 - International Economics OR ECON 372 - Economics of Developing Countries (4 credits)"
                ],
                "Junior": [
                    "Track electives (4 credits)"
                ],
                "Senior": []
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Option One: St. Mary's Project (8 credits)",
                    "Option Two: PPOL/POSC 408 with senior paper (4 credits) + elective credits (4 credits)"
                ]
            }
        }
    },

    "Biochemistry": {
        "has_tracks": False,
        "elective_courses": {
            "Advanced Biochemistry & Related Courses": [
                "CHEM 452 - Physical Chemistry II (4 credits)",
                "CHEM 306 - Instrumental Analysis (4 credits)",
                "BIOL 380 - Topics in Biology (2-4 credits)",
                "BIOL 430 - Cellular and Molecular Neurobiology (4 credits)",
                "BIOL 435 - Plant Physiology (4 credits)",
                "BIOL 480 - Advanced Topics in Biology (4 credits)",
                "CHEM 480 - Topics in Chemistry (2-4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Chemistry Core": {
                "First Year": [
                    "CHEM 106 - General Chemistry II (4 credits)"
                ],
                "Sophomore": [
                    "CHEM 311 - Organic Chemistry I (4 credits)",
                    "CHEM 312 - Organic Chemistry II (4 credits)"
                ],
                "Junior": [
                    "CHEM 420 - Biochemistry I (4 credits)",
                    "CHEM 425 - Biochemistry II (4 credits)"
                ],
                "Senior": [
                    "CHEM 451 - Physical Chemistry I (4 credits)"
                ]
            },
            "Biology Core": {
                "First Year": [
                    "BIOL 105 - Principles of Biology I (4 credits)",
                    "BIOL 105L - Principles of Biology Lab I (1 credit)"
                ],
                "Sophomore": [
                    "BIOL 270 - Genetics (4 credits)",
                    "BIOL 270L - Genetics Lab (1 credit)"
                ],
                "Junior": [
                    "BIOL 471 - Molecular Biology (4 credits)"
                ],
                "Senior": []
            },
            "Mathematics & Physics": {
                "First Year": [],
                "Sophomore": [
                    "MATH 151 - Calculus I (4 credits)",
                    "MATH 152 - Calculus II (4 credits)"
                ],
                "Junior": [
                    "Physics Sequence: PHYS 141/142 OR PHYS 151/152 (8 credits)"
                ],
                "Senior": []
            },
            "Advanced Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Optional advanced electives in biochemistry and related fields (recommended for graduate school preparation)"
                ],
                "Senior": [
                    "Continue advanced electives as desired"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "St. Mary's Project in biochemistry or related discipline (8 credits)"
                ]
            }
        }
    },

    "Neuroscience": {
        "has_tracks": False,
        "elective_courses": {
            "Biology Electives": [
                "BIOL 365 - Animal Behavior (4 credits)",
                "BIOL 430 - Cellular and Molecular Neurobiology (4 credits)",
                "BIOL 450 - Sensory Biology (4 credits)",
                "BIOL 465 - Comparative Animal Physiology (4 credits)"
            ],
            "Chemistry Electives": [
                "CHEM 420 - Biochemistry I (4 credits)",
                "CHEM 425 - Biochemistry II (4 credits)"
            ],
            "Psychology Electives": [
                "PSYC 308 - Biological Psychology (4 credits)",
                "PSYC 310 - Cognitive Psychology (4 credits)",
                "PSYC 312 - Developmental Psychology (4 credits)",
                "PSYC 320 - Social Psychology (4 credits)",
                "PSYC 330 - Abnormal Psychology (4 credits)",
                "PSYC 340 - Sensation and Perception (4 credits)",
                "PSYC 350 - Learning and Memory (4 credits)"
            ],
            "Philosophy Electives": [
                "PHIL 330 - Philosophy of Mind (4 credits)",
                "PHIL 382 - Meditation and the Mind (4 credits)"
            ],
            "Neuroscience Electives": [
                "NEUR 310 - Special Topics in Neuroscience (4 credits)",
                "NEUR 397/497 - Directed Research (1-4 credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation Courses": {
                "First Year": [
                    "BIOL 105 - Principles of Biology I (4 credits)",
                    "BIOL 105L - Principles of Biology Lab I (1 credit)",
                    "BIOL 106 - Principles of Biology II (4 credits)",
                    "BIOL 106L - Principles of Biology Lab II (1 credit)",
                    "CHEM 103 - General Chemistry I (4 credits)",
                    "CHEM 106 - General Chemistry II (4 credits)",
                    "PSYC 101 - Introduction to Psychology (4 credits)"
                ],
                "Sophomore": [],
                "Junior": [],
                "Senior": []
            },
            "Neuroscience Core": {
                "First Year": [],
                "Sophomore": [
                    "NEUR 201 - Introduction to Neuroscience (4 credits)",
                    "NEUR 201L - Introduction to Neuroscience Laboratory (1 credit)"
                ],
                "Junior": [
                    "NEUR 310 - Special Topics in Neuroscience (4 credits)"
                ],
                "Senior": []
            },
            "Statistics": {
                "First Year": [],
                "Sophomore": [
                    "Statistics: PSYC 204 & PSYC 206 (8 credits) OR BIOL 311 - Biostatistics (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Neuroscience electives from 2+ disciplines (BIOL, CHEM, NEUR, PHIL, PSYC) including minimum 2 lab-based courses (12 credits)"
                ],
                "Senior": [
                    "Complete elective requirements as needed"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "NEUR 493/494 - St. Mary's Project in Neuroscience (8 credits)"
                ]
            }
        }
    },

    "Business Administration and Management": {
        "has_tracks": True,
        "tracks": ["Business Analytics and Finance", "International Business", "Business Management"],
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundational Core": {
                "First Year": [
                    "BADM 101 - Introduction to Business Leadership and Business Ethics (4 credits)",
                    "ECON 102 - Principles of Microeconomics (4 credits)",
                    "ECON 103 - Principles of Macroeconomics (4 credits)"
                ],
                "Sophomore": [],
                "Junior": [],
                "Senior": []
            },
            "Technical Core": {
                "First Year": [],
                "Sophomore": [
                    "BADM 201 - Principles of Accounting I (4 credits)",
                    "ECON 253 - Economic Statistics (4 credits)",
                    "One from: BADM 202, ECON 251, or ECON 252 (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Business Core": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "BADM 301 - Management (4 credits)",
                    "BADM 302 - Marketing (4 credits)",
                    "BADM 303 - Corporation Finance (4 credits)"
                ],
                "Senior": []
            },
            "Track Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Business Analytics & Finance: Select from BADM 304, 305, 310, 315, 340, 345, 350; ECON 318, 342, 380; SOCI 355",
                    "International Business: Select from BADM 315; ECON 318, 357; HIST 352, 355; ILCC upper-division language/culture; POSC 408, 468, 469",
                    "Business Management: Select from ART 431, BADM 304, 306; ECON 351, 355; PSYC 483, 487; SOCI 304, 330",
                    "Complete 16 credits (4 courses) from track-specific options"
                ],
                "Senior": [
                    "Continue track electives as needed"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "Option One: BADM 401 - Seminar in Business (4 credits) + BADM 498 - Off-Campus Internship (4+ credits)",
                    "Option Two: BADM 493/494 - St. Mary's Project in Business (8 credits)"
                ]
            }
        }
    },

    "Studio Art": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation Studio": {
                "First Year": [
                    "ART 205 - Visual Thinking (4 credits)",
                    "ART 214 - Digital Media (4 credits)"
                ],
                "Sophomore": [
                    "Three 200-level art courses: drawing, painting, photography, sculpture, printmaking, etc. (12 credits)",
                    "ARTH 225 - Art History Survey I (4 credits)",
                    "ARTH 226 - Art History Survey II (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Advanced Studio & Art History": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Three 300-level advanced studio courses (12 credits)",
                    "One additional art history course (4 credits)"
                ],
                "Senior": []
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "ART 430 - Capstone Creative Practices (4 credits)",
                    "ART 431 - Capstone Professional Practices (4 credits)"
                ]
            }
        }
    },

    "Spanish": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher - Spanish placement)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Language Foundation": {
                "First Year": [
                    "Placement into ILCS 202 or higher based on proficiency"
                ],
                "Sophomore": [
                    "ILCS 202 - Intermediate Spanish (4 credits)",
                    "ILCS 260 - Spanish Composition (4 credits)",
                    "Begin upper-level courses (4+ credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Upper-Level Requirements": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Upper-level ILCS courses (12+ credits from: ILCS 360, 361, 362, 363, 365, 372, 373, 374, 390, 440)"
                ],
                "Senior": [
                    "Complete 32 total credits in Spanish (minimum 24 at upper level)",
                    "Study abroad strongly recommended"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "St. Mary's Project in ILC or another discipline (8 credits)"
                ]
            }
        }
    },

    "Asian Studies": {
        "has_tracks": False,
        "elective_courses": {
            "History": [
                "HIST 206 - Survey of East Asian History (4 credits)",
                "HIST 280 - Introduction to South Asian History (4 credits)",
                "HIST 351 - Modern China (4 credits)",
                "HIST 352 - Modern Japan (4 credits)",
                "HIST 354 - South Asia (4 credits)",
                "HIST 355 - Southeast Asia (4 credits)",
                "HIST 358 - Islam (4 credits)",
                "HIST 360 - Modern Middle East (4 credits)",
                "HIST 361 - History of India (4 credits)",
                "HIST 369 - Topics in Asian History (4 credits)",
                "HIST 388 - The Silk Road (4 credits)",
                "HIST 389 - The Mongol Empire (4 credits)",
                "HIST 394 - Topics in Asian and African History (4 credits)",
                "HIST 455 - Senior Seminar in Asian History (4 credits)"
            ],
            "Economics": [
                "ECON 318 - International Trade (4 credits)",
                "ECON 356 - Economic Development (4 credits)",
                "ECON 357 - International Finance (4 credits)",
                "ECON 372 - Economics of Developing Countries (4 credits)"
            ],
            "Political Science": [
                "POSC 252 - Introduction to Comparative Politics (4 credits)",
                "POSC 269 - Introduction to International Relations (4 credits)",
                "POSC 320 - Theories of International Relations (4 credits)",
                "POSC 353 - East Asian Politics (4 credits)",
                "POSC 468 - Topics in Comparative Politics (4 credits)",
                "POSC 469 - Topics in International Politics (4 credits)"
            ],
            "Philosophy": [
                "PHIL 351 - East Asian Philosophies (4 credits)",
                "PHIL 352 - South Asian Philosophies (4 credits)"
            ],
            "Languages & Culture": [
                "ILCC 101/102 - Elementary Chinese I & II (8 credits)",
                "ILCC 202 - Intermediate Chinese (4 credits)",
                "ILCC 360 - Advanced Chinese Language and Culture (4 credits)",
                "Asian language courses at 300-400 level (variable credits)",
                "ASIA 200 - Introduction to Asian Studies (4 credits)",
                "Asian culture and literature courses from ILC department (variable credits)"
            ]
        },
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "Begin Asian language study: ILCC 101/102 or equivalent",
                    "ASIA 200 - Introduction to Asian Studies (4 credits)"
                ],
                "Sophomore": [
                    "Continue language study to proficiency",
                    "Electives from 2+ disciplines (8+ credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Interdisciplinary Requirements": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Interdisciplinary electives: 24 credits across 3+ disciplines - History, Economics, Philosophy, Political Science, Languages (minimum 20 at 300/400-level)"
                ],
                "Senior": [
                    "Complete distribution requirements"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "ASIA 493/494 - St. Mary's Project in Asian Studies (8 credits)",
                    "Note: If SMP is interdisciplinary with only 4 credits in ASIA 493/494, add 4 upper-level Asian Studies credits"
                ]
            }
        }
    },

    "Women, Gender, and Sexuality Studies": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "WGSX 220 - Women, Gender, and Sexuality Studies (4 credits)"
                ],
                "Sophomore": [
                    "Feminist/queer theory course (4 credits)",
                    "WGSX 340 - WGSX Methods and Modes of Thinking (4 credits)",
                    "Category electives: Global, literary/cultural, society/politics, historical (4+ credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Category Distribution": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Continue category distribution requirements (16+ credits)",
                    "Minimum 12 credits at 300-level from 4 different categories"
                ],
                "Senior": [
                    "Complete 44 total credits with appropriate category distribution"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "WGSX 493/494 - St. Mary's Project in Women, Gender, and Sexuality Studies (8 credits)"
                ]
            }
        }
    },

    "Performing Arts (Integrated)": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "PERF 110 - Critical Creativity in the Performing Arts (4 credits)",
                    "TDPS 170/171 - Theatre and Performance Studies I & II (8 credits)",
                    "TDPS 230 OR TDPS 250 - Acting/Movement (4 credits)",
                    "MUSC 201/203 - Music Theory/Musicianship (4 credits)"
                ],
                "Sophomore": [
                    "MUSC 301/302 - Theory and Ear Training (4 credits)",
                    "Begin ensemble and private lessons (4+ credits each semester)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Performance Requirements": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Continue performance requirements: 4 semesters ensemble + 4 semesters private lessons",
                    "Electives in music or TDPS (8 credits)"
                ],
                "Senior": [
                    "Complete performance requirements (total 22 credits developmental)"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "PERF 475/476 - Seminar (4 credits)",
                    "SMP: MUSC 493/494, TDPS 493/494, or PERF 490/491 (8 credits)"
                ]
            }
        }
    },

    "Performing Arts (Music)": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "PERF 110 - Critical Creativity in the Performing Arts (4 credits)",
                    "MUSC 203/201 - Musicianship/Theory (4 credits)",
                    "MUSC 216 - Music History (4 credits)",
                    "Begin ensemble and lessons (4 credits)"
                ],
                "Sophomore": [
                    "MUSC 301/302/318/319 - Theory, ear training, history (12 credits)",
                    "Continue performance (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Performance Requirements": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Complete performance: 4 semesters ensemble (12 credits) + 4 semesters private lessons (4 credits)"
                ],
                "Senior": []
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "PERF 475/476 - Seminar (4 credits)",
                    "SMP: MUSC 493/494 OR PERF 490/491 (8 credits)"
                ]
            }
        }
    },

    "Performing Arts (Theater, Dance, Performance Studies)": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (C- or higher; transfers with 24+ credits: LEAD 301)",
                    "LEAD 111 - Career Networking and Navigation",
                    "LEAD 112 - Career Networking and Navigation II",
                    "Language Course (102/110 level or higher)",
                    "Knowledge & Methods: Start LEAD Inquiry (4-5 courses, 17-22 credits) OR LEAD Exploration courses"
                ],
                "Sophomore": [
                    "LEAD 211 - Honors College Externship (guaranteed internship/research/immersive experience)",
                    "Knowledge & Methods: Continue LEAD Inquiry OR complete LEAD Exploration breadth areas"
                ],
                "Junior": [
                    "Knowledge & Methods: Complete remaining LEAD Inquiry or LEAD Exploration requirements"
                ],
                "Senior": []
            },
            "Foundation": {
                "First Year": [
                    "PERF 110 - Critical Creativity in the Performing Arts (4 credits)",
                    "TDPS 170/171 - Theatre and Performance Studies I & II (8 credits)",
                    "TDPS 230 - Acting (4 credits)",
                    "TDPS 250 - Movement (4 credits)"
                ],
                "Sophomore": [
                    "PERF 325 - Methods (4 credits)",
                    "TDPS 371 - Production Lab (begin 4-semester sequence)",
                    "Participate in TDPS 370 Studio productions"
                ],
                "Junior": [],
                "Senior": []
            },
            "Electives & Production": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Electives: acting/directing, history/theory, design, or dance (12+ credits)",
                    "Continue production lab participation"
                ],
                "Senior": [
                    "Complete production requirements"
                ]
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [],
                "Senior": [
                    "PERF 475/476 - Seminar (4 credits)",
                    "SMP: TDPS 493/494 OR PERF 490/491 (8 credits)"
                ]
            }
        }
    }
}

# ==============================================================================
# MINOR DATA STRUCTURE
# ==============================================================================
# This structure contains all available minors
# ==============================================================================

minor_data = {
    "Biology": {
        "course_data": {
            "Core Courses": {
                "First Year": [
                    "BIOL 105 - Principles of Biology I (4 credits)",
                    "BIOL 105L - Principles of Biology Lab I (1 credit)",
                    "BIOL 106 - Principles of Biology II (4 credits)",
                    "BIOL 106L - Principles of Biology II Lab (1 credit)"
                ],
                "Sophomore": [
                    "BIOL 270 - Genetics (4 credits)",
                    "BIOL 270L - Genetics Lab (1 credit)",
                    "BIOL 271 - Ecology and Evolution (4 credits)",
                    "BIOL 271L - Ecology and Evolution Lab (1 credit)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Upper-division Biology Elective (4+ credits) - Choose from 300/400 level BIOL courses"
                ],
                "Senior": []
            }
        }
    },
    "Anthropology": {
        "course_data": {
            "Core Courses": {
                "First Year": [
                    "ANTH 101 - Introduction to Anthropology (4 credits)"
                ],
                "Sophomore": [
                    "ANTH 201 - Anthropology Toolkit OR ANTH 202 - Archaeology Practicum (4 credits)",
                    "Two 200-level courses from: ANTH 230 - Cultural Anthropology, ANTH 243 - Biological Anthropology, ANTH 250 - Language and Culture, ANTH 281 - Archaeology and Prehistory (8 credits total)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Two Anthropology electives at 300 or 400 level (8 credits)"
                ],
                "Senior": []
            }
        }
    },
    "Data Science": {
        "course_data": {
            "Foundation": {
                "First Year": [
                    "MATH 151 - Calculus I (4 credits)",
                    "DATA 101 - Introduction to Data Science 1 (4 credits)"
                ],
                "Sophomore": [
                    "DATA 102 - Introduction to Data Science 2 (4 credits)",
                    "Statistics: Choose from BIOL 311, BIOL 313, DATA 301, ECON 253, MATH 221, PHYS 312, POSC 200, PSYC 206, or SOCI 201 (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Data Science Electives: Choose from COSC 460, DATA 250, DATA 310, ENST 182, ECON 380, or other approved courses (8+ credits)"
                ],
                "Senior": []
            }
        }
    },
    "Environmental Studies": {
        "course_data": {
            "Foundation": {
                "First Year": [
                    "ENST 100 - Environment and Society (4 credits)"
                ],
                "Sophomore": [
                    "ENST 250 - Environmental Science OR ENST 265 - Earth Systems (4 credits)",
                    "One elective from Sciences, Social Sciences/Policy, or Arts/Humanities track (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Track Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Two track electives from different tracks (8 credits - 4 each from 2 different tracks)",
                    "One upper-level (300-400) ENST elective (4 credits)",
                    "Note: At least 8 credits must be ENST-coded, at least 8 credits at 300-400 level"
                ],
                "Senior": []
            }
        }
    },
    "Political Science": {
        "course_data": {
            "Foundation": {
                "First Year": [
                    "POSC 100 - Introduction to Politics (4 credits)"
                ],
                "Sophomore": [
                    "Two 200-level Political Science courses (8 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Upper-Level Courses": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Three 300 or 400-level Political Science courses (12 credits)"
                ],
                "Senior": []
            }
        }
    },
    "Women, Gender, and Sexuality Studies": {
        "course_data": {
            "Core Course": {
                "First Year": [
                    "WGSX 220 - Women, Gender, and Sexuality Studies (4 credits)"
                ],
                "Sophomore": [],
                "Junior": [],
                "Senior": []
            },
            "Electives": {
                "First Year": [],
                "Sophomore": [
                    "WGSX electives from approved courses across disciplines (8 credits; at least 4 credits should be 300+ level to meet the 12-credit upper-level requirement)"
                ],
                "Junior": [
                    "Upper-level (300+) WGSX electives from at least 3 different disciplines (8 credits, completing 12 total upper-level credits across all electives)"
                ],
                "Senior": []
            }
        }
    },
    "African and African Diaspora Studies": {
        "course_data": {
            "Required Courses": {
                "All Years": ["AADS 214 - Africa and the African Diaspora (4 credits)", "16 credits of approved electives (at least 8 at 300-400 level, drawn from at least two disciplines)", "Total: 20 credits minimum, grade of C or better in each course"]
            }
        }
    },
    "Art": {
        "course_data": {
            "Required Courses": {
                "All Years": ["ART 205 - Introduction to Visual Thinking (4 credits)", "Three 200-level studio art courses (12 credits)", "Two 300-level advanced studio courses (8 credits)", "Total: 22 credits minimum across 6 courses, C- or better in each"]
            }
        }
    },
    "Asian Studies": {
        "course_data": {
            "Required Courses": {
                "All Years": ["ASIA 200 - Introduction to Asian Studies (4 credits)", "Five electives from approved interdisciplinary list, at least 2 disciplines, at least 2 at 300-400 level (20 credits)", "Language requirement (required): ILCC 102 - Elementary Chinese II or equivalent Asian language proficiency", "Total: 24 credits minimum, C- or better in each course"]
            }
        }
    },
    "Business Administration and Management": {
        "course_data": {
            "Required Courses": {
                "All Years": ["BADM 101 - Introduction to Business Leadership and Business Ethics (4 credits)", "ECON 102 - Principles of Microeconomics (4 credits)", "ECON 103 - Principles of Macroeconomics (4 credits)", "BADM 201 - Principles of Accounting I (4 credits)", "BADM 301 - Management (4 credits)", "BADM 302 - Marketing (4 credits)", "Total: 24 credits minimum, C- or better in each course"]
            }
        }
    },
    "Computer Science": {
        "course_data": {
            "Required Courses": {
                "All Years": ["COSC 120 - Introduction to Computer Science I (4 credits)", "COSC 130 - Introduction to Computer Science II (4 credits)", "COSC 201 - Algorithms and Data Structures (4 credits)", "Three electives from: MATH 200/281, COSC 230, 251, 301, 335, 336, 338, 360, 370, 420, 435, 438, 440, 445, 450, 455, 460, 480 (12 credits)", "Total: 24 credits minimum"]
            }
        }
    },
    "Creative Writing": {
        "course_data": {
            "Required Courses": {
                "All Years": ["ENGL 204 - Reading and Writing in the Major (4 credits)", "ENGL 270 - Creative Writing (4 credits)", "Two 300-level workshops in distinct genres: ENGL 395, ENGL 495, or ILC 360 (8 credits)", "One literature elective from approved list (4 credits)", "Total: 18+ credits minimum across 5 courses, C- or better in each"]
            }
        }
    },
    "Economics": {
        "course_data": {
            "Required Courses": {
                "All Years": ["ECON 102 - Principles of Microeconomics (4 credits)", "ECON 103 - Principles of Macroeconomics (4 credits)", "ECON 251 - Intermediate Macroeconomics OR ECON 252 - Intermediate Microeconomics (4 credits)", "Three additional ECON courses, at least two at 300-400 level (12 credits)", "Total: 24 credits minimum"]
            }
        }
    },
    "Educational Studies": {
        "course_data": {
            "Required Courses": {
                "All Years": ["EDUC 206 - Education in America: Social Foundations of Education (4 credits)", "EDUC 336 - Exceptionality: An Introduction to Special Education (4 credits)", "EDUC 368 - Educational Psychology (4 credits)", "EDUC 396 - Language Acquisition and Phonemic Awareness OR EDUC 386 - Literacy in the Content Areas for Secondary Teachers (4 credits)", "PSYC 230 - Lifespan Development OR PSYC 431 - Infant and Child Development (4 credits)", "Note: EDUC 491 (ESL Across the Curriculum) required for MAT licensure tracks", "Total: 20 credits minimum, C or better in each course (at least 16 credits must be EDUC-coded, at least 12 upper-division)"]
            }
        }
    },
    "English": {
        "course_data": {
            "Required Courses": {
                "All Years": ["ENGL 204 - Reading and Writing in the Major (4 credits)", "Four additional English courses (at least 8 credits at 300/400 level, up to 4 credits from other departments)", "Total: 18 credits minimum across 5 courses, C- or better in each"]
            }
        }
    },
    "History": {
        "course_data": {
            "Required Courses": {
                "All Years": ["24 credits in history total", "At least 16 credits at the 300-400 level", "At least one course at the 400 level", "Courses must draw from at least two of four areas: The Americas; Europe; Africa & Asia; Comparative/Thematic/Global", "Grade of C- or better in each course"]
            }
        }
    },
    "Mathematics": {
        "course_data": {
            "Required Courses": {
                "All Years": ["MATH 151 - Calculus I (4 credits)", "MATH 152 - Calculus II (4 credits)", "MATH 255 - Vector Calculus (4 credits)", "MATH 256 - Linear Algebra (4 credits)", "MATH 281 - Foundations of Mathematics (4 credits)", "Total: 20 credits minimum, C- or better in each course"]
            }
        }
    },
    "Philosophy": {
        "course_data": {
            "Required Courses": {
                "All Years": ["PHIL 101 - Introduction to Philosophy OR PHIL 120 - Introduction to Ethics (4 credits)", "PHIL 300 - Cranks and Sages: Greek and Roman Philosophy OR PHIL 302 - Mind and Knowledge: Descartes to Kant (4 credits)", "Electives: 12 credits total - at least 8 at upper level, at least 4 credits non-Western philosophy (PHIL 351, 352, or approved PHIL 380)", "Total: 20 credits minimum"]
            }
        }
    },
    "Physics": {
        "course_data": {
            "Required Courses": {
                "All Years": ["Introductory sequence (12 credits): PHYS 151/152/251 OR PHYS 141/142/251", "Two elective courses (8 credits): choose from PHYS 281, 311, 312, 342, 351, 382, 391, 392, 462, 473, 475, 490 (PHYS 311 and 312 cannot both be used)", "Total: 20 credits minimum, 2.0 GPA in minor courses"]
            }
        }
    },
    "Sociology": {
        "course_data": {
            "Required Courses": {
                "All Years": ["SOCI 101 - Introduction to Sociology (4 credits)", "16 additional credits in sociology courses of choice", "Total: 20 credits minimum, C- or better in each course"]
            }
        }
    },
    "Neuroscience": {
        "course_data": {
            "Required Courses": {
                "All Years": ["CHEM 101 - Contemporary Chemistry with Lab OR CHEM 106 - General Chemistry II (4 credits)", "PSYC 101 - Introduction to Psychology (4 credits)", "NEUR 201 - Introduction to Neuroscience (4 credits)", "NEUR 310 - Special Topics in Neuroscience (4 credits)", "Electives: 12 credits from at least 2 disciplines (BIOL, CHEM, NEUR, PHIL, PSYC)", "Total: 20+ credits minimum, C or better in each course"]
            }
        }
    },
    "Music": {
        "course_data": {
            "Required Courses": {
                "All Years": ["MUSC 203 - Music Theory I (3 credits) + MUSC 201 - Sight Singing & Dictation I (1 credit)", "MUSC 302 - Music Theory II (3 credits) + MUSC 301 - Sight Singing & Dictation II (1 credit)", "MUSA 48x - Ensemble (4 semesters × 3 credits = 12 credits required)", "MUSA 38x - Private Lessons (4 semesters × 1 credit = 4 credits required)", "Two elective courses in music (credits vary)", "Total: 26+ credits minimum, C- or better in each course; not available to Performing Arts (Music) majors"]
            }
        }
    },
    "Theater Studies": {
        "course_data": {
            "Required Courses": {
                "All Years": ["PERF 110 - Critical Creativity in the Performing Arts (4 credits)", "TDPS 171 - Elements of Design (4 credits)", "TDPS 230 - Acting I OR TDPS 250 - Movement I (4 credits)", "12 credits of electives from approved TDPS list (at least 4 credits at 300-400 level; max 4 credits from practicum TDPS 290/490)", "Total: 20 credits minimum, C- or better in each course"]
            }
        }
    },
    "International Languages and Cultures": {
        "course_data": {
            "Required Courses": {
                "All Years": ["18 credits minimum; concentration-specific requirements:", "French/Spanish: 12 credits at 300-400 level, at least 4 upper-level credits at SMCM", "Chinese: 14 credits in Chinese language, 12 credits at 300-400 level; up to 4 upper-level credits may be Asian Studies electives (ASIA 305, HIST 351/352, PHIL 351, POSC 333, ECON 377, etc.)", "Grade of C- or better in each course, GPA 2.0 in minor courses"]
            }
        }
    },
    "Materials Science": {
        "course_data": {
            "Required Courses": {
                "All Years": ["CHEM 106 - General Chemistry II (4 credits, satisfies Natural Sciences Core requirement)", "PHYS 141 - General Physics I OR PHYS 151 - Fundamentals of Physics I (4 credits)", "PHYS 142 - General Physics II OR PHYS 152 - Fundamentals of Physics II (4 credits)", "MTSC 301 - Introduction to Materials Science (4 credits)", "CHEM 311 - Organic Chemistry I (4 credits)", "PHYS 462 - Quantum Mechanics (4 credits)", "One elective from: CHEM 312, CHEM 405, CHEM 451, BIOL 471, MTSC 302, PHYS 311, or approved upper-level special topics (4 credits)", "Total: 24+ credits minimum, C- or better in each course"]
            }
        }
    },
    "Museum Studies": {
        "course_data": {
            "Required Courses": {
                "All Years": ["MUST 200 - Introduction to Museum Studies (4 credits, must complete before declaring minor)", "12 credits of approved electives with museum studies focus (at least 8 at 300-400 level, from at least two disciplines)", "MUST 398 - Internship in a museum or related organization (4 credits)", "Total: 20 credits minimum, C- or better in each course"]
            }
        }
    },
    "Musical Arts Administration": {
        "course_data": {
            "Required Courses": {
                "All Years": ["MUSC 316 - Arts Administration: The Business Behind the Curtain (4 credits)", "ECON 102 - Principles of Microeconomics (4 credits)", "MUSC 398 - Off-Campus Internship in concert production (4+ credits)", "Finance/Business elective: BADM 201, BADM 301, or BADM 304 (4 credits)", "Music elective: MUSC 216 - Introduction to the World's Music OR MUSC 217 - The Jazz Makers (4 credits)", "Total: 18+ credits minimum, grade of C or better in each course"]
            }
        }
    },
    "Special Education": {
        "course_data": {
            "Required Courses": {
                "All Years": ["EDUC 331 - Behavior and Related Disorders (4 credits)", "EDUC 336 - Exceptionality: An Introduction to Special Education (4 credits)", "EDUC 339 - Learning Disabilities (4 credits)", "EDUC 368 - Educational Psychology (4 credits)", "EDUC 396 - Language Acquisition and Phonemic Awareness (4 credits)", "PSYC 431 - Infant and Child Development OR PSYC 230 - Lifespan Development (4 credits)", "Total: 28 credits"]
            }
        }
    }
}

# ==============================================================================
# DROPDOWN MENUS FOR MAJOR, YEAR, TRACK, LEAD PATH, AND MINOR
# ==============================================================================

# LEAD Path selection (first, since it applies to all students)
col1_lead, col2_lead, col3_lead = st.columns(3)

with col1_lead:
    st.markdown('<p style="color: #364B9A; font-weight: 700; margin-bottom: 0.25rem;">Select Your LEAD Path:</p>', unsafe_allow_html=True)
    lead_path = st.selectbox(
        "Select Your LEAD Path:",
        [""] + list(lead_paths.keys()),
        format_func=lambda x: "-- Select LEAD Path --" if x == "" else x,
        label_visibility="collapsed"
    )

with col2_lead:
    if lead_path:
        st.markdown("")
        st.caption(f"*{lead_paths[lead_path]['description']}*")

st.markdown("")

# Major, Year, and Track in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<p style="color: #1B7837; font-weight: 700; margin-bottom: 0.25rem;">Select Your Major:</p>', unsafe_allow_html=True)
    major = st.selectbox(
        "Select Your Major:",
        [""] + list(major_data.keys()),
        format_func=lambda x: "-- Select Major --" if x == "" else x,
        label_visibility="collapsed"
    )

with col2:
    st.markdown('<p style="color: var(--smcm-navy); font-weight: 700; margin-bottom: 0.25rem;">Select Your Current Year:</p>', unsafe_allow_html=True)
    year = st.selectbox(
        "Select Your Current Year:",
        ["", "First Year", "Sophomore", "Junior", "Senior"],
        format_func=lambda x: "-- Select Year --" if x == "" else x,
        label_visibility="collapsed"
    )

with col3:
    # Only show track dropdown if the major has tracks
    if major and major_data.get(major, {}).get("has_tracks"):
        st.markdown('<p style="color: var(--smcm-navy); font-weight: 700; margin-bottom: 0.25rem;">Select Your Track:</p>', unsafe_allow_html=True)
        track = st.selectbox(
            "Select Your Track:",
            [""] + major_data[major]["tracks"],
            format_func=lambda x: "-- Select Track --" if x == "" else x,
            label_visibility="collapsed"
        )
    else:
        track = None
        if major:
            st.markdown("**Track:** N/A")
        else:
            st.markdown("**Track:**")

st.markdown("")

# Double major / minor toggle
double_major = st.toggle("Double Major", value=False, key="double_major_toggle",
                         help="Enable to add a second major instead of a minor.")

if double_major:
    col_m2, col_t2, _ = st.columns(3)
    with col_m2:
        major2_options = [m for m in DOUBLE_MAJOR_OPTIONS if m != major]
        st.markdown('<p style="color: var(--smcm-navy); font-weight: 700; margin-bottom: 0.25rem;">Select Second Major:</p>', unsafe_allow_html=True)
        major2 = st.selectbox(
            "Select Second Major:",
            [""] + major2_options,
            format_func=lambda x: "-- Select Second Major --" if x == "" else x,
            label_visibility="collapsed"
        )
    with col_t2:
        if major2 and major_data.get(major2, {}).get("has_tracks"):
            st.markdown('<p style="color: var(--smcm-navy); font-weight: 700; margin-bottom: 0.25rem;">Second Major Track:</p>', unsafe_allow_html=True)
            track2 = st.selectbox(
                "Second Major Track:",
                [""] + major_data[major2]["tracks"],
                format_func=lambda x: "-- Select Track --" if x == "" else x,
                label_visibility="collapsed"
            )
        else:
            track2 = None
            st.markdown("**Second Major Track:** N/A")
    minor = None
else:
    major2 = None
    track2 = None
    col1_minor, col2_minor, col3_minor = st.columns(3)
    with col1_minor:
        st.markdown('<p style="color: var(--smcm-navy); font-weight: 700; margin-bottom: 0.25rem;">Select Your Minor (Optional):</p>', unsafe_allow_html=True)
        minor = st.selectbox(
            "Select Your Minor (Optional):",
            [""] + list(minor_data.keys()),
            format_func=lambda x: "-- No Minor / Select Minor --" if x == "" else x,
            label_visibility="collapsed"
        )
    with col2_minor:
        st.markdown("")
        if minor:
            st.caption(f"*Adding {minor} Minor to your plan*")
        else:
            st.caption("*Optional: You can add a minor to your degree*")

# Color guide — shows 4 colors when double major is active
if double_major and major2:
    st.markdown(f"""
<div class="no-print" style="display: flex; gap: 24px; align-items: center; margin: 4px 0 12px 0; font-size: 0.9em;">
    <span style="font-weight: 600; color: #444;">Color guide:</span>
    <span><span style="color: #364B9A; font-size: 1.1em;">&#9679;</span>&nbsp;<span style="color: #364B9A; font-weight: 600;">LEAD Path</span></span>
    <span><span style="color: #1B7837; font-size: 1.1em;">&#9679;</span>&nbsp;<span style="color: #1B7837; font-weight: 600;">{major}</span></span>
    <span><span style="color: #B05D0E; font-size: 1.1em;">&#9679;</span>&nbsp;<span style="color: #B05D0E; font-weight: 600;">{major2}</span></span>
    <span><span style="color: #C0392B; font-size: 1.1em;">&#9679;</span>&nbsp;<span style="color: #C0392B; font-weight: 600;">Both Majors</span></span>
</div>
""", unsafe_allow_html=True)
else:
    st.markdown("""
<div class="no-print" style="display: flex; gap: 24px; align-items: center; margin: 4px 0 12px 0; font-size: 0.9em;">
    <span style="font-weight: 600; color: #444;">Color guide:</span>
    <span><span style="color: #364B9A; font-size: 1.1em;">&#9679;</span>&nbsp;<span style="color: #364B9A; font-weight: 600;">LEAD Path</span></span>
    <span><span style="color: #1B7837; font-size: 1.1em;">&#9679;</span>&nbsp;<span style="color: #1B7837; font-weight: 600;">Major</span></span>
    <span><span style="color: #762A83; font-size: 1.1em;">&#9679;</span>&nbsp;<span style="color: #762A83; font-weight: 600;">Satisfies Both</span></span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Check if all required selections are made
selections_complete = bool(lead_path and major and year)

# For majors with tracks, also check if track is selected
if selections_complete and major and major_data.get(major, {}).get("has_tracks"):
    selections_complete = bool(track)

# Double major: also require major2 (and track2 if major2 has tracks)
if selections_complete and double_major:
    selections_complete = bool(major2)
    if selections_complete and major2 and major_data.get(major2, {}).get("has_tracks"):
        selections_complete = bool(track2)

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def extract_course_code(course_string):
    """
    Extract course code from a course string.
    Examples:
        'ENST 100 - Environment and Society (4 credits)' -> 'ENST 100'
        'LEAD 101 - LEAD Seminar (must earn C- or higher)' -> 'LEAD 101'
        'CHEM 103 - General Chemistry I (4 credits)' -> 'CHEM 103'
    """
    if not course_string:
        return None

    # Split by common delimiters and get the first part
    parts = course_string.split('-')[0].strip().split('(')[0].strip().split(':')[0].strip()

    # Extract department code and number (e.g., "ENST 100", "LEAD 101")
    tokens = parts.split()
    if len(tokens) >= 2:
        # Check if second token looks like a course number
        second_token = tokens[1].replace('/', '')
        if second_token.isdigit() or (len(second_token) > 0 and second_token[0].isdigit()):
            return f"{tokens[0]} {tokens[1]}"

    return None

def get_courses_for_year(year_name, selected_major, selected_lead_path, selected_track=None, selected_minor=None, selected_major2=None, selected_track2=None):
    """Get all courses for a specific year, with deduplication for courses that satisfy LEAD, major, and/or minor/major2."""
    lead_courses = []
    major_courses = []
    minor_courses = []
    major2_courses = []

    # First, get LEAD path courses for this year
    if year_name in lead_paths[selected_lead_path]["courses"]:
        lead_courses = lead_paths[selected_lead_path]["courses"][year_name][:]

    # Helper: extract courses for a major+track into a list
    def collect_major_courses(maj, trk):
        result = []
        cd = major_data[maj]["course_data"]
        if major_data[maj]["has_tracks"] and trk:
            for category, years in cd.items():
                if year_name in years:
                    if category in major_data[maj]["tracks"]:
                        if category == trk:
                            result.extend(years[year_name])
                    elif category != "LEAD":
                        result.extend(years[year_name])
        else:
            for category, years in cd.items():
                if year_name in years and category != "LEAD":
                    result.extend(years[year_name])
        return result

    major_courses = collect_major_courses(selected_major, selected_track)

    if selected_major2:
        major2_courses = collect_major_courses(selected_major2, selected_track2)
    elif selected_minor:
        minor_course_data = minor_data[selected_minor]["course_data"]
        for category, years in minor_course_data.items():
            if year_name in years:
                minor_courses.extend(years[year_name])

    # Build code maps
    lead_course_map = {extract_course_code(c): c for c in lead_courses if extract_course_code(c)}
    major_course_map = {extract_course_code(c): c for c in major_courses if extract_course_code(c)}
    minor_course_map = {extract_course_code(c): c for c in minor_courses if extract_course_code(c)}
    major2_course_map = {extract_course_code(c): c for c in major2_courses if extract_course_code(c)}

    lead_codes = set(lead_course_map.keys())
    major_codes = set(major_course_map.keys())
    minor_codes = set(minor_course_map.keys())
    major2_codes = set(major2_course_map.keys())

    courses = []

    if selected_major2:
        # ---- Double major mode ----
        lead_major1_major2 = lead_codes & major_codes & major2_codes
        lead_major1 = (lead_codes & major_codes) - lead_major1_major2
        lead_major2 = (lead_codes & major2_codes) - lead_major1_major2
        major1_major2 = (major_codes & major2_codes) - lead_major1_major2

        for course in lead_courses:
            code = extract_course_code(course)
            if code in lead_major1_major2:
                courses.append(("lead_major1_major2", course))
            elif code in lead_major1:
                courses.append(("lead_major1", course))
            elif code in lead_major2:
                courses.append(("lead_major2", course))
            else:
                courses.append(("lead_only", course))

        for course in major_courses:
            code = extract_course_code(course)
            if code not in lead_codes:
                if code in major1_major2:
                    courses.append(("major1_major2", course))
                else:
                    courses.append(("major_only", course))

        for course in major2_courses:
            code = extract_course_code(course)
            if code not in lead_codes and code not in major_codes:
                courses.append(("major2_only", course))

    else:
        # ---- Single major + optional minor mode (original logic) ----
        all_three = lead_codes & major_codes & minor_codes
        lead_major = (lead_codes & major_codes) - all_three
        lead_minor = (lead_codes & minor_codes) - all_three
        major_minor = (major_codes & minor_codes) - all_three

        for course in lead_courses:
            code = extract_course_code(course)
            if code in all_three:
                courses.append(("all_three", course))
            elif code in lead_major:
                courses.append(("lead_major", course))
            elif code in lead_minor:
                courses.append(("lead_minor", course))
            else:
                courses.append(("lead_only", course))

        for course in major_courses:
            code = extract_course_code(course)
            if code not in lead_codes:
                if code in major_minor:
                    courses.append(("major_minor", course))
                else:
                    courses.append(("major_only", course))

        # Note: minor_only courses are NOT added here
        # They will be displayed in a separate "Minor Courses Left" section

    return courses

def get_all_minor_courses(selected_minor, selected_major, selected_lead_path, selected_track=None):
    """
    Get all minor courses across all years, identifying which are already covered
    by major/LEAD requirements and which still need to be taken.
    Returns list of tuples: (status, course_string)
    where status is "covered_by_major", "covered_by_lead", "covered_by_both", or "still_needed"
    """
    if not selected_minor:
        return []

    # Get all minor courses across all years
    all_minor_courses = []
    minor_course_data = minor_data[selected_minor]["course_data"]
    for category, years in minor_course_data.items():
        for year, courses in years.items():
            all_minor_courses.extend(courses)

    # Get all major courses across all years
    all_major_courses = []
    year_order = ["First Year", "Sophomore", "Junior", "Senior"]
    course_data = major_data[selected_major]["course_data"]

    for year_name in year_order:
        if major_data[selected_major]["has_tracks"] and selected_track:
            for category, years in course_data.items():
                if year_name in years:
                    if category in major_data[selected_major]["tracks"]:
                        if category == selected_track:
                            all_major_courses.extend(years[year_name])
                    else:
                        if category != "LEAD":
                            all_major_courses.extend(years[year_name])
        else:
            for category, years in course_data.items():
                if year_name in years:
                    if category != "LEAD":
                        all_major_courses.extend(years[year_name])

    # Get all LEAD courses across all years
    all_lead_courses = []
    for year_name in year_order:
        if year_name in lead_paths[selected_lead_path]["courses"]:
            all_lead_courses.extend(lead_paths[selected_lead_path]["courses"][year_name])

    # Create course code maps
    major_codes = set()
    for course in all_major_courses:
        code = extract_course_code(course)
        if code:
            major_codes.add(code)

    lead_codes = set()
    for course in all_lead_courses:
        code = extract_course_code(course)
        if code:
            lead_codes.add(code)

    # Categorize minor courses
    result = []
    for course in all_minor_courses:
        code = extract_course_code(course)
        if code:
            in_major = code in major_codes
            in_lead = code in lead_codes

            if in_major and in_lead:
                result.append(("covered_by_both", course))
            elif in_major:
                result.append(("covered_by_major", course))
            elif in_lead:
                result.append(("covered_by_lead", course))
            else:
                result.append(("still_needed", course))
        else:
            # If we can't extract a code, assume it's still needed
            result.append(("still_needed", course))

    return result

def display_course_with_checkbox(course_data, key_prefix, selected_major, selected_track=None, selected_lead_path=None, selected_major2=None, selected_track2=None):
    """Display a course with a checkbox for completion tracking"""
    # Handle tuple format (requirement_type, course_string)
    if isinstance(course_data, tuple):
        requirement_type, course = course_data
    else:
        # Backwards compatibility - treat as major_only
        requirement_type = "major_only"
        course = course_data

    # Determine color class and inline color upfront so all branches can use it
    if requirement_type in ["lead_major1_major2", "major1_major2"]:
        color_class = "course-both-majors"
        inline_color = "#C0392B"
    elif requirement_type in ["major2_only", "lead_major2"]:
        color_class = "course-major2-only"
        inline_color = "#B05D0E"
    elif requirement_type in ["lead_major1"]:
        color_class = "course-major-only"
        inline_color = "#1B7837"
    elif requirement_type in ["all_three", "lead_major", "lead_minor", "major_minor"]:
        color_class = "course-multiple"
        inline_color = "#762A83"
    elif requirement_type == "lead_only":
        color_class = "course-lead-only"
        inline_color = "#364B9A"
    elif requirement_type == "major_only":
        color_class = "course-major-only"
        inline_color = "#1B7837"
    else:
        color_class = ""
        inline_color = ""

    # Check if this is a LEAD Inquiry course with electives
    if selected_lead_path and selected_lead_path in lead_paths and "inquiry_electives" in lead_paths[selected_lead_path]:
        # Check if the course mentions any category that has electives defined
        inquiry_electives = lead_paths[selected_lead_path]["inquiry_electives"]
        matched_category = None
        for category in inquiry_electives.keys():
            if category in course:
                matched_category = category
                break

        if matched_category:
            # Use column layout for alignment with regular courses
            col1, col2 = st.columns([0.05, 0.95])
            with col1:
                any_checked = any(
                    st.session_state.get(f"{key_prefix}_inquiry_elective_{e}", False)
                    for e in inquiry_electives[matched_category]
                )
                st.markdown("☑" if any_checked else "☐")
            with col2:
                strikethrough = "text-decoration:line-through;" if any_checked else ""
                color_style = f"color:{inline_color};" if inline_color else ""
                st.markdown(f'<span style="{color_style}{strikethrough}font-weight:bold;">{course}</span>', unsafe_allow_html=True)
                with st.expander(f"View {matched_category} courses"):
                    for elective in inquiry_electives[matched_category]:
                        col1_inner, col2_inner = st.columns([0.05, 0.95])
                        with col1_inner:
                            elective_key = f"{key_prefix}_inquiry_elective_{elective}"
                            current_state = st.session_state.completed_courses.get(elective_key, False)
                            is_completed = st.checkbox("✓", value=current_state, key=elective_key, label_visibility="collapsed")
                            st.session_state.completed_courses[elective_key] = is_completed
                        with col2_inner:
                            if is_completed:
                                st.markdown(f'<span style="color:{inline_color};">~~{elective}~~</span>' if inline_color else f"~~{elective}~~", unsafe_allow_html=True)
                            else:
                                st.markdown(f'<span style="color:{inline_color};">{elective}</span>' if inline_color else elective, unsafe_allow_html=True)
            return  # Exit early since we've handled this course

    # Use req_type to determine which major "owns" this course for elective expansion.
    # major2_only and lead_major2 courses belong to major2; everything else to major1.
    _eff_major = (selected_major2 if (requirement_type in ["major2_only", "lead_major2"] and selected_major2) else selected_major)
    _eff_track = (selected_track2 if (requirement_type in ["major2_only", "lead_major2"] and selected_major2) else selected_track)

    # Check if this is a depth electives item that should show an expander
    if "Track Depth Electives" in course and major_data.get(_eff_major, {}).get("has_tracks") and _eff_track:
        col1, col2 = st.columns([0.05, 0.95])
        with col1:
            any_checked = any(
                st.session_state.get(f"{key_prefix}_{_eff_major}_elective_{e}", False)
                for e in major_data[_eff_major]["track_electives"].get(_eff_track, [])
            )
            st.markdown("☑" if any_checked else "☐")
        with col2:
            strikethrough = "text-decoration:line-through;" if any_checked else ""
            color_style = f"color:{inline_color};" if inline_color else ""
            st.markdown(f'<span style="{color_style}{strikethrough}font-weight:bold;">{course}</span>', unsafe_allow_html=True)
            with st.expander(f"View all {_eff_track} track courses"):
                st.markdown(f"**Choose {course.split(':')[1].strip().split('(')[0]} from the following courses:**")
                for elective in major_data[_eff_major]["track_electives"].get(_eff_track, []):
                    col1_inner, col2_inner = st.columns([0.05, 0.95])
                    with col1_inner:
                        elective_key = f"{key_prefix}_{_eff_major}_elective_{elective}"
                        current_state = st.session_state.completed_courses.get(elective_key, False)
                        is_completed = st.checkbox("✓", value=current_state, key=elective_key, label_visibility="collapsed")
                        st.session_state.completed_courses[elective_key] = is_completed
                    with col2_inner:
                        if is_completed:
                            st.markdown(f'<span style="color:{inline_color};">~~{elective}~~</span>' if inline_color else f"~~{elective}~~", unsafe_allow_html=True)
                        else:
                            st.markdown(f'<span style="color:{inline_color};">{elective}</span>' if inline_color else elective, unsafe_allow_html=True)
    # Check if this course mentions electives and the owning major has elective_courses
    elif ("elective" in course.lower() or "Electives" in course) and "elective_courses" in major_data.get(_eff_major, {}):
        col1, col2 = st.columns([0.05, 0.95])
        with col1:
            all_electives = [e for cat_courses in major_data[_eff_major]["elective_courses"].values() for e in cat_courses]
            any_checked = any(
                st.session_state.get(f"{key_prefix}_{_eff_major}_elective_{e}", False)
                for e in all_electives
            )
            st.markdown("☑" if any_checked else "☐")
        with col2:
            strikethrough = "text-decoration:line-through;" if any_checked else ""
            color_style = f"color:{inline_color};" if inline_color else ""
            st.markdown(f'<span style="{color_style}{strikethrough}font-weight:bold;">{course}</span>', unsafe_allow_html=True)
            elective_data = major_data[_eff_major]["elective_courses"]
            for category, courses in elective_data.items():
                with st.expander(f"View {category} courses"):
                    for elective in courses:
                        col1_inner, col2_inner = st.columns([0.05, 0.95])
                        with col1_inner:
                            elective_key = f"{key_prefix}_{_eff_major}_elective_{elective}"
                            current_state = st.session_state.completed_courses.get(elective_key, False)
                            is_completed = st.checkbox("✓", value=current_state, key=elective_key, label_visibility="collapsed")
                            st.session_state.completed_courses[elective_key] = is_completed
                        with col2_inner:
                            if is_completed:
                                st.markdown(f'<span style="color:{inline_color};">~~{elective}~~</span>' if inline_color else f"~~{elective}~~", unsafe_allow_html=True)
                            else:
                                st.markdown(f'<span style="color:{inline_color};">{elective}</span>' if inline_color else elective, unsafe_allow_html=True)
    else:
        # Regular course display
        col1, col2 = st.columns([0.05, 0.95])
        with col1:
            checkbox_key = f"{key_prefix}_{course}"
            current_state = st.session_state.completed_courses.get(checkbox_key, False)
            is_completed = st.checkbox("✓", value=current_state, key=checkbox_key, label_visibility="collapsed")
            st.session_state.completed_courses[checkbox_key] = is_completed
        with col2:
            # Badge text
            if requirement_type == "lead_major1_major2":
                badge = f" *Satisfies LEAD, {selected_major} & {selected_major2}*" if selected_major2 else " *Satisfies LEAD, Major 1 & Major 2*"
            elif requirement_type == "major1_major2":
                badge = f" *Satisfies {selected_major} & {selected_major2}*" if selected_major2 else " *Satisfies Major 1 & Major 2*"
            elif requirement_type == "lead_major2":
                badge = f" *Satisfies LEAD & {selected_major2}*" if selected_major2 else " *Satisfies LEAD & Major 2*"
            elif requirement_type == "lead_major1":
                badge = f" *Satisfies LEAD & {selected_major}*"
            elif requirement_type == "all_three":
                badge = " *Satisfies LEAD, Major & Minor*"
            elif requirement_type == "lead_major":
                badge = " *Satisfies LEAD & Major*"
            elif requirement_type == "lead_minor":
                badge = " *Satisfies LEAD & Minor*"
            elif requirement_type == "major_minor":
                badge = " *Satisfies Major & Minor*"
            else:
                badge = ""

            # Apply strikethrough if completed and color coding
            if color_class:
                if is_completed:
                    st.markdown(f'<span class="{color_class}">~~{course}~~{badge}</span>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<span class="{color_class}">{course}{badge}</span>', unsafe_allow_html=True)
            else:
                if is_completed:
                    st.markdown(f"~~{course}~~{badge}")
                else:
                    st.markdown(f"{course}{badge}")

def generate_rtf(year_order, current_year_index, selected_major, selected_lead_path, selected_track, selected_minor, selected_year, selected_major2=None, selected_track2=None):
    """Generate an RTF document reflecting the current course plan and completion state."""

    def esc(text):
        """Escape RTF special characters and encode non-ASCII as Unicode escapes."""
        text = text.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")
        out = []
        for ch in text:
            if ord(ch) > 127:
                out.append(f"\\u{ord(ch)}?")
            else:
                out.append(ch)
        return "".join(out)

    def course_line(course, key, indent=""):
        """Return an RTF line with [x]/[ ] and strikethrough based on session state."""
        done = st.session_state.completed_courses.get(key, False)
        text = esc(course)
        if done:
            return f"{indent}[x] {{\\strike {text}}}\\par\n"
        return f"{indent}[ ] {text}\\par\n"

    def section_rtf(courses_list, key_prefix):
        """Render a list of (req_type, course) tuples as RTF lines."""
        lines = []
        for _req_type, course in courses_list:
            # Inquiry electives — expand inline
            if selected_lead_path in lead_paths and "inquiry_electives" in lead_paths[selected_lead_path]:
                matched = False
                for category, electives in lead_paths[selected_lead_path]["inquiry_electives"].items():
                    if category in course:
                        lines.append(f"\\b {esc(course)}\\b0\\par\n")
                        for e in electives:
                            lines.append(course_line(e, f"{key_prefix}_inquiry_elective_{e}", indent="  "))
                        matched = True
                        break
                if matched:
                    continue
            # Track depth electives — use requirement_type to pick the owning major
            _rtf_eff_major = (selected_major2 if (_req_type in ["major2_only", "lead_major2"] and selected_major2) else selected_major)
            _rtf_eff_track = (selected_track2 if (_req_type in ["major2_only", "lead_major2"] and selected_major2) else selected_track)
            if "Track Depth Electives" in course and major_data.get(_rtf_eff_major, {}).get("has_tracks") and _rtf_eff_track:
                lines.append(f"\\b {esc(course)}\\b0\\par\n")
                for e in major_data[_rtf_eff_major]["track_electives"].get(_rtf_eff_track, []):
                    lines.append(course_line(e, f"{key_prefix}_{_rtf_eff_major}_elective_{e}", indent="  "))
                continue
            # Major elective_courses — use owning major derived from requirement_type
            if ("elective" in course.lower() or "Electives" in course) and "elective_courses" in major_data.get(_rtf_eff_major, {}):
                lines.append(f"\\b {esc(course)}\\b0\\par\n")
                for cat_name, cat_courses in major_data[_rtf_eff_major]["elective_courses"].items():
                    lines.append(f"  \\i {esc(cat_name)}:\\i0\\par\n")
                    for e in cat_courses:
                        lines.append(course_line(e, f"{key_prefix}_{_rtf_eff_major}_elective_{e}", indent="    "))
                continue
            # Regular course
            lines.append(course_line(course, f"{key_prefix}_{course}"))
        return "".join(lines)

    r = []
    r.append("{\\rtf1\\ansi\\deff0\n")
    r.append("{\\fonttbl{\\f0\\fswiss\\fcharset0 Arial;}}\n")
    r.append("\\f0\\fs20\n")

    # Header
    r.append(f"\\b\\fs28 SMCM Course Planning Guide\\b0\\fs20\\par\n")
    r.append(f"\\b Major 1:\\b0 {esc(selected_major)}" if selected_major2 else f"\\b Major:\\b0 {esc(selected_major)}")
    if selected_track:
        r.append(f" ({esc(selected_track)} track)")
    if selected_major2:
        r.append(f"  \\b Major 2:\\b0 {esc(selected_major2)}")
        if selected_track2:
            r.append(f" ({esc(selected_track2)} track)")
    r.append(f"  \\b LEAD Path:\\b0 {esc(selected_lead_path)}")
    r.append(f"  \\b Year:\\b0 {esc(selected_year)}")
    if selected_minor:
        r.append(f"  \\b Minor:\\b0 {esc(selected_minor)}")
    r.append("\\par\n\\par\n")

    # Past years
    if current_year_index > 0:
        r.append("\\b\\fs24 COURSES YOU SHOULD HAVE TAKEN\\b0\\fs20\\par\n\\par\n")
        for i in range(current_year_index):
            r.append(f"\\b {esc(year_order[i])}:\\b0\\par\n")
            courses = get_courses_for_year(year_order[i], selected_major, selected_lead_path, selected_track, selected_minor, selected_major2, selected_track2)
            r.append(section_rtf(courses, "past"))
            r.append("\\par\n")

    # Current year
    r.append(f"\\b\\fs24 COURSES THIS YEAR ({esc(selected_year)})\\b0\\fs20\\par\n\\par\n")
    courses = get_courses_for_year(selected_year, selected_major, selected_lead_path, selected_track, selected_minor, selected_major2, selected_track2)
    r.append(section_rtf(courses, "current"))
    r.append("\\par\n")

    # Next year
    if current_year_index < len(year_order) - 1:
        next_year = year_order[current_year_index + 1]
        r.append(f"\\b\\fs24 COURSES NEXT YEAR ({esc(next_year)})\\b0\\fs20\\par\n\\par\n")
        next_courses = get_courses_for_year(next_year, selected_major, selected_lead_path, selected_track, selected_minor, selected_major2, selected_track2)
        r.append(section_rtf(next_courses, "next"))
        r.append("\\par\n")

    # Future years
    if current_year_index <= 1:
        r.append("\\b\\fs24 FUTURE COURSE REQUIREMENTS\\b0\\fs20\\par\n\\par\n")
        for i in range(current_year_index + 2, len(year_order)):
            year_name = year_order[i]
            courses = get_courses_for_year(year_name, selected_major, selected_lead_path, selected_track, selected_minor, selected_major2, selected_track2)
            if courses:
                r.append(f"\\b {esc(year_name)}:\\b0\\par\n")
                r.append(section_rtf(courses, f"future_{year_name}"))
                r.append("\\par\n")

    # Minor (only in single-major mode)
    if selected_minor:
        r.append(f"\\b\\fs24 {esc(selected_minor).upper()} MINOR\\b0\\fs20\\par\n\\par\n")
        minor_status = get_all_minor_courses(selected_minor, selected_major, selected_lead_path, selected_track)
        covered = [(s, c) for s, c in minor_status if s != "still_needed"]
        still_needed = [(s, c) for s, c in minor_status if s == "still_needed"]
        if covered:
            r.append("\\i Already covered by your Major/LEAD requirements:\\i0\\par\n")
            for status, course in covered:
                note = {"covered_by_both": " (Covered by LEAD & Major)",
                        "covered_by_major": " (Covered by Major)",
                        "covered_by_lead": " (Covered by LEAD)"}.get(status, "")
                r.append(course_line(course + note, f"minor_covered_{course}"))
            r.append("\\par\n")
        if still_needed:
            r.append("\\i Additional courses needed for minor:\\i0\\par\n")
            for _, course in still_needed:
                r.append(course_line(course, f"minor_needed_{course}"))

    r.append("}\n")
    return "".join(r)


# ==============================================================================
# DISPLAY COURSE RECOMMENDATIONS
# ==============================================================================

# Only display course planning if all selections are made
if selections_complete:
    year_order = ["First Year", "Sophomore", "Junior", "Senior"]
    current_year_index = year_order.index(year)

    st.header("Your Course Planning Guide")

    # Courses you should have taken (only show for Sophomore and above)
    if current_year_index > 0:
        st.subheader("Courses You Should Have Taken")
        past_courses = []
        for i in range(current_year_index):
            past_courses.extend(get_courses_for_year(year_order[i], major, lead_path, track, minor, major2, track2))

        if past_courses:
            for course in past_courses:
                display_course_with_checkbox(course, "past", major, track, lead_path, major2, track2)
        else:
            st.markdown("*No prior courses required yet*")

        st.markdown("---")

    # Courses you should be taking this year
    st.subheader(f"Courses You Should Be Taking This Year ({year})")
    current_courses = get_courses_for_year(year, major, lead_path, track, minor, major2, track2)

    if current_courses:
        for course in current_courses:
            display_course_with_checkbox(course, "current", major, track, lead_path, major2, track2)
    else:
        st.markdown("*No specific required courses this year - focus on electives and breadth requirements*")

    st.markdown("---")
    
    # Courses you should take next year
    if current_year_index < len(year_order) - 1:
        next_year = year_order[current_year_index + 1]
        st.subheader(f"Courses You Should Take Next Year ({next_year})")
        next_courses = get_courses_for_year(next_year, major, lead_path, track, minor, major2, track2)

        if next_courses:
            for course in next_courses:
                display_course_with_checkbox(course, "next", major, track, lead_path, major2, track2)
        else:
            st.markdown("*No specific required courses next year - focus on completing remaining requirements*")
    else:
        st.subheader("Next Steps")
        st.markdown("*You're in your final year! Focus on completing your capstone and any remaining requirements.*")
    
    # Future courses section (only for First Year and Sophomore students)
    if current_year_index <= 1:  # First Year (0) or Sophomore (1)
        st.markdown("---")
        st.subheader("Future Course Requirements")
        st.caption("Courses you'll take in your Junior and Senior years")
    
        future_courses = []
        for i in range(current_year_index + 2, len(year_order)):
            year_name = year_order[i]
            courses = get_courses_for_year(year_name, major, lead_path, track, minor, major2, track2)
            if courses:
                st.markdown(f"**{year_name}:**")
                for course in courses:
                    display_course_with_checkbox(course, f"future_{year_name}", major, track, lead_path, major2, track2)
                if i < len(year_order) - 1:  # Add spacing between years
                    st.markdown("")

    # Minor Courses Left section (if minor is selected) - shows for all years
    if minor:
        st.markdown("---")
        st.subheader(f"{minor} Minor - Courses to Complete")
        st.caption("These courses are needed for your minor (not organized by year)")

        minor_courses_status = get_all_minor_courses(minor, major, lead_path, track)

        if minor_courses_status:
            # Separate covered and still needed
            covered = [c for c in minor_courses_status if c[0] in ["covered_by_major", "covered_by_lead", "covered_by_both"]]
            still_needed = [c for c in minor_courses_status if c[0] == "still_needed"]

            # Show covered courses first (they're already in your plan!)
            if covered:
                st.markdown("*Already covered by your Major/LEAD requirements:*")
                for status, course in covered:
                    col1, col2 = st.columns([0.05, 0.95])
                    with col1:
                        # These are automatically completed since they're in major/lead
                        checkbox_key = f"minor_covered_{course}"
                        current_state = st.session_state.completed_courses.get(checkbox_key, False)
                        is_completed = st.checkbox("✓", value=current_state, key=checkbox_key, label_visibility="collapsed")
                        st.session_state.completed_courses[checkbox_key] = is_completed
                    with col2:
                        if status == "covered_by_both":
                            badge = " *Covered by LEAD & Major*"
                        elif status == "covered_by_major":
                            badge = " *Covered by Major*"
                        else:  # covered_by_lead
                            badge = " *Covered by LEAD*"

                        if is_completed:
                            st.markdown(f"~~{course}~~{badge}")
                        else:
                            st.markdown(f"{course}{badge}")
                st.markdown("")

            # Show courses still needed
            if still_needed:
                st.markdown("*Additional courses needed for minor:*")
                for status, course in still_needed:
                    col1, col2 = st.columns([0.05, 0.95])
                    with col1:
                        checkbox_key = f"minor_needed_{course}"
                        current_state = st.session_state.completed_courses.get(checkbox_key, False)
                        is_completed = st.checkbox("✓", value=current_state, key=checkbox_key, label_visibility="collapsed")
                        st.session_state.completed_courses[checkbox_key] = is_completed
                    with col2:
                        if is_completed:
                            st.markdown(f"~~{course}~~")
                        else:
                            st.markdown(course)
            else:
                st.success("All minor courses are covered by your Major/LEAD requirements!")
        else:
            st.markdown("*No minor course data available*")

    # ==============================================================================
    # PROGRAM REQUIREMENTS SUMMARY
    # ==============================================================================
    
    st.markdown("---")
    st.subheader("Program Requirements Summary")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown(f"**LEAD Curriculum Requirements**")
        st.markdown(f"*Selected Path: {lead_path}*")
        st.markdown("")
    
        if lead_path == "LEAD Exploration":
            st.markdown("""
            - LEAD 101 Seminar (C- or higher; transfers 24+ cr: LEAD 301)
            - LEAD 111 & 112 (Career Networking)
            - LEAD 211 (Honors College Externship; transfers: LEAD 311 optional)
            - Language Course (102/110+)
            - **Exploration:** 6 breadth areas (24 credits)
              - Arts (4 cr)
              - Cultural Literacy (4 cr)
              - Humanities (4 cr)
              - Mathematics (4 cr)
              - Natural Sciences with Lab (4 cr)
              - Social and Behavioral Sciences (4 cr)
            - Capstone (4-8 credits, public presentation required)
            - Minimum C- in LEAD courses, 2.0 GPA
            - Minimum D in all Foundational Study courses
            """)
        else:
            st.markdown(f"""
            - LEAD 101 Seminar (C- or higher; transfers 24+ cr: LEAD 301)
            - LEAD 111 & 112 (Career Networking)
            - LEAD 211 (Honors College Externship; transfers: LEAD 311 optional)
            - Language Course (102/110+)
            - **{lead_path}:** Integrated pathway (17-21 credits)
              - 4-5 thematically-linked courses + LEAD 250/ILPF 200 (1 cr, C/NC)
              - Fulfills all breadth requirements
            - Capstone (4-8 credits, public presentation required)
            - Minimum C- in LEAD courses, 2.0 GPA
            - Minimum D in all Foundational Study courses
            """)
    
    with col_b:
        st.markdown(f"**{major} Major Requirements**")
    
        # Major-specific summary
        if major == "Environmental Studies":
            st.markdown(f"""
            - Foundation Courses (17 credits)
            - Depth: 16 credits in {track} track
              - 8 credits at 300-400 level
            - Breadth: 8 credits (4 each from 2 other tracks)
            - ENST 490 Junior Seminar
            - Application: 4 credits
            - Capstone: 8 credits
            - Minimum C- with 2.0 GPA in major courses
            - **Total Major Credits:** 59+ minimum
            """)
        elif major == "Biology":
            st.markdown("""
            - Physical Science Foundation (12+ credits)
            - Biology Core Courses (16 credits)
            - Biology Core Labs (4 credits)
            - Upper-Level Electives (16+ credits, 8 with lab)
            - St. Mary's Project Capstone
            - Minimum C or better in core biology
            - Minimum C- in remaining major courses
            - **Total Major Credits:** 48+ minimum
            """)
        elif major == "Marine Science":
            st.markdown("""
            - Physical Science Foundation (12 credits)
            - Biology Core (10 credits)
            - Mathematics (4 credits)
            - Marine Science Core (12 credits)
            - Marine Science Electives (16 credits)
            - Professional Experience (4 credits)
            - Capstone (4 credits)
            - Minimum C in core biology
            - Minimum C- in remaining major courses
            - **Total Major Credits:** 62+ minimum
            """)
        elif major == "Psychology":
            st.markdown("""
            - Foundation Courses (16 credits)
            - Breadth Requirements (20-22 credits)
              - One from each of 5 areas
              - Min two 200-level
              - Min two 300-level lab courses
            - Upper-Level Elective (4-5 credits)
            - St. Mary's Project Capstone (8 credits)
            - Minimum C- with 2.0 GPA
            - **Total Major Credits:** 48+ minimum
            """)
        elif major == "Political Science":
            st.markdown(f"""
            - Core Breadth Requirements (24 credits)
              - POSC 100 Introduction
              - POSC 200 Methods
              - One from each subfield: American, Comparative, International, Theory
            - Depth & Concentration (12 credits)
              - {track} track
              - Upper-level courses in specialization
            - Capstone (12 credits)
              - Two 400-level seminars + one 300-level course
              - OR one 400-level + 8-credit St. Mary's Project
            - Minimum C- with 2.0 GPA
            - **Total Major Credits:** 48 credits
            """)
        elif major == "English":
            st.markdown("""
            - Core Requirements (24 credits)
              - Historical Literature: ENGL 284 & 285 (8 cr)
              - Writing & Methodology: ENGL 204 & 304 (8 cr)
              - Capstone (8 cr): Two 400-level seminars OR St. Mary's Project
            - Electives (20+ credits)
              - At least 12 credits at 300/400 level
              - Up to 4 credits: guided readings/independent study
              - Up to 8 credits: approved courses from other departments
            - Minimum C- with 2.0 GPA
            - **Total Major Credits:** 44+ minimum
            """)

    # Minor Requirements (if selected)
    if minor:
        st.markdown("---")
        st.markdown(f"**{minor} Minor Requirements**")

        if minor == "Biology":
            st.markdown("""
            - **Core Courses (16 credits):**
              - BIOL 105 & 106 - Principles of Biology I & II (8 credits)
              - BIOL 270 - Genetics (4 credits)
              - BIOL 271 - Ecology and Evolution (4 credits)
            - **Core Labs (4 credits):**
              - BIOL 105L, 106L, 270L, 271L (1 credit each)
            - **Electives (4 credits):**
              - Upper-division Biology (300/400 level)
            - Minimum C or better in all courses
            - **Total Minor Credits:** 24 credits
            """)
        elif minor == "Anthropology":
            st.markdown("""
            - **Core Courses (12 credits):**
              - ANTH 101 - Introduction to Anthropology (4 credits)
              - ANTH 201 or 202 - Toolkit/Practicum (4 credits)
              - Two 200-level courses (8 credits)
            - **Electives (6+ credits):**
              - Two 300-400 level courses
            - Minimum C- in all courses
            - **Total Minor Credits:** 22+ credits
            """)
        elif minor == "Data Science":
            st.markdown("""
            - **Foundation (16 credits):**
              - MATH 151 - Calculus I (4 credits)
              - DATA 101 & 102 - Introduction to Data Science 1 & 2 (8 credits)
              - Statistics course (4 credits)
            - **Electives (8+ credits):**
              - Choose from approved data science courses
            - **Total Minor Credits:** 24+ credits
            """)
        elif minor == "Environmental Studies":
            st.markdown("""
            - **Foundation (8 credits):**
              - ENST 100 - Environment and Society (4 credits)
              - ENST 250 or 265 - Science/Earth Systems (4 credits)
            - **Track Electives (16 credits):**
              - 4 credits each from 3 different tracks
              - At least 8 credits ENST-coded
              - At least 8 credits at 300-400 level
            - Minimum C- and 2.0 GPA
            - **Total Minor Credits:** 24+ credits
            """)
        elif minor == "Political Science":
            st.markdown("""
            - **Foundation (4 credits):**
              - POSC 100 - Introduction to Politics
            - **200-level courses (8 credits):**
              - Two courses at 200-level
            - **Upper-level courses (12 credits):**
              - Three courses at 300-400 level
            - Minimum 2.0 GPA in minor courses
            - **Total Minor Credits:** 24 credits
            """)
        elif minor == "Women, Gender, and Sexuality Studies":
            st.markdown("""
            - **Core Course (4 credits):**
              - WGSX 220 - Women, Gender, and Sexuality Studies
            - **Electives (16 credits):**
              - From approved courses across disciplines
              - At least 12 credits at 300+ level
              - Must span at least 3 different disciplines
            - Minimum C- in all courses
            - **Total Minor Credits:** 20 credits
            """)

else:
    # Show message when selections are not complete
    st.info("Please select your LEAD Path, Major, Year, and Track (if applicable) from the dropdowns above to view your personalized course planning guide.")

# ==============================================================================
# DOWNLOAD BUTTON
# ==============================================================================

if selections_complete:
    rtf_content = generate_rtf(
        ["First Year", "Sophomore", "Junior", "Senior"],
        ["First Year", "Sophomore", "Junior", "Senior"].index(year),
        major, lead_path, track, minor, year, major2, track2,
    )
    major2_slug = f"_{major2.replace(' ', '_')}" if major2 else ""
    filename = f"course_plan_{major.replace(' ', '_')}{major2_slug}_{year.replace(' ', '_')}.rtf"
    st.download_button(
        label="Download Course Plan (.rtf)",
        data=rtf_content.encode("latin-1", errors="replace"),
        file_name=filename,
        mime="application/rtf",
        help="Downloads a plain-text RTF file with your checkboxes and strikethroughs. Opens in Word, Pages, or any text editor.",
    )

# ==============================================================================
# FOOTER
# ==============================================================================

st.markdown("""
<div class="footer-box">
    <p><strong>Developed by</strong></p>
    <p><strong>Rafael B. de Andrade</strong></p>
    <p class="title">Assistant Professor of Environmental Studies</p>
    <p class="title">St. Mary's College of Maryland</p>
    <p class="email">rbdeandrade@smcm.edu</p>
</div>
""", unsafe_allow_html=True)
