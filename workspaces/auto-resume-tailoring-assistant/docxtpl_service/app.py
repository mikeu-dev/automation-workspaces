from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from docxtpl import DocxTemplate
import json
import os
import uuid

app = FastAPI()

@app.post("/render")
async def render_docx(template: UploadFile = File(...), data: str = Form(...)):
    # Load JSON data
    context = json.loads(data)
    
    # Save uploaded template temporarily
    temp_id = str(uuid.uuid4())
    in_path = f"/tmp/{temp_id}_in.docx"
    out_path = f"/tmp/{temp_id}_out.docx"
    
    with open(in_path, "wb") as f:
        f.write(await template.read())
        
    # Render with docxtpl
    doc = DocxTemplate(in_path)
    doc.render(context)
    doc.save(out_path)
    
    # Return the generated file
    return FileResponse(out_path, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename="resume_tailored.docx")
