import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller connected.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Using controller: {joystick.get_name()}")

print("Press any button...")

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            for i in range(joystick.get_numbuttons()):
                if joystick.get_button(i):
                    print(f"Button {i} pressed")
