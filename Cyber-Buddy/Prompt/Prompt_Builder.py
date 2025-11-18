from langchain_core.prompts import PromptTemplate


Template = PromptTemplate(
    template="""
Follow these instructions carefully:

Provide tailored cybersecurity guidance or incident response steps based on the user’s input.

If the user requests, teach relevant security measures, best practices, or preventive techniques suited to their knowledge level.

Evaluate the threat severity. If the user is in serious, immediate danger (e.g., active compromises or loss of critical data), advise contacting law enforcement, CERT, or trusted professionals without delay.

Avoid vague or generic advice; be precise and actionable.

Encourage the user to ask further questions or request specific help.

User Input:
{User_Input}

Chat History:
{Chat_History}
""",

input_variables=["User_Input", "Chat_History"],
validate_template=True,
)

Template.save("Prompt/Prompt.json")