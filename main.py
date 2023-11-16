from fastapi import FastAPI 

from fastapi.middleware.cors import CORSMiddleware       

 

app = FastAPI() 

  

#orgins is a list of locations we expect traffic from, by default running a new react project starts at port 3000 

orgins = [ 

    "http://localhost", 

    "https://localhost", 

    "http://localhost:3000", 

    "https://localhost:3000" 

] 

  

# The following code adds the cors middleware to the app, with default settings that allow all methods, and use the orgins we defined above 

app.add_middleware( 

    CORSMiddleware, 

    allow_origins=orgins, 

    allow_credentials=True, 

    allow_methods=["*"], 

    allow_headers=["*"] 

) 