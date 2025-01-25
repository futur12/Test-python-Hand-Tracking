from src.hand_tracking import HandTracker
from src.mouse_control import MouseController
from src.gesture_mapping import GestureMapper

def main():
    print("Initialisation de l'application...")
    hand_tracker = HandTracker()
    mouse_controller = MouseController()
    gesture_mapper = GestureMapper()

    # Lancer le suivi et le contrôle des gestes
    hand_tracker.start_tracking(mouse_controller, gesture_mapper)

if __name__ == "__main__":
    main()