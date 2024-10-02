import random
from tinygrad.tensor import Tensor

class NavigationNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.fc1 = Tensor.uniform(hidden_size, input_size)  
        self.fc2 = Tensor.uniform(output_size, hidden_size)

    def forward(self, x):
        x = x.dot(self.fc1).relu()
        x = x.dot(self.fc2)
        return x
    def parameters(self):
        return [self.fc1, self.fc2]

# Initialize the Neural Network
input_size = 4  # blob_x, blob_y, food1_x, food1_y, food2_x, food2_y
hidden_size = 16
output_size = 4  # up, down, right, left

nn = NavigationNN(input_size, hidden_size, output_size)
learning_rate = 0.01

# Initialize the Coordinate Plane
coordinate_plane = [[i, j] for i in range(100) for j in range(100)]
food_at_places = random.sample(coordinate_plane, 2)
print("Food Locations:", food_at_places)

blob_food = 0
blob_location = random.choice(coordinate_plane)

# Define Movement Directions
directions = ['up', 'down', 'right', 'left']

def get_input_features(blob, food1, food2):
    return [blob[0], blob[1], food1[0], food1[1], food2[0], food2[1]]

def choose_move(predictions):
    return directions[predictions.argmax()]

def train_step(inputs, target):
    # Forward pass
    output = nn.forward(inputs)
    # Compute loss (simple mean squared error)
    loss = ((output - target) * (output - target)).sum()
    # Backward pass
    loss.backward()
    # Update parameters
    for param in nn.parameters():
        param -= param.grad * learning_rate
    # Zero gradients
    for param in nn.parameters():
        param.grad = None

def direction_to_target(blob, food):
    if blob[0] < food[0]:
        return 'right'
    elif blob[0] > food[0]:
        return 'left'
    elif blob[1] < food[1]:
        return 'up'
    elif blob[1] > food[1]:
        return 'down'
    return random.choice(directions)

while blob_food < 2:
    inputs = Tensor(get_input_features(blob_location, food_at_places[0], food_at_places[1]))
    output = nn.forward(inputs)
    move = choose_move(output.data)
    
    # Execute Move
    if move == "up" and blob_location[1] < 99:
        blob_location[1] += 1
    elif move == "down" and blob_location[1] > 0:
        blob_location[1] -= 1
    elif move == "right" and blob_location[0] < 99:
        blob_location[0] += 1
    elif move == "left" and blob_location[0] > 0:
        blob_location[0] -= 1
    
    # Check for Food
    if blob_location in food_at_places:
        blob_food += 1
        print(f"Blob found food: {blob_food} at location {blob_location}")
        # Optionally, place new food or terminate

    # Training Placeholder
    # In a real scenario, you'd have target moves and train the network accordingly
    # Here, we skip training for simplicity

print("Blob has found all food!")