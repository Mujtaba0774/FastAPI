from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import openai

app = FastAPI()

# Set up OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Define a route for the chatbot
@app.post("/chat")
async def chat(request: Request):
    # Get the user's message from the request body
    message = await request.form()

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message["message"],
        max_tokens=2048,
        temperature=0.5,
    )

    # Return the response as HTML
    return HTMLResponse(content=f"<html><body><p>{response['choices'][0]['text']}</p></body></html>")

# Define a route for the chatbot interface
@app.get("/")
def read_root():
    return HTMLResponse(content="""
    <html>
    <body>
    <h1>Chatbot</h1>
    <form action="/chat" method="post">
    <input type="text" name="message" placeholder="Type a message...">
    <input type="submit" value="Send">
    </form>
    </body>
    </html>
    """)