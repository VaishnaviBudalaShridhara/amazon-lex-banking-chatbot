# Serverless Banking Chatbot using Amazon Lex & AWS Lambda

## Overview
This project implements a **serverless conversational banking chatbot** using **Amazon Lex** and **AWS Lambda**.  
The chatbot can understand natural language queries, classify intents and trigger backend fulfilment logic.

## Architecture
- Amazon Lex for natural language understanding and intent classification
- AWS Lambda for fulfilment logic
- Stateless, serverless design
- Error handling and fallback responses for unknown intents

## Features
- Intent classification (Check Balance, Transfer Money, Help)
- Slot filling for required inputs
- Lambda-based fulfilment
- Graceful error handling and fallback responses
- Easily extensible intent model

## Technologies Used
- Amazon Lex
- AWS Lambda (Python)
- JSON-based intent and slot configuration

## How It Works
1. User sends a natural language query
2. Amazon Lex identifies intent and slots
3. Lambda fulfilment function processes the request
4. A structured response is returned to Lex
5. Lex responds to the user

## Testing
Sample Lex event payloads are provided in the `events/` directory and can be used to test Lambda logic locally or in AWS.

## Notes
- No real banking data is used
- Credentials and sensitive configuration are excluded

