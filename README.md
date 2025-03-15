# AI-based-lab-3
a news summarization application using LangChain that retrieves articles on specific topics and creates concise summaries according to user preferences.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/AlyFarrag/AI-based-lab-3.git
   cd AI-based-lab-3



   Usage
Run the application from the command line:
python main.py --user <user_id> --topic "<topic>" --summary-type <brief|detailed>

Examples
Save a topic of interest:
python main.py --user 123 --save-topic "Artificial Intelligence"

Search for news and get a brief summary:
python main.py --user 123 --topic "Artificial Intelligence" --summary-type brief

View user preferences and search history:
python main.py --user 123
