customerName = input("Escriba su nombre, por favor: ")
customerSalary = float(input("Digite el salario correspondiente a este mes: "))
comission = (customerSalary * 13)/ 100
totalSalary = customerSalary + comission
print(f"{customerName} tiene un salario de {customerSalary}\n Comision = {comission} \nEl salario total es: {totalSalary} ")
