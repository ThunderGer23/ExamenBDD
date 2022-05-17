from fastapi import FastAPI
from document.docs import tags_metadata

app = FastAPI(title = 'API para el examen, análisis del documento',
    description = 'Esta API es para facilitar la tarea de hacer el examen',
    version = '1.0',
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "ThunderGer",
        "url": "http://x-force.example.com/contact/",
        "email": "ThunderGer@outlook.com",
    },
    license_info={
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT'
    },
    openapi_tags= tags_metadata)