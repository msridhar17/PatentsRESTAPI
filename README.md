# PatentsRESTAPI
## Flask
    It is microframework and doesn't have a lot of overhead, Flask is very performant. Extensions could impact performance negatively.
    Very flexible
    ORM used in current api is pymongo
    Flask documentation is comprehensive, full of examples and well structured.
    It is super easy to deploy Flask in production
    High Flexibility
    Easy to divide the code in to multiple chunks
    Easy installation
    Flask ORM frame works supports SQL and NOSQL
    Data Validation
    Built in unittest library

## Project Structure
The data preprocessing

   1. to downlaod the zip file content to the docker container/machine
   2. Extract zip file to the normal repository
   3. Extract the data using bs4 library and preprocess according to 
          our required meta fields and filtered with removing spaces
          a) Date
          b) title
          c) patent id
          d) full text(text-content): headings as key and content as value
          
The Python Flask based backend api
   
   * db(initiating the db for creating the collection object)
   * Two end points one for loading data into db and another for delete patent data wrt IDS 
         ### First End point needs the parameter as url and return the response with legnth of patents available through url and meta data of the patents
           Ex: ({'len':len(patents),"total_data":total_data})
         ### Second End point needs patent Id as the parameter and throuh the API it deletes patent from the DB and returns response successfully if Id found in DB
        
   
     

## Backed Setup and Configuration with Docker

### Step 1.

   * git init .
   * git pull  https://github.com/msridhar17/PatentsRESTAPI.git
   
### step2
 * docker-compose up -d (to run in background)

### step3 test with curl
   * curl --request GET  "http://0.0.0.0:7890/loadarchieves"
   * curl --request GET  "http://0.0.0.0:7890/deletepatent"

  
