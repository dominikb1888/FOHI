import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pydicom

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

def get_images():
    images = []
    dcm_files = [file for file in os.listdir() if file.endswith(".dcm")]
    for i, filename in enumerate(dcm_files):
        ds = pydicom.dcmread(filename)
        new_image = ds.pixel_array.astype(float)
        scaled_image = (np.maximum(new_image, 0) / new_image.max()) * 255.0
        scaled_image = np.uint8(scaled_image)
        imagepath= f"static/{filename}.png"
        img = Image.fromarray(scaled_image)
        img.save(imagepath, 'PNG')

        images.append({
            'path': imagepath,
            'age': ds.PatientAge,
            'date': ds.AcquisitionDate,
            'id': ds.PatientID
        })

    return images




@app.get("/", response_class=HTMLResponse)
async def patients():
    # HTML content to render the images in a 4x4 grid
    html_content = """
    <html>
    <head>
        <style>
            .grid-container {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 10px;
                padding: 10px;
            }
            .grid-item {
                width: 100%;
                height: auto;
            }
        </style>
    </head>
    <body>
        <div class="grid-container">
    """

    for image in get_images():
        html_content += f"<div class='grid-item'><img src='/{image['path']}' alt='{image['path']}' /><p>{image['id']}, {image['date']}, {image['age']}</p></div>"

    html_content += """
        </div>
    </body>
    </html>
    """

    return html_content



@app.get("/patient/{patient_id}", response_class=HTMLResponse)
async def patient(patient_id):

    # HTML content to render the images in a 4x4 grid
    html_content = """
    <html>
    <head>
        <style>
            .grid-container {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 10px;
                padding: 10px;
            }
            .grid-item {
                width: 100%;
                height: auto;
            }
        </style>
    </head>
    <body>        <div class="grid-container">
    """


    filtered_images = [image for image in get_images() if image['id'] == patient_id]
    for image in get_images():
        html_content += f"<div class='grid-item'><img src='/{image['path']}' alt='{image['path']}' /><p>{image['id']}, {image['date']}, {image['age']}</p></div>"

    html_content += """
        </div>
    </body>
    </html>
    """

    return html_content

@app.get("/api")
async def api_patients():
    return JSONResponse(get_images())

@app.get("/api/{patient_id}")
async def api_patient(patient_id):
    filtered_images = [image for image in get_images() if image['id'] == patient_id]
    # ERROR! this does not work, but...
    # Potential fixes:
    # - do abc
    # -> Look into Jupyter notebook for more experiments or snippets i tried

    return JSONResponse(filtered_images)




