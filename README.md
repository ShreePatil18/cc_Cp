# VIT Project Management System ✨

Welcome to the **VIT Project Management System**! This is a web application built using Flask and MongoDB to manage user data and project details. Users can register, log in, add projects, view their projects, and search projects by domain.

## Features 🔥

- **User Authentication**
  - Registration and login functionality
  - Session management with secure cookies

- **Project Management**
  - Add project details (year, intro, domain, achievements)
  - View and search project details

- **Team and Account Pages**
  - Dedicated pages for team information and user account details

- **Responsive Dashboard**
  - Centralized user-friendly dashboard

## Tech Stack 🚀

- **Backend:** Flask
- **Database:** MongoDB (Local and Cloud)
- **Frontend:** HTML templates (rendered using Flask's `render_template` function)

---

## Installation 🌐

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/vit-project-management.git
   cd vit-project-management
   ```

2. **Set Up Python Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure MongoDB:**
   - **Local MongoDB:**
     Ensure MongoDB is installed and running on `localhost:27017`. The database will be named `vitproject`.
   - **Cloud MongoDB:**
     Update the connection string in the code:
     ```python
     cluster = MongoClient("<your-mongodb-cloud-uri>")
     ```

4. **Run the Application:**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## Application Structure 📄

### Routes

1. `/`: Landing page with login functionality.
2. `/registration`: User registration page.
3. `/dashboard`: User dashboard.
4. `/adddata`: Endpoint to add project data.
5. `/getdata`: View all projects added by the user.
6. `/search`: Search projects by domain.
7. `/logout`: Log out the user.
8. `/addproject`: Page to add a new project.
9. `/team`: Team information page.
10. `/account`: User account details page.

### MongoDB Collections

- **`userdata`:** Stores user information (PRN, email, username, and password).
- **`projectdetail`:** Stores project information (year, intro, domain, achievements, and timestamps).

---


