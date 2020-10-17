import torch
import torchvision.transforms as transforms
from PIL import Image

transform = transforms.Compose([transforms.Resize(224), transforms.RandomResizedCrop(336), transforms.RandomHorizontalFlip(), transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
model = torch.load('cxhNet.pth', map_location=torch.device('cpu'))
model.eval()
image = Image.open('./test.jpg').convert('RGB').resize((224, 224), Image.ANTIALIAS)
image_transformed = transform(image)
image_transformed = image_transformed.unsqueeze(0)
out = model(image_transformed)
pred = torch.max(out, 1)[1]
print(pred)
