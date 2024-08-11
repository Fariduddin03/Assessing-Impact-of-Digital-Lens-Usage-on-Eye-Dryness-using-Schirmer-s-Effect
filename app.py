from flask import Flask, render_template, request
import pickle
import numpy as np

filename = 'C:\\Users\\saira\\OneDrive\\Desktop\\ipbl\\DigitalEye\\Eyemodel.pkl'
with open(filename, 'rb') as f:
    loaded_classifiers = pickle.load(f)


app = Flask(__name__)
def make_predictions(data):
    predictions = {}
    for key, clf in loaded_classifiers.items():
        prediction = clf.predict(data)
        predictions[key] = prediction[0]
    return predictions
@app.route('/')
def home():
	return render_template('frontpage.html')

@app.route('/Test', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        Name=request.form.get('name')
        Age=int(request.form['age'])
        Sex = int(request.form.get('sex'))
        wearables = int(request.form.get('eyewear'))
        Duration = int(request.form.get('usageDuration'))
        onlineplatforms = int(request.form.get('onlinePlatforms'))
        Nature = int(request.form.get('computerUsage'))
        screenillumination = int(request.form.get('screenIllumination'))
        workingyears = int(request.form.get('yearsWorking'))
        hoursspentdailycurricular = int(request.form.get('hoursOnlineClasses'))
        hoursspentdailynoncurricular = int(request.form.get('screenTimeNonCurricular'))
        Gadgetsused = int(request.form.get('mostUsedGadget'))
        levelofgadjetwithrespecttoeyes = int(request.form.get('gadgetLevel'))
        Distancekeptbetweeneyesandgadjet = int(request.form.get('distanceEyesGadget'))
        Avgnighttimeusageperday = int(request.form.get('nightTimeUsage'))
        Blinkingduringscreenusage = int(request.form.get('remindToBlink'))
        Difficultyinfocusingafterusingscreens = int(request.form.get('difficultyFocusing'))
        freqquencyofcomplaints = int(request.form.get('complaintsFrequency'))
        Severityofcomplaints = int(request.form.get('ocularSeverity'))
        
        Ocularsymptomsobservedlately= request.form.getlist('ocularSymptoms')
        total_symptoms = sum(int(symptom) for symptom in  Ocularsymptomsobservedlately)/len(Ocularsymptomsobservedlately)
        Ocularsymptomsobservedlately=int(total_symptoms) 
        
        Symptomsobservingatleasthalfofthetimes =request.form.getlist('symptomsObservation')
        total = sum(int(sy) for sy in  Symptomsobservingatleasthalfofthetimes)/len(Symptomsobservingatleasthalfofthetimes )
        Symptomsobservingatleasthalfofthetimes =int(total) 
        
        Complaintsfrequency = int(request.form.get('complaintFrequency'))
        frequencyofdryeyes = int(request.form.get('dryFrequency'))
        
        data = np.array([[Age, wearables, workingyears, Nature,
                    hoursspentdailycurricular, hoursspentdailynoncurricular,
                    Gadgetsused, Avgnighttimeusageperday, Blinkingduringscreenusage,
                    freqquencyofcomplaints, Severityofcomplaints,
                    Ocularsymptomsobservedlately, Symptomsobservingatleasthalfofthetimes,
                    Complaintsfrequency]])
        

        predictions = make_predictions(data)
        return render_template('result.html', predictions=predictions)
        
        
if __name__ == '__main__':
	app.run()

