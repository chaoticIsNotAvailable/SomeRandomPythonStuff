import view
import model
import main


def run():
    while True:
        num1, operator, num2 = view.get_user_input()
        result = model.calculate(num1, num2, operator)
        view.display_result(result)
        resultSQ = model.calculateSQ(num12, num22)
def runSQ():
    num12, num22 = view.choise_mode()
    resultSQ = model.calculateSQ(num12, num22)
    view.display_resultSQ(resultSQ)



