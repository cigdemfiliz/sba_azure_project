import azure.functions as func
import json
import math

app = func.FunctionApp()

@app.route(route="calculate", auth_level=func.AuthLevel.ANONYMOUS)
def calculate(req: func.HttpRequest) -> func.HttpResponse:

    shape = req.params.get("shape")

    if shape == "square":
        side = float(req.params.get("side"))
        result = side * side

    elif shape == "circle":
        radius = float(req.params.get("radius"))
        result = math.pi * radius * radius

    else:
        return func.HttpResponse("Invalid shape", status_code=400)

    return func.HttpResponse(
        json.dumps({"area": result}),
        mimetype="application/json"
    )