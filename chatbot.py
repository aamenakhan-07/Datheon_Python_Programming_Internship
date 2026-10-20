
import json
import re
from pathlib import Path


def load_faq_data():
    file_path = Path(__file__).parent / "sample_faq.json"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: sample_faq.json was not found.")
    except json.JSONDecodeError:
        print("Error: The FAQ JSON file is invalid.")
    except OSError as error:
        print(f"Could not read FAQ data: {error}")

    return None


def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text)


def find_intents(message, data):
    text = normalize_text(message)
    intents = []

    # Greeting detection
    for greeting in data.get("greetings", []):
        pattern = r"\b" + re.escape(normalize_text(greeting)) + r"\b"

        if re.search(pattern, text):
            intents.append("greeting")
            break

    # FAQ keyword matching
    keyword_rules = {
        "hours": [
            "hours", "operation", "opening time",
            "business hours", "working hours"
        ],
        "submission": [
            "submit", "submission", "github",
            "student workspace", "internship project"
        ],
        "certificate": [
            "certificate", "certificates",
            "when will i receive"
        ]
    }

    for intent, keywords in keyword_rules.items():
        if any(
            re.search(
                r"\b" + re.escape(normalize_text(keyword)) + r"\b",
                text
            )
            for keyword in keywords
        ):
            intents.append(intent)

    return list(dict.fromkeys(intents))


def answer_faq(intent, data):
    faq_index = {
        "hours": 0,
        "submission": 1,
        "certificate": 2
    }

    index = faq_index.get(intent)
    faqs = data.get("faqs", [])

    if index is not None and index < len(faqs):
        return faqs[index].get("answer", "Answer unavailable.")

    return None


def chatbot():
    data = load_faq_data()

    if data is None:
        print("Chatbot could not start because FAQ data is unavailable.")
        return

    print("=" * 45)
    print("Welcome to the Internship Support Chatbot!")
    print("Ask about business hours, project submission,")
    print("or certificates. Type 'bye' to exit.")
    print("=" * 45)

    while True:
        try:
            message = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Have a great day!")
            break

        if not message:
            print("Bot: Please type a question.")
            continue

        normalized = normalize_text(message)

        if re.fullmatch(r"(bye|exit|quit)", normalized):
            print("Bot: Goodbye! Have a great day!")
            break

        intents = find_intents(message, data)

        if "greeting" in intents:
            print("Bot: Hello! How can I help you today?")

        answered = False

        for intent in intents:
            if intent == "greeting":
                continue

            answer = answer_faq(intent, data)

            if answer:
                print("Bot:", answer)
                answered = True

        if not intents or (intents == ["greeting"]):
            if normalized not in ["hello", "hi", "hey",
                                  "good morning", "good afternoon"]:
                print(
                    "Bot: Sorry, I didn't understand that. "
                    "You can ask about business hours, "
                    "project submission, or certificates."
                )


if __name__ == "__main__":
    chatbot()
