#!/usr/bin/env python3
"""
Ugandan Educational Structure Script

This script defines default school types, classes, subjects, and departments
based on the Ugandan education system, with each entity having name, code, and description attributes.
"""

# Define the Ugandan educational structure
ugandan_educational_structure = {
    "nursery": {
        "description": "Early childhood education for children aged 3-6 years",
        "classes": [
            {
                "name": "Baby Class",
                "code": "BC",
                "description": "First year of nursery education for 3-4 year olds"
            },
            {
                "name": "Middle Class",
                "code": "MC",
                "description": "Second year of nursery education for 4-5 year olds"
            },
            {
                "name": "Top Class",
                "code": "TC",
                "description": "Final year of nursery education for 5-6 year olds"
            }
        ],
        "departments": [
            {
                "name": "Early Childhood Development",
                "code": "ECD",
                "description": "Focuses on holistic development of young children"
            }
        ],
        "subjects": [
            {
                "name": "English Language",
                "code": "ENG-N",
                "description": "Basic vocabulary and communication skills",
                "department_code": "ECD"
            },
            {
                "name": "Mathematics",
                "code": "MATH-N",
                "description": "Basic number recognition and counting",
                "department_code": "ECD"
            },
            {
                "name": "Social Development",
                "code": "SOC-N",
                "description": "Learning social interaction and cultural awareness",
                "department_code": "ECD"
            },
            {
                "name": "Creative Arts",
                "code": "ART-N",
                "description": "Drawing, coloring, and creative expression",
                "department_code": "ECD"
            },
            {
                "name": "Physical Development",
                "code": "PHY-N",
                "description": "Activities for motor skill development",
                "department_code": "ECD"
            }
        ]
    },
    "primary": {
        "description": "Basic education for students aged 6-13 years (P1-P7)",
        "classes": [
            {
                "name": "Primary One",
                "code": "P1",
                "description": "First year of primary education"
            },
            {
                "name": "Primary Two",
                "code": "P2",
                "description": "Second year of primary education"
            },
            {
                "name": "Primary Three",
                "code": "P3",
                "description": "Third year of primary education"
            },
            {
                "name": "Primary Four",
                "code": "P4",
                "description": "Fourth year of primary education"
            },
            {
                "name": "Primary Five",
                "code": "P5",
                "description": "Fifth year of primary education"
            },
            {
                "name": "Primary Six",
                "code": "P6",
                "description": "Sixth year of primary education"
            },
            {
                "name": "Primary Seven",
                "code": "P7",
                "description": "Final year of primary education, culminating in PLE exams"
            }
        ],
        "departments": [
            {
                "name": "Languages",
                "code": "LANG-P",
                "description": "Department handling language instruction"
            },
            {
                "name": "Mathematics",
                "code": "MATH-P",
                "description": "Department for mathematical education"
            },
            {
                "name": "Social Studies",
                "code": "SS-P",
                "description": "Department focused on social sciences"
            },
            {
                "name": "Science",
                "code": "SCI-P",
                "description": "Department for scientific education"
            },
            {
                "name": "Religious Education",
                "code": "RE-P",
                "description": "Department for religious instruction"
            },
            {
                "name": "Creative Arts",
                "code": "CA-P", 
                "description": "Department for artistic and creative education"
            },
            {
                "name": "Physical Education",
                "code": "PE-P",
                "description": "Department for sports and physical activities"
            }
        ],
        "subjects": [
            {
                "name": "English",
                "code": "ENG-P",
                "description": "Reading, writing, and English language skills",
                "department_code": "LANG-P"
            },
            {
                "name": "Mathematics",
                "code": "MATH-P",
                "description": "Arithmetic, geometry, and basic mathematical concepts",
                "department_code": "MATH-P"
            },
            {
                "name": "Science",
                "code": "SCI-P",
                "description": "Basic scientific concepts and environmental studies",
                "department_code": "SCI-P"
            },
            {
                "name": "Social Studies",
                "code": "SST-P",
                "description": "History, geography, and civic education",
                "department_code": "SS-P"
            },
            {
                "name": "Religious Education (CRE/IRE)",
                "code": "RE-P",
                "description": "Christian or Islamic religious education",
                "department_code": "RE-P"
            },
            {
                "name": "Local Language",
                "code": "LL-P",
                "description": "Instruction in relevant local language (e.g., Luganda, Runyankole)",
                "department_code": "LANG-P"
            },
            {
                "name": "Physical Education",
                "code": "PE-P",
                "description": "Sports, games, and physical fitness",
                "department_code": "PE-P"
            },
            {
                "name": "Music, Dance, and Drama",
                "code": "MDD-P",
                "description": "Cultural expressions through performance arts",
                "department_code": "CA-P"
            },
            {
                "name": "Art and Craft",
                "code": "AC-P",
                "description": "Visual arts and handicrafts",
                "department_code": "CA-P"
            },
            {
                "name": "Agriculture",
                "code": "AGRIC-P",
                "description": "Basic farming and agricultural practices",
                "department_code": "SCI-P"
            }
        ]
    },
    "secondary_o_level": {
        "description": "Lower secondary education (S1-S4) leading to Uganda Certificate of Education (UCE)",
        "classes": [
            {
                "name": "Senior One",
                "code": "S1",
                "description": "First year of secondary education"
            },
            {
                "name": "Senior Two",
                "code": "S2",
                "description": "Second year of secondary education"
            },
            {
                "name": "Senior Three",
                "code": "S3",
                "description": "Third year of secondary education"
            },
            {
                "name": "Senior Four",
                "code": "S4",
                "description": "Final year of O-level, culminating in UCE exams"
            }
        ],
        "departments": [
            {
                "name": "Languages",
                "code": "LANG-S",
                "description": "Department for language instruction"
            },
            {
                "name": "Mathematics",
                "code": "MATH-S",
                "description": "Department for mathematical sciences"
            },
            {
                "name": "Sciences",
                "code": "SCI-S",
                "description": "Department for natural sciences"
            },
            {
                "name": "Humanities",
                "code": "HUM-S",
                "description": "Department for humanities and social sciences"
            },
            {
                "name": "Technical and Vocational",
                "code": "TECH-S",
                "description": "Department for technical and practical subjects"
            }
        ],
        "subjects": [
            {
                "name": "English Language",
                "code": "ENG-S",
                "description": "Advanced English grammar, literature, and composition",
                "department_code": "LANG-S"
            },
            {
                "name": "Mathematics",
                "code": "MATH-S",
                "description": "Algebra, geometry, statistics, and calculus",
                "department_code": "MATH-S"
            },
            {
                "name": "Physics",
                "code": "PHY-S",
                "description": "Study of matter, energy, and their interactions",
                "department_code": "SCI-S"
            },
            {
                "name": "Chemistry",
                "code": "CHEM-S",
                "description": "Study of substances, their properties, and reactions",
                "department_code": "SCI-S"
            },
            {
                "name": "Biology",
                "code": "BIO-S",
                "description": "Study of living organisms and life processes",
                "department_code": "SCI-S"
            },
            {
                "name": "Geography",
                "code": "GEO-S",
                "description": "Study of Earth's landscapes, environments, and human societies",
                "department_code": "HUM-S"
            },
            {
                "name": "History",
                "code": "HIST-S",
                "description": "Study of past events and societies",
                "department_code": "HUM-S"
            },
            {
                "name": "Religious Education",
                "code": "RE-S",
                "description": "Christian or Islamic religious education",
                "department_code": "HUM-S"
            },
            {
                "name": "Agriculture",
                "code": "AGRIC-S",
                "description": "Principles and practices of farming and agriculture",
                "department_code": "SCI-S"
            },
            {
                "name": "Commerce",
                "code": "COMM-S",
                "description": "Basic business principles and practices",
                "department_code": "HUM-S"
            },
            {
                "name": "Computer Studies",
                "code": "COMP-S",
                "description": "Information technology and computer applications",
                "department_code": "TECH-S"
            },
            {
                "name": "Fine Art",
                "code": "ART-S",
                "description": "Drawing, painting, and visual arts",
                "department_code": "HUM-S"
            },
            {
                "name": "Music",
                "code": "MUS-S",
                "description": "Music theory and practice",
                "department_code": "HUM-S"
            },
            {
                "name": "Kiswahili",
                "code": "KIS-S",
                "description": "Study of Swahili language",
                "department_code": "LANG-S"
            },
            {
                "name": "French",
                "code": "FRE-S",
                "description": "Study of French language",
                "department_code": "LANG-S"
            },
            {
                "name": "Local Language",
                "code": "LL-S",
                "description": "Study of relevant local language",
                "department_code": "LANG-S"
            },
            {
                "name": "Entrepreneurship",
                "code": "ENT-S",
                "description": "Business creation and management skills",
                "department_code": "HUM-S"
            },
            {
                "name": "Technical Drawing",
                "code": "TD-S",
                "description": "Mechanical and engineering drawing",
                "department_code": "TECH-S"
            }
        ]
    },
    "secondary_a_level": {
        "description": "Upper secondary education (S5-S6) leading to Uganda Advanced Certificate of Education (UACE)",
        "classes": [
            {
                "name": "Senior Five",
                "code": "S5",
                "description": "First year of A-level education"
            },
            {
                "name": "Senior Six",
                "code": "S6",
                "description": "Final year of A-level, culminating in UACE exams"
            }
        ],
        "departments": [
            {
                "name": "Sciences",
                "code": "SCI-A",
                "description": "Department for science subjects"
            },
            {
                "name": "Arts",
                "code": "ARTS-A",
                "description": "Department for arts and humanities"
            },
            {
                "name": "Mathematics",
                "code": "MATH-A",
                "description": "Department for mathematics"
            },
            {
                "name": "Technical and Vocational",
                "code": "TECH-A",
                "description": "Department for technical and vocational subjects"
            }
        ],
        "subjects": [
            {
                "name": "Mathematics",
                "code": "MATH-A",
                "description": "Advanced mathematical concepts and applications",
                "department_code": "MATH-A"
            },
            {
                "name": "Physics",
                "code": "PHY-A",
                "description": "Advanced physics theories and applications",
                "department_code": "SCI-A"
            },
            {
                "name": "Chemistry",
                "code": "CHEM-A",
                "description": "Advanced chemistry theories and applications",
                "department_code": "SCI-A"
            },
            {
                "name": "Biology",
                "code": "BIO-A",
                "description": "Advanced biological concepts and applications",
                "department_code": "SCI-A"
            },
            {
                "name": "History",
                "code": "HIST-A",
                "description": "Advanced historical studies and research",
                "department_code": "ARTS-A"
            },
            {
                "name": "Geography",
                "code": "GEO-A",
                "description": "Advanced geographical studies and research",
                "department_code": "ARTS-A"
            },
            {
                "name": "Economics",
                "code": "ECON-A",
                "description": "Economic theories and applications",
                "department_code": "ARTS-A"
            },
            {
                "name": "Literature in English",
                "code": "LIT-A",
                "description": "Advanced literary analysis and criticism",
                "department_code": "ARTS-A"
            },
            {
                "name": "Christian Religious Education",
                "code": "CRE-A",
                "description": "Advanced studies in Christianity",
                "department_code": "ARTS-A"
            },
            {
                "name": "Islamic Religious Education",
                "code": "IRE-A",
                "description": "Advanced studies in Islam",
                "department_code": "ARTS-A"
            },
            {
                "name": "Art",
                "code": "ART-A",
                "description": "Advanced art techniques and theory",
                "department_code": "ARTS-A"
            },
            {
                "name": "Entrepreneurship Skills",
                "code": "ENT-A",
                "description": "Advanced business and entrepreneurial skills",
                "department_code": "TECH-A"
            },
            {
                "name": "Computer Science",
                "code": "CS-A",
                "description": "Advanced computer theory and applications",
                "department_code": "TECH-A"
            },
            {
                "name": "Agriculture",
                "code": "AGRIC-A",
                "description": "Advanced agricultural studies",
                "department_code": "SCI-A"
            },
            {
                "name": "Subsidiary Mathematics",
                "code": "SUBMATH-A",
                "description": "Mathematics at a level suitable for arts students",
                "department_code": "MATH-A"
            },
            {
                "name": "Subsidiary ICT",
                "code": "SUBICT-A",
                "description": "Basic ICT skills for non-technical students",
                "department_code": "TECH-A"
            },
            {
                "name": "General Paper",
                "code": "GP-A",
                "description": "Essay writing and general knowledge",
                "department_code": "ARTS-A"
            }
        ]
    },
    "university": {
        "description": "Tertiary education leading to diplomas, bachelor's degrees, master's degrees, and doctorates",
        "classes": [
            {
                "name": "Year One",
                "code": "Y1",
                "description": "First year of university education"
            },
            {
                "name": "Year Two",
                "code": "Y2",
                "description": "Second year of university education"
            },
            {
                "name": "Year Three",
                "code": "Y3",
                "description": "Third year of university education"
            },
            {
                "name": "Year Four",
                "code": "Y4",
                "description": "Fourth year for some degree programs"
            },
            {
                "name": "Year Five",
                "code": "Y5",
                "description": "Fifth year for medicine, engineering, and other professional programs"
            },
            {
                "name": "Masters Year One",
                "code": "M1",
                "description": "First year of master's degree"
            },
            {
                "name": "Masters Year Two",
                "code": "M2",
                "description": "Second year of master's degree"
            },
            {
                "name": "Doctoral Studies",
                "code": "PHD",
                "description": "Doctoral research program"
            }
        ],
        "departments": [
            {
                "name": "College of Agricultural and Environmental Sciences",
                "code": "CAES",
                "description": "Focuses on agriculture, environment, and related sciences"
            },
            {
                "name": "College of Business and Management Sciences",
                "code": "COBAMS",
                "description": "Focuses on business, management, and economics"
            },
            {
                "name": "College of Computing and Information Sciences",
                "code": "COCIS",
                "description": "Focuses on computer science and IT"
            },
            {
                "name": "College of Education and External Studies",
                "code": "CEES",
                "description": "Focuses on education and distance learning"
            },
            {
                "name": "College of Engineering, Design, Art and Technology",
                "code": "CEDAT",
                "description": "Focuses on engineering and technology fields"
            },
            {
                "name": "College of Health Sciences",
                "code": "CHS",
                "description": "Focuses on medicine and health sciences"
            },
            {
                "name": "College of Humanities and Social Sciences",
                "code": "CHUSS",
                "description": "Focuses on arts, humanities, and social sciences"
            },
            {
                "name": "College of Natural Sciences",
                "code": "CONAS",
                "description": "Focuses on basic sciences"
            },
            {
                "name": "College of Veterinary Medicine",
                "code": "COVAB",
                "description": "Focuses on veterinary medicine"
            },
            {
                "name": "School of Law",
                "code": "LAW",
                "description": "Focuses on legal education"
            }
        ],
        "subjects": [
            # CAES Subjects
            {
                "name": "Crop Science",
                "code": "CROP-U",
                "description": "Study of agricultural crop production and management",
                "department_code": "CAES"
            },
            {
                "name": "Animal Science",
                "code": "ANIM-U",
                "description": "Study of animal husbandry and production",
                "department_code": "CAES"
            },
            {
                "name": "Agricultural Engineering",
                "code": "AGENG-U",
                "description": "Engineering applications in agriculture",
                "department_code": "CAES"
            },
            {
                "name": "Environmental Management",
                "code": "ENVMGT-U",
                "description": "Study of environmental conservation and management",
                "department_code": "CAES"
            },
            
            # COBAMS Subjects
            {
                "name": "Accounting",
                "code": "ACC-U",
                "description": "Study of financial record-keeping and reporting",
                "department_code": "COBAMS"
            },
            {
                "name": "Finance",
                "code": "FIN-U",
                "description": "Study of financial management and investment",
                "department_code": "COBAMS"
            },
            {
                "name": "Marketing",
                "code": "MKT-U",
                "description": "Study of market analysis and product promotion",
                "department_code": "COBAMS"
            },
            {
                "name": "Economics",
                "code": "ECON-U",
                "description": "Study of economic theory and applications",
                "department_code": "COBAMS"
            },
            
            # COCIS Subjects
            {
                "name": "Software Engineering",
                "code": "SE-U",
                "description": "Development and maintenance of software systems",
                "department_code": "COCIS"
            },
            {
                "name": "Information Systems",
                "code": "IS-U",
                "description": "Study of information processing and management systems",
                "department_code": "COCIS"
            },
            {
                "name": "Computer Science",
                "code": "CS-U",
                "description": "Study of computational theory and practice",
                "department_code": "COCIS"
            },
            {
                "name": "Information Technology",
                "code": "IT-U",
                "description": "Application of technology for information processing",
                "department_code": "COCIS"
            },
            
            # CEES Subjects
            {
                "name": "Educational Psychology",
                "code": "EDPSY-U",
                "description": "Psychology applied to education",
                "department_code": "CEES"
            },
            {
                "name": "Curriculum Studies",
                "code": "CURR-U",
                "description": "Development and evaluation of educational curricula",
                "department_code": "CEES"
            },
            {
                "name": "Educational Administration",
                "code": "EDADM-U",
                "description": "Management of educational institutions",
                "department_code": "CEES"
            },
            {
                "name": "Adult and Community Education",
                "code": "ACE-U",
                "description": "Education for adults and communities",
                "department_code": "CEES"
            },
            
            # CEDAT Subjects
            {
                "name": "Civil Engineering",
                "code": "CIVENG-U",
                "description": "Design and construction of built environment",
                "department_code": "CEDAT"
            },
            {
                "name": "Mechanical Engineering",
                "code": "MECHENG-U",
                "description": "Design and manufacturing of mechanical systems",
                "department_code": "CEDAT"
            },
            {
                "name": "Electrical Engineering",
                "code": "ELECENG-U",
                "description": "Study of electrical systems and electronics",
                "department_code": "CEDAT"
            },
            {
                "name": "Architecture",
                "code": "ARCH-U",
                "description": "Design of buildings and physical structures",
                "department_code": "CEDAT"
            },
            
            # CHS Subjects
            {
                "name": "Medicine",
                "code": "MED-U",
                "description": "Study of disease diagnosis, treatment, and prevention",
                "department_code": "CHS"
            },
            {
                "name": "Nursing",
                "code": "NURS-U",
                "description": "Study of patient care and health management",
                "department_code": "CHS"
            },
            {
                "name": "Pharmacy",
                "code": "PHARM-U",
                "description": "Study of drug preparation and dispensing",
                "department_code": "CHS"
            },
            {
                "name": "Public Health",
                "code": "PUBH-U",
                "description": "Study of community health and disease prevention",
                "department_code": "CHS"
            },
            
            # CHUSS Subjects
            {
                "name": "Literature",
                "code": "LIT-U",
                "description": "Study of written works and their analysis",
                "department_code": "CHUSS"
            },
            {
                "name": "Philosophy",
                "code": "PHIL-U",
                "description": "Study of fundamental questions about existence and knowledge",
                "department_code": "CHUSS"
            },
            {
                "name": "Sociology",
                "code": "SOC-U",
                "description": "Study of human society and social interactions",
                "department_code": "CHUSS"
            },
            {
                "name": "Psychology",
                "code": "PSY-U",
                "description": "Study of mind and behavior",
                "department_code": "CHUSS"
            },
            
            # CONAS Subjects
            {
                "name": "Mathematics",
                "code": "MATH-U",
                "description": "Study of quantity, structure, space, and change",
                "department_code": "CONAS"
            },
            {
                "name": "Physics",
                "code": "PHY-U",
                "description": "Study of matter, energy, and their interactions",
                "department_code": "CONAS"
            },
            {
                "name": "Chemistry",
                "code": "CHEM-U",
                "description": "Study of composition and properties of substances",
                "department_code": "CONAS"
            },
            {
                "name": "Biology",
                "code": "BIO-U",
                "description": "Study of living organisms and life processes",
                "department_code": "CONAS"
            },
            
            # COVAB Subjects
            {
                "name": "Veterinary Medicine",
                "code": "VETMED-U",
                "description": "Medical care for animals",
                "department_code": "COVAB"
            },
            {
                "name": "Animal Production",
                "code": "ANPROD-U",
                "description": "Study of livestock management and production",
                "department_code": "COVAB"
            },
            {
                "name": "Wildlife Health",
                "code": "WILDH-U",
                "description": "Health management of wildlife",
                "department_code": "COVAB"
            },
            
            # LAW Subjects
            {
                "name": "Constitutional Law",
                "code": "CONLAW-U",
                "description": "Study of fundamental laws of state",
                "department_code": "LAW"
            },
            {
                "name": "Criminal Law",
                "code": "CRIMLAW-U",
                "description": "Study of laws related to criminal offenses",
                "department_code": "LAW"
            },
            {
                "name": "Commercial Law",
                "code": "COMLAW-U",
                "description": "Laws governing business and commerce",
                "department_code": "LAW"
            },
            {
                "name": "International Law",
                "code": "INTLAW-U",
                "description": "Laws governing international relations",
                "department_code": "LAW"
            }
        ]
    },
    "vocational": {
        "description": "Technical and vocational education focusing on practical skills for specific trades",
        "classes": [
            {
                "name": "Certificate Year One",
                "code": "C1",
                "description": "First year of certificate program"
            },
            {
                "name": "Certificate Year Two",
                "code": "C2",
                "description": "Second year of certificate program"
            },
            {
                "name": "Diploma Year One",
                "code": "D1",
                "description": "First year of diploma program"
            },
            {
                "name": "Diploma Year Two",
                "code": "D2",
                "description": "Second year of diploma program"
            },
            {
                "name": "Higher Diploma",
                "code": "HD",
                "description": "Advanced diploma program"
            }
        ],
        "departments": [
            {
                "name": "Construction",
                "code": "CONST-V",
                "description": "Department for building trades and construction"
            },
            {
                "name": "Mechanical",
                "code": "MECH-V",
                "description": "Department for mechanical trades"
            },
            {
                "name": "Electrical",
                "code": "ELEC-V",
                "description": "Department for electrical trades"
            },
            {
                "name": "Agriculture",
                "code": "AGRIC-V",
                "description": "Department for agricultural skills"
            },
            {
                "name": "Hospitality",
                "code": "HOSP-V", 
                "description": "Department for hospitality and tourism"
            },
            {
                "name": "Business",
                "code": "BUS-V",
                "description": "Department for business skills"
            },
            {
                "name": "ICT",
                "code": "ICT-V",
                "description": "Department for information technology skills"
            }
        ],
        "subjects": [
            # Construction
            {
                "name": "Masonry",
                "code": "MASON-V",
                "description": "Building with brick, concrete, and stone",
                "department_code": "CONST-V"
            },
            {
                "name": "Carpentry",
                "code": "CARP-V",
                "description": "Woodworking and furniture making",
                "department_code": "CONST-V"
            },
            {
                "name": "Plumbing",
                "code": "PLUMB-V",
                "description": "Installation and repair of water systems",
                "department_code": "CONST-V"
            },
            
            # Mechanical
            {
                "name": "Motor Vehicle Mechanics",
                "code": "MVM-V",
                "description": "Repair and maintenance of vehicles",
                "department_code": "MECH-V"
            },
            {
                "name": "Welding and Metal Fabrication",
                "code": "WELD-V",
                "description": "Joining and forming metal structures",
                "department_code": "MECH-V"
            },
            {
                "name": "Machining",
                "code": "MACH-V",
                "description": "Operation of machine tools for metal working",
                "department_code": "MECH-V"
            },
            
            # Electrical
            {
                "name": "Electrical Installation",
                "code": "ELECINS-V",
                "description": "Installation of electrical systems",
                "department_code": "ELEC-V"
            },
            {
                "name": "Electronics",
                "code": "ELECTR-V",
                "description": "Repair and maintenance of electronic devices",
                "department_code": "ELEC-V"
            },
            {
                "name": "Telecommunications",
                "code": "TELECOM-V",
                "description": "Installation and maintenance of communication systems",
                "department_code": "ELEC-V"
            },
            
            # Agriculture
            {
                "name": "Crop Production",
                "code": "CROP-V",
                "description": "Growing and managing crops",
                "department_code": "AGRIC-V"
            },
            {
                "name": "Animal Husbandry",
                "code": "ANIM-V",
                "description": "Raising and caring for livestock",
                "department_code": "AGRIC-V"
            },
            {
                "name": "Fisheries",
                "code": "FISH-V",
                "description": "Fish farming and management",
                "department_code": "AGRIC-V"
            },
            
            # Hospitality
            {
                "name": "Catering",
                "code": "CATER-V",
                "description": "Food preparation and service",
                "department_code": "HOSP-V"
            },
            {
                "name": "Hotel Management",
                "code": "HOTEL-V",
                "description": "Management of hospitality facilities",
                "department_code": "HOSP-V"
            },
            {
                "name": "Tourism",
                "code": "TOUR-V",
                "description": "Tourism operation and management",
                "department_code": "HOSP-V"
            },
            
            # Business
            {
                "name": "Secretarial Studies",
                "code": "SEC-V",
                "description": "Office administration and management",
                "department_code": "BUS-V"
            },
            {
                "name": "Accounting",
                "code": "ACC-V",
                "description": "Financial record keeping and reporting",
                "department_code": "BUS-V"
            },
            {
                "name": "Marketing",
                "code": "MKT-V",
                "description": "Sales and marketing techniques",
                "department_code": "BUS-V"
            },
            
            # ICT
            {
                "name": "Computer Repair and Maintenance",
                "code": "COMP-V",
                "description": "Hardware troubleshooting and repair",
                "department_code": "ICT-V"
            },
            {
                "name": "Network Installation",
                "code": "NET-V",
                "description": "Setting up and maintaining computer networks",
                "department_code": "ICT-V"
            },
            {
                "name": "Web Design",
                "code": "WEB-V",
                "description": "Creating and maintaining websites",
                "department_code": "ICT-V"
            }
        ]
    }
}

def get_school_types():
    """Return a list of all school types."""
    return list(ugandan_educational_structure.keys())

def get_classes_for_school_type(school_type):
    """Return a list of classes for a specific school type."""
    if school_type in ugandan_educational_structure:
        return ugandan_educational_structure[school_type]["classes"]
    return []

def get_departments_for_school_type(school_type):
    """Return a list of departments for a specific school type."""
    if school_type in ugandan_educational_structure:
        return ugandan_educational_structure[school_type]["departments"]
    return []

def get_subjects_for_school_type(school_type):
    """Return a list of subjects for a specific school type."""
    if school_type in ugandan_educational_structure:
        return ugandan_educational_structure[school_type]["subjects"]
    return []

def get_subjects_by_department(school_type, department_code):
    """Return subjects belonging to a specific department in a school type."""
    subjects = []
    if school_type in ugandan_educational_structure:
        for subject in ugandan_educational_structure[school_type]["subjects"]:
            if subject["department_code"] == department_code:
                subjects.append(subject)
    return subjects

def print_school_types():
    """Print all available school types."""
    print("Available School Types in Uganda:")
    for i, school_type in enumerate(ugandan_educational_structure.keys(), 1):
        description = ugandan_educational_structure[school_type]["description"]
        print(f"{i}. {school_type.capitalize()} - {description}")
    print()

def print_classes_for_school_type(school_type):
    """Print all classes for a specific school type."""
    if school_type in ugandan_educational_structure:
        print(f"Classes for {school_type.capitalize()}:")
        for i, class_info in enumerate(ugandan_educational_structure[school_type]["classes"], 1):
            print(f"{i}. {class_info['name']} (Code: {class_info['code']}) - {class_info['description']}")
        print()
    else:
        print(f"School type '{school_type}' not found.")
        print()

def print_departments_for_school_type(school_type):
    """Print all departments for a specific school type."""
    if school_type in ugandan_educational_structure:
        print(f"Departments for {school_type.capitalize()}:")
        for i, dept_info in enumerate(ugandan_educational_structure[school_type]["departments"], 1):
            print(f"{i}. {dept_info['name']} (Code: {dept_info['code']}) - {dept_info['description']}")
        print()
    else:
        print(f"School type '{school_type}' not found.")
        print()

def print_subjects_for_school_type(school_type):
    """Print all subjects for a specific school type."""
    if school_type in ugandan_educational_structure:
        print(f"Subjects for {school_type.capitalize()}:")
        for i, subject_info in enumerate(ugandan_educational_structure[school_type]["subjects"], 1):
            print(f"{i}. {subject_info['name']} (Code: {subject_info['code']}) - {subject_info['description']}")
            print(f"   Department: {subject_info['department_code']}")
        print()
    else:
        print(f"School type '{school_type}' not found.")
        print()

def print_subjects_by_department(school_type, department_code):
    """Print subjects belonging to a specific department in a school type."""
    if school_type in ugandan_educational_structure:
        subjects = get_subjects_by_department(school_type, department_code)
        if subjects:
            print(f"Subjects in department '{department_code}' for {school_type.capitalize()}:")
            for i, subject_info in enumerate(subjects, 1):
                print(f"{i}. {subject_info['name']} (Code: {subject_info['code']}) - {subject_info['description']}")
            print()
        else:
            print(f"No subjects found for department '{department_code}' in {school_type}.")
            print()
    else:
        print(f"School type '{school_type}' not found.")
        print()

def main():
    """Main function to demonstrate the Ugandan educational structure."""
    print("\n===== Ugandan Educational Structure Information =====\n")
    
    # Print all school types
    print_school_types()
    
    # Example: Print classes, departments, and subjects for each school type
    for school_type in ugandan_educational_structure:
        print(f"===== {school_type.upper()} =====")
        print(f"Description: {ugandan_educational_structure[school_type]['description']}")
        print()
        print_classes_for_school_type(school_type)
        print_departments_for_school_type(school_type)
        print_subjects_for_school_type(school_type)
        print("\n" + "="*50 + "\n")
    
    # Example: Print subjects by department for Secondary O-level
    print("Example of subjects by department:")
    print_subjects_by_department("secondary_o_level", "SCI-S")

if __name__ == "__main__":
    main()