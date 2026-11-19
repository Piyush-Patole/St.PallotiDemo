import os, json
from dept_extractor import get_dept_data

DEPT_CONFIGS = [
    {
        "pid": 1,
        "slug": "computer-science-and-engineering",
        "name": "Computer Science & Engineering",
        "degree": "B.Tech & M.Tech",
        "intake": "180 B.Tech + 18 M.Tech",
        "dte_code": "417424210",
        "nba_status": "NBA Tier-I Accredited",
        "tagline": "Engineering the Intelligent Software Era",
        "overview": "Established in 2004, the Department of Computer Science & Engineering has evolved into a premier center of computing education in central India. Accredited by the National Board of Accreditation (NBA), the department provides state-of-the-art computing facilities, Gigabit fiber connectivity, and a curriculum tuned to global software demands.",
        "placement_rate": "92% Campus Conversion",
        "top_recruiters": ["TCS Digital", "Persistent Systems", "Infosys", "Cognizant", "Capgemini", "Amazon", "Cisco"],
        "labs": [
            {"name": "AI & Deep Learning Computing Lab", "focus": "NVIDIA GPU workstations, PyTorch, TensorFlow, Computer Vision research"},
            {"name": "Cloud Computing & Distributed Systems Lab", "focus": "AWS/Azure Cloud instances, Kubernetes, Docker, Microservices"},
            {"name": "Cyber Defense & Ethical Hacking Arena", "focus": "Kali Linux, Wireshark, Metasploit, Network Defense firewalls"},
            {"name": "Full Stack Software Development Studio", "focus": "React, Node.js, Spring Boot, PostgreSQL, MongoDB, Git workflows"},
            {"name": "Advanced Data Structures & Algorithms Lab", "focus": "High-efficiency competitive programming, C++, Java, Python"},
            {"name": "Database & Big Data Engineering Lab", "focus": "Oracle 19c, Apache Hadoop, Apache Spark, NoSQL architectures"}
        ]
    },
    {
        "pid": 2,
        "slug": "electronics-telecommunication",
        "name": "Electronics & Telecommunication",
        "degree": "B.Tech",
        "intake": "120 B.Tech Seats",
        "dte_code": "417437210",
        "nba_status": "NBA Tier-I Accredited",
        "tagline": "Connecting the World through 5G, VLSI & Embedded Systems",
        "overview": "The Department of Electronics and Telecommunication Engineering offers cutting-edge education in semiconductor design, wireless communication, and embedded intelligence. Boasting NBA accreditation, modern labs, and high-frequency RF equipment, the department prepares engineers for top core telecom and semiconductor companies.",
        "placement_rate": "89% Placement Record",
        "top_recruiters": ["Qualcomm", "Texas Instruments", "L&T Technology Services", "Tata Elxsi", "TCS", "Cognizant", "Ericsson"],
        "labs": [
            {"name": "5G & Advanced Wireless Communication Lab", "focus": "SDR platforms, spectrum analyzers, digital modulation kits, RF transmitters"},
            {"name": "VLSI Design & Embedded Systems Lab", "focus": "Cadence EDA Suite, Xilinx Vivado, FPGA development boards (Spartan/Zynq)"},
            {"name": "Digital Signal & Image Processing Lab", "focus": "MATLAB, DSP Starter Kits (TMS320C6713), Computer Vision cameras"},
            {"name": "IoT & Smart Hardware Prototyping Lab", "focus": "ARM Cortex-M4, ESP32, NodeMCU, ZigBee sensor networks"},
            {"name": "Optical Fiber & Microwave Engineering Lab", "focus": "Optical time-domain reflectometers (OTDR), microwave test benches, waveguides"},
            {"name": "PCB Design & Fabrication Facility", "focus": "Eagle CAD, automated chemical etching machines, surface mount soldering"}
        ]
    },
    {
        "pid": 3,
        "slug": "civil-engineering",
        "name": "Civil Engineering",
        "degree": "B.Tech",
        "intake": "60 B.Tech Seats",
        "dte_code": "417419110",
        "nba_status": "NBA Tier-I Accredited",
        "tagline": "Building Resilient, Sustainable & Smart Infrastructure",
        "overview": "The Department of Civil Engineering trains visionary engineers capable of executing mega-structures, smart cities, and sustainable green buildings. Equipped with sophisticated testing apparatus, computerized UTM, and GIS mapping stations, the department also operates an active material testing and environmental consultancy cell.",
        "placement_rate": "85% Placement & Higher Studies",
        "top_recruiters": ["Larsen & Toubro (L&T)", "Afcons Infrastructure", "Tata Consulting Engineers", "Shapoorji Pallonji", "Godrej Construction", "UltraTech"],
        "labs": [
            {"name": "Advanced Concrete Technology & Testing Lab", "focus": "2000 kN Digital Compression Testing Machine, rebound hammers, ultrasonic pulse"},
            {"name": "Geotechnical & Soil Mechanics Lab", "focus": "Triaxial shear apparatus, direct shear, consolidation cells, permeameters"},
            {"name": "Environmental & Water Quality Engineering Lab", "focus": "Spectrophotometers, BOD incubators, COD digesters, pH/turbidity analyzers"},
            {"name": "Surveying & Advanced Geomatics Lab", "focus": "Total Stations (Leica/Topcon), differential GPS, digital auto-levels, ArcGIS"},
            {"name": "Transportation & Highway Engineering Lab", "focus": "Los Angeles abrasion machine, bitumen penetrometer, Marshall stability apparatus"},
            {"name": "Computer-Aided Structural Design (CAD) Lab", "focus": "AutoCAD Civil 3D, STAAD.Pro, ETABS, Bentley Systems structural modeling"}
        ]
    },
    {
        "pid": 4,
        "slug": "electrical-engineering",
        "name": "Electrical Engineering",
        "degree": "B.Tech",
        "intake": "60 B.Tech Seats",
        "dte_code": "417429310",
        "nba_status": "NBA Tier-I Accredited",
        "tagline": "Powering Clean Energy, EV Powertrains & Smart Grids",
        "overview": "The Department of Electrical Engineering stands at the forefront of the green energy transition, electric vehicle systems, and industrial automation. With NBA accreditation and state-of-the-art power electronics setups, students gain mastery over renewable energy integration, motor drives, and microprocessor control.",
        "placement_rate": "88% Campus Conversion",
        "top_recruiters": ["Schneider Electric", "Siemens", "Tata Power", "L&T Electrical & Automation", "Adani Power", "Bajaj Auto", "TCS"],
        "labs": [
            {"name": "Electric Vehicle & Power Electronics Lab", "focus": "BLDC motor test benches, regenerative braking, IGBT inverter converters"},
            {"name": "Electrical Machines & Drives Testing Arena", "focus": "AC/DC motor generator sets, synchronous machines, slip-ring induction setups"},
            {"name": "Power Systems & Smart Grid Simulation Lab", "focus": "ETAP software, PSCAD, transmission line simulators, numerical relays"},
            {"name": "Control Systems & Industrial Automation Lab", "focus": "Siemens S7-1200 PLCs, SCADA software, closed-loop servo control, MATLAB Simulink"},
            {"name": "Renewable & Solar Energy Research Station", "focus": "Rooftop 100 kW grid-tied solar setup, MPPT charge controllers, PV characterization"},
            {"name": "High Voltage & Switchgear Protection Lab", "focus": "High voltage AC/DC testing transformer, sphere gap assemblies, SF6 circuit breakers"}
        ]
    },
    {
        "pid": 5,
        "slug": "mechanical-engineering",
        "name": "Mechanical Engineering",
        "degree": "B.Tech & M.Tech (CAD/CAM)",
        "intake": "60 B.Tech + 18 M.Tech",
        "dte_code": "417461210",
        "nba_status": "NBA Tier-I Accredited",
        "tagline": "Mastering Advanced Manufacturing, CAD/CAM & Robotics",
        "overview": "Established to cultivate innovative mechanical technocrats, the Department of Mechanical Engineering blends deep theoretical mechanics with modern CNC manufacturing, mechatronics, and thermal sciences. Accredited by NBA Tier-I, the department houses an authorized Dassault Systèmes 3D CAD modeling suite and a dedicated Formula student racing team.",
        "placement_rate": "90% Placement & Core Recruitment",
        "top_recruiters": ["Tata Motors", "Mahindra & Mahindra", "Bosch", "Godrej & Boyce", "Thermax", "L&T", "Kirloskar Brothers"],
        "labs": [
            {"name": "Advanced CAD/CAM & 3D Modeling Center", "focus": "CATIA V5, SolidWorks, ANSYS Mechanical, Mastercam, CreO Parametric"},
            {"name": "CNC Machining & Additive Prototyping Workshop", "focus": "CNC Lathe, CNC Vertical Milling Center, industrial dual-extruder 3D printers"},
            {"name": "Internal Combustion Engines & Automotive Lab", "focus": "Computerized multi-cylinder petrol and CRDI diesel test rigs with gas analyzers"},
            {"name": "Fluid Mechanics & Turbo-Machinery Lab", "focus": "Pelton wheel, Francis turbine, Kaplan turbine, wind tunnel aerodynamics"},
            {"name": "Heat Transfer & Refrigeration Testing Lab", "focus": "Thermal conductivity test rigs, heat exchangers, vapor compression chillers"},
            {"name": "Mechatronics & Industrial Robotics Lab", "focus": "Electro-pneumatic automation kits, pick-and-place articulated robot, hydraulic trainers"}
        ]
    },
    {
        "pid": 6,
        "slug": "information-technology",
        "name": "Information Technology",
        "degree": "B.Tech",
        "intake": "60 B.Tech Seats",
        "dte_code": "417424610",
        "nba_status": "NBA Tier-I Accredited",
        "tagline": "Architecting Enterprise Computing & Secure Cloud Infrastructure",
        "overview": "The Department of Information Technology delivers world-class education in enterprise systems, cloud platforms, full-stack technologies, and network engineering. With Tier-I NBA accreditation, strong industry MOUs, and continuous corporate internships, graduates thrive as lead engineers in global software conglomerates.",
        "placement_rate": "91% Campus Conversion",
        "top_recruiters": ["Persistent", "TCS", "Accenture", "Cognizant", "Capgemini", "Wipro", "Hexaware"],
        "labs": [
            {"name": "Enterprise Web & Cloud Solutions Lab", "focus": "Microservices, Spring Cloud, Node.js, Angular, React, Kubernetes clusters"},
            {"name": "Database Systems & Information Retrieval Lab", "focus": "Oracle, PostgreSQL, MongoDB, Elasticsearch, indexing optimization"},
            {"name": "Network Security & Cryptography Lab", "focus": "Snort IDS/IPS, OpenSSL, VPN configuration, security vulnerability assessment"},
            {"name": "Mobile Application & Cross-Platform Lab", "focus": "Flutter, Android Studio, iOS Swift, React Native, Firebase backend integration"},
            {"name": "Software Engineering & Automated Testing Lab", "focus": "Selenium WebDriver, JUnit, Jenkins CI/CD, SonarQube code quality"},
            {"name": "Open Source Innovation & Project Studio", "focus": "Linux kernel, Git/GitHub, Docker containerization, open-source collaborative code"}
        ]
    },
    {
        "pid": 9,
        "slug": "artificial-intelligence",
        "name": "Artificial Intelligence",
        "degree": "B.Tech",
        "intake": "60 B.Tech Seats",
        "dte_code": "417426310",
        "nba_status": "AICTE Approved (Autonomous)",
        "tagline": "Pioneering Machine Intelligence, Computer Vision & LLMs",
        "overview": "The Department of Artificial Intelligence is SVPCET's specialized high-tech wing dedicated to artificial cognitive systems, deep learning algorithms, natural language understanding, and autonomous perception. Students train on high-capacity GPU clusters to build production-grade AI models for industry automation.",
        "placement_rate": "93% High-Package Placements",
        "top_recruiters": ["NVIDIA Ecosystem", "Persistent AI", "TCS Digital", "Amazon AWS", "Cognizant AI", "Accenture", "Infosys"],
        "labs": [
            {"name": "Deep Learning & High-Performance GPU Cluster", "focus": "NVIDIA RTX 4090/A5000 GPUs, PyTorch, CUDA, Distributed Training"},
            {"name": "Computer Vision & Visual Perception Lab", "focus": "OpenCV, YOLOv8, facial recognition, autonomous vehicle perception sensors"},
            {"name": "Natural Language Processing & Generative AI Lab", "focus": "HuggingFace Transformers, LLM fine-tuning, LangChain, vector databases"},
            {"name": "Reinforcement Learning & Cognitive Systems Lab", "focus": "OpenAI Gym, deep Q-networks, multi-agent reinforcement environments"},
            {"name": "Edge AI & Embedded Intelligence Lab", "focus": "NVIDIA Jetson Nano/Orin, Google Coral TPU, Raspberry Pi 5 AI cameras"},
            {"name": "AI Capstone & Model Deployment Sandbox", "focus": "FastAPI, Docker, ONNX Runtime, TensorRT, Triton Inference Server"}
        ]
    },
    {
        "pid": 10,
        "slug": "data-science",
        "name": "CSE (Data Science)",
        "degree": "B.Tech",
        "intake": "60 B.Tech Seats",
        "dte_code": "417426010",
        "nba_status": "AICTE Approved (Autonomous)",
        "tagline": "Unlocking Predictive Insights with Big Data & Statistical Learning",
        "overview": "The Department of Computer Science & Engineering (Data Science) equips students to navigate petabyte-scale data lakes, statistical inferences, predictive machine learning, and executive visualization. The curriculum blends rigorous mathematical foundations with practical industry analytics platforms.",
        "placement_rate": "92% Campus Conversion",
        "top_recruiters": ["Mu Sigma", "LatentView", "Persistent Analytics", "TCS", "Accenture Data Practice", "Capgemini", "Infosys"],
        "labs": [
            {"name": "Big Data Engineering & Apache Spark Lab", "focus": "Apache Hadoop, PySpark, Databricks Community, Kafka streaming streams"},
            {"name": "Statistical Machine Learning & Modeling Lab", "focus": "R Programming, Scikit-learn, Statsmodels, Bayesian inference setups"},
            {"name": "Business Intelligence & Data Visualization Studio", "focus": "Tableau Desktop, Power BI, D3.js interactive charting, Qlik Sense"},
            {"name": "Cloud Data Warehousing & ETL Pipelines Lab", "focus": "Snowflake, Google BigQuery, PostgreSQL, dbt, Apache Airflow workflows"},
            {"name": "Time Series & Financial Analytics Lab", "focus": "ARIMA, Prophet, financial algorithmic backtesting, econometrics"},
            {"name": "Data Mining & Predictive Analytics Studio", "focus": "KNIME, RapidMiner, association rule mining, automated ML pipelines"}
        ]
    },
    {
        "pid": 12,
        "slug": "cyber-security",
        "name": "CSE (Cyber Security)",
        "degree": "B.Tech",
        "intake": "60 B.Tech Seats",
        "dte_code": "417424410",
        "nba_status": "AICTE Approved (Autonomous)",
        "tagline": "Defending Digital Frontiers with Ethical Hacking & Forensics",
        "overview": "With digital infrastructure facing sophisticated cyber threats globally, the Department of CSE (Cyber Security) provides mission-critical training in penetration testing, threat hunting, secure software engineering, cryptography, and digital forensics. Students learn in an isolated, sandboxed cyber range.",
        "placement_rate": "91% Placement Rate",
        "top_recruiters": ["PwC Cyber", "Deloitte Risk & Advisory", "EY Security Practice", "TCS Cyber Defense", "Quick Heal", "Paladion", "Infosys"],
        "labs": [
            {"name": "Isolated Cyber Defense Range & Simulation Sandbox", "focus": "Virtual cyber attack/defense wargames, SOC simulation, SIEM tools (Splunk)"},
            {"name": "Ethical Hacking & Penetration Testing Lab", "focus": "Burp Suite Pro, Metasploit, Nmap, OWASP Top 10 vulnerabilities"},
            {"name": "Digital Forensics & Malware Reverse Engineering Lab", "focus": "Autopsy, FTK Imager, Ghidra, IDA Pro, volatility memory analysis"},
            {"name": "Applied Cryptography & Blockchain Architecture Lab", "focus": "RSA/ECC cryptography, Solidity smart contracts, Hyperledger Fabric"},
            {"name": "Network Security & Firewall Testing Lab", "focus": "Cisco ASA, pfSense, Snort IDS/IPS, Wireshark packet inspection"},
            {"name": "Secure Software Engineering & DevSecOps Studio", "focus": "SonarQube, Snyk, GitGuardian, CI/CD automated vulnerability scanning"}
        ]
    },
    {
        "pid": 14,
        "slug": "computer-science-and-business-systems",
        "name": "Computer Science & Business Systems (TCS)",
        "degree": "B.Tech (In Collaboration with TCS)",
        "intake": "60 B.Tech Seats",
        "dte_code": "417426210",
        "nba_status": "TCS Industry Curriculum",
        "tagline": "Merging Deep Computer Science with Global Business Leadership",
        "overview": "Curated in direct collaboration with Tata Consultancy Services (TCS), this unique B.Tech program integrates core computer science with enterprise financial acumen, design thinking, business analytics, and executive communication. Graduates emerge with a profound dual advantage for global technology consulting.",
        "placement_rate": "95% TCS & Premier Industry Conversion",
        "top_recruiters": ["Tata Consultancy Services (TCS)", "Cognizant", "Persistent", "Accenture", "LTI Mindtree", "Deloitte", "KPMG"],
        "labs": [
            {"name": "TCS Enterprise Software Systems Lab", "focus": "Enterprise Java, Microservices, Spring Boot, DevOps, Cloud deployment"},
            {"name": "Business Analytics & Financial Computing Lab", "focus": "Financial modeling, algorithmic trading simulations, Python for Finance, PowerBI"},
            {"name": "Design Thinking & Innovation Studio", "focus": "Miro, Figma, human-centric UX design, agile sprint simulations"},
            {"name": "Cloud Enterprise Architecture Studio", "focus": "AWS/Azure Solution Architect configurations, enterprise ERP integrations"},
            {"name": "Data Analytics & Strategic Decision Lab", "focus": "Predictive modeling for business KPIs, supply chain optimization, SQL"},
            {"name": "Executive Communication & Soft Skills Studio", "focus": "Video capture for client presentations, mock boardrooms, corporate negotiation"}
        ]
    },
    {
        "pid": 15,
        "slug": "robotics-and-artificial-intelligence",
        "name": "Robotics & Artificial Intelligence",
        "degree": "B.Tech",
        "intake": "60 B.Tech Seats",
        "dte_code": "417491110",
        "nba_status": "AICTE Approved (Autonomous)",
        "tagline": "Empowering Autonomous Machines, Drones & Smart Robotics",
        "overview": "The Department of Robotics & Artificial Intelligence merges mechanical kinematics, sensor electronics, computer vision, and ROS-based autonomous navigation. Equipped with physical drone arenas, 6-axis robotic arms, and e-Yantra IIT Bombay setups, students engineer real-world robots for manufacturing, defense, and healthcare.",
        "placement_rate": "90% Placement & Robotics R&D",
        "top_recruiters": ["Tata Motors Robotics", "FANUC India", "ABB Robotics", "KUKA", "Tech Mahindra", "DRDO Research Units", "TCS"],
        "labs": [
            {"name": "Autonomous Mobile Robots & ROS Lab", "focus": "Robot Operating System (ROS 2), LiDAR, SLAM algorithms, TurtleBot platforms"},
            {"name": "Texcelrators Drone Aeronautics & Aerial Arena", "focus": "Quadcopter flight controllers, PX4, Mission Planner, aerial video analytics"},
            {"name": "Industrial Manipulators & Kinematics Lab", "focus": "6-Axis articulated industrial robotic arm, SCARA robots, servo kinematics"},
            {"name": "e-Yantra Embedded Robotics Lab (IIT Bombay)", "focus": "Firebird V robot platforms, AVR/ARM microcontrollers, sensor fusion"},
            {"name": "Robotics Simulation & Digital Twin Studio", "focus": "Gazebo simulator, Webots, CoppeliaSim, MATLAB Simscape Multibody"},
            {"name": "Additive Prototyping & Mechatronics Lab", "focus": "Fused Deposition 3D printers, laser cutting, electronic prototyping benches"}
        ]
    },
    {
        "pid": 13,
        "slug": "industrial-IOT",
        "name": "Industrial Internet of Things (IIoT)",
        "degree": "B.Tech",
        "intake": "30 B.Tech Seats",
        "dte_code": "417424910",
        "nba_status": "AICTE Approved (Autonomous)",
        "tagline": "Powering Industry 4.0, Smart Factories & Edge Telemetry",
        "overview": "The Department of Industrial Internet of Things (IIoT) trains engineers to digitize manufacturing ecosystems through cyber-physical sensors, SCADA automation, Edge AI, and industrial cloud platforms. Students master real-time telemetry, predictive maintenance, and smart factory operations.",
        "placement_rate": "88% Campus Conversion",
        "top_recruiters": ["Siemens Industry", "Honeywell", "Schneider Electric", "Rockwell Automation", "TCS IoT Practice", "L&T", "Bosch"],
        "labs": [
            {"name": "Industry 4.0 & Smart Factory Testbed", "focus": "Miniature automated conveyor lines, pick-and-place actuators, optical sensors"},
            {"name": "Industrial SCADA & PLC Automation Lab", "focus": "Siemens S7-1500, Allen Bradley PLCs, Wonderware InTouch SCADA software"},
            {"name": "Edge Computing & Industrial Telemetry Lab", "focus": "Raspberry Pi Industrial CM4, ESP32 Industrial, Modbus, MQTT, OPC-UA protocols"},
            {"name": "Wireless Sensor Networks & LoRaWAN Lab", "focus": "LoRa gateways, Zigbee mesh nodes, long-range telemetry transmitters"},
            {"name": "Smart Instrumentation & Transducers Lab", "focus": "LVDT, strain gauges, RTDs, thermocouples, piezoelectric accelerometers"},
            {"name": "IoT Cloud Platform & Analytics Studio", "focus": "AWS IoT Core, Azure IoT Hub, ThingSpeak, Node-RED dashboarding"}
        ]
    },
    {
        "pid": 8,
        "slug": "first-year",
        "name": "Applied Sciences & Humanities (First Year)",
        "degree": "B.Tech Foundation",
        "intake": "All First-Year Engineering Batches",
        "dte_code": "4174 (Common)",
        "nba_status": "Autonomous Foundation Wing",
        "tagline": "Nurturing Foundational Scientific Rigor & Engineering Excellence",
        "overview": "The Department of Applied Sciences and Humanities forms the academic bedrock for all incoming engineering undergraduates. Comprising Physics, Chemistry, Mathematics, Professional Communication, and Social Sciences, the department builds rigorous foundational thinking, multidisciplinary hands-on skills, and ethical values.",
        "placement_rate": "100% Transition to Upper Division",
        "top_recruiters": ["Academic Excellence Awards", "Hackathon Winners", "TCS CodeVita Finalists", "IIT Techfest Qualifiers"],
        "labs": [
            {"name": "Engineering Physics & Optics Lab", "focus": "He-Ne lasers, spectrometer grating, Newton's rings, Hall effect measurement"},
            {"name": "Engineering Chemistry & Materials Lab", "focus": "Water hardness titrations, spectrophotometers, flash point, Cleveland viscometer"},
            {"name": "Advanced Language & Communication Skills Lab", "focus": "Orell Digital Language Lab software, audio-visual pronunciation, GD booths"},
            {"name": "Basic Electrical & Electronics Engineering Lab", "focus": "RLC circuits, transformers, regulated power supplies, oscilloscopes"},
            {"name": "Engineering Graphics & Computer-Aided Drawing", "focus": "AutoCAD Drafting stations, orthographic/isometric projections, solid modeling"},
            {"name": "Tinkering & Innovation Maker Space", "focus": "Basic mechanical tools, soldering stations, Arduino starter kits, 3D printing"}
        ]
    }
]

all_dept_data = []
for cfg in DEPT_CONFIGS:
    data = get_dept_data(
        pid=cfg['pid'],
        slug=cfg['slug'],
        name=cfg['name'],
        degree=cfg['degree'],
        intake=cfg['intake'],
        dte_code=cfg['dte_code'],
        nba_status=cfg['nba_status']
    )
    # Merge custom details
    data['tagline'] = cfg['tagline']
    data['overview'] = cfg['overview']
    data['placement_rate'] = cfg['placement_rate']
    data['top_recruiters'] = cfg['top_recruiters']
    data['labs'] = cfg['labs']
    all_dept_data.append(data)

with open('assets/data/departments_full.json', 'w', encoding='utf-8') as f:
    json.dump(all_dept_data, f, indent=2)

print(f"Generated comprehensive data model for all {len(all_dept_data)} departments!")
