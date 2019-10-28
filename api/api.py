from starlette.requests import Request
from starlette.responses import JSONResponse
from fastai.vision import *
from io import BytesIO
import base64

data = DataBunch.load_empty('/data', 'empty_databunch.pkl')
learn = cnn_learner(data, models.densenet121, pretrained=False)
learn.path = Path('/data')
learn.load('pets');


def predict_from_b64(str_b64):
    x = PIL.Image.open(BytesIO(base64.b64decode(str_b64))).convert('RGB')
    x = pil2tensor(x,np.float32)
    x.div_(255)
    x = Image(x)
    return learn.predict(x)

async def app(scope, receive, send):
    request = Request(scope, receive)
    json = await request.json()
    predicted_class, _, preds = predict_from_b64(json['image'])
    response = JSONResponse({'predicted_class': predicted_class.obj, 'probability': preds.max().item()})

    await response(scope, receive, send)
