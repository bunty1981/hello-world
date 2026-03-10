
#AI-copilot-vibe-app:


#Prompt-
For the below Application specification, please create:
1. User journey
2. Technical stack
3. High level system architecture diagram

#Application specification-

Application specification:
This is an application that allows multiple users to share their personal calendars in view-only and view-and-edit modes.
To begin with each user is presented with a blank calendar for the current and next 3 calendar years.
Users can update their calendars either by interactively adding events or by submitting an excel-sheet that has events listed for specific dates.Each user can keep their calendar private or share it with other users. 
Each user can grant view or view-and-edit access to users they have shared their calendar with.
Every event shown on the calendar also show which created it. Supported event creation methods are - 1) manual entry via a user interface for start-date, (optional) end-date, event name and optional event details or 2) events entered via an excel-sheet upload with start-date, (optional) end-date, event name and optional event details.
If not end-date is provided, assume the event is a single day event on the start-date.
