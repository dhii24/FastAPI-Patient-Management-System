from fastapi import FastAPI,Path,HTTPException,Query
import json

app=FastAPI()


# LOAD DATA
def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data


# SAVE DATA
def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f,indent=4)


# HOME ROUTE
@app.get("/")
def hello():
    return {'message':'Patient Management System API'}


# ABOUT ROUTE
@app.get('/about')
def about():
    return {'message':'A fully functional API to manage your patient record'}


# VIEW ALL PATIENTS
@app.get('/view')
def view():
    data=load_data()
    return data


# VIEW SINGLE PATIENT
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(...,description='ID of the patient in the DB',example='P001')):
    data=load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(
        status_code=404,
        detail='Patient not found'
    )



# SORT PATIENTS
@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description='Sort on the basis of height, weight, BMI'),order: str = Query('asc',description='sort in asc or desc order')):

    valid_fields=['height','weight','bmi']


    # checking if user gave valid field
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid field, select from {valid_fields}')


    # checking if order is valid
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400,detail='Invalid order, select between asc and desc')


    # load patient data
    data=load_data()


    # if desc -> True
    # else -> False
    sort_order = True if order=='desc' else False



    # sorting logic
    sorted_data=sorted(data.values(),key=lambda x: x.get(sort_by, 0),reverse=sort_order)
    return sorted_data


# CREATE PATIENT
@app.post('/create/{patient_id}')
def create_patient(patient_id: str, new_patient: dict):

    data=load_data()

    # check if patient already exists
    if patient_id in data:
        raise HTTPException(status_code=400,detail='Patient already exists')

    # add new patient
    data[patient_id]=new_patient

    # save updated data
    save_data(data)

    return {'message':'Patient created successfully','patient':new_patient}


# DELETE PATIENT
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    data=load_data()

    # check if patient exists
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Patient not found')

    # delete patient
    deleted_patient=data.pop(patient_id)

    # save updated data
    save_data(data)

    return {'message':'Patient deleted successfully','deleted patient':deleted_patient}

