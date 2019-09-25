def askUserSalary():
  annualSalary = int(input("Enter your annual salary here"))
  return annualSalary

  def convertAnnualSalary(annualSalary):
      weeklyRate = annualSalary / 50
      hourlyRate = weeklyRate /4
      return hourlyRate
    
salary = askUserSalary()

usersHourlyRate = convertAnnualSalary(salary)

print("your Hourly rate is" + str(usersHourlyRate))
    
