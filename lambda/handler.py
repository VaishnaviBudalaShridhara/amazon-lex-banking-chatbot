def lambda_handler(event, context):
    intent_name = event["sessionState"]["intent"]["name"]

    if intent_name == "CheckBalance":
        return check_balance(event)
    elif intent_name == "TransferMoney":
        return transfer_money(event)
    else:
        return close("Sorry, I didn’t understand that request.")

def check_balance(event):
    account_type = event["sessionState"]["intent"]["slots"]["AccountType"]["value"]["interpretedValue"]
    
    # Example
    balance = "5,000 EUR"

    return close(f"Your {account_type} account balance is {balance}.")

def transfer_money(event):
    return close("Your transfer has been initiated successfully.")

def close(message):
    return {
        "sessionState": {
            "dialogAction": { "type": "Close" },
            "intent": { "state": "Fulfilled" }
        },
        "messages": [
            { "contentType": "PlainText", "content": message }
        ]
    }
