import os
print("Current working directory:", os.getcwd())


from flask import Flask, render_template, request

app = Flask(__name__, template_folder='Templates')

# Example symptom-disease mapping (replace this with your own data)

symptom_disease_mapping = {

    'fever': ['flu', 'common cold'],

    'cough': ['flu', 'common cold'],

    'headache': ['Migraine', 'Tension Headache'],

    'fatigue': ['Flu', 'Common Cold', 'Anemia'],

    'chest_pain': [

        'Coronary Heart Disease', 'Heart Attack', 'Pericarditis',

        'Aortic Valve Stenosis', 'Congestive Heart Failure'

    ],

    'shortness_of_breath': [

        'Congenital Heart Disease', 'Atherosclerosis', 'Cardiomyopathy',

        'Heart Attack', 'Pericarditis', 'Peripheral Vascular Disease',

        'Rheumatic Heart Disease', 'Aortic Valve Stenosis',

        'Congestive Heart Failure', 'Atrial Fibrillation'

    ],

    'sweating': ['Heart Attack', 'Atrial Fibrillation'],

    'nausea': ['Heart Attack', 'Aortic Valve Stenosis'],

    'palpitations': ['Atrial Fibrillation', 'Rheumatic Heart Disease'],

    'dizziness': ['Atrial Fibrillation', 'Congestive Heart Failure'],

    'coughing_blood': ['Bronchitis', 'Tuberculosis'],

    'swollen_legs': ['Peripheral Vascular Disease', 'Congestive Heart Failure'],

    'chest_pressure': ['Coronary Heart Disease', 'Heart Attack'],

    'rapid_pulse': ['Atrial Fibrillation', 'Tachycardia'],

    'blue_skin': ['Cyanosis', 'Peripheral Vascular Disease'],

    'arrhythmia': ['Arrhythmia', 'Atrial Fibrillation'],

    'artery_blockage': ['Atherosclerosis', 'Coronary Heart Disease'],

    'yellow_skin': [

        'Hepatitis', 'Hepatitis A', 'Hepatitis B',

        'Hepatitis C', 'Hepatitis E', 'Cirrhosis'

    ],

    'abdominal_pain': [

        'Fatty Liver', 'Hepatitis', 'Hepatitis A', 'Hepatitis B',

        'Hepatitis C', 'Hepatitis E', 'Cirrhosis', 'Appendicitis'

    ],

    'dark_urine': [

        'Hepatitis', 'Hepatitis A', 'Hepatitis B',

        'Hepatitis C', 'Hepatitis E', 'Cirrhosis'

    ],

    'jaundice': [

        'Hepatitis', 'Hepatitis A', 'Hepatitis B',

        'Hepatitis C', 'Hepatitis E', 'Cirrhosis'

    ],

    'fatigue': [

        'Hepatitis', 'Hepatitis A', 'Hepatitis B',

        'Hepatitis C', 'Hepatitis E', 'Cirrhosis', 'Anemia'

    ],

    'itching': [

        'Hepatitis', 'Hepatitis A', 'Hepatitis B',

        'Hepatitis C', 'Hepatitis E', 'Cirrhosis'

    ],

    'urinary_changes': [

        'Chronic Kidney Disease', 'Kidney Infection/Pyelonephritis',

        'Nephrotic Syndrome', 'Glomerulonephritis'

    ],

    'abdominal_swelling': [

        'Chronic Kidney Disease', 'Polycystic Kidney Disease',

        'Nephrotic Syndrome', 'Glomerulonephritis'

    ],

    'back_pain': [

        'Kidney Stones', 'Polycystic Kidney Disease',

        'Chronic Kidney Disease'

    ],

    'urinary_blood': [

        'Kidney Stones', 'Kidney Infection/Pyelonephritis',

        'Glomerulonephritis'

    ],

    'urination_frequent': [

        'Diabetic Nephropathy', 'Chronic Kidney Disease',

        'Polycystic Kidney Disease'

    ],

    'urine_protein': [

        'Nephrotic Syndrome', 'Chronic Kidney Disease', 'Glomerulonephritis'

    ],

    'depression': ['Depression', 'Bipolar Disorder'],

    'hallucinations': ['Schizophrenia'],

    'acid_reflux': [

        'Acidity', 'Gastritis', 'Peptic Ulcer', 'Gastroenteritis',

        'Dyspepsia'

    ],

    'appendix_pain': ['Appendicitis'],

    'food_poisoning': ['Food Poisoning'],

    'ibd': ['IBS', 'Colitis', 'Crohn’s Disease', 'Ulcerative Colitis'],

    'allergic_rhinitis': ['Allergic Rhinitis'],

    'asthma': ['Asthma'],

    'lung_infections': [

        'Pneumonia', 'Bronchitis', 'Tuberculosis', 'MERS-CoV'

    ],

    'dry_cough': ['Dry Cough'],

    'seizures': ['Epilepsy'],

    'weakness_one_side': ['Stroke'],

    'sudden_headache': ['Brain Aneurysm'],

    'tremors': ['Parkinson\'s Disease'],

    'mood_swings': ['Bipolar Disorder'],

    'memory_loss': ['Dementia', 'Alzheimer\'s Disease'],

    'persistent_sadness': ['Depression'],

    'hallucinations': ['Schizophrenia'],

    'heartburn': ['Acidity'],

    'abdominal_pain': ['Appendicitis', 'IBS', 'Peptic Ulcer', 'Colitis'],

    'indigestion': ['Dyspepsia', 'Gastritis', 'Gastroenteritis'],

    'nausea_vomiting': ['Food Poisoning'],

    'diarrhea': ['Food Poisoning', 'Gastroenteritis', 'IBS', 'Colitis'],

    'abdominal_swelling': ['IBS', 'Colitis'],

    'food_allergy': ['Food Allergy'],

    'sneezing_runny_nose': ['Allergic Rhinitis'],

    'wheezing': ['Asthma'],

    'cough_shortness_breath': ['Asthma', 'COPD'],

    'lung_infections': ['Pneumonia', 'Bronchitis', 'Tuberculosis'],

    'dry_cough': ['Dry Cough'],

    'chronic_lung_disease': ['COPD', 'Emphysema'],

    'eye_infections': ['Blepharitis', 'Stye'],

    'vision_problems': ['Cataract', 'Glaucoma', 'Retinal Detachment', 'Strabismus'],

    'color_vision_loss': ['Color Blindness'],

    'thyroid_problems': ['Hyperthyroidism', 'Hypothyroidism'],

    'insomnia_sleep_problems': ['Insomnia'],

    'thyroid_disease': ['Thyroid Disease'],

    'high_blood_sugar': ['Diabetes', 'Type 1 Diabetes', 'Type 2 Diabetes', 'Gestational Diabetes'],

    'brain_bleeding': ['Stroke', 'Brain Aneurysm'],

    'muscle_stiffness': ['Parkinson\'s Disease'],

    'mania': ['Bipolar Disorder'],

    'memory_problems': ['Dementia', 'Alzheimer\'s Disease'],

    'loss_interest': ['Depression'],

    'delusions': ['Schizophrenia'],

    'acid_reflux': ['Acidity'],

    'appendix_pain': ['Appendicitis'],

    'stomach_pain': ['Dyspepsia', 'Peptic Ulcer', 'Gastritis'],

    'poisoning': ['Food Poisoning'],

    'stomach_cramps': ['Gastroenteritis'],

    'intestinal_pain': ['IBS', 'Colitis'],

    'allergic_reaction_food': ['Food Allergy'],

    'itchy_eyes_nose': ['Allergic Rhinitis'],

    'breathing_difficulty': ['Asthma'],

    'bronchial_irritation': ['COPD', 'Emphysema'],

    'lung_inflammation': ['Pneumonia', 'Bronchitis', 'Tuberculosis'],

    'excessive_sputum': ['Bronchitis'],

    'shortness_breath_mucus': ['Bronchitis', 'COPD'],

    'joint_pain': ['Arthritis'],

    'back_pain': ['Back Pain'],

    'brittle_bones': ['Brittle Bone Disease'],

    'eye_irritation': ['Dry Eyes'],

    'eye_pressure': ['Glaucoma'],

    'retinal_problems': ['Retinal Detachment'],

    'strabismus': ['Strabismus'],

    'eye_redness_swelling': ['Eye Infections'],

    'thinning_bones': ['Osteoporosis'],

    'joint_swelling': ['Arthritis'],

    'hives_rashes': ['Allergies', 'Atopic Dermatitis', 'Contact Dermatitis'],

    'burn_injury': ['Burns'],

    'skin_infection': ['Cellulitis'],

    'itchy_skin': ['Dermatitis', 'Seborrheic Dermatitis', 'Eczema'],

    'skin_growth': ['Keloids'],

    'cleft_lip_palate': ['Cleft Lip Palate'],

    'mouth_ulcers': ['Mouth Ulcers'],

    'oral_fungal_infection': ['Oral Thrush'],

    'gum_bleeding': ['Gum Disease', 'Periodontitis'],

    'teeth_sensitivity': ['Teeth Sensitivity'],

    'dry_mouth': ['Dry Mouth'],

    'bad_breath': ['Bad Breath'],

    'oral_cancer': ['Oral Cancer'],

    'breast_lump': ['Breast Cancer'],

    'thyroid_nodule': ['Thyroid Cancer'],

    'childhood_cancers': ['Cancers in Children'],

    'prostate_problems': ['Prostate Cancer'],

    'ovarian_problems': ['Ovarian Cysts', 'Ovarian Cancer'],

    'skin_spot': ['Skin Cancer'],

    'bowel_changes': ['Bowel Cancer', 'Colorectal Cancer'],

    'cough_blood': ['Lung Cancer', 'Tuberculosis'],

    'thick_blood_phlegm': ['Pneumonia'],

    'anaemia': ['Anaemia'],

    'high_blood_pressure': ['Hypertension'],

    'thalaessemia': ['Thalassemia'],

    'aneurysm': ['Aneurysm'],

    'blood_clot_legs': ['Deep Vein Thrombosis'],

    'rheumatic_swelling': ['Arthritis'],

    'spine_pain': ['Back Pain'],

    'brittle_bone': ['Brittle Bone Disease'],

    'carpal_tunnel_syndrome': ['Carpal Tunnel Syndrome'],

    'joint_infection': ['Osteomyelitis'],

    'lupus': ['Lupus'],

    'thyroid_problems': ['Hyperthyroidism', 'Hypothyroidism'],

    'insomnia_sleep_problems': ['Insomnia'],

    'thyroid_disease': ['Thyroid Disease'],

    'high_blood_sugar': ['Diabetes', 'Type 1 Diabetes', 'Type 2 Diabetes', 'Gestational Diabetes'],

    'painful_shoulder': ['Frozen Shoulder'],

    'muscle_paralysis': ['Paralysis'],

    'sciatic_nerve_pain': ['Sciatica'],

    'vein_swelling': ['Varicose Veins'],

    'facial_weakness': ['Bell\'s Palsy'],

    'anaemia': ['Anaemia'],

    'high_blood_pressure': ['Hypertension'],

    'thalaessemia': ['Thalassemia'],

    'aneurysm': ['Aneurysm'],

    'blood_clot_legs': ['Deep Vein Thrombosis'],

    # ... other symptoms and diseases

}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        symptoms = request.form.getlist('symptoms')

        selected_diseases = set()

        for symptom in symptoms:

            if symptom in symptom_disease_mapping:
                selected_diseases.update(symptom_disease_mapping[symptom])

        return render_template('result.html', diseases=selected_diseases)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



