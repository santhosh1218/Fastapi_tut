from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
templates = Jinja2Templates(directory="src/fastapi_tut/templates")
app.mount("/static", StaticFiles(directory="src/fastapi_tut/static"), name="static")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


posts: list[dict] = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
    {"id": 3, "title": "Third Post", "content": "This is the third post."},
]

@app.get("/api/posts")
def get_posts():
    return posts

# @app.get('/',response_class=HTMLResponse,include_in_schema=False)
# def home():
#     return HTMLResponse(content="<h1>Welcome to the FastAPI Tutorial!</h1>", status_code=200)

@app.get('/', include_in_schema=False,name="home")
def home(request: Request):
    return templates.TemplateResponse(request, "base.html", {"posts": posts,"title": "FastAPI Tutorial"})