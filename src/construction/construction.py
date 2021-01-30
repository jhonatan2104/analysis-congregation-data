from ..bricks.install import install
from ..bricks.getting import getting
from ..bricks.validation import validation
from ..bricks.wiping import wiping
from ..bricks.analyze import analyze
from ..bricks.save import save


def construction():

    # install()
    data = getting()
    data = wiping(data)
    data = validation(data)
    data = analyze(data)
    save(data)

    print("Success Run")
