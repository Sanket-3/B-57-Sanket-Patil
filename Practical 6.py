def medical_expert_system():
    print("🏥 Medical Expert System")
    print("Answer with yes or no\n")
    
    fever = input("Do you have fever? ").lower()
    cough = input("Do you have cough? ").lower()
    headache = input("Do you have headache? ").lower()
    fatigue = input("Do you feel fatigue? ").lower()
    
    print("\n🩺 Diagnosis:")

    # Rule-based decision making
    if fever == "yes" and cough == "yes":
        print("You may have Flu or COVID-19")
    
    elif fever == "yes" and headache == "yes":
        print("You may have Viral Fever")
    
    elif fatigue == "yes" and headache == "yes":
        print("You may have Stress or Migraine")
    
    elif cough == "yes":
        print("You may have Cold")
    
    else:
        print("Symptoms unclear. Please consult a doctor.")


# Run system
medical_expert_system()