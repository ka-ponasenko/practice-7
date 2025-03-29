previous_temperature = None
decrease_count = 0

print("Введите значения температуры (введите 0 для завершения):")

while True:
    current_temperature = float(input())
    
    if current_temperature == 0:
        break
    

    if 37.4 <= current_temperature <= 37.8:
        if previous_temperature is not None:
            if current_temperature < previous_temperature:
                decrease_count += 1
        
        previous_temperature = current_temperature
    else:
        print("Температура вне допустимого диапазона. Пожалуйста, введите значение от 37.4 до 37.8.")

print(f"Температура уменьшалась {decrease_count} раз(а).")
