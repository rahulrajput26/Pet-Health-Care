import streamlit as st
from streamlit_option_menu import option_menu
# a=st.sidebar.radio("categories",("Home","Information about pet","About Us","Help"))
st.title("ONE STOP SOLUTION FOR PET HEALTH CARE...")
with st.sidebar:
    b=option_menu(
        menu_title="Main Menu",
        options=["Home","Help"]
    )
if  b=="Home":
    a=option_menu(
        menu_title=None,
        options=["Home","Diseases,Symptoms and their Solutions"],
        orientation="horizontal"
    )
    if a=="Diseases,Symptoms and their Solutions":
        z=st.selectbox("Select your pet",("Select ↓","Cat","Dog","Birds","Fish","Rabbit","Hamster"))
        b1=st.button("Select")
        if z== "Cat" and b1:
            st.markdown("""Cats are susceptible to various diseases that can affect their health and quality of life. Here is a guide to common cat diseases, their symptoms, causes, and solutions:

---

### *1. Feline Upper Respiratory Infections (URI)*
- *Symptoms:*
  - Sneezing, nasal discharge, and congestion.
  - Watery eyes or discharge.
  - Loss of appetite and fever.
- *Causes:* 
  - Viral or bacterial infections (e.g., Feline Herpesvirus or Calicivirus).
- *Solutions:*
  - Supportive care (hydration, appetite stimulants).
  - Antibiotics for secondary bacterial infections.
  - Vaccinate against common viruses.

---

### *2. Feline Leukemia Virus (FeLV)*
- *Symptoms:*
  - Lethargy and weight loss.
  - Pale gums and recurring infections.
  - Enlarged lymph nodes.
- *Causes:* 
  - Viral infection spread through saliva, urine, or blood.
- *Solutions:*
  - No cure; supportive care includes boosting immunity and treating symptoms.
  - Vaccination and keeping cats indoors to reduce exposure.

---

### *3. Feline Panleukopenia (Feline Distemper)*
- *Symptoms:*
  - Severe vomiting and diarrhea.
  - Fever and loss of appetite.
  - Dehydration and lethargy.
- *Causes:* 
  - Highly contagious virus (Parvovirus).
- *Solutions:*
  - Supportive care (fluids, anti-nausea medication).
  - Vaccination is essential for prevention.

---

### *4. Feline Immunodeficiency Virus (FIV)*
- *Symptoms:*
  - Recurring infections (e.g., respiratory or skin infections).
  - Weight loss and poor coat condition.
  - Enlarged lymph nodes and fever.
- *Causes:* 
  - Virus spread through bite wounds or blood.
- *Solutions:*
  - No cure; manage symptoms and secondary infections.
  - Keep FIV-positive cats indoors and avoid interactions with healthy cats.

---

### *5. Hyperthyroidism*
- *Symptoms:*
  - Weight loss despite a good appetite.
  - Increased thirst and urination.
  - Hyperactivity and vomiting.
- *Causes:* 
  - Overproduction of thyroid hormones (common in older cats).
- *Solutions:*
  - Medications to regulate thyroid hormones.
  - Surgery or radioactive iodine treatment in severe cases.

---

### *6. Feline Lower Urinary Tract Disease (FLUTD)*
- *Symptoms:*
  - Difficulty urinating or frequent attempts.
  - Blood in urine and crying in pain.
  - Licking the genital area excessively.
- *Causes:* 
  - Stress, bladder stones, urinary tract infections, or obesity.
- *Solutions:*
  - Immediate veterinary care if a blockage occurs.
  - Special diets and stress management.
  - Ensure access to clean water.

---

### *7. Ringworm*
- *Symptoms:*
  - Circular patches of hair loss.
  - Red, scaly, or crusty skin.
  - Itching or excessive grooming.
- *Causes:* 
  - Fungal infection spread through contact with infected animals or surfaces.
- *Solutions:*
  - Antifungal creams or oral medications.
  - Isolate infected cats and disinfect the environment.

---

### *8. Toxoplasmosis*
- *Symptoms:*
  - Lethargy and fever.
  - Loss of appetite and diarrhea.
  - Respiratory distress in severe cases.
- *Causes:* 
  - Caused by the parasite Toxoplasma gondii, often from raw meat or infected prey.
- *Solutions:*
  - Antibiotics like clindamycin prescribed by a vet.
  - Prevent by avoiding raw meat and keeping cats indoors.

---

### *9. Dental Disease*
- *Symptoms:*
  - Bad breath and drooling.
  - Red or bleeding gums.
  - Difficulty eating or pawing at the mouth.
- *Causes:* 
  - Plaque buildup, gingivitis, or infections.
- *Solutions:*
  - Regular dental cleanings and brushing.
  - Dental treats or special diets to reduce plaque.

---

### *10. Diabetes Mellitus*
- *Symptoms:*
  - Increased thirst and urination.
  - Weight loss despite normal eating habits.
  - Weakness in the hind legs.
- *Causes:* 
  - Insufficient insulin production or resistance (common in overweight cats).
- *Solutions:*
  - Insulin injections and a controlled diet.
  - Monitor blood sugar levels regularly.

---

### *11. Flea and Tick Infestations*
- *Symptoms:*
  - Excessive scratching and biting at the skin.
  - Hair loss or red, irritated skin.
  - Presence of fleas or flea dirt in the fur.
- *Causes:* 
  - Infestation by fleas, ticks, or mites.
- *Solutions:*
  - Use vet-recommended flea and tick treatments.
  - Regularly clean bedding and vacuum carpets.

---

### *12. Obesity*
- *Symptoms:*
  - Excess body weight.
  - Difficulty grooming or reduced activity.
  - Increased risk of diabetes and joint problems.
- *Causes:* 
  - Overfeeding, lack of exercise, or improper diet.
- *Solutions:*
  - Implement a vet-approved weight loss plan.
  - Provide portion-controlled meals and regular playtime.

---

### *13. Hairballs*
- *Symptoms:*
  - Gagging or retching without vomiting.
  - Constipation or loss of appetite.
- *Causes:* 
  - Ingested hair during grooming that accumulates in the stomach.
- *Solutions:*
  - Regular brushing to reduce shedding.
  - Use hairball remedies or high-fiber diets.

---

### *14. Arthritis*
- *Symptoms:*
  - Limping or difficulty jumping.
  - Reduced activity and stiffness.
  - Behavior changes like irritability.
- *Causes:* 
  - Age-related joint degeneration or injuries.
- *Solutions:*
  - Joint supplements (glucosamine, chondroitin).
  - Pain management under veterinary guidance.

---

### *Prevention Tips for Cat Diseases*
1. *Vaccination:* Ensure core vaccinations for FeLV, FIV, rabies, and distemper.
2. *Hygiene:* Keep litter boxes clean and wash bedding regularly.
3. *Healthy Diet:* Provide a balanced diet with fresh water.
4. *Regular Vet Visits:* Annual checkups help detect diseases early.
5. *Parasite Prevention:* Use flea, tick, and worm preventatives as recommended.
6. *Indoor Lifestyle:* Reduces exposure to infections and parasites.

---

By monitoring your cat's health closely and seeking veterinary care when needed, you can ensure a long and healthy life for your feline friend.""")
    
        elif z=="Dog"and b1:
            st.markdown("""Dogs are prone to a variety of diseases, ranging from mild to life-threatening. Here is an overview of common dog diseases, their symptoms, causes, and solutions:

---

### *1. Canine Parvovirus (Parvo)*
- *Symptoms:*
  - Severe vomiting and diarrhea (often bloody).
  - Loss of appetite.
  - Lethargy and fever.
- *Causes:* 
  - Highly contagious virus transmitted through contaminated feces or environments.
- *Solutions:*
  - Immediate veterinary treatment (fluids, antibiotics for secondary infections).
  - Prevent with vaccination.
  - Disinfect contaminated areas thoroughly.

---

### *2. Canine Distemper*
- *Symptoms:*
  - Nasal and eye discharge.
  - Fever, coughing, and lethargy.
  - Seizures or twitching in severe cases.
- *Causes:* 
  - Virus spread through respiratory droplets, shared food/water, or direct contact.
- *Solutions:*
  - Supportive care from a vet (fluids, antibiotics for secondary infections).
  - Vaccination is the best prevention.

---

### *3. Kennel Cough*
- *Symptoms:*
  - Persistent, hacking cough (sounds like honking).
  - Gagging or retching.
  - Nasal discharge and lethargy in severe cases.
- *Causes:* 
  - Caused by Bordetella bronchiseptica or viruses like parainfluenza.
- *Solutions:*
  - Mild cases resolve with rest; severe cases need antibiotics or cough suppressants.
  - Vaccinate if your dog is in contact with other dogs (boarding, daycare, etc.).

---

### *4. Rabies*
- *Symptoms:*
  - Behavior changes (aggression or lethargy).
  - Excessive drooling or difficulty swallowing.
  - Paralysis and seizures.
- *Causes:* 
  - Virus transmitted through bites from infected animals.
- *Solutions:*
  - Fatal if untreated; no cure once symptoms appear.
  - Vaccinate your dog and avoid contact with wild animals.

---

### *5. Lyme Disease*
- *Symptoms:*
  - Fever and lethargy.
  - Lameness (shifting between legs).
  - Swollen joints and loss of appetite.
- *Causes:* 
  - Bacterial infection transmitted through tick bites (Borrelia burgdorferi).
- *Solutions:*
  - Antibiotics like doxycycline prescribed by a vet.
  - Use tick prevention products and check for ticks after outdoor activities.

---

### *6. Heartworm Disease*
- *Symptoms:*
  - Coughing and difficulty breathing.
  - Fatigue after mild exercise.
  - Weight loss and a swollen abdomen in severe cases.
- *Causes:* 
  - Spread by mosquito bites carrying Dirofilaria immitis larvae.
- *Solutions:*
  - Prevention with monthly heartworm medication.
  - Treatment involves a series of vet-administered injections (can be risky in advanced cases).

---

### *7. Canine Influenza (Dog Flu)*
- *Symptoms:*
  - Coughing and nasal discharge.
  - Fever and lethargy.
  - Loss of appetite.
- *Causes:* 
  - Virus spread through respiratory droplets, direct contact, or contaminated surfaces.
- *Solutions:*
  - Supportive care (fluids and medications for secondary infections).
  - Vaccination for dogs in high-risk areas.

---

### *8. Skin Allergies*
- *Symptoms:*
  - Itchy, red, or inflamed skin.
  - Excessive scratching, licking, or chewing.
  - Hair loss or skin infections.
- *Causes:* 
  - Allergens like pollen, food, flea bites, or dust mites.
- *Solutions:*
  - Identify and avoid allergens (diet trials, flea treatments).
  - Antihistamines, medicated shampoos, or prescription medications like Apoquel.
  - Consult a vet for chronic cases.

---

### *9. Canine Diabetes*
- *Symptoms:*
  - Increased thirst and urination.
  - Weight loss despite a good appetite.
  - Lethargy and cloudy eyes (cataracts).
- *Causes:* 
  - Insufficient insulin production or response (often genetic or due to obesity).
- *Solutions:*
  - Insulin injections and a controlled diet prescribed by a vet.
  - Regular blood glucose monitoring.

---

### *10. Obesity*
- *Symptoms:*
  - Excess weight or difficulty moving.
  - Shortness of breath during activity.
  - Increased risk of joint problems, diabetes, or heart issues.
- *Causes:* 
  - Overfeeding, lack of exercise, or underlying health problems.
- *Solutions:*
  - Implement a vet-approved diet and exercise plan.
  - Measure food portions and limit treats.

---

### *11. Ear Infections*
- *Symptoms:*
  - Red, inflamed ears with discharge.
  - Foul odor and head shaking.
  - Scratching or pawing at the ears.
- *Causes:* 
  - Bacteria, yeast, mites, or allergies.
- *Solutions:*
  - Clean ears as recommended by a vet.
  - Use prescribed ear drops or medications.
  - Keep ears dry, especially for breeds with floppy ears.

---

### *12. Gastrointestinal Issues*
- *Symptoms:*
  - Vomiting, diarrhea, or constipation.
  - Loss of appetite and lethargy.
  - Abdominal pain.
- *Causes:* 
  - Dietary indiscretion (eating something harmful), infections, or parasites.
- *Solutions:*
  - Offer bland food (boiled chicken and rice) for mild cases.
  - Deworming for parasitic infections.
  - Seek veterinary help for persistent symptoms.

---

### *13. Arthritis*
- *Symptoms:*
  - Difficulty getting up or moving.
  - Limping or stiffness.
  - Reduced activity and reluctance to climb stairs.
- *Causes:* 
  - Aging, joint wear-and-tear, or injury.
- *Solutions:*
  - Joint supplements (glucosamine, chondroitin) and anti-inflammatory medications.
  - Maintain a healthy weight and provide soft bedding.

---

### *Prevention Tips*
1. *Vaccination:* Keep your dog's vaccinations up to date to prevent serious diseases.
2. *Regular Vet Checkups:* Annual health checkups catch problems early.
3. *Healthy Diet:* Provide a balanced diet suitable for your dog’s age and breed.
4. *Hygiene:* Keep your dog's environment clean, groom regularly, and provide dental care.
5. *Parasite Control:* Use flea, tick, and heartworm prevention products year-round.

Early detection and prompt veterinary care can make a significant difference in your dog's recovery and overall health.""")
        
        elif z=="Birds"and b1:
             st.markdown("""Birds are susceptible to various diseases, many of which can spread rapidly in confined or unclean environments. Here's a detailed guide to common bird diseases, their symptoms, causes, and solutions:

---

### *1. Psittacosis (Parrot Fever)*
- *Symptoms:*
  - Watery or greenish droppings.
  - Difficulty breathing, nasal discharge.
  - Lethargy and loss of appetite.
- *Causes:* 
  - Caused by the bacterium Chlamydia psittaci; transmitted through inhalation of infected droppings or secretions.
- *Solutions:*
  - Treat with antibiotics like doxycycline prescribed by a vet.
  - Isolate infected birds and clean the environment thoroughly.

---

### *2. Avian Influenza (Bird Flu)*
- *Symptoms:*
  - Sudden death in severe cases.
  - Respiratory distress, nasal discharge.
  - Swollen head or neck.
- *Causes:* 
  - Viral infection spread through contact with infected birds or contaminated surfaces.
- *Solutions:*
  - No direct treatment; supportive care may help.
  - Prevent by avoiding contact with wild birds and maintaining biosecurity.

---

### *3. Aspergillosis*
- *Symptoms:*
  - Difficulty breathing, coughing, or wheezing.
  - Loss of appetite and weight.
  - Swollen abdomen in severe cases.
- *Causes:* 
  - Fungal infection caused by inhalation of moldy feed, bedding, or damp conditions.
- *Solutions:*
  - Antifungal medications prescribed by a vet.
  - Ensure proper ventilation and remove moldy materials from the environment.

---

### *4. Candidiasis*
- *Symptoms:*
  - White plaques in the mouth or throat.
  - Regurgitation or difficulty swallowing.
  - Reduced appetite and lethargy.
- *Causes:* 
  - Yeast infection (Candida albicans) often caused by poor hygiene or stress.
- *Solutions:*
  - Treat with antifungal medications like nystatin.
  - Maintain clean feeding areas and avoid overuse of antibiotics.

---

### *5. Newcastle Disease*
- *Symptoms:*
  - Respiratory distress, coughing, and sneezing.
  - Twisting of the neck or paralysis in severe cases.
  - Diarrhea and reduced egg production.
- *Causes:* 
  - Viral infection spread through contact with infected birds or contaminated materials.
- *Solutions:*
  - No cure; provide supportive care.
  - Vaccinate to prevent outbreaks and practice biosecurity.

---

### *6. Avian Pox*
- *Symptoms:*
  - Wart-like growths on the skin or unfeathered areas.
  - Lesions in the mouth or throat (wet pox).
  - Weakness and difficulty eating in severe cases.
- *Causes:* 
  - Viral infection spread by mosquitoes or direct contact.
- *Solutions:*
  - Treat lesions with antiseptics and provide supportive care.
  - Reduce mosquito exposure and vaccinate if available.

---

### *7. Egg Binding*
- *Symptoms:*
  - Straining to lay an egg.
  - Swollen abdomen or lethargy.
  - Difficulty perching or breathing.
- *Causes:* 
  - Calcium deficiency, obesity, or malformed eggs.
- *Solutions:*
  - Seek immediate veterinary assistance.
  - Provide a calcium-rich diet and ensure proper nesting conditions.

---

### *8. Proventricular Dilatation Disease (PDD)*
- *Symptoms:*
  - Regurgitation, undigested food in feces.
  - Weight loss despite a good appetite.
  - Neurological symptoms in advanced cases.
- *Causes:* 
  - Likely caused by a viral infection (avian bornavirus).
- *Solutions:*
  - No cure; supportive care and diet adjustments.
  - Maintain strict hygiene to reduce transmission.

---

### *9. Bumblefoot (Pododermatitis)*
- *Symptoms:*
  - Swollen or inflamed foot pads.
  - Limping or reluctance to perch.
  - Abscess or pus-filled lesion in advanced cases.
- *Causes:* 
  - Poor perching surfaces, obesity, or bacterial infections.
- *Solutions:*
  - Clean and bandage affected areas; use antibiotics if prescribed.
  - Provide proper perches and a clean environment.

---

### *10. Mites and Lice Infestations*
- *Symptoms:*
  - Excessive scratching or feather loss.
  - Scaly legs or beak.
  - Restlessness, especially at night.
- *Causes:* 
  - Parasitic infestation from contact with infected birds or materials.
- *Solutions:*
  - Use vet-recommended anti-parasitic treatments (e.g., ivermectin).
  - Clean and disinfect cages and replace bedding regularly.

---

### *11. Sour Crop*
- *Symptoms:*
  - Swollen crop with foul-smelling liquid.
  - Regurgitation and lethargy.
  - Loss of appetite.
- *Causes:* 
  - Bacterial or fungal infection due to food stuck in the crop.
- *Solutions:*
  - Empty the crop under veterinary guidance.
  - Provide antifungal or antibiotic treatment as needed.
  - Avoid overfeeding and ensure proper feeding practices.

---

### *12. Psittacine Beak and Feather Disease (PBFD)*
- *Symptoms:*
  - Feather loss and abnormal feather growth.
  - Beak deformities or fractures.
  - Weakness and weight loss.
- *Causes:* 
  - Viral infection caused by a circovirus, spread through feather dust or droppings.
- *Solutions:*
  - No cure; focus on supportive care and minimizing stress.
  - Quarantine infected birds and maintain hygiene.

---

### *13. Obesity*
- *Symptoms:*
  - Excessive weight and difficulty flying.
  - Fat deposits under the skin.
  - Increased risk of liver disease.
- *Causes:* 
  - Overfeeding or lack of exercise.
- *Solutions:*
  - Adjust diet to include more vegetables and fewer seeds.
  - Provide opportunities for flying and exercise.

---

### *Prevention Tips for Bird Diseases*
1. *Cleanliness:* Maintain clean cages, feeding areas, and water bowls.
2. *Quarantine:* Isolate new birds for 30 days before introducing them to others.
3. *Nutrition:* Provide a balanced diet with fresh fruits, vegetables, and high-quality bird feed.
4. *Ventilation:* Ensure proper airflow to prevent mold and fungal growth.
5. *Veterinary Checkups:* Regular visits help detect diseases early.
6. *Vaccination:* Vaccinate against preventable diseases where available.

---

By maintaining proper care, hygiene, and a healthy diet, many bird diseases can be prevented or managed effectively. If symptoms persist, consult an avian veterinarian promptly.""")
        
        elif z=="Fish" and b1:
            st.markdown("""### *1. Ich (White Spot Disease)*
- *Symptoms:*
  - White spots on the skin, gills, and fins.
  - Rubbing against objects.
  - Lethargy and difficulty breathing.
- *Causes:* 
  - Caused by the parasite Ichthyophthirius multifiliis.
  - Often due to sudden temperature changes or stress.
- *Solutions:*
  - Increase water temperature gradually to 78–86°F (25–30°C).
  - Use anti-parasitic medications like malachite green or formalin.
  - Quarantine affected fish and clean the tank.

---

### *2. Fin Rot*
- *Symptoms:*
  - Frayed or disintegrating fins.
  - Discoloration at the fin edges.
- *Causes:* 
  - Bacterial infection due to poor water quality or injuries.
- *Solutions:*
  - Improve water quality with regular changes and filtration.
  - Use antibiotics like tetracycline or erythromycin.
  - Isolate affected fish if the infection is severe.

---

### *3. Swim Bladder Disease*
- *Symptoms:*
  - Difficulty swimming (floating upside down or sinking).
  - Loss of balance.
- *Causes:* 
  - Overfeeding, constipation, or injury to the swim bladder.
- *Solutions:*
  - Fast the fish for 24–48 hours, then feed a peeled, boiled pea.
  - Maintain stable water parameters.
  - Avoid overfeeding in the future.

---

### *4. Dropsy*
- *Symptoms:*
  - Swollen body with raised scales (pinecone appearance).
  - Lethargy and loss of appetite.
- *Causes:* 
  - Bacterial infection or organ failure due to poor water quality.
- *Solutions:*
  - Isolate the affected fish.
  - Use antibacterial medications like kanamycin or erythromycin.
  - Improve tank conditions and maintain proper filtration.

---

### *5. Velvet Disease*
- *Symptoms:*
  - Golden or rust-colored dust on the body.
  - Rubbing against objects.
  - Lethargy and difficulty breathing.
- *Causes:* 
  - Caused by the parasite Oodinium.
- *Solutions:*
  - Dim tank lighting to weaken the parasite.
  - Treat with copper-based medications or aquarium salt.
  - Improve water quality and quarantine new fish.

---

### *6. Anchor Worms*
- *Symptoms:*
  - Visible worm-like parasites on the skin.
  - Red sores or irritation at the attachment site.
- *Causes:* 
  - Infection by crustacean parasites, often from infected fish or plants.
- *Solutions:*
  - Physically remove worms with tweezers (gently).
  - Treat the tank with anti-parasitic medication like potassium permanganate.
  - Quarantine new additions to prevent infestations.

---

### *7. Hole in the Head (HITH) Disease*
- *Symptoms:*
  - Small pits or holes around the head and lateral line.
  - Loss of appetite and weight.
- *Causes:* 
  - Poor diet, lack of vitamins, or infection by Hexamita parasites.
- *Solutions:*
  - Improve the diet with vitamin-rich foods.
  - Treat with metronidazole if a parasitic infection is confirmed.
  - Maintain pristine water quality.

---

### *8. Ammonia Poisoning*
- *Symptoms:*
  - Red or inflamed gills.
  - Gasping at the water surface.
  - Lethargy.
- *Causes:* 
  - Elevated ammonia levels due to poor filtration or overfeeding.
- *Solutions:*
  - Perform an immediate water change.
  - Test and reduce ammonia levels with a water conditioner.
  - Avoid overstocking and overfeeding.

---

### *9. Fungal Infections*
- *Symptoms:*
  - Cotton-like growths on the body, fins, or gills.
- *Causes:* 
  - Fungal spores thriving in dirty or injured areas.
- *Solutions:*
  - Treat with antifungal medications like methylene blue.
  - Clean the tank and maintain water parameters.
  - Avoid injuries by removing sharp objects.

---

### *10. Gill Flukes*
- *Symptoms:*
  - Rapid gill movement or gasping at the surface.
  - Scratching against objects.
- *Causes:* 
  - Parasitic worms (Dactylogyrus) that attach to gills.
- *Solutions:*
  - Use anti-parasitic medications like praziquantel.
  - Perform water changes to reduce parasite load.
  - Quarantine affected fish.

---

### *Prevention Tips for Fish Diseases*
1. *Maintain Water Quality:* Regular water changes, filtration, and testing for pH, ammonia, nitrites, and nitrates.
2. *Proper Diet:* Feed a balanced diet and avoid overfeeding.
3. *Quarantine New Fish:* Isolate new additions for 2–4 weeks before introducing them to the main tank.
4. *Clean Environment:* Remove uneaten food, clean the substrate, and sanitize decorations regularly.
5. *Monitor Behavior:* Watch for early signs of illness like lethargy, loss of appetite, or unusual swimming.
""")
        
        elif z=="Rabbit"and b1:
             st.markdown("""
Rabbits are prone to various diseases, and understanding their symptoms, causes, and solutions is essential for their care. Here’s a detailed overview:

---

### 1. *Common Rabbit Diseases*

#### A. *Myxomatosis*
- *Symptoms:* Swelling around the eyes, nose, and genitals; discharge from the eyes; lethargy; fever.
- *Causes:* Spread by biting insects like fleas and mosquitoes or direct contact with infected rabbits.
- *Solutions:*  
  - Vaccination is the best preventive measure.  
  - Keep rabbits indoors or use insect-proof enclosures.  
  - Supportive care for infected rabbits; euthanasia may be recommended in severe cases.

#### B. *Rabbit Hemorrhagic Disease (RHD)*
- *Symptoms:* Sudden death, fever, bleeding from the nose or mouth, lethargy, difficulty breathing.
- *Causes:* Viral infection spread through direct contact, contaminated objects, or insect bites.
- *Solutions:*  
  - Vaccination is crucial.  
  - Quarantine new rabbits before introducing them to others.  
  - Maintain good hygiene and sanitation.

#### C. *Pasteurellosis (Snuffles)*
- *Symptoms:* Nasal discharge, sneezing, head tilt, eye infections, abscesses.
- *Causes:* Caused by Pasteurella multocida bacteria, often triggered by stress or a weakened immune system.
- *Solutions:*  
  - Antibiotics prescribed by a veterinarian.  
  - Maintain a stress-free, clean environment.

#### D. *Ear Mites*
- *Symptoms:* Excessive ear scratching, crusty or scabby ears, head shaking.
- *Causes:* Parasitic mites like Psoroptes cuniculi.
- *Solutions:*  
  - Topical or injectable antiparasitic medications.  
  - Regular cleaning of the rabbit’s living area.

#### E. *Gastrointestinal Stasis (GI Stasis)*
- *Symptoms:* Loss of appetite, no feces or small, dry feces, bloating, lethargy.
- *Causes:* Low fiber diet, stress, dehydration, or dental problems.
- *Solutions:*  
  - Provide a high-fiber diet (mainly hay).  
  - Immediate veterinary attention for severe cases.  
  - Regular exercise and hydration.

#### F. *Malocclusion (Dental Disease)*
- *Symptoms:* Overgrown teeth, drooling, difficulty eating, weight loss.
- Causes: Genetic predisposition, insufficient chewing on hay.
- Solutions:
  - Routine dental check-ups and trimming of overgrown teeth.  
  - Provide chew toys and fibrous food like hay.

---

#### 2. General Preventive Measures
- Regular veterinary check-ups.
- Provide a balanced diet rich in fiber (e.g., hay, vegetables, and limited pellets).
- Maintain a clean, spacious, and safe living environment.
- Quarantine new rabbits before introducing them to others.
- Keep stress levels low by handling rabbits gently and avoiding loud noises.

---

 3. When to See a Veterinarian
If your rabbit shows signs of illness such as loss of appetite, changes in behavior, or unusual symptoms, seek veterinary care immediately. Early intervention is critical for recovery.""")
        
        elif z=="Hamster"and b1:
             st.markdown("""Hamsters, like all pets, can suffer from various diseases. Knowing the symptoms, causes, and treatment options is essential for their care.

---

### 1. *Common Hamster Diseases*

#### A. *Wet Tail (Proliferative Ileitis)*
- *Symptoms:* Watery diarrhea, lethargy, loss of appetite, hunched posture, foul-smelling rear.
- *Causes:* Stress, poor hygiene, abrupt dietary changes, or bacterial infection (Lawsonia intracellularis).
- *Solutions:*  
  - Seek immediate veterinary treatment; antibiotics may be prescribed.  
  - Maintain clean cages and reduce stress.  
  - Ensure proper hydration and a balanced diet.

---

#### B. *Respiratory Infections*
- *Symptoms:* Sneezing, wheezing, nasal discharge, lethargy, labored breathing.
- *Causes:* Exposure to drafts, damp environments, or contact with sick animals.
- *Solutions:*  
  - Keep the cage in a warm, draft-free environment.  
  - Consult a vet for antibiotics or other treatments.  
  - Avoid using dusty bedding (use paper-based bedding instead).

---

#### C. *Skin Issues (Mites, Ringworm, or Allergies)*
- *Symptoms:* Hair loss, itching, scabs, redness, flaky skin.
- *Causes:* Parasites, fungal infections, or allergic reactions to bedding or food.
- *Solutions:*  
  - Use veterinary-prescribed antiparasitic medications for mites.  
  - For ringworm, antifungal creams may be recommended.  
  - Switch to hypoallergenic bedding and avoid scented products.

---

#### D. *Abscesses*
- *Symptoms:* Swollen lumps, pus, pain when touched, or reluctance to eat.
- *Causes:* Infections from wounds or injuries, such as bites or sharp objects in the cage.
- *Solutions:*  
  - Visit a vet to have the abscess drained and treated with antibiotics.  
  - Regularly inspect your hamster for wounds.

---

#### E. *Diabetes*
- *Symptoms:* Excessive drinking, frequent urination, lethargy, weight loss.
- *Causes:* Genetic predisposition (common in certain breeds like Campbell’s hamsters) and high-sugar diets.
- *Solutions:*  
  - Provide a low-sugar, high-fiber diet (avoid sweet treats).  
  - Monitor blood sugar levels under veterinary guidance.

---

#### F. *Dental Problems*
- *Symptoms:* Overgrown teeth, difficulty eating, drooling, weight loss.
- *Causes:* Lack of chewable items to wear down teeth.
- *Solutions:*  
  - Provide chew toys, wooden blocks, or untreated branches.  
  - Have teeth trimmed by a vet if they become overgrown.

---

#### G. *Tumors*
- *Symptoms:* Lumps or growths, weight loss, behavioral changes.
- *Causes:* Genetic predisposition, age-related factors.
- *Solutions:*  
  - Consult a veterinarian for diagnosis.  
  - Surgical removal may be possible depending on the tumor's nature and the hamster's health.

---

### 2. *General Preventive Measures*
- *Proper Nutrition:* Provide a balanced diet of hamster pellets, fresh vegetables, and occasional treats.
- *Clean Environment:* Regularly clean the cage and change bedding to prevent infections.
- *Reduce Stress:* Handle hamsters gently and avoid loud noises or sudden changes in their routine.
- *Quarantine New Hamsters:* Isolate new pets before introducing them to others to prevent disease spread.
- *Regular Monitoring:* Check your hamster daily for any signs of illness or unusual behavior.

---

### 3. *When to See a Veterinarian*
If your hamster shows symptoms such as lethargy, loss of appetite, difficulty breathing, or visible signs of illness, seek veterinary care immediately. Quick treatment is vital for recovery.""")
        elif z=="Select ↓" and b1:
             st.error("Please select a pet")
        else:
            if b1:
                st.markdown("### Comming Soon")
    else:
        st.markdown("""#### One-stop healthcare solutions, or comprehensive healthcare or medical homes, aim to provide a single access point for a wide range of healthcare services. These solutions are designed to simplify the healthcare experience for families, making it more efficient and patient-centered.""")
        st.image("pets1.jpeg") 
        st.markdown("""#### A one-stop solution for pet health and pet care refers to a comprehensive service that provides everything a pet needs to stay healthy, happy, and well-cared for under one roof. These services typically include preventive care like vaccinations, parasite control, and regular health check-ups, as well as emergency care, diagnostics, surgery, and long-term treatment for chronic conditions. Such facilities may also offer specialized care for pets with unique health needs, including dental care, grooming, and nutrition counseling. In addition to medical services, these centers often feature pet boarding, daycare, and training to ensure pets are well looked after even when their owners are away.""")
        st.markdown("""### Advantages :""")
        st.markdown("""##### • Convenience: All pet care services are available under one roof, eliminating the need to visit multiple locations for different treatments and services. \n##### • Continuity of Care: Veterinarians and staff have access to comprehensive health records, ensuring consistent and informed care for your pet. \n##### • Comprehensive Services: A variety of services are available, including preventive care, diagnostics, surgery, grooming, nutrition counseling, and emergency care. \n##### • Time and Stress Savings: Pet owners save time by not having to juggle appointments at different clinics, and pets experience less stress with familiar surroundings and caregivers. \n##### • Personalized Care: With a complete record of a pet's health, the care provided can be tailored to meet their specific needs, improving overall well-being. \n##### • Expert Access: Many one-stop centers offer specialized services such as dental care, dermatology, and behavior therapy, giving pets access to expert care in various areas. \n##### • Increased Health Monitoring: Routine health checks, vaccinations, and preventive treatments are easier to manage with reminders and centralized record-keeping. \n##### • Emergency Care: Immediate access to emergency services ensures that pets receive timely care when unexpected health issues arise. \n##### • Peace of Mind: Knowing that all aspects of your pet’s health and care are covered in one place provides owners with peace of mind. \n##### • Cost Efficiency: Bundling services at one center can often result in cost savings through packages or discounted rates for multiple services. """)
        st.markdown("""#### """)
 
elif b=="Help":
        pet=st.selectbox("Select your pet",("Select ↓","Cat","Dog","parrot","Love birds","pigeon","Fish","Rabbit","Tortoise","Hamster"))
        age=st.number_input("Enter Age Of Your Pet(in years(approx))....(if you known)",value=0,step=1)
        date=st.date_input("Enter Today's Date")
        email=st.text_input("Enter Your Email")
        problem=st.text_area("Enter Problem Of Your Pet")
        sub_butt=st.button("Submit")
        if len(pet) == "Select ↓" or len(email)==0 or len(problem)==0 :
            if sub_butt:
                st.error("Please fill a full informatoin..")
        else:
            if sub_butt :
                    date1=str(date)
                    pet1=str(pet)
                    age1=str(age)
                    email1=str(email)
                    problem1=str(problem)
                    f=open("pet_problems.txt","a")
                    f.write("Date     : ")
                    f.write(date1)
                    f.write("\nPet      : ")
                    f.write(pet1)
                    f.write("\nage      : ")
                    f.write(age1)
                    f.write("\nEmail    : ")
                    f.write(email1)
                    f.write("\nProblem  : ")
                    f.write(problem1)
                    f.write("\n______________________________________________________________________________________\n")
                    f.close()
                    st.success("Submited Successfuly...(solution will be sent on your email)")  
                    
else:
    st.markdown("### Comming Soon")
