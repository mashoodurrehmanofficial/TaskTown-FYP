# chat/utils.py

from app.models import MessagesTable, ProfilesTable,ProjectsTable

def save_message(user_id, message, project_id):
    profile = ProfilesTable.objects.get(user__id=user_id)
    required_project = ProjectsTable.objects.get(id=project_id)
    new_message = MessagesTable.objects.create(user=profile, text=message)
    required_project.messages.add(new_message)




def fetch_messages(project_id): 
    messages = [
        {
            "text":x.text,
            'user_id':x.user.user.id
            
        } 
        for x in  ProjectsTable.objects.get(id=project_id).messages.all()]
    print(messages)
    return list(messages)