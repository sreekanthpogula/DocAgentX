# DocAgentX - Multi-Agentic Doctor Appointment System

DocAgentX is an intelligent multi-agent system designed to manage doctor appointments using advanced AI capabilities. The system leverages LangGraph and LangChain to create specialized agents that handle appointment booking, cancellation, rescheduling, and availability checking.

## Features

- 🤖 **Multi-Agent Architecture**: Specialized agents for information retrieval and booking operations
- 📅 **Appointment Management**: Book, cancel, and reschedule appointments
- 🔍 **Doctor Availability**: Check availability by doctor name or specialization
- 🌐 **FastAPI Backend**: RESTful API for seamless integration
- 🎨 **Streamlit UI**: User-friendly web interface
- 📊 **Data Models**: Robust data validation with Pydantic models

## Prerequisites

- Python 3.8+
- OpenAI API Key (set in `.env` file)

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd DocAgentX
    ```

2. Create and activate virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory:
    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Usage

### Running the FastAPI Server

1. Activate your virtual environment:
    ```bash
    source venv/bin/activate
    ```

2. Start the FastAPI server:
    ```bash
    uvicorn main:app --host 127.0.0.1 --port 8003 --reload
    ```

3. API will be available at `http://127.0.0.1:8003`

### Running the Streamlit UI

1. In a new terminal, activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

2. Run the Streamlit app:
    ```bash
    streamlit run streamlit_ui.py
    ```

3. Access the web interface at `http://localhost:8501`

### Using the Jupyter Notebook

For development and testing, you can use the provided Jupyter notebook:
```bash
jupyter notebook notebook/multiagent_system.ipynb
```

## API Endpoints

### POST `/execute`
Execute agent workflow with user query.

**Request Body:**
```json
{
    "id_number": 12345678,
    "messages": "I want to book an appointment with Dr. Kevin Anderson on 15-08-2024 at 10:00"
}
```

**Response:**
```json
{
    "messages": [
        // Array of conversation messages
    ]
}
```

## Available Doctors and Specializations

### Doctors:
- Kevin Anderson
- Robert Martinez
- Susan Davis
- Daniel Miller
- Sarah Wilson
- Michael Green
- Lisa Brown
- Jane Smith
- Emily Johnson
- John Doe

### Specializations:
- General Dentist
- Cosmetic Dentist
- Prosthodontist
- Pediatric Dentist
- Emergency Dentist
- Oral Surgeon
- Orthodontist

## Project Structure

```
DocAgentX/
├── main.py                     # FastAPI server entry point
├── agent.py                    # Main agent orchestration logic
├── streamlit_ui.py            # Streamlit web interface
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup configuration
├── README.md                  # Project documentation
├── data/
│   └── doctor_availability.csv # Doctor availability database
├── data_models/
│   ├── __init__.py
│   └── models.py              # Pydantic data models
├── prompt_library/
│   ├── __init__.py
│   └── prompt.py              # System prompts for agents
├── toolkit/
│   ├── __init__.py
│   └── toolkits.py           # Agent tools and functions
├── utils/
│   ├── __init__.py
│   └── llms.py               # LLM configuration utilities
└── notebook/
    ├── availability.csv
    └── multiagent_system.ipynb # Development notebook
```

## Agent Architecture

The system consists of three main components:

1. **Supervisor Node**: Routes user queries to appropriate specialized agents
2. **Information Node**: Handles availability queries and general information
3. **Booking Node**: Manages appointment booking, cancellation, and rescheduling

### Available Tools

**Information Tools:**
- `check_availability_by_doctor`: Check specific doctor availability
- `check_availability_by_specialization`: Check availability by medical specialization

**Booking Tools:**
- `set_appointment`: Book new appointments
- `cancel_appointment`: Cancel existing appointments  
- `reschedule_appointment`: Reschedule existing appointments

## Example Queries

- "Can you check if Dr. Kevin Anderson is available on 15-08-2024?"
- "I want to book an appointment with a general dentist on 20-08-2024 at 2 PM"
- "Cancel my appointment on 10-08-2024 at 9:00 AM with Dr. Susan Davis"
- "Reschedule my appointment from 12-08-2024 10:00 to 15-08-2024 14:30"

## Data Format Requirements

- **Dates**: DD-MM-YYYY format (e.g., "15-08-2024")
- **Date-Time**: DD-MM-YYYY HH:MM format (e.g., "15-08-2024 14:30")
- **ID Numbers**: 7-8 digit numbers
- **Doctor Names**: Use full names in lowercase (e.g., "kevin anderson")

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Structure
- All agents are built using LangGraph framework
- Data validation handled by Pydantic models
- Tools are implemented as LangChain tools with proper typing
- State management through TypedDict structures

## Troubleshooting

1. **API Key Issues**: Ensure your `.env` file contains a valid OpenAI API key
2. **Port Conflicts**: Change the port in `main.py` if 8003 is already in use
3. **Data Format Errors**: Ensure dates and times follow the specified formats
4. **Package Installation**: Use `pip install -r requirements.txt` to install all dependencies

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository or contact the development team.