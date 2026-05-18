from app.contact.models import Contacts
from app.contact.schemas import CreateContact
async def create_contact(request: CreateContact):
    contact = Contacts(
        full_name=request.name,
        phone_number=request.phone,
        email=request.email,
        
    )
