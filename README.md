#  FlipWhiz: An Interactive E-Book Library 

FlipWhiz is a full-stack web application that reimagines the e-book reading experience. Built with Python and Django, it transforms a standard book library into an immersive, animated virtual flipbook. The platform is designed to be a personalized and engaging space for readers, featuring user accounts, custom bookshelves, and an innovative AI-powered text-to-speech feature.


## Key Features

*   **Interactive Flipbook UI:** Browse the library through a beautifully animated, skeuomorphic book interface powered by `turn.js`.
*   **Complete User Authentication:** Secure user registration, login, and a custom logout flow that includes a feedback form.
*   **Personalized Profile Page:** A "Reading Journal" style profile page for each user to track their literary journey.
*   **Custom Bookshelves:** Users can organize books onto three distinct shelves:
    *   **Favorites:** A collection of all-time favorite books.
    *   **Reading List:** A "read next" list for future adventures.
    *   **Completed:** A satisfying, struck-through list of finished books.
*   **AI-Powered Narration:** Listen to any book with a realistic, AI-generated voice using the ElevenLabs Text-to-Speech API.
*   **Dynamic Category Filtering:** Easily filter the library view by book categories.
*   **Full Admin Control:** A powerful, built-in Django admin panel for easy management of books, categories, users, and feedback.

## Tech Stack

*   **Backend:** Python, Django
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Database:** SQLite3 (for development)
*   **Core Python Libraries:**
    *   `Pillow` for image processing.
    *   `PyPDF2` for extracting text from PDF files.
    *   `elevenlabs` for Text-to-Speech integration.
*   **Core JavaScript Libraries:**
    *   `jQuery` (v1.9.1 for compatibility)
    *   `turn.js` for the flipbook animation.

## Setup and Installation

Follow these steps to get a local copy of FlipWhiz up and running.

### Prerequisites

*   Python 3.10+
*   Git

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Deekshitha-DV/FlipWhiz.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd FlipWhiz
    ```

3.  **Create and activate a virtual environment:**

    *   **Windows (PowerShell):**
        ```powershell
        # Create the environment (you only need to do this once)
        python -m venv venv

        # Activate the environment (do this every time you work on the project)
        .\venv\Scripts\Activate.ps1
        # If you get an error, you may need to set the execution policy for the session:
        # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
        ```

    *   **macOS / Linux:**
        ```bash
        # Create the environment
        python3 -m venv venv

        # Activate the environment
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up the database:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser account** to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```
    (Follow the prompts to create your username and password).

7.  **Add your API Key:**
    *   The Text-to-Speech feature requires an API key from [ElevenLabs](https://elevenlabs.io/).
    *   Sign up for a free account and get your key.
    *   Open the `FlipWhiz/settings.py` file and add your key at the bottom:
        ```python
        ELEVENLABS_API_KEY = "your_secret_api_key_here"
        ```
    *   *Note: For a production application, this key should be stored securely as an environment variable, not in the code.*

8.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

## Usage

*   **Main Library:** Navigate to `http://127.0.0.1:8000/` to be redirected to the main library.
*   **Admin Panel:** Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser account to add book categories and upload new e-books.
*   **Create an Account:** Use the "Sign Up" button to create a regular user account and test the personalization features.

## Future Enhancements

*   Support for `.epub` file parsing for the TTS feature.
*   Allowing users to choose from different AI voices.
*   A user rating and review system for books.
*   Full-text search within the e-book content.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
