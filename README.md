# Agentic Planner Bot

## Overview

The **Agentic Planner Bot** is a conversational AI developed with **FastAPI** and **Langchain** to handle various user queries. The bot is designed to provide information on product prices, details, and perform basic arithmetic calculations. The bot can also assist in locating outlets and providing details about them.

## Features

- **Greeting**: Responds to greetings such as "Hello", "Hi", etc.
- **Product Information**: Provides information such as price, color, and material for a specific list of products.
- **Arithmetic Calculations**: Handles basic math operations like addition, subtraction, multiplication, and division.
- **Outlet Information**: Can look up details about outlet locations, including opening hours.

## Setup & Run Instructions

### Prerequisites
- Python 3.7+
- Pip package manager

### Step-by-Step Setup

1. Clone the Repository:
   Open a terminal or command prompt and run the following command:
   ```bash
   git clone https://github.com/hakimkamaruzaman/mindhive_assessment.git
   cd mindhive_assessment

2. Install Dependencies:
In the project directory, install all required packages using pip:
pip install -r requirements.txt

3. Run the Application:
To start the chatbot, use the following command:
python -m app.main

4. Test the APIs:
You can test the bot's functionality through the following endpoints:
Product Info (e.g., price, color, material):
    * URL: http://127.0.0.1:8000/product_info?query=ZUS All-Can Tumbler
Calculate (perform basic math):
    * URL: http://127.0.0.1:8000/calculate?expression=2+2
RAG (Question Answering):
    * POST request: /rag
    * Payload example: { "question": "What is the price of ZUS Thermal Flask?" }

Example Usage
When running the bot:

User: "Hi"
Bot: "Hello! How can I help you today?"

User: "What is the price of ZUS All-Can Tumbler?"
Bot: "The Zus All-Can Tumbler is RM39.90."

User: "2 * 2"
Bot: "The result is 4."

User: "Is there an outlet in Petaling Jaya?"
Bot: "Which outlet are you referring to?"

Architecture Overview
The Agentic Planner Bot is built using the following key components:
    1. FastAPI: A modern and fast web framework used to expose RESTful APIs for the chatbot. It handles product-related queries, math calculations, and outlet information.
    2. Langchain: Used for natural language processing (NLP) to detect user intents based on input. It classifies intents like "greeting", "product_info", "calculate", and "find_outlet".
    3. API Integration:
        * Product Info API: Fetches product details like price, color, and material from a predefined list.
        * Calculation API: Performs simple arithmetic calculations based on user input.
        * RAG (Retrieval-Augmented Generation): Queries external knowledge bases or services to generate contextually relevant answers to user questions.

Key Trade-offs
    * FastAPI was chosen for its speed and ease of integration with Python-based projects.
    * Langchain provides a highly extensible solution for NLP and intent recognition.
    * The use of API-based architecture ensures scalability, allowing for easy extension with more functionalities (e.g., product database, more advanced calculations).

API Specification
/product_info
  Method: GET
  Query Parameters:
      * query (string): The name of the product (e.g., ZUS All-Can Tumbler).
  Response:
    {
      "result": "The Zus All-Can Tumbler is RM39.90"
    }

/calculate
  Method: GET
  Query Parameters:
      * expression (string): The arithmetic expression to calculate (e.g., 2+2).

  Response:
    {
      "result": 4
    }

/rag (Retrieval-Augmented Generation)
  Method: POST
  Payload:
    {
      "question": "What is the price of ZUS Thermal Flask?"
    }
  Response:
    {
      "answer": "The ZUS Thermal Flask is RM59.90."
    }


Conclusion
This project demonstrates a simple yet functional conversational AI that leverages FastAPI, Langchain, and RAG for delivering product information, performing calculations, and more. The system is scalable, easily extendable, and can be enhanced further to meet additional requirements.

Additional Notes:
    * RAG (Retrieval-Augmented Generation): Helps the bot provide more accurate answers by retrieving relevant information from external sources or databases.
    * Basic Calculator: Allows the bot to perform arithmetic calculations.
    * Product Info: Bot provides real-time product details based on predefined data.
