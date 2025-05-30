from fastapi import FastAPI, HTTPException
from app.scraper import scrape_and_summarize


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Twitter Scraper API"}

@app.post("/scrape/")
def scrape_twitter():
    
    try:
        summary = scrape_and_summarize()
        if "error" in summary:
            raise HTTPException(status_code=500, detail=summary["error"])
        # Assuming summary is a string, split it into lines
        # summary_lines = summary.split("\n")  # Split the summary by newlines

        # Return the summary as a list of lines
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/scrape/")
def scrape_twitter():
    try:
        summary = scrape_and_summarize()
        if "error" in summary:
            raise HTTPException(status_code=500, detail=summary["error"])
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
