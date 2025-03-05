#Use python version 3.11
FROM python:3.11

#Copy requirements into docker
COPY requirements.txt .

#Install all requirements
RUN pip install -r requirements.txt

#Copy the rest of the code into the container
COPY . .
#Set port environment variable
ENV PORT=5001

#Expose the port so our computer can acess it 
EXPOSE 5001

#Run the app
CMD ["python", "app.py"]
