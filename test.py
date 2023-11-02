import pytesseract
from PIL import Image
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
# from custom_dataset import OCRResult  # You need to create a custom dataset class

def extract_text_from_image(image_path):
    try:
        # Open the image using PIL (Python Imaging Library)
        img = Image.open(image_path)
        
        # Use Tesseract to extract text from the image
        text = pytesseract.image_to_string(img, lang='eng')  # 'eng' for English language
        
        return text
    except Exception as e:
        return str(e)

# Replace 'handwritten_image.png' with the path to your image
image_path = 'handwritten_images/example_4.jpg'

extracted_text = extract_text_from_image(image_path)

print("Extracted Text:")
print(extracted_text)

# class OCRResult:
#     def __init__(self, text, confidence, image_path):
#         self.text = text  # Recognized text
#         self.confidence = confidence  # Confidence score of the recognition (if available)
#         self.image_path = image_path  # Path to the input image

#     def __str__(self):
#         return f"Text: {self.text}\nConfidence: {self.confidence}\nImage Path: {self.image_path}"

# # Define a simple CNN model
# class SimpleOCRModel(nn.Module):
#     def __init__(self):
#         super(SimpleOCRModel, self).__init__()
#         self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
#         self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
#         self.fc1 = nn.Linear(32 * 16 * 16, 128)
#         self.fc2 = nn.Linear(128, num_classes)  # num_classes is the number of characters to recognize

#     def forward(self, x):
#         x = self.pool(torch.relu(self.conv1(x)))
#         x = x.view(-1, 32 * 16 * 16)
#         x = torch.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x

# # Hyperparameters
# batch_size = 32
# learning_rate = 0.001
# num_epochs = 10

# # Create a dataset and data loader
# transform = transforms.Compose([transforms.Grayscale(num_output_channels=1), transforms.ToTensor()])
# dataset = OCRResult(root='path_to_training_data', transform=transform)  # You need to create the CustomDataset class
# data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# # Initialize the model
# model = SimpleOCRModel()

# # Define loss and optimizer
# criterion = nn.CrossEntropyLoss()
# optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# # Training loop
# for epoch in range(num_epochs):
#     total_loss = 0
#     for images, labels in data_loader:
#         optimizer.zero_grad()
#         outputs = model(images)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()
#         total_loss += loss.item()
#     print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss/len(data_loader)}')

# # Save the trained model
# torch.save(model.state_dict(), 'custom_ocr_model.pth')
