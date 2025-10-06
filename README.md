# Carwash Management System

A web-based system developed with Python/Flask for managing a car wash business, enabling control of customers, vehicles, services, and scheduling. This project was developed as the final project for the Full Stack Development Postgraduate course at PUCRS University (Pontifícia Universidade Católica do Rio Grande do Sul) and served as a learning experience in web development using Python and Flask.

## Features

- ✨ User management and registration
- 🚗 Vehicle registration and management
- 🛠️ Services management
- 📅 Booking system
- 🔐 User authentication
- 👥 Role-based access control (admin/user)

## Requirements

- Python 3.10 or higher
- pip (Python package manager)
- SQLite

## Installation

1. Clone the repository:
```bash
git clone https://github.com/joaolms/carwash.git
cd carwash
```

2. Create a Python virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Linux/MacOS
source venv/bin/activate

# Windows
.\venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up environment variables:
```bash
# Linux/MacOS
export FLASK_APP=main.py
export FLASK_ENV=development
export SECRET_KEY=<YOUR SECRET KEY>


# Windows
set FLASK_APP=main.py
set FLASK_ENV=development
set SECRET_KEY=<YOUR SECRET KEY>
```

## Database Initialization

1. Run the database creation script:
```bash
python create_database.py
```

## Running the Project

1. Start the Flask server:
```bash
python main.py
```

2. Access the application in your browser:
```
http://localhost:5001
```

## Documentation

For detailed information about the system's architecture, database design, user journey, and interface prototypes, please check our [Architecture Documentation](docs/ARCHITECTURE.md).

## Project Structure

```
carwash/
├── carwash/              # Main package
│   ├── __init__.py      # Application configuration
│   ├── forms.py         # WTForms forms
│   ├── models.py        # Database models
│   ├── routes.py        # Routes and controllers
│   └── templates/       # HTML templates
├── docs/                # Documentation
│   ├── ARCHITECTURE.md  # System architecture documentation
│   └── static/         # Documentation assets and diagrams
├── instance/            # SQLite database
├── requirements.txt     # Project dependencies
├── create_database.py   # DB initialization script
└── main.py             # Application entry point
```

## Technologies Used

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM
- [Flask-Login](https://flask-login.readthedocs.io/) - Authentication management
- [WTForms](https://wtforms.readthedocs.io/) - Forms
- [Bootstrap](https://getbootstrap.com/) - CSS framework
- [Jinja2](https://jinja.palletsprojects.com/) - Template engine

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

João Luiz Messias - [@joaolms](https://github.com/joaolms)

## Support

If you find any bugs or have suggestions for improvements, please open an issue in the GitHub repository.
