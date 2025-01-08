
from fastapi import FastAPI, Request
from pydantic import BaseModel
from groq import Groq
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

client = Groq(api_key="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")

app = FastAPI()

templates = Jinja2Templates(directory=r"C:\Users\yahya\Desktop\newfiles\aicodes\new\templates")

app.mount("/1static", StaticFiles(directory=r"C:\Users\yahya\Desktop\newfiles\aicodes\new\1static"), name="static")

class EmailRequest(BaseModel):
    email: str

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("1index.html", {"request": request})

@app.post('/analyse')  
async def analyse(request: EmailRequest):
    try:
        email_content = request.email
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that formats email analysis into structured HTML with headings, lists, and paragraphs."
                },
                {
                    "role": "user",
                    "content": email_content,
                }
            ],
            model="llama-3.3-70b-versatile",
            stream=False,
        )
        response = chat_completion.choices[0].message.content

        # Add HTML formatting
        formatted_response = f"""
        <h3>Email Analysis</h3>
        {response.replace('###', '<h4>').replace('####', '<h5>').replace('**', '<strong>').replace('**', '</strong>')}
        """

        return {"result": formatted_response}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
