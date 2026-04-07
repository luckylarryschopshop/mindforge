# PRD.md

## Product Overview  
Mindforge Idea Tracker is a web application designed to help users manage and organize their ideas. The application features a FastAPI backend and an HTML frontend. Ideas are stored in JSON files, providing a simple and efficient way to manage data.

## User Stories  
1. As a user, I want to add an idea with a title and description so that I can track my thoughts.  
2. As a user, I want to search through my ideas so that I can quickly find specific ideas.  
3. As a user, I want to delete an idea so that I can remove ideas that are no longer relevant.  
4. As a user, I want to view all my ideas so that I can see my entire collection at a glance.

## Acceptance Criteria  
- Users can add an idea with a title and description.  
- Users can search for ideas by title or description.  
- Users can delete individual ideas.  
- Users can view all ideas in a list format.  
- The application stores ideas in a JSON file.  
- The application provides a clean and intuitive interface for managing ideas.

## UI Wireframe  
- **Header**: Displays the title of the application.  
- **Add Form**: Located at the top of the page, includes fields for title and description, and a submit button.  
- **Search Bar**: Located near the add form, allows users to search through ideas.  
- **Idea Cards**: Displayed below the search bar. Each card contains the title, description, and a delete button.  

## Tech Stack  
- **Backend**: FastAPI  
- **Frontend**: HTML, CSS, and JavaScript  
- **Storage**: JSON files  
- **Serving**: FastAPI serves the HTML frontend  

## API Design  
- **GET /api/ideas**: Returns a list of all ideas.  
- **POST /api/ideas**: Adds a new idea to the list.  
- **DELETE /api/ideas/{idea_id}**: Deletes an idea by its ID.