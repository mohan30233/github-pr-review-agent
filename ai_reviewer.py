import os

from certifi import contents
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def review_patch(filename, patch, model):
    prompt = f"""
    You are a Senior Software Engineer at Google.

    Review the following GitHub Pull Request like an experienced code reviewer.

    Filename:
    {filename}

    Code Changes:
    {patch}

    Analyze the code for:

    1. 🐞 Bugs
    2. ⚠️ Edge Cases
    3. 📖 Readability
    4. 🏗️ Maintainability
    5. ⚡ Performance
    6. 🔒 Security Issues
    7. ✅ Python Best Practices

    Rules:
    - Be constructive and professional.
    - Explain why something is a problem.
    - Suggest improvements where appropriate.
    - If there are no issues in a category, explicitly say "No issues found."

    Return the response in Markdown using these headings:

    # Review

    ## ✅ Strengths

    ## 🐞 Bugs

    ## ⚠️ Edge Cases

    ## 📖 Readability

    ## 🏗️ Maintainability

    ## ⚡ Performance

    ## 🔒 Security

    ## 💡 Suggestions

    ## ⭐ Overall Score
    Give a score out of 10 and briefly justify it.
    """

    response = client.chat.completions.create(
        model = model,
        messages=[
         {"role": "user",
            "content": prompt
             }
     ]
    )

    return response.choices[0].message.content

def summarize_pr(reviews, model):
    prompt = f"""
    You're a senior software Engineer.
    
    Below are the AI reviews for multiple files in one pull request.
    
    {reviews}
    
    Generate:
    
    1.Overall Score (/10)
    2.Summary
    3.Biggest Risk
    4.Best Practice
    5.Final Recommendations (Approve / Request Changes)
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
             "role": "user",
             "content": prompt
             }
        ]
    )

    return response.choices[0].message.content

