import os # for manage the file brother
import requests # for api call 

outputFolder = "/home/N3xthar-Voryx/CelestialNeRF/data/balva_crater_sol772"# folder where i have to put the image brother

sol = 772 # which mars day data you want brother !!!

imageType = "Natural Color"  # choose as per NASA's filter option !! 


# where the api hit brother !!! 

apiUrl = "https://mastcamz.asu.edu/api/v1/images"

# creating the destination folder if it exit than fine otherwise create it brother !! 
os.makedirs(outputFolder , exist_ok = True )



# now i am making the function for image list from the api 

# FETCH IMAGE LIST FROM API  

# what the function do brother !!! 
# fetchImageMetadata(...) ka kaam sirf API se image metadata list lana hai, actual image files nahi.

#     API tumhe directly image nahi bhejta, pehle wo JSON format me metadata deta hai jisme:

#         Image ka URL

#         Image ka type

#         Date / sol

#         Camera info

#     Ye function us JSON ko parse karke ek Python list me save karta hai.

def fetchImageMetadata (sol , imageType):

    allImage = []   # for storing all  the images brother !! 
    page = 1 ; # for selecting the image page by page bro 
    while True:
        print (f"Fetching the data page {page} from API  ............")    
        parameter = {
            "sol":sol,          # specify the day of the mars for downloading the data 
            "type":imageType,   # image filtering bro !! 
            "page":page,    # selecting the page bro
            "per_page":100    # how much image you want per page brother! 
        }


        # now request the to get the data brother !! 
        req = requests.get(apiUrl , params = parameter )


        # now if there is any error occurs then handling this brother !! 
        if req.status_code != 200:
            print(f"Error in fetching the page number  {page} data : {req.status_code}")

        # converting the api json format to python dictionary for easy traversing 

        # .json() ka main kaam hi yeh hai ki:

        # API se aaya JSON text → Python ke dictionary (ya list) me convert kar dena


        data = req.json()  

        #  {
        #   "data": [
        #     {"id": 1, "url": "image1.jpg"},
        #     {"id": 2, "url": "image2.jpg"}
        #   ],
        #   "success": true
        # }

        # now i want only the image list form api list brother !! !!! 

        images = data.get("data",[])

        # if no image found then break it brother !! 
        if not images:
            break 

        # add this page image into the allImage list 

        allImage.extend(images)

        # move the page to the next page brother !! 

        page+=1

    return allImage

        

 
