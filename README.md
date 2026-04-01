# Smart Notes API
AI-powered Smart Notes API with search, statistics, and fallback handling

This is a backend project I built while learning how APIs work beyond basic tutorials.

The main goal was to understand how a system handles a request, processes data, and returns a response instead of just building a simple CRUD app.

## What this project does

It allows users to create notes with a title and content. Each note automatically stores the word count. You can retrieve all notes, delete a specific note, and also view overall statistics like total notes, total words, and average words per note.

## What I focused on while building this

I focused on understanding how API methods work such as GET, POST, and DELETE. I worked on writing backend logic instead of just storing data. I also handled cases where input might be missing or incorrect and made sure responses are structured clearly.

## Tech stack

Python
Flask

## API endpoints

POST /notes
Creates a new note

GET /notes
Returns all notes

DELETE /notes/{id}
Deletes a note by its id

GET /notes/stats
Returns statistics about all notes

## How to run

Install Flask using pip install flask

Run the application using python app.py

Then open http://127.0.0.1:5000

## Future improvements

I plan to replace the in memory storage with MongoDB so that data persists. I also want to add AI based summarization of notes and build a frontend interface to interact with the API.

## Note

This project is part of my learning process where I am moving from following tutorials to building and understanding backend systems on my own.
