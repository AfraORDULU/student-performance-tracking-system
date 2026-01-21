def calculate_average(midterm, final, homework):
    return (midterm * 0.3) + (final * 0.5) + (homework * 0.2)
  
def letter_grade(average):
  
    if average >= 90:
        return "AA"
    elif average >= 80:
        return "BA"
    elif average >= 70:
        return "BB"
    elif average >= 60:
        return "CB"
    else:
        return "FF"

def process_students(file_name):
    print("Öğrenci Not Durumu\n")
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            name, midterm, final, homework = line.strip().split(",")

            midterm = int(midterm)
            final = int(final)
            homework = int(homework)

            avg = calculate_average(midterm, final, homework)
            grade = letter_grade(avg)

            status = "Geçti" if grade != "FF" else "Kaldı"

            print(f"{name} | Ortalama: {avg:.2f} | Harf Notu: {grade} | Durum: {status}")
process_students("students.txt")
