# Medical Chatbot Application
This project is a medical chatbot system designed to assist users with healthcare-related tasks, such as receiving medical advice based on symptoms, viewing information about doctors, and booking appointments. The chatbot is powered by an LLM-based (Large Language Model) conversational system, providing recommendations, handling medical inquiries, and streamlining the appointment scheduling process.


## Key Features:

- **Chatbot-Driven Medical Interaction:** </br>
  The system allows users to interact with a chatbot that provides medical advice and suggests appropriate specialists based on the user’s symptoms or medical issues.

* **Appointment Scheduling:** </br>
    The backend integrates with the Google Calendar API to schedule appointments with doctors. Users can view available time slots and book appointments seamlessly. Once an appointment is booked, the data is stored in the database for the doctor’s reference.

* **Doctor and Patient Management:** </br>
    The system manages data related to doctors and patients. The database efficiently stores and retrieves this information.

* **User Data Processing:** </br>
    The chatbot allows users to input symptoms, medical data, and other health-related information to receive personalized responses and recommendations.

* **Frontend for Interactive Experience:** </br>
    The frontend React app provides an intuitive interface where users can interact with the chatbot, view available doctors, fill in medical details, and book appointments.

## Project Architecture

### Frontend (React)

frontend/src/\
│\
├── Images/\
│\
├── SharedComponents/\
│   ├── BouncingLoader.jsx\
│   └── TypingAnimation.jsx\
│\
├── Utils/\
│   └── CapitalizeFirstLetter.js\
│\
├── Views/\
│   ├── DoctorsList/\
│   ├── FirstVisitCheck/\
│   └── MedicalDetailsForm/\
│\
└── App.js

* `Images/` </br>
Contains all image assets used in the application. 

* `SharedComponents/` </br>
    Houses reusable components shared across various views in the application, such as loaders and animations.

* `Utils/`</br>
    Contains utility functions for processing or transforming data used across the app.

* `DoctorsList/` </br>
    Contains components related to displaying a list of doctors.

* `FirstVisitCheck/` </br>
    Contains components for checking if it’s the user's first visit.
    
* `MedicalDetailsForm/` </br>
    Contains components for a form where users can input their medical details, potentially to get personalized recommendations.


### Backend (Flask)
backend/\
│\
├── calendarAPI/\
│   ├── calendar.py     
│   ├── credentials.json\
│\
├── instance/\
│   ├── medicalDB.sqlite3\
│\
├── llm/\
│   ├── documents/\
│   │── constants.py\
│   ├── medBot.py    
│   ├── vectorstore.py     
│\
├── database.py\
├── insertDataToDB.py\
├── main.py  
├── models.py           
├── utils.py              
│\
├── requirements.txt          

* `calendar.py` </br>
    Handles integration with the Google Calendar API to manage appointments. It provides methods for authentication, retrieving existing events, and inserting new appointments into the calendar.

* `constants.py` </br>
   Initializes the embedding model and the LLM model.

* `vectorStore.py` </br>
    Handles the extraction of data from documents and stores it in a vector database (Faiss).

* `medgpt.py` </br>
    Responsible for generating medical advice and treatment plans using an LLM model with Retrieval-Augmented Generation (RAG) to fetch necessary context.

* `database.py` </br>
    Initializes and manages the SQLAlchemy object for database interactions.

* `insertDataToDB.py` </br>
    Populates the database with initial data for doctors and patients when setting up the system.

* `main.py` </br>
    Defines the Flask server, sets up CORS, and provides API endpoints for interacting with patients and doctors.

* `models.py` </br>
    Defines the database models for Doctors and Patients.

* `utils.py` </br>
    Provides utility functions for tasks related to appointment booking, finding specialists, and interacting with the calendar.


## Prerequisites:
* Python.
* Node.js and npm.
* Google Calendar API credentials
* SQLite

## Steps to Run the Application:
Step 1: Clone the repository

```
git clone https://github.com/your-repo-name/medical-chatbot.git
cd medical-chatbot
```
Step 2: Backend 
```
# download libraries
pip install -r requirements.txt

# run vectorstore to generate and store embeddings
python vectorstore.py

# run the backend
flask run
```
Step 3: Frontend 
```
# download node modules
npm install

# start the app
npm start
```

## User Workflow:

1. **User Initiates Chat:**
The user can input their medical concerns into the chatbot. The chatbot, powered by LLM, responds with disorder name based on the provided symptoms, suggesting possible specializations.

2. **Get Treatment Recommendations:**
The user can input their medical data and get treatment recommendations from the chatbot.

3. **Doctor Selection:**
The user can view a list of available doctors based on the specialization suggested by the chatbot.

4. **Book Appointment:**
    - After identifying the appropriate specialist, The user can book an appointment directly through the chat interface. 
    - The system retrieves available slots by interacting with Google Calendar and allows the user to confirm a time.
    - After successful booking, the system stores the user's data securely in the database. The chatbot uses this information to offer personalized recommendations for future interactions.

https://github.com/user-attachments/assets/44e52262-dff0-46aa-8a01-be74478c5478

## Conclusion:
This Medical Chatbot Application offers a user-friendly solution to help patients navigate healthcare services. With the integration of AI-based medical suggestions, appointment scheduling via Google Calendar, and seamless doctor-patient interaction management, it simplifies the process of accessing healthcare. The chatbot’s ability to personalize responses based on user data ensures that users receive relevant and actionable advice, enhancing the overall user experience.

