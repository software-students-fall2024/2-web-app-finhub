# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement
"Empowering beginners to navigate the world of finance with confidence through simplified news, interactive vocabulary tools, and engaging learning experiences."

## User stories
1. Teenager from Rich Chinese Family
"As a teenager from a wealthy Chinese family, I want a reliable source of easy-to-understand financial information, so I can invest confidently without searching multiple sources."

2. Rational Investor
"As a rational investor, I want a clean platform without distracting news, so I can focus on learning and investing wisely, avoiding unnecessary stress."

3. Hobbyist Investor
"As a hobbyist investor, I want to understand financial jargon easily through interactive vocabulary and quizzes, so I can spend less time deciphering complicated terms."

4. New Parent
"As a new parent, I need simple and relevant investment options and definitions, so I can make smart financial decisions for my child's future without being overwhelmed."

5. Wife of an Investment Manager
"As the wife of an investment manager, I want simplified news with definitions for confusing terms, so I can understand the financial world without getting lost in jargon."

6. Middle Schooler
"As a 6th grader, I want to learn to invest like my dad through easy-to-understand news and vocabulary quizzes, so I can feel more engaged in learning finance."

7. Art Student
"As an art student, I want simple and accessible explanations of finance terms in news articles, so I can learn without being intimidated by complex terminology."

8. Math College Student
"As a Courant student, I need a concise and simple finance app to enhance my knowledge for a potential career as a quant, without being overwhelmed by complex systems."

9. Elderly
"As an elderly person, I need a user-friendly financial app to help me make informed decisions for my grandson, with easy-to-read news and simple definitions."

10. Computer Science Student
"As a computer science student, I want clear and digestible financial news with vocabulary support, so I can start learning investment strategies without constantly needing external explanations."

## Steps necessary to run the software


### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/software-students-fall2024/2-web-app-finhub.git
```

Navigate into the cloned directory:

```bash

cd 2-web-app-finhub
```

### 2. Set Up a Python Virtual Environment

It is recommended to use a virtual environment to avoid conflicts with system-wide packages. You can create one with:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On macOS/Linux:
    
    ```bash
    source venv/bin/activate
    ```
    
- On Windows:
    
    ```bash
    .\venv\Scripts\activate
    ```
    

### 3. Install the Required Dependencies

Once the virtual environment is activated, install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

This project requires some environment variables to be set. Create a `.env` file in the root directory of the project:

```bash
touch .env
```

Add the following content to the `.env` file:

```
SECRET_KEY=your_secret_key
MONGO_URI=mongodb+srv://your_mongodb_connection_string
```

Make sure to replace `your_secret_key` and `your_mongodb_connection_string` with your own values.

### 5. Run the Application

After setting up everything, you can run the application:

```bash
python app.py
```

The app should now be running on `http://127.0.0.1:5000/` by default.

### 6. Register a New User

To use the application, go to the sign-up page and create a new account.

---

## Additional Commands

### Running the App in Debug Mode

To run the Flask app in debug mode for development:

```bash
FLASK_ENV=development flask run
```

### Deactivating the Virtual Environment

Once you're done working on the project, you can deactivate the virtual environment by running:

```bash
deactivate
```

---

### Contributing

Feel free to fork this project and contribute by submitting pull requests. Please make sure to write clear commit messages and create detailed pull requests.

---

### License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.


## Task boards

https://github.com/orgs/software-students-fall2024/projects/45
