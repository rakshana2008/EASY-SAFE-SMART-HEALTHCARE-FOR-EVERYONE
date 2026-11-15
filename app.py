# Health Safety Loop
# Simple healthcare monitoring system

def check_blood_sugar(value):
    if value < 70:
        return "⚠️ Alert: Blood sugar is low. Please contact a healthcare professional."
    elif value > 180:
        return "⚠️ Alert: Blood sugar is high. Please follow your doctor's advice."
    else:
        return "✅ Blood sugar reading is within the selected reference range."


def check_blood_pressure(systolic, diastolic):
    if systolic >= 140 or diastolic >= 90:
        return "⚠️ Alert: Blood pressure is high. Consider contacting a healthcare professional."
    elif systolic < 90 or diastolic < 60:
        return "⚠️ Alert: Blood pressure is low. Consider seeking medical advice."
    else:
        return "✅ Blood pressure reading is within the selected reference range."


def main():
    print("=" * 45)
    print("       HEALTH SAFETY LOOP")
    print("=" * 45)

    print("\n1. Check Blood Sugar")
    print("2. Check Blood Pressure")

    choice = input("\nChoose an option (1 or 2): ")

    if choice == "1":
        sugar = float(input("Enter blood sugar reading: "))
        print("\nResult:", check_blood_sugar(sugar))

    elif choice == "2":
        systolic = float(input("Enter systolic pressure: "))
        diastolic = float(input("Enter diastolic pressure: "))
        print("\nResult:", check_blood_pressure(systolic, diastolic))

    else:
        print("Invalid choice. Please run the program again.")


if __name__ == "__main__":
    main()
