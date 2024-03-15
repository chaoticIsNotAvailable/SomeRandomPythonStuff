import controller

choise = int(input('Выберете 1-Прост калькулятор лол, 2-ПЛОЩАДББ'))
if __name__ == "__main__":
    calculator = controller.run()
    if choise == 1:
        calculator.run()
    if choise == 2:
        calculator.runSQ()