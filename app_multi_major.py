import streamlit as st

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
        "description": "Take one course in each of 6 breadth areas (24 credits total)",
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (must earn C- or higher)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "Exploration Course: Arts (4 credits) - Choose from ART 204, TDPS 230, MUSA 180-189",
                "Exploration Course: Cultural Literacy (4 credits) - Choose from AADS 214, ASIA 200, HIST 253, ILCS 201",
                "Exploration Course: Humanities (4 credits) - Choose from ENGL 106, HIST 104, PHIL 101, ARTH 225"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship",
                "Exploration Course: Mathematics (4 credits) - Choose from MATH 131, COSC 120, ECON 253, PHIL 215",
                "Exploration Course: Natural Sciences with Lab (4 credits) - Choose from BIOL 101, CHEM 101, PHYS 141, ASTR 154",
                "Exploration Course: Social/Behavioral Sciences (4 credits) - Choose from ANTH 101, ECON 102, PSYC 101, SOCI 101"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Climate Inquiry": {
        "description": "Understanding climate change through scientific, social, cultural, and political perspectives (17-21 credits)",
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (must earn C- or higher)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "ENST 100 - Environment and Society (Anchor Course, 4 credits)",
                "Natural Sciences: Choose from Biology, Chemistry, Environmental Science, or Marine Science (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship",
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
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (must earn C- or higher)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "Humanities/Cultural Literacy: Ethics, Environmental Ethics, or Bioethics (4 credits)",
                "Mathematics: Computer Science or Survey Mathematics (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship",
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
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (must earn C- or higher)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "IDIS 122 - Gateway Course (4 credits)",
                "Natural Sciences: Biology or Chemistry (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship",
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
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (must earn C- or higher)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "MATH 132 - Calling BS (Mathematics/Cultural Literacy, 4 credits)",
                "Social/Behavioral Sciences: Women, Gender, and Sexuality Studies (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship",
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
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (must earn C- or higher)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "POSC 100 - Gateway Course (4 credits)",
                "Mathematics: Economics, Statistics, or Calculus (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship",
                "Global/Non-Western Perspectives: African Diaspora, Asian Studies, History, or Philosophy (4 credits)",
                "Cultural Expression: Literature, World Music, or Film/Media (4 credits)",
                "Natural Sciences with Lab: Astronomy, Environmental Science, or Oceanography (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Asia in the World Inquiry": {
        "description": "Contextualizing Asia's role within global frameworks (17-21 credits)",
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (must earn C- or higher)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "ASIA 200 - Gateway Course (4 credits)",
                "Next Level Contexts: Economics, History, Philosophy, or Political Science (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship",
                "Creative/Interpretive: Visual Arts, Writing, Film/Media, or Performance (4 credits)",
                "Computational: Computer Science, Statistics, or Economics (4 credits)",
                "Natural Science with Lab: Environmental Science, Oceanography, or Marine Science (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Latinx Americas Inquiry": {
        "description": "Hemispheric perspective on history, politics, and cultures of the Americas with emphasis on Latinx contributions (17-21 credits)",
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (must earn C- or higher)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "Cultural Studies: Latinx Experience and Latin American Cultural Studies (4 credits each)",
                "Societies/Institutions: Anthropology, History, or Political Science (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship",
                "Creative/Embodied Processes: Visual Arts or Music (4 credits)",
                "Mathematical Perspective: Computer Science, Economics, or Political Science Methods (4 credits)",
                "Natural Science with Lab: Environmental Science or Earth Systems (4 credits)",
                "ILPF 200 - Integrated Learning Portfolio (1 credit)"
            ],
            "Junior": [],
            "Senior": []
        }
    },
    "Idea of the West Inquiry": {
        "description": "Interrogating how 'the West' became geographically and culturally centered on Western Europe and the USA (17-21 credits)",
        "courses": {
            "First Year": [
                "LEAD 101 - LEAD Seminar (must earn C- or higher)",
                "LEAD 111 - Career Networking and Navigation",
                "LEAD 112 - Career Networking and Navigation II",
                "Language Course (102/110 level or higher)",
                "ANTH 101 - Introduction to Anthropology (4 credits)",
                "Humanities: Literature in History or World History (4 credits)"
            ],
            "Sophomore": [
                "LEAD 211 - Honors College Externship",
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
                    "LEAD 101 - LEAD Seminar (must earn C- or higher)",
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
                    "College-level Biology with Lab (3 credits)"
                ],
                "Sophomore": [
                    "ENST 250 - Environmental Science (4 credits)",
                    "College-level Chemistry with Lab (3 credits)",
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
                    "Environmental Science Track Depth Electives: 8+ credits at 300-400 level"
                ],
                "Senior": [
                    "Environmental Science Track Depth Electives: 4+ credits to complete 16 credit depth requirement",
                    "Application Requirement: ENST 390 (Sustainability Practicum), ENST 391 (Field Study), 4 credits Independent Study/Research/Internship, or Study Abroad (4 credits)"
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
                    "Environmental Policy and Social Science Track Depth Electives: 8+ credits at 300-400 level"
                ],
                "Senior": [
                    "Environmental Policy and Social Science Track Depth Electives: 4+ credits to complete 16 credit depth requirement",
                    "Application Requirement: ENST 390 (Sustainability Practicum), ENST 391 (Field Study), 4 credits Independent Study/Research/Internship, or Study Abroad (4 credits)"
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
                    "Environmental Arts and Humanities Track Depth Electives: 8+ credits at 300-400 level"
                ],
                "Senior": [
                    "Environmental Arts and Humanities Track Depth Electives: 4+ credits to complete 16 credit depth requirement",
                    "Application Requirement: ENST 390 (Sustainability Practicum), ENST 391 (Field Study), 4 credits Independent Study/Research/Internship, or Study Abroad (4 credits)"
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
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (must earn C- or higher)",
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
                    "CHEM 312 - Organic Chemistry II (4 credits) - Recommended",
                    "PHYS 121 - College Physics I (4 credits) - Recommended",
                    "PHYS 122 - College Physics II (4 credits) - Recommended",
                    "MATH 151 - Calculus I (4 credits) - Recommended",
                    "MATH 152 - Calculus II (4 credits) - Recommended"
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
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (must earn C- or higher)",
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
                    "CHEM 106 - General Chemistry II (4 credits)",
                    "Physics Sequence (8 credits): PHYS 121-122 OR PHYS 141-142 OR PHYS 151-152"
                ],
                "Sophomore": [],
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
                "First Year": [],
                "Sophomore": [
                    "MATH 221 - Introduction to Statistics OR BIOL 311 - Biostatistics (4 credits)",
                    "Note: Calculus I & II recommended for all students"
                ],
                "Junior": [],
                "Senior": []
            },
            "Marine Science Core": {
                "First Year": [
                    "MRNE 110 - Introduction to Marine Science (4 credits)"
                ],
                "Sophomore": [
                    "MRNE 220 - Physical Oceanography (4 credits)",
                    "BIOL 383 - Biological Oceanography (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Marine Science Electives": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "Marine Science Electives: 16 credits (minimum 12 credits at 300+ level)"
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
                    "MRNE 490 - Marine Science Capstone (4 credits)"
                ]
            }
        }
    },

    "Psychology": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (must earn C- or higher)",
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
                    "PSYC 101 - Introduction to Psychology (4 credits)",
                    "Breadth Courses: Start taking 200-level courses from 5 areas"
                ],
                "Sophomore": [
                    "PSYC 204 - Psychological Research, Analysis, and Writing I (4 credits)",
                    "PSYC 206 - Psychological Research, Analysis, and Writing II (4 credits)",
                    "Breadth Courses: Continue 200-level courses"
                ],
                "Junior": [
                    "PSYC 310 - Scientific Writing and Professional Development (4 credits)"
                ],
                "Senior": []
            },
            "Breadth Requirements": {
                "First Year": [],
                "Sophomore": [
                    "Choose courses from 5 areas: Biological & Sensory Processes, Culture & Community, Development & Learning, Health & Counseling, Social & Cognitive Processes",
                    "Minimum two 200-level courses across all areas"
                ],
                "Junior": [
                    "Minimum two 300-level laboratory courses (5 credits) or lab seminar courses (4 credits)"
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
                    "LEAD 101 - LEAD Seminar (must earn C- or higher)",
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
                    "POSC 100 - Introduction to Politics (4 credits)"
                ],
                "Sophomore": [
                    "POSC 200 - Scope and Methods of Political Science (4 credits)",
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
                "Sophomore": [],
                "Junior": [
                    "12 credits from upper-level courses in chosen concentration (or across subfields for General Track)"
                ],
                "Senior": []
            },
            "Capstone": {
                "First Year": [],
                "Sophomore": [],
                "Junior": [
                    "One 300-level POSC course (4 credits) - if choosing Option One"
                ],
                "Senior": [
                    "Option One: Two 400-level seminars (8 credits) - completing this year",
                    "Option Two: One 400-level seminar (4 credits) + POSC 493/494 - St. Mary's Project (8 credits)"
                ]
            }
        }
    },

    "English": {
        "has_tracks": False,
        "course_data": {
            "LEAD": {
                "First Year": [
                    "LEAD 101 - LEAD Seminar (must earn C- or higher)",
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
                "First Year": [],
                "Sophomore": [
                    "ENGL 284 - Literature in History I: Before 1800 (4 credits)",
                    "ENGL 285 - Literature in History II: After 1800 (4 credits)"
                ],
                "Junior": [],
                "Senior": []
            },
            "Core Requirements - Writing & Methodology": {
                "First Year": [],
                "Sophomore": [
                    "ENGL 204 - Reading and Writing in the Major (4 credits)"
                ],
                "Junior": [
                    "ENGL 304 - Methods of Literary Study (4 credits)"
                ],
                "Senior": []
            },
            "Electives": {
                "First Year": [],
                "Sophomore": [
                    "Begin taking English electives (at least 20 credits total needed, with 12+ at 300/400 level)"
                ],
                "Junior": [
                    "Continue English electives at 300/400 level (at least 12 credits at upper level)"
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
                    "Two Anthropology electives at 300 or 400 level (6+ credits)"
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
                    "Statistics: Choose from BIOL 311, DATA 301, ECON 253, MATH 221, PSYC 206, or SOCI 201 (4 credits)"
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
                    "WGSX electives from approved courses across disciplines (8 credits)"
                ],
                "Junior": [
                    "Upper-level (300+) WGSX electives from at least 3 different disciplines (8 credits, completing 12 total upper-level credits)"
                ],
                "Senior": []
            }
        }
    }
}

# ==============================================================================
# DROPDOWN MENUS FOR MAJOR, YEAR, TRACK, LEAD PATH, AND MINOR
# ==============================================================================

# LEAD Path selection (first, since it applies to all students)
st.markdown('<p style="color: #364B9A; font-weight: 700; margin-bottom: 0.25rem;">Select Your LEAD Path:</p>', unsafe_allow_html=True)
lead_path = st.selectbox(
    "Select Your LEAD Path:",
    [""] + list(lead_paths.keys()),
    format_func=lambda x: "-- Select LEAD Path --" if x == "" else x,
    label_visibility="collapsed"
)

if lead_path:
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

# Optional Minor selection
col1_minor, col2_minor = st.columns(2)

with col1_minor:
    st.markdown('<p style="color: var(--smcm-navy); font-weight: 700; margin-bottom: 0.25rem;">Select Your Minor (Optional):</p>', unsafe_allow_html=True)
    minor = st.selectbox(
        "Select Your Minor (Optional):",
        [""] + list(minor_data.keys()),
        format_func=lambda x: "-- No Minor / Select Minor --" if x == "" else x,
        label_visibility="collapsed"
    )

with col2_minor:
    if minor:
        st.caption(f"*Adding {minor} Minor to your plan*")
    else:
        st.caption("*Optional: You can add a minor to your degree*")

st.markdown("---")

# Check if all required selections are made
selections_complete = bool(lead_path and major and year)

# For majors with tracks, also check if track is selected
if selections_complete and major and major_data.get(major, {}).get("has_tracks"):
    selections_complete = bool(track)

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

def get_courses_for_year(year_name, selected_major, selected_lead_path, selected_track=None, selected_minor=None):
    """Get all courses for a specific year, with deduplication for courses that satisfy LEAD, major, and/or minor"""
    lead_courses = []
    major_courses = []
    minor_courses = []

    # First, get LEAD path courses for this year
    if year_name in lead_paths[selected_lead_path]["courses"]:
        lead_courses = lead_paths[selected_lead_path]["courses"][year_name][:]

    # Then get major-specific courses
    course_data = major_data[selected_major]["course_data"]

    # For majors with tracks (like Environmental Studies)
    if major_data[selected_major]["has_tracks"] and selected_track:
        # Add courses from all categories
        for category, years in course_data.items():
            if year_name in years:
                # For track-specific categories, only add if it matches the selected track
                if category in major_data[selected_major]["tracks"]:
                    if category == selected_track:
                        major_courses.extend(years[year_name])
                else:
                    # Add courses from non-track categories (Foundation, etc.)
                    # Skip LEAD since it's now handled by lead_paths
                    if category != "LEAD":
                        major_courses.extend(years[year_name])
    else:
        # For majors without tracks
        for category, years in course_data.items():
            if year_name in years:
                # Skip LEAD since it's now handled by lead_paths
                if category != "LEAD":
                    major_courses.extend(years[year_name])

    # Get minor courses if a minor is selected
    if selected_minor:
        minor_course_data = minor_data[selected_minor]["course_data"]
        for category, years in minor_course_data.items():
            if year_name in years:
                minor_courses.extend(years[year_name])

    # Deduplicate courses that appear in LEAD, major, and/or minor
    # Create mappings of course codes to full course strings
    lead_course_map = {}
    for course in lead_courses:
        code = extract_course_code(course)
        if code:
            lead_course_map[code] = course

    major_course_map = {}
    for course in major_courses:
        code = extract_course_code(course)
        if code:
            major_course_map[code] = course

    minor_course_map = {}
    for course in minor_courses:
        code = extract_course_code(course)
        if code:
            minor_course_map[code] = course

    # Find all overlapping course codes
    lead_codes = set(lead_course_map.keys())
    major_codes = set(major_course_map.keys())
    minor_codes = set(minor_course_map.keys())

    # Identify different types of overlaps
    all_three = lead_codes & major_codes & minor_codes
    lead_major = (lead_codes & major_codes) - all_three
    lead_minor = (lead_codes & minor_codes) - all_three
    major_minor = (major_codes & minor_codes) - all_three

    # Build final course list with deduplication markers
    # Note: We don't include minor_only courses in the yearly plan
    # They'll be shown separately in a "Minor Courses Left" section
    courses = []

    # Add all LEAD courses, marking overlaps
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

    # Add major courses that don't overlap with LEAD
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

def display_course_with_checkbox(course_data, key_prefix, selected_major, selected_track=None):
    """Display a course with a checkbox for completion tracking"""
    # Handle tuple format (requirement_type, course_string)
    if isinstance(course_data, tuple):
        requirement_type, course = course_data
    else:
        # Backwards compatibility - treat as major_only
        requirement_type = "major_only"
        course = course_data

    # Check if this is a depth electives item that should show an expander
    if "Track Depth Electives" in course and major_data[selected_major]["has_tracks"]:
        st.markdown(f"**{course}**")
        # Determine which track's electives to show
        track_name = selected_track
        with st.expander(f"📚 View all {track_name} track courses"):
            st.markdown(f"**Choose {course.split(':')[1].strip().split('(')[0]} from the following courses:**")
            for elective in major_data[selected_major]["track_electives"].get(track_name, []):
                col1, col2 = st.columns([0.05, 0.95])
                with col1:
                    elective_key = f"{key_prefix}_elective_{elective}"
                    current_state = st.session_state.completed_courses.get(elective_key, False)
                    is_completed = st.checkbox("✓", value=current_state, key=elective_key, label_visibility="collapsed")
                    st.session_state.completed_courses[elective_key] = is_completed
                with col2:
                    if is_completed:
                        st.markdown(f"~~{elective}~~")
                    else:
                        st.markdown(elective)
    else:
        # Regular course display
        col1, col2 = st.columns([0.05, 0.95])
        with col1:
            # Create unique key for each checkbox
            checkbox_key = f"{key_prefix}_{course}"
            # Get current state or default to False
            current_state = st.session_state.completed_courses.get(checkbox_key, False)
            # Display checkbox
            is_completed = st.checkbox("✓", value=current_state, key=checkbox_key, label_visibility="collapsed")
            # Update session state
            st.session_state.completed_courses[checkbox_key] = is_completed
        with col2:
            # Determine color class based on requirement type
            if requirement_type in ["all_three", "lead_major", "lead_minor", "major_minor"]:
                color_class = "course-multiple"
            elif requirement_type == "lead_only":
                color_class = "course-lead-only"
            elif requirement_type == "major_only":
                color_class = "course-major-only"
            else:
                color_class = ""

            # Add badge based on which requirements the course satisfies
            if requirement_type == "all_three":
                badge = " 🎯 *Satisfies LEAD, Major & Minor*"
            elif requirement_type == "lead_major":
                badge = " 🎓 *Satisfies LEAD & Major*"
            elif requirement_type == "lead_minor":
                badge = " 🎓 *Satisfies LEAD & Minor*"
            elif requirement_type == "major_minor":
                badge = " 🎓 *Satisfies Major & Minor*"
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
        st.subheader("📚 Courses You Should Have Taken")
        past_courses = []
        for i in range(current_year_index):
            past_courses.extend(get_courses_for_year(year_order[i], major, lead_path, track, minor))

        if past_courses:
            for course in past_courses:
                display_course_with_checkbox(course, "past", major, track)
        else:
            st.markdown("*No prior courses required yet*")

        st.markdown("---")

# Courses you should be taking this year
    st.subheader(f"📖 Courses You Should Be Taking This Year ({year})")
    current_courses = get_courses_for_year(year, major, lead_path, track, minor)
    
    if current_courses:
        for course in current_courses:
            display_course_with_checkbox(course, "current", major, track)
    else:
        st.markdown("*No specific required courses this year - focus on electives and breadth requirements*")
    
    st.markdown("---")
    
    # Courses you should take next year
    if current_year_index < len(year_order) - 1:
        next_year = year_order[current_year_index + 1]
        st.subheader(f"🎯 Courses You Should Take Next Year ({next_year})")
        next_courses = get_courses_for_year(next_year, major, lead_path, track, minor)
    
        if next_courses:
            for course in next_courses:
                display_course_with_checkbox(course, "next", major, track)
        else:
            st.markdown("*No specific required courses next year - focus on completing remaining requirements*")
    else:
        st.subheader("🎓 Next Steps")
        st.markdown("*You're in your final year! Focus on completing your capstone and any remaining requirements.*")
    
    # Future courses section (only for First Year and Sophomore students)
    if current_year_index <= 1:  # First Year (0) or Sophomore (1)
        st.markdown("---")
        st.subheader("🔮 Future Course Requirements")
        st.caption("Courses you'll take in your Junior and Senior years")
    
        future_courses = []
        for i in range(current_year_index + 2, len(year_order)):
            year_name = year_order[i]
            courses = get_courses_for_year(year_name, major, lead_path, track, minor)
            if courses:
                st.markdown(f"**{year_name}:**")
                for course in courses:
                    display_course_with_checkbox(course, f"future_{year_name}", major, track)
                if i < len(year_order) - 1:  # Add spacing between years
                    st.markdown("")

    # Minor Courses Left section (if minor is selected) - shows for all years
    if minor:
        st.markdown("---")
        st.subheader(f"📘 {minor} Minor - Courses to Complete")
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
                            badge = " ✅ *Covered by LEAD & Major*"
                        elif status == "covered_by_major":
                            badge = " ✅ *Covered by Major*"
                        else:  # covered_by_lead
                            badge = " ✅ *Covered by LEAD*"

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
                st.success("🎉 All minor courses are covered by your Major/LEAD requirements!")
        else:
            st.markdown("*No minor course data available*")

    # ==============================================================================
    # PROGRAM REQUIREMENTS SUMMARY
    # ==============================================================================
    
    st.markdown("---")
    st.subheader("📋 Program Requirements Summary")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown(f"**LEAD Curriculum Requirements**")
        st.markdown(f"*Selected Path: {lead_path}*")
        st.markdown("")
    
        if lead_path == "LEAD Exploration":
            st.markdown("""
            - LEAD 101 Seminar (C- or higher)
            - LEAD 111 & 112 (Career Networking)
            - LEAD 211 (Honors College Externship)
            - Language Course (102/110+)
            - **Exploration:** 6 breadth areas (24 credits)
              - Arts (4 cr)
              - Cultural Literacy (4 cr)
              - Humanities (4 cr)
              - Mathematics (4 cr)
              - Natural Sciences with Lab (4 cr)
              - Social/Behavioral Sciences (4 cr)
            - Capstone (4-8 credits)
            - Minimum C- in LEAD courses, 2.0 GPA
            """)
        else:
            st.markdown(f"""
            - LEAD 101 Seminar (C- or higher)
            - LEAD 111 & 112 (Career Networking)
            - LEAD 211 (Honors College Externship)
            - Language Course (102/110+)
            - **{lead_path}:** Integrated pathway (17-21 credits)
              - 4-5 thematically-linked courses
              - ILPF 200 Portfolio (1 cr)
              - Fulfills all breadth requirements
            - Capstone (4-8 credits)
            - Minimum C- in LEAD courses, 2.0 GPA
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
    st.info("👆 Please select your LEAD Path, Major, Year, and Track (if applicable) from the dropdowns above to view your personalized course planning guide.")

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
