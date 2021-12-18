from parent_a import parent_a
from parent_b import parent_b


class main(parent_a, parent_b):
    pass


mainIn = main()

mainIn.doSomething()
mainIn.gotoSchool()
mainIn.gotoMarket()