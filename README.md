## Repository Structure

```text
amazon-lex-banking-chatbot/
├── architecture/
│   └── architecture-diagram.png
├── lambda/
│   ├── handler.py
│   ├── intents.py
│   └── utils.py
├── lex/
│   ├── intents/
│   │   ├── CheckBalance.json
│   │   ├── TransferMoney.json
│   │   └── Help.json
│   ├── slot-types/
│   │   └── AccountType.json
│   └── bot-config.json
├── events/
│   ├── check_balance_event.json
│   └── transfer_money_event.json
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── .gitignore
└── README.md
